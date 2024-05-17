class GeometricPatternFinder:
    def find_pattern(self, numbers):
        # Vérifier si le quotient entre chaque paire de nombres est constant
        ratio = numbers[1] / numbers[0]
        for i in range(2, len(numbers)):
            if numbers[i] / numbers[i - 1] != ratio:
                return None, None

        # Si le quotient est constant, la séquence est une suite géométrique
        # Déterminer la forme de la suite géométrique
        if ratio != 1:
            if ratio.is_integer():
                ratio = int(ratio)
            pattern_form = f"n*{ratio}"
        else:
            pattern_form = "n"

        # Le motif est la séquence de nombres avec la forme de la suite géométrique
        pattern = "Geometric " + f"({pattern_form})"

        # Le prochain élément est le dernier nombre multiplié par le ratio constant
        next_element = numbers[-1] * ratio

        # Si le prochain élément est un entier, retirer la virgule
        if next_element.is_integer():
            next_element = int(next_element)

        return pattern, next_element
