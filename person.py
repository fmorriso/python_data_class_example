import random
import string
from dataclasses import dataclass, field


@dataclass(kw_only=True, match_args=True, slots=True)
class Person:

    @staticmethod
    def generate_id() -> str:
        return ''.join(random.choices(string.ascii_uppercase, k=12))

    # instance fields
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    # NOTE: init=False prevents callers from providing their own ID
    id: str = field(init=False, default_factory=generate_id)
    __search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.__search_string = f'{self.name} {self.address}'

    # define getter for pseudo-private, pseudo-readonly search_string instance property
    @property
    def search_string(self) -> str:
        return self.__search_string
