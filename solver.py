class Solver(object):
    """This class defines the ruleset"""

    def __init__(self):
        """The initializer for the class"""

    def is_horizontal_complete(self, input_array):
        return_value = False
        if len(input_array)==9:
            return_value = True
        return return_value

    def is_vertical_complete(self, input_array):
        return_value = False
        if len(input_array)==9:
            return_value = True
        return return_value

    def is_square_complete(self, input_array):
        return_value = False
        merged_array = []
        for value in input_array:
            merged_array.extend(value)

        if len(merged_array)==9:
            return_value = True
        return return_value
