class GreetingModel():
    def __init__(self):
        self.name = ""

    def set_name(self, name):
        self.name = name 

    def get_greeting(self, name):
        return f"hello {self.name}"