from re import S


class Str(str):
    def __init__(self, object=''):
        self.data = object
    def __new__(cls, content):
        return str.__new__(cls, content)
    def is_contains_repeats(self,s):
        return s in self
    def polindrome(self):
        d=self.upper()
        return d==d[::-1]


if __name__ == "__main__":
    a = Str("polop")
    assert a.polindrome(), "should be True"
    assert a.is_contains_repeats("pol"), "should be True"