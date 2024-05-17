class ArithmeticPatternFinder:
    def find_pattern(self, numbers):
        # Vérifier si la différence entre chaque paire de nombres est constante
        diff = numbers[1] - numbers[0]
        for i in range(2, len(numbers)):
            if numbers[i] - numbers[i - 1] != diff:
                return None, None

        # Si la différence est constante, la séquence est une suite arithmétique
        # Déterminer la forme de la suite arithmétique
        if diff > 0:
            pattern_form = f"n+{diff}"
        elif diff < 0:
            pattern_form = f"n{diff}"
        else:
            pattern_form = "n"

        # Le motif est le nom et la forme de la suite arithmétique
        pattern = "Arithmetic " + f"({pattern_form})"
        # Le prochain élément est le dernier nombre plus la différence constante
        next_element = numbers[-1] + diff
        return pattern, next_element
