from app.src import *

import unittest


class test_scan_pwm(unittest.TestCase):
    """
    Class qui contient tout les tests du fichier
    'scan_pwm.py'
    * pseudo poids fixe a: 0.1
    * sueuil fixe a: -2.0
    """
    def test_MA0083_NM_007389(self):
        """
        >> python src/scan_pwm.py MA0083.jaspar NM_007389 500 -20
        """
        # scan_pwm.main("MA0083.jaspar", "NM_007389", 500, -20)
        

    def test_MA0114_NM_007389(self):
        """
        >> python src/scan_pwm.py MA0114.jaspar NM_007389 500 -20
        """
        pass

    def test_MA0056_NM_007389(self):
        """
        >> python src/scan_pwm.py MA0056.jaspar NM_007389 500 -20
        """
        pass

if __name__ == '__main__':
    unittest.main()