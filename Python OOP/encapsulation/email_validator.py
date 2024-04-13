from typing import List


class EmailValidator:

    def __init__(self, min_length: int, mails: List[str], domains: List[str]) -> None:
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail: str) -> bool:
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain: str) -> bool:
        if domain in self.domains:
            return True
        return False

    def validate(self, email: str):
        username, data = email.split('@')
        mail, domain = data.split('.')

        is_valid = self.__is_name_valid(username) and self.__is_domain_valid(domain) and self.__is_mail_valid(mail)

        return is_valid

