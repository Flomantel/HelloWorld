class MiniInjector:
    def __init__(self):
        self.dependencies = {}

    def add_dependency(self, interface, implementation):
        self.dependencies[interface] = implementation

    def get(self, interface):
        implementation = self.dependencies.get(interface)

        if not implementation:
            raise ValueError(f"No dependency found {interface}")
        return implementation()
    
def run_app():
    injector = MiniInjector()
    controller = injector.get
    controller.run()