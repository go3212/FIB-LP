from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Variable:
    name: str

@dataclass
class Application:
    func: Expression
    arg: Expression

@dataclass
class Abstraction:
    var: Variable
    body: Expression

@dataclass
class Macro:
    name: str
    body: Expression

Expression = Abstraction | Application | Variable | Macro