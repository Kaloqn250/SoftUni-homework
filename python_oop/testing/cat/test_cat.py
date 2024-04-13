from unittest import TestCase, main

# from testing.cat.cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat('Jivko')

    def test_correct__init__(self):
        self.assertEqual('Jivko', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_make_cat_eat_when_it_is_fed_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_make_cat_eat_when_it_is_not_fed_expect_size_increase(self):
        expected_size = self.cat.size + 1
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_make_cat_sleep_when_it_is_not_sleepy_raises_exception(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_make_cat_sleep_when_it_is_fed(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()