from dataclasses import dataclass

@dataclass
class Person:
    name: str
    address: str
    active: bool = True
