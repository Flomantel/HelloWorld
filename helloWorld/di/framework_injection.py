from injector import Injector, Inject
from mvc.model import GreetingModel
from mvc.views import GreetingView
from mvc.controller import GreetingController

class AppInjector(Injector):
    def configure(self, binder):
        binder.bind(GreetingModel, to=GreetingModel, scope=singleton)
        binder.bind(GreetingView, to=GreetingView, scope=singleton)
        binder.bind(GreetingController, to=GreetingController, scope=singleton)

def run_app(controller: GreetingController):
    controller.run()

if __name__ == '__main__':
    Injector = AppInjector()
    run_app = Injector.get(run_app)
    run_app()