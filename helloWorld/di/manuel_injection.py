from mvc.model import GreetingModel
from mvc.controller import GreetingController
from mvc.views import GreetingView

def run_app():
    model = GreetingModel()
    view = GreetingView()
    controller = GreetingController(model, view)
    controller.run()