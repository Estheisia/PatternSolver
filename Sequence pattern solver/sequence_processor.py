from pattern.arithmetic_pattern_finder import ArithmeticPatternFinder
from pattern.geometric_pattern_finder import GeometricPatternFinder
from pattern.square_pattern_finder import SquarePatternFinder
from pattern.cube_pattern_finder import CubePatternFinder
from pattern.power_pattern_finder import PowerPatternFinder
from pattern.prime_pattern_finder import PrimePatternFinder
from pattern.symetric_pattern_finder import SymmetricPatternFinder
from pattern.repetitive_pattern_finder import RepetitivePatternFinder
from pattern.symetrics_pattern_finder import SingleCentralSymmetricPatternFinder
from pattern.symetrics_pattern_finder import DoubleCentralSymmetricPatternFinder


class SequenceProcessor:
    def process_sequence(self, numbers):
        # Vérifier s'il y a suffisamment de nombres dans la séquence
        if len(numbers) < 3:
            return None, None

        # Créer une liste pour stocker les réponses récupérées
        responses = []

        # Créer une liste d'instances de chaque classe de recherche de motif
        pattern_finders = [
            ArithmeticPatternFinder(),
            GeometricPatternFinder(),
            #SquarePatternFinder(),
            #CubePatternFinder(),
            PowerPatternFinder(),
            PrimePatternFinder(),
            #SymmetricPatternFinder(),
            RepetitivePatternFinder(),
            SingleCentralSymmetricPatternFinder(),
            DoubleCentralSymmetricPatternFinder(),
        ]

        # Parcourir les instances de classes de recherche de motif
        for finder in pattern_finders:
            # Appeler la méthode de recherche de motif de chaque instance
            pattern, next_element = finder.find_pattern(numbers)

            # Ajouter la réponse à la liste des réponses
            responses.append((pattern, next_element))

        # Retourner le motif et le prochain élément
        return responses

