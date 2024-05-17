import math

class PowerPatternFinder:
    def find_pattern(self, numbers):
        power, is_power = self.find_power(numbers)
        pattern_inc, next_element_inc = self.common_find_pattern(numbers, power, 1) if (is_power and self.is_increasing_power_sequence(numbers, power)) else (None, None)
        pattern_dec, next_element_dec = self.common_find_pattern(numbers, power, -1) if (is_power and self.is_decreasing_power_sequence(numbers, power)) else (None, None)
        if pattern_inc is not None:
            return pattern_inc, next_element_inc
        return pattern_dec, next_element_dec

    def common_find_pattern(self, numbers, power, variation):
        pattern_form = "n^" + f"{power}"
        pattern = "Power " + f"({pattern_form})"
        next_element = (numbers[-1] ** (1 / power) + variation) ** power
        if next_element.is_integer():
            next_element = int(next_element)
        return pattern, next_element

    def is_increasing_power_sequence(self, numbers, power):
        for i, num in enumerate(numbers):
            if round(num ** (1 / power)) ** power != num or (i > 0 and num <= numbers[i - 1]):
                return False
        return True

    def is_decreasing_power_sequence(self, numbers, power):
        root = int(round(numbers[0]**(1/power)))
        for i, num in enumerate(numbers):
            expected = (root - i) ** power
            if num != expected:
                return False
        return True

    def find_power(self, numbers):
        for i in range(2, 15):
            power = math.log(numbers[1], i)
            if power.is_integer() and power != 0 and power != 1:
                if self.is_increasing_power_sequence(numbers, int(power)):
                    return int(power), True
                if self.is_decreasing_power_sequence(numbers, int(power)):
                    return int(power), True
        return None, False
