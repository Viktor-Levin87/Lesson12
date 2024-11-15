import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Test for walk function in runner"""
        walk = runner.Runner('Вася')
        for i in range(0, 10):
            walk.walk()
        self.assertEqual(walk.distance, 50)

    def test_run(self):
        """Test for run function in runner"""
        run = runner.Runner('Петя')
        for i in range(0, 10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        """Test for function run and walk in runner"""
        run = runner.Runner('Петя')
        walk = runner.Runner('Вася')
        for i in range(0, 10):
            run.run()
            walk.walk()
        self.assertNotEqual(run.distance, walk.distance)


if __name__ == '__main__':
    unittest.main()
