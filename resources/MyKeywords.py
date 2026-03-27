# resources/MyKeywords.py

from robot.api.deco import keyword


class MyKeywords:

    @keyword
    def say_hello(self, name):
        """Keyword, który zwraca powitanie dla podanej osoby"""
        return f"Hello, {name}!"