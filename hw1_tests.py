"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest
import math
import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        
        self.assertEqual(hw1.vowel_count("AEiou"),5)

    def test_vowel_count_empty_string(self):
        
        self.assertEqual(hw1.vowel_count(""),0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        
        items = [[1],[1,2],[1,2,3],[],[4,5,6,7]]
        self.assertEqual(hw1.short_lists(items), [[1,2]])

    def test_short_lists_no_matching_lengths(self):
        
        items = [[1,2,3],[4,5,6,7]]
        self.assertEqual(hw1.short_lists(items),[])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        
        items = [[3,1],[1,4],[9,2]]
        self.assertEqual(hw1.ascending_pairs(items),[[1,3],[1,4],[2,9]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        
        items = [[3],[4,1,6],[],[7,2],[8,9]]
        self.assertEqual(hw1.ascending_pairs(items),[[3],[4,1,6],[],[2,7],[8,9]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        
        first = data.Price(2,30)
        second = data.Price(3,40)
        self.assertEqual(hw1.add_prices(first, second), data.Price(5,70))

    def test_add_prices_with_cents_carry(self):
        
        first = data.Price(2,75)
        second = data.Price(3,50)
        self.assertEqual(hw1.add_prices(first, second), data.Price(6,25))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        
        rectangle = data.Rectangle(data.Point(1,5), data.Point(4,1))
        self.assertAlmostEqual(hw1.rectangle_area(rectangle),12.0)

    def test_rectangle_area_negative_coordinates(self):
        
        rectangle = data.Rectangle(data.Point(-3,4), data.Point(2,-2))
        self.assertAlmostEqual(hw1.rectangle_area(rectangle),30.0)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        
        book1 = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = data.Book(['Neil Gaiman'], 'Coraline')
        book3 = data.Book(['Frank Herbert'], 'Dune')
        books = [book1, book2, book3]

        self.assertEqual(hw1.books_by_author('Neil Gaiman', books), [book1, book2])

    def test_books_by_author_no_matches(self):
        
        book1 = data.Book(['Neil Gaimen', 'Terry Pratchett'], 'Good Omens')
        book2 = data.Book(['Neil Gaimen'], 'Coraline')
        books = [book1, book2]

        self.assertEqual(hw1.books_by_author('Jane Austen', books), [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        
        rectangle = data.Rectangle(data.Point(0,2), data.Point(2,0))
        expected = data.Circle(data.Point(1,1), math.sqrt(2))
        self.assertEqual(hw1.circle_bound(rectangle), expected)

    def test_circle_bound_non_square_rectangle(self):
        
        rectangle = data.Rectangle(data.Point(0,4), data.Point(6,0))
        expected = data.Circle(data.Point(3,2), math.sqrt(13))
        self.assertEqual(hw1.circle_bound(rectangle), expected)

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        
        employees = [
            data.Employee('Neil', 10),
            data.Employee('Terry', 20),
            data.Employee('Sam', 30),
            data.Employee('Alex', 15)
        ]
        self.assertEqual(hw1.below_pay_average(employees), ['Neil', 'Alex'])

    def test_below_pay_average_empty_list(self):
        
        self.assertEqual(hw1.below_pay_average([]),[])


if __name__ == '__main__':
    unittest.main()
