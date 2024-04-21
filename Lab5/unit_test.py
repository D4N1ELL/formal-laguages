from main import Grammar
import unittest


class TestGrammar(unittest.TestCase):
    def setUp(self):
        self.g = Grammar()
        self.P1, self.P2, self.P3, self.P4, self.P5 = self.g.ReturnProductions()

    def test_remove_epsilon(self):
        # Test RemoveEpsilon method
        expected_result = {'S': ['abAB', 'abA'], 'A': ['aSab', 'BS', 'aA', 'b', 'abAB', 'abA'],
                           'B': ['BA', 'ababB', 'b', 'abab', 'aSab', 'BS', 'aA', 'b', 'abAB', 'abA'], 'C': ['AS']}
        self.assertEqual(self.P1, expected_result)

    def test_eliminate_unit_prod(self):
        # Test EliminateUnitProd method
        expected_result = {'S': ['abAB', 'abA'], 'A': ['aSab', 'BS', 'aA', 'b', 'abAB', 'abA'],
                           'B': ['BA', 'ababB', 'b', 'abab', 'aSab', 'BS', 'aA', 'b', 'abAB', 'abA'], 'C': ['AS']}
        self.assertEqual(self.P2, expected_result)

    def test_eliminate_inaccesible(self):
        # Test EliminateInaccesible method
        expected_result = {'S': ['abAB', 'abA'], 'A': ['aSab', 'BS', 'aA', 'b', 'abAB', 'abA'],
                           'B': ['BA', 'ababB', 'b', 'abab', 'aSab', 'BS', 'aA', 'b', 'abAB', 'abA']}
        self.assertEqual(self.P3, expected_result)

    def test_remove_unprod(self):
        # Test RemoveUnprod method
        expected_result = {'S': ['abAB', 'abA'], 'A': ['aSab', 'BS', 'aA', 'b', 'abAB', 'abA'],
                           'B': ['BA', 'ababB', 'b', 'abab', 'aSab', 'BS', 'aA', 'b', 'abAB', 'abA']}
        self.assertEqual(self.P4, expected_result)

    def test_obtain_cnf(self):
        # Test ObtainCNF method
        expected_result = {'S': ['CD', 'EF'], 'A': ['GC', 'BS', 'EH', 'b', 'CD', 'EF'], 'B': ['BA', 'CI', 'b', 'CC', 'GC', 'BS', 'EH', 'b', 'CD', 'EF'],
                           'C': ['ab'], 'D': ['AB'], 'E': ['a'], 'F': ['bA'], 'G': ['aS'], 'H': ['A'], 'I': ['abB']}
        self.assertEqual(self.P5, expected_result)


if __name__ == '__main__':
    unittest.main()