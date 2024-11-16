import unittest

import tests_12_3

run_tor_TS = unittest.TestSuite()
run_tor_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
run_tor_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tor_TS)
