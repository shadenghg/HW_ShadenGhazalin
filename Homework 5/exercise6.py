class Strings:
    def __init__(self):
        self._str = ""

    def get_String(self):
        self._str = input("Please enter a string: ")

    def print_String(self):
        print(f"The upper case of your string: {self._str.upper()}")


_str = Strings()
_str.get_String()
_str.print_String()
