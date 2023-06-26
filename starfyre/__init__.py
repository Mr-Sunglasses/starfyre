import inspect

from starfyre.component import Component
from .transpiler import transpile

from .parser import RootParser



def create_component(pyml="", css="", js="", client_side_python=""):
    if client_side_python:
        new_js = transpile(client_side_python) + js
        js = new_js

    local_variables = inspect.currentframe().f_back.f_back.f_locals.copy()
    global_variables = inspect.currentframe().f_back.f_back.f_globals.copy()

    parser = RootParser(local_variables, global_variables, css, js)
    pyml = pyml.strip("\n").strip()
    parser.feed(pyml)
    parser.close()
    pyml_root = parser.get_root()

    if pyml_root is None:
        return Component("div", {}, [], {}, {}, uuid="store", js=js)

    return pyml_root


