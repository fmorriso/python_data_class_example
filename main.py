import sys

from person import Person


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    person = Person(name="John", address="123 Main St")
    print(person)
    person.name = 'Fred'
    print(person)
    # NOT WHEN slots=True: print(person.__dict__['name'])
    # FAILS due to psuedo-private "scopre" person.__search_string = ''
    # NOTE: there is no such thing as a true "private" variable in Python.
    #       Even if you use the double-underscore (a.k.a., dunder) prefix,
    #       that supposedly "private" variable can be hacked as shown below.
    person._Person__search_string = ''
    print(person)
