class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        email = email.split('@')
        name, mail, domain = email[0], email[1][0:email[1].index('.')], email[1][email[1].index('.') + 1::]
        conditions = [self.__is_name_valid(name), self.__is_mail_valid(mail), self.__is_domain_valid(domain)]

        if all(conditions):
            return True
        return False
