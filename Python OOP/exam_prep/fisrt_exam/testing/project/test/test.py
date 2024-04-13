from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.railway = RailwayStation('SomeName')

    def test_correct_init(self):
        self.assertEqual('SomeName', self.railway.name)
        self.assertEqual(deque(), self.railway.arrival_trains)
        self.assertEqual(deque(), self.railway.departure_trains)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.railway.name = 'N'

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.railway.new_arrival_on_board("SomeTrain")

        self.assertEqual(deque(["SomeTrain"]), self.railway.arrival_trains)

    def test_train_has_arrived_but_there_trains_arrived_before_this_train(self):
        self.railway.arrival_trains = deque(['FirstTrain'])

        result = self.railway.train_has_arrived('SecondTrain')
        expected_message = f"There are other trains to arrive before SecondTrain."

        self.assertEqual(expected_message, result)

    def test_train_has_arrived_and_theres_no_trains_before_it(self):
        self.railway.arrival_trains = deque(['SomeTrain'])
        result = self.railway.train_has_arrived('SomeTrain')
        expected_message = f"SomeTrain is on the platform and will leave in 5 minutes."

        self.assertEqual(deque(), self.railway.arrival_trains)
        self.assertEqual(deque(['SomeTrain']), self.railway.departure_trains)
        self.assertEqual(expected_message, result)

    def test_train_has_left_with_existing_train(self):
        self.railway.departure_trains = deque(['SomeTrain'])
        result = self.railway.train_has_left('SomeTrain')

        self.assertEqual(deque(), self.railway.departure_trains)
        self.assertTrue(result)

    def test_train_has_left_with_non_existing_train(self):
        self.railway.departure_trains = deque(['FirstTrain'])
        result = self.railway.train_has_left('SecondTrain')

        self.assertEqual(deque(['FirstTrain']), self.railway.departure_trains)
        self.assertFalse(result)


if __name__ == '__main__':
    main()