import unittest

import runner_and_tournament

import runner


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        self.tournament1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.all_result = self.tournament1.start()
        last_name = self.all_result[max(self.all_result.keys())]
        self.assertTrue(last_name == 'Ник')
        TournamentTest.all_result[0] = self.all_result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        self.tournament2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.all_result = self.tournament2.start()
        last_name = self.all_result[max(self.all_result.keys())]
        self.assertTrue(last_name == 'Ник')
        TournamentTest.all_result[1] = self.all_result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        self.tournament3 = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_result = self.tournament3.start()
        last_name = self.all_result[max(self.all_result.keys())]
        self.assertTrue(last_name == 'Ник')
        TournamentTest.all_result[2] = self.all_result

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_result.values():
            print(i)
        pass


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
#        """Test for walk function in runner"""
        walk = runner.Runner('Вася')
        for i in range(0, 10):
            walk.walk()
        self.assertEqual(walk.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
#        """Test for run function in runner"""
        run = runner.Runner('Петя')
        for i in range(0, 10):
            run.run()
        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
#        """Test for function run and walk in runner"""
        run = runner.Runner('Петя')
        walk = runner.Runner('Вася')
        for i in range(0, 10):
            run.run()
            walk.walk()
        self.assertNotEqual(run.distance, walk.distance)


if __name__ == '__main__':
    unittest.main()
