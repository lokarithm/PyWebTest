from ..helpers.dom_type import DomType
from ..errors.invalid_dom_type import InvalidDomTypeError


class TestCaseStep:
    def __init__(self, dom_type, selector, validate_type, validation_value, action, action_input):
        self.dom_type = dom_type
        self.selector = selector
        self.validate_type = validate_type
        self.validation_value = validation_value
        self.action = action
        self.action_input = action_input
