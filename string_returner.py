class StringReturner:
    def __init__(self, text="Hello, Python!"):
        self.text = text
    
    def get_string(self):
        return self.text

string_obj = StringReturner()
print(string_obj.get_string())