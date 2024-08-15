import unittest
import test_12_2


runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)