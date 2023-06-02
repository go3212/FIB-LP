from custom_dataclasses.expression import Abstraction, Expression, Application, Variable
from visitors.visitor import MyVisitor, print_expression

class Evaluator:

    def __init__(self, max_reductions: int):
        self.max_reductions = max_reductions

    def is_val(self, term):
        return isinstance(term, Abstraction)

    def eval(self, term: Expression, reductions: int = 0):
        if reductions > self.max_reductions:
            print('Maximum reduction limit reached')
            return term

        if isinstance(term, Variable):
            return term

        elif isinstance(term, Application):
            reduced_func = self.eval(term.func, reductions + 1)
            reduced_arg = self.eval(term.arg, reductions + 1)
            if isinstance(reduced_func, Abstraction):
                # β-reduction
                replaced_term = self.substitute(reduced_func.body, reduced_func.var, reduced_arg)
                if (term != replaced_term):
                    print(f"β-reduction: {print_expression(term)} → {print_expression(replaced_term)}")
                return self.eval(replaced_term, reductions + 1)
            else:
                return Application(reduced_func, reduced_arg)

        elif isinstance(term, Abstraction):
            return Abstraction(term.var, self.eval(term.body, reductions + 1))

    def substitute(self, body, var, val):
        if isinstance(body, Variable) and body == var:
            return val
        elif isinstance(body, Variable):
            return body
        elif isinstance(body, Application):
            return Application(self.substitute(body.func, var, val), self.substitute(body.arg, var, val))
        elif isinstance(body, Abstraction):
            if body.var == var:
                return body
            elif self.occurs_in(body.body, var):
                if self.occurs_in(val, body.var):
                    # α-conversion
                    new_var = Variable(self.new_name(body.var.name))
                    print(f"α-conversion: {body.var.name} → {new_var.name}")
                    new_body = self.substitute(body.body, body.var, new_var)
                    return Abstraction(new_var, self.substitute(new_body, var, val))
                else:
                    return Abstraction(body.var, self.substitute(body.body, var, val))
            else:
                return body

    def occurs_in(self, term, var):
        if isinstance(term, Variable) and term == var:
            return True
        elif isinstance(term, Application):
            return self.occurs_in(term.func, var) or self.occurs_in(term.arg, var)
        elif isinstance(term, Abstraction):
            return term.var != var and self.occurs_in(term.body, var)

    def new_name(self, name):
        return name + "'"
