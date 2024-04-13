from unittest import TestCase, main

# from testing.List.extended_list import IntegerList


class TestList(TestCase):
    def setUp(self):
        self.i_list = IntegerList(1, 'к', 2, '%', 3)

    def test_correct__init__and_get_data_method(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())

    def test_try_to_add_non_integer_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.add('k')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_with_integer_expect_element_to_append_to_the_list(self):
        self.i_list.add(4)

        self.assertEqual([1, 2, 3, 4], self.i_list.get_data())

    def test_try_to_remove_item_with_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_item_with_correct_index(self):
        self.i_list.remove_index(0)

        self.assertEqual([2, 3], self.i_list.get_data())

    def test_try_get_item_with_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_item_with_correct_index(self):
        result = self.i_list.get(0)

        self.assertEqual(1, result)

    def test_try_to_insert_item_with_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(10, 1)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_try_to_insert_a_non_integer_with_correct_index_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(2,'k')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_item_with_correct_index_and_correct_data(self):
        self.i_list.insert(1, 5)

        self.assertEqual([1, 5, 2, 3], self.i_list.get_data())

    def test_get_biggest_expects_biggest_integer(self):
        result = self.i_list.get_biggest()

        self.assertEqual(3, result)

    def test_get_index_expects_the_index_of_an_element(self):
        result = self.i_list.get_index(2)

        self.assertEqual(1, result)


if __name__ == '__main__':
    main()