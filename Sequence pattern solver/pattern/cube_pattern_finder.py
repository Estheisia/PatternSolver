class CubePatternFinder:
    def find_pattern(self, numbers):
        increasing_pattern, next_increasing_element = self.find_pattern_for_sequence(numbers, self.find_increasing_pattern)
        if increasing_pattern:
            return increasing_pattern, next_increasing_element

        decreasing_pattern, next_decreasing_element = self.find_pattern_for_sequence(numbers, self.find_decreasing_pattern)
        if decreasing_pattern:
            return decreasing_pattern, next_decreasing_element

        return None, None

    def find_pattern_for_sequence(self, numbers, pattern_function):
        pattern, next_element = pattern_function(numbers)
        return pattern, next_element

    def find_increasing_pattern(self, numbers):
        if self.is_increasing_square_sequence(numbers):
            pattern_form = "n^3"
            pattern = "Cube Increasing " + f"({pattern_form})"
            next_element = (numbers[-1] ** (1 / 3) + 1) ** 3
            if next_element.is_integer():
                next_element = int(next_element)
            return pattern, next_element
        return None, None

    def find_decreasing_pattern(self, numbers):
        if self.is_decreasing_square_sequence(numbers):
            pattern_form = "n^3"
            pattern = "Cube Decreasing " + f"({pattern_form})"
            next_element = (numbers[-1] ** (1 / 3) - 1) ** 3
            if next_element.is_integer():
                next_element = int(next_element)
            return pattern, next_element
        return None, None

    def is_increasing_square_sequence(self, numbers):
        for i, num in enumerate(numbers):
            if round(num ** (1 / 3)) ** 3 != num or (i > 0 and num <= numbers[i - 1]):
                return False
        return True

    def is_decreasing_square_sequence(self, numbers):
        cube_root = int(round(numbers[0]**(1/3)))
        for i, num in enumerate(numbers):
            expected = (cube_root - i) ** 3
            if num != expected:
                return False
        return True
