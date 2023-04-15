from unittest import TestCase, main
from custom_list import CustomList


class CustomListTests(TestCase):
    # setup
    def setUp(self):
        self.l = CustomList()
        self.l.lst = [9, -99999, "hellooo"]

    # init test
    def test_initialization(self):
        self.assertEqual(9, self.l.lst[0])
        self.assertEqual(-99999, self.l.lst[1])
        self.assertEqual("hellooo", self.l.lst[2])

    # append() test
    def test_append_successfully(self):
        self.assertEqual([9, -99999, "hellooo", 30], self.l.append(30))

    # remove() tests
    def test_remove_successfully(self):
        self.l.lst.append(50)
        self.assertEqual(self.l.lst.copy().remove(50), self.l.lst.remove(50))

    def test_remove_unsuccessfully(self):
        self.l = CustomList()
        self.l.lst = [10, 20, 30]
        value_to_remove = 500
        with self.assertRaises(Exception) as error:
            self.l.remove(value_to_remove)
        self.assertEqual(f"{value_to_remove} not found!", str(error.exception))

    # get() tests
    def test_get_successfully(self):
        self.l = CustomList()
        self.l.lst = [10, 'a']
        self.assertEqual('a', self.l.get(1))

    def test_get_unsuccessfully(self):
        l = CustomList()
        l.lst = []
        idx = 3
        with self.assertRaises(Exception) as error:
            self.l.get(idx)
        self.assertEqual(f"No such index: {idx}", str(error.exception))

    # pop() tests
    def test_pop_successfully(self):
        l = CustomList()
        l.lst = [10, 99]
        self.assertEqual(99, l.pop())

    def test_pop_unsuccessfully(self):
        l = CustomList()
        with self.assertRaises(Exception) as error:
            l.pop()
        self.assertEqual("List is empty!", str(error.exception))

    # index() tests
    def test_index_successfully(self):
        l = CustomList()
        l.lst = [1, 2, 3, 'b', 'a']
        value = 3
        self.assertEqual(2, l.index(value))

    def test_index_unsuccessfully(self):
        l = CustomList()
        l.lst = [1, 'a']
        value = 'c'
        with self.assertRaises(Exception) as error:
            l.index(value)
        self.assertEqual(f"{value} not in list!", str(error.exception))

    # count() test
    def test_count(self):
        l = CustomList()
        l.lst = [1, 1, 1, 3, 4, 5]
        value = 1
        self.assertEqual(3, l.count(value))

    # reverse() test
    def test_reverse(self):
        l = CustomList()
        self.assertEqual([], l.reverse())

    # copy() test
    def test_copy(self):
        l = CustomList()
        l.lst = [3, 'a', None]
        self.assertEqual([3, 'a', None], l.copy())

    # size() test
    def test_size(self):
        l = CustomList()
        l.lst = list(range(10))
        self.assertEqual(10, l.size())

    # add_first() test
    def test_add_first(self):
        l = CustomList()
        l.lst = ['is', 'a', 'string']
        self.assertEqual(['this', 'is', 'a', 'string'], l.add_first("this"))

    # dictionize() test
    def test_dictionize(self):
        l = CustomList()
        l.lst = [1, 2, 3, 4, 5]
        self.assertEqual({1: 2, 3: 4, 5: ' '}, l.dictionize())

    # move() test
    def test_move_successfully(self):
        l = CustomList()
        l.lst = [1, 2, 3, 4, 5, 6, 7]
        value = 5
        self.assertEqual([6, 7, 1, 2, 3, 4, 5], l.move(value))

    def test_move_unsuccessfully(self):
        '''this is a custom test: i.e. code won't throw an error without this case'''
        l = CustomList()
        l.lst = [1, 2, 3]
        value = 3
        with self.assertRaises(Exception) as error:
            l.move(value)
        self.assertEqual("List cannot be rearranged!", str(error.exception))

    # sum() tests
    def test_sum_numbers(self):
        l = CustomList()
        l.lst = [1, 2, 3, -10.5, 0]
        self.assertEqual(-4.5, l.sum())

    def test_sum_strings(self):
        '''Ignoring cases where Objects/Booleans in list'''
        l = CustomList()
        l.lst = [1, 2, 3, 4, "thelongestone"]
        self.assertEqual(len("thelongestone") + 10, l.sum())

    def test_sum_unsuccessfully(self):
        l = CustomList()
        with self.assertRaises(Exception) as error:
            l.sum()
        self.assertEqual("List is empty!", str(error.exception))

    # overbound() tests
    def test_overbound_successfully(self):
        l = CustomList()
        l.lst = [1, 2, 3, 4, 5, 6]
        self.assertEqual(6, l.overbound())

    def test_overbound_unsuccessfully(self):
        l = CustomList()
        with self.assertRaises(Exception) as error:
            l.overbound()
        self.assertEqual("List is empty!", str(error.exception))

    # underbound() tests
    def test_underbound_successfully(self):
        l = CustomList()
        l.lst = [-10, -9999, -43]
        self.assertEqual(-9999, l.underbound())

    def test_underbound_unsuccessfully(self):
        l = CustomList()
        with self.assertRaises(Exception) as error:
            l.underbound()
        self.assertEqual("List is empty!", str(error.exception))


if __name__ == "__main__":
    main()
