import sympy

class PrimePatternFinder:
    def find_pattern(self, numbers):
        prime_numbers = [num for num in numbers if sympy.isprime(num)]
        if prime_numbers != numbers:
            return None, None
        increasing_pattern, next_increasing_element = self.find_next_prime_pattern(numbers, 1)
        decreasing_pattern, next_decreasing_element = self.find_next_prime_pattern(numbers, -1)

        return increasing_pattern or decreasing_pattern, next_increasing_element or next_decreasing_element

    def find_next_prime_pattern(self, numbers, variation):
        for i in range(1, len(numbers)):
            if sympy.isprime(numbers[i]) and (numbers[i] - numbers[i - 1]) * variation >= 0:
                pattern = "Prime number"
                next_element = self.find_next_prime(numbers[-1] + variation, backward=(variation < 0))
                return pattern, next_element
        return None, None

    def find_next_prime(self, start, backward=False):
        step = -1 if backward else 1
        current = start
        while not sympy.isprime(current):
            current += step
        return current