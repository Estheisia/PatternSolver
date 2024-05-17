class RepetitivePatternFinder:
    def find_pattern(self, numbers): return None, None
    def find_pattern2(self, numbers):
        n = len(numbers)
        i = 0
        while i < n:
            start_index = i
            current_value = numbers[i]
            # Trouver le prochain élément différent
            while i < n and numbers[i] == current_value:
                i += 1
            # Si nous avons atteint la fin de la séquence, arrêter
            if i == n:
                break
            # Vérifier si la longueur de la séquence de la deuxième valeur est identique
            if n % (i - start_index) == 0:
                first_value_sequence_length = i - start_index
                first_value_sequence = numbers[start_index:i]
                second_value_sequence_length = 0
                # Trouver la longueur de la séquence de la deuxième valeur
                for j in range(i, n, first_value_sequence_length):
                    if numbers[j:j + first_value_sequence_length] != first_value_sequence:
                        second_value_sequence_length = j - i
                        break
                if second_value_sequence_length == 0:
                    second_value_sequence_length = n - i
                # Vérifier si les longueurs des séquences sont identiques
                if n % second_value_sequence_length == 0:
                    is_repetitive = True
                    for j in range(i + second_value_sequence_length, n, second_value_sequence_length):
                        if numbers[j:j + second_value_sequence_length] != numbers[i:i + second_value_sequence_length]:
                            is_repetitive = False
                            break
                    if is_repetitive:
                        next_element_index = i + second_value_sequence_length
                        next_element = numbers[next_element_index]
                        return "Repetitive", next_element
            i += 1
        return None, None

    def find_pattern2(self, numbers):
        n = len(numbers)
        i = 0
        while i < n:
            start_index = i
            current_value = numbers[i]
            # Trouver le prochain élément différent
            while i < n and numbers[i] == current_value:
                i += 1
            # Si nous avons atteint la fin de la séquence, arrêter
            if i == n:
                break
            # Vérifier si la longueur de la séquence de la deuxième valeur est identique
            if n % (i - start_index) == 0:
                first_value_sequence_length = i - start_index
                first_value_sequence = numbers[start_index:i]
                second_value_sequence_length = 0
                # Trouver la longueur de la séquence de la deuxième valeur
                for j in range(i, n, first_value_sequence_length):
                    if numbers[j:j+first_value_sequence_length] != first_value_sequence:
                        second_value_sequence_length = j - i
                        break
                if second_value_sequence_length == 0:
                    second_value_sequence_length = n - i
                # Vérifier si les longueurs des séquences sont identiques
                if n % second_value_sequence_length == 0:
                    is_repetitive = True
                    for j in range(i + second_value_sequence_length, n, second_value_sequence_length):
                        if numbers[j:j+second_value_sequence_length] != numbers[i:i+second_value_sequence_length]:
                            is_repetitive = False
                            break
                    if is_repetitive:
                        return second_value_sequence_length, n // second_value_sequence_length
            i += 1
        return None