import unittest

import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    def test_tournament1(self):
        self.tournament1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.all_result = self.tournament1.start()
        last_name = self.all_result[max(self.all_result.keys())]
        self.assertTrue(last_name == 'Ник')
        TournamentTest.all_result[0] = self.all_result

    def test_tournament2(self):
        self.tournament2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.all_result = self.tournament2.start()
        last_name = self.all_result[max(self.all_result.keys())]
        self.assertTrue(last_name == 'Ник')
        TournamentTest.all_result[1] = self.all_result

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


if __name__ == '__main__':
    unittest.main()
