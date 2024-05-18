import math
import statistics

class SymmetricPatternFinder:
    def find_pattern(self, numbers, tested_central_indices=None):
        if tested_central_indices is None:
            tested_central_indices = []

        for i in range(len(numbers)):
            if numbers[i] in numbers[i+1:]:
                index = numbers[i+1:].index(numbers[i]) + i + 1
                central_index_floor = math.floor(statistics.mean([index, i]))
                central_index_ceil = math.ceil(statistics.mean([index, i]))

                # Vérifier que les indices centraux n'ont pas été testés et qu'ils sont identiques
                if central_index_floor in tested_central_indices and central_index_ceil in tested_central_indices:
                    continue
                if numbers[central_index_ceil] != numbers[central_index_floor]:
                    continue

                # Vérifier la symétrie
                is_symmetric = self.is_symmetric_sequence(numbers, central_index_floor, central_index_ceil)

                if is_symmetric:
                    pattern = "Symmetric"
                    next_floor_index = len(numbers) - central_index_floor
                    next_ceil_index = len(numbers) - central_index_ceil

                    if len(numbers[:central_index_floor]) <= len(numbers[central_index_ceil + 1:]):
                        next_element = "Complete"
                    else:
                        next_element = numbers[central_index_floor - math.floor(statistics.mean([next_floor_index, next_ceil_index]))]
                    return pattern, next_element
                else:
                    # Ajouter les indices centraux testés et appeler récursivement find_pattern
                    new_tested_central_indices = tested_central_indices + [central_index_floor, central_index_ceil]
                    result = self.find_pattern(numbers, new_tested_central_indices)
                    if result is not None:
                        return result

        return None, None

    def is_symmetric_sequence(self, numbers, central_index_floor, central_index_ceil):
        left_sequence = numbers[:central_index_floor]
        right_sequence = numbers[central_index_ceil + 1:]

        # Si une des deux séquences est vide
        if len(left_sequence) == 0 or len(right_sequence) == 0:
            return False
        # Vérifier que la plus petite des deux est bien la symétrie de l'autre
        min_length = min(len(left_sequence), len(right_sequence))
        if left_sequence[-min_length:] != right_sequence[:min_length][::-1]:
            return False
        # Vérifier que dans la séquence la plus longue, seuls les éléments asymétriques sont présents
        if len(right_sequence) <= min_length:
            return True

        return False
# 1 2 3 4 5 3 2 1 est reconnue à tort