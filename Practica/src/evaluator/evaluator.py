from collections import deque
import copy
from typing import Set, Tuple
from custom_dataclasses.expression import Abstraction, Expression, Application, Macro, Variable
from visitors.visitor import MyVisitor, print_expression

class Evaluator:

    def __init__(self, max_reductions: int):
        self.max_reductions = max_reductions
        self.queue = deque()

    def add_to_queue(self, term: Expression, conversion: str):
        self.queue.append((term, conversion))

    def is_val(self, term):
        return isinstance(term, Abstraction)

    def eval(self, term: Expression) -> Tuple[Expression, str]:
        return self.singleEval(term)


    def evalDeep(self, term: Expression, reductions: int = 0):
        if reductions > self.max_reductions:
            print('Maximum reduction limit reached')
            return term

        if isinstance(term, Variable):
            return term

        elif isinstance(term, Application):
            reduced_func = self.evalDeep(term.func, reductions + 1)
            reduced_arg = self.evalDeep(term.arg, reductions + 1)
            if isinstance(reduced_func, Abstraction):
                # β-reduction
                replaced_term = self.substitute(reduced_func.body, reduced_func.var, reduced_arg)
                if (term != replaced_term):
                    print(f"β-reduction: {print_expression(term)} → {print_expression(replaced_term)}")
                    self.add_to_queue(copy.deepcopy(replaced_term), 'beta')
                return self.evalDeep(replaced_term, reductions + 1)
            else:
                return Application(reduced_func, reduced_arg)

        elif isinstance(term, Abstraction):
            return Abstraction(term.var, self.evalDeep(term.body, reductions + 1))

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
                    self.add_to_queue(copy.deepcopy(body), 'alpha')
                    new_body = self.substitute(body.body, body.var, new_var)
                    return Abstraction(new_var, self.substitute(new_body, var, val))
                else:
                    return Abstraction(body.var, self.substitute(body.body, var, val))
            else:
                return body

    def occurs_in(self, expr: Expression, var: Variable) -> bool:
        if isinstance(expr, Variable):
            return expr == var
        elif isinstance(expr, Application):
            return self.occurs_in(expr.func, var) or self.occurs_in(expr.arg, var)
        elif isinstance(expr, Abstraction):
            return expr.var != var and self.occurs_in(expr.body, var)
        
    def new_name(self, abstraction: Abstraction) -> str:
        used_names = self.get_used_names(abstraction)
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char not in used_names:
                return char
        raise Exception("All variable names from a-z are already used!")

    def singleEval(self, term: Expression, r=0) -> Tuple[Expression, str]:
        if r > self.max_reductions:
            return term, "None"
        if isinstance(term, Variable):
            return term, "None"
        elif isinstance(term, Application):
            if isinstance(term.func, Abstraction):
                # Check if α-conversion is needed
                if isinstance(term.func.body, Abstraction) and self.alpha_conversion_needed(term.func.body, term.func.var, term.arg):
                    # Perform α-conversion
                    converted_abstraction = self.alpha_convert(term.func)
                    return Application(converted_abstraction, term.arg), "α"
                else:
                    # β-reduction
                    replaced_term = self.substitute_2(term.func.body, term.func.var, term.arg)
                    return replaced_term, "β"
            reduced_func, func_op = self.singleEval(term.func, r + 1)
            if (func_op != "None"):
                return Application(reduced_func, term.arg), func_op
            reduced_arg, arg_op = self.singleEval(term.arg, r + 1)
            if (arg_op != "None"):
                return Application(term.func, reduced_arg), arg_op
            else:
                return Application(reduced_func, reduced_arg), "None"

        elif isinstance(term, Abstraction):
            expr, operation = self.singleEval(term.body, r + 1)
            return Abstraction(term.var, expr), operation
        

    def alpha_conversion_needed(self, body: Abstraction, var: Variable, val: Expression) -> bool:
        # Condition 1: `var` appears free in the body of the abstraction
        var_in_body = self.occurs_in(body.body, var) and body.var != var

        # Condition 2: The variable of the abstraction (`body.var`) appears free in `val`
        body_var_in_val = self.occurs_in(val, body.var)

        return var_in_body and body_var_in_val

    def get_used_names(self, expr: Expression) -> Set[str]:
        if isinstance(expr, Variable):
            return {expr.name}
        elif isinstance(expr, Application):
            return self.get_used_names(expr.func) | self.get_used_names(expr.arg)
        elif isinstance(expr, Abstraction):
            return {expr.var.name} | self.get_used_names(expr.body)
        else:
            return set()

    def substitute_2(self, body, var, val):
        if isinstance(body, Variable):
            if body == var:
                return val
            else:
                return body
        elif isinstance(body, Application):
            return Application(self.substitute_2(body.func, var, val), self.substitute_2(body.arg, var, val))
        elif isinstance(body, Abstraction):
            if body.var == var:
                # The variable is shadowed by this abstraction, do not replace
                return body
            else:
                return Abstraction(body.var, self.substitute_2(body.body, var, val))
            
    def get_variables(self, expression: Expression) -> set:
        if isinstance(expression, Variable):
            return {expression.name}
        elif isinstance(expression, Application):
            return Evaluator.get_variables(expression.func) | Evaluator.get_variables(expression.arg)
        elif isinstance(expression, Abstraction):
            return {expression.var.name} | Evaluator.get_variables(expression.body)
        elif isinstance(expression, Macro):
            return Evaluator.get_variables(expression.body)
        else:
            return set()
        
    def needs_alpha_conversion(self, abstraction: Abstraction, argument: Expression) -> bool:
        return abstraction.var.name in self.get_variables(argument)

    def alpha_convert(self, abstraction: Abstraction) -> Abstraction:
        new_var = Variable(self.new_name(abstraction))
        # Perform alpha conversion
        if isinstance(abstraction.body, Abstraction):
            abstraction = self.replace_variable(abstraction, abstraction.body.var.name, new_var.name)
        return abstraction
    
    def replace_variable(self, expression: Expression, old_var_name: str, new_var_name: str) -> Expression:
        if isinstance(expression, Variable):
            if expression.name == old_var_name:
                return Variable(new_var_name)
            else:
                return expression
        elif isinstance(expression, Application):
            return Application(
                self.replace_variable(expression.func, old_var_name, new_var_name),
                self.replace_variable(expression.arg, old_var_name, new_var_name))
        elif isinstance(expression, Abstraction):
            return Abstraction(
                Variable(new_var_name) if expression.var.name == old_var_name else expression.var,
                self.replace_variable(expression.body, old_var_name, new_var_name))
        else:
            return expression



