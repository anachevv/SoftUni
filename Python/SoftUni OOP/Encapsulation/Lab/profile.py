class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, name):
        if not 5 <= len(name) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = name

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, pwd):
        conditions = [len(pwd) >= 8, any(el.isupper() for el in pwd), any(el.isdigit() for el in pwd)]

        if not all(conditions):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = pwd

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.__password)}"
