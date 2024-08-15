import unittest
import runner
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    frize = False

    @unittest.skipIf(frize == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        name_runner = runner.Runner('NIK')
        for i in range(10):
            name_runner.walk()
        self.assertEqual(name_runner.distance, 50)

    @unittest.skipIf(frize == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        name_runner = runner.Runner('ANDREY')
        for i in range(10):
            name_runner.run()
        self.assertEqual(name_runner.distance, 100)

    @unittest.skipIf(frize == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        object_runner_1 = runner.Runner('NIK')
        object_runner_2 = runner.Runner('ANDREY')
        for i in range(10):
            object_runner_1.walk()
            object_runner_2.run()
        self.assertNotEqual(object_runner_1.distance, object_runner_2.distance)


class TournamentTest(unittest.TestCase):
    all_results = None
    frize = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усэйн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    @unittest.skipIf(frize == False, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        first_run = runner_and_tournament.Tournament(90, self.usain, self.nik)
        result = first_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @unittest.skipIf(frize == False, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        second_run = runner_and_tournament.Tournament(90, self.andrey, self.nik)
        result = second_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result

    @unittest.skipIf(frize == False, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        third_run = runner_and_tournament.Tournament(90, self.andrey, self.usain, self.nik)
        result = third_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == 'Ник')
        self.all_results[result.values()] = result


if __name__ == '__main__':
    unittest.main()
