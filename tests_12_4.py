import logging
import unittest
import rt_with_exceptions as rt


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            r1 = rt.Runner('Name', -7)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner")
            logging.error('Ошибка', exc_info=True)

    def test_run(self):
        try:
            logging.info('"test_run" выполнен успешно')
            r2 = rt.Runner(('Den', 5), 20)
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)

        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.error('Ошибка', exc_info=True)


if __name__ == "__main__":
    unittest.main()
