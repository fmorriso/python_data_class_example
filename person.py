import random
import string
from dataclasses import dataclass, field


@dataclass
class Person:

    @staticmethod
    def generate_id() -> str:
        return ''.join(random.choices(string.ascii_uppercase, k=12))

    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    # NOTE: init=False prevents callers from providing their own ID
    id: str = field(init=False, default_factory=generate_id)
