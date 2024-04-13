from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class ContainMoreAtSymbols(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidName(Exception):
    pass


VALID_DOMAINS = (".com", ".bg", ".org", ".net")
MIN_NAME_LEN = 4
valid_pattern = r'\w+'

email = input()

while email != 'End':
    if '@' not in email:
        raise MustContainAtSymbolError('Emails must contain @')

    elif email.count('@') > 1:
        raise ContainMoreAtSymbols('Emails must contain only one @ symbol')

    elif len(email.split('@')[0]) < MIN_NAME_LEN:
        raise NameTooShortError('Name must be more than 4 characters')

    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join([x for x in VALID_DOMAINS])}')

    elif len(findall(valid_pattern, email.split('@')[0])) != 1:
        raise InvalidName('Name must not contain symbols')

    print('Email is valid')

    email = input()