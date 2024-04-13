from unittest import TestCase, main

# from testing.worker.worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker('SomeGuy', 1200, 100)

    def test_for_correct_init(self):
        self.assertEqual('SomeGuy', self.worker.name)
        self.assertEqual(1200, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_try_to_work_without_energy_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_with_enough_energy_expect_money_raise_and_decrease_energy(self):
        self.worker.work()

        self.assertEqual(1200, self.worker.money)
        self.assertEqual(99, self.worker.energy)

    def test_rest_expect_energy_raise(self):
        self.worker.energy = 0
        self.worker.rest()

        self.assertEqual(1, self.worker.energy)

    def test_get_info(self):
        self.assertEqual(f'SomeGuy has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    main()