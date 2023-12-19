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
