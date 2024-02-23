class GreetingController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        name = self.view.get_name()
        self.model.set_name(name)
        greeting = self.model.get_greeting(name)
        self.view.display_greeting(greeting)