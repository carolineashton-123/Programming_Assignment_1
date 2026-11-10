"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""
import math
import data



# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: Counts the vowels in a string
    # TODO: Input(s): text - a string to check for vowels
    # TODO: Output: The number of vowels in the string
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: Finds nested lists that have exactly 2 elements
    # TODO: Input(s): items - a list of lists containing integers
    # TODO: Output: A new list containing only the lists with 2 elements
    result = []
    for inner_list in items:
        if len(inner_list)==2:
            result.append(inner_list)
    return result


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: Puts lists of 2 integers in ascending order
    # TODO: Input(s): items - a list of lists containing integers
    # TODO: Output: A new list with pairs in ascending order and other lists unchanged
    result = []

    for inner_list in items:
        if len(inner_list)==2 and inner_list[0] > inner_list[1]:
            result.append([inner_list[1], inner_list[0]])
        else:
            result.append(inner_list)
    return result


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: Adds two prices together
    # TODO: Input(s): first and second - two Price objects
    # TODO: Output: A new Price object with the total dollars and cents 
    total_cents = first.cents + second.cents
    total_dollars = first.dollars + second.dollars

    total_dollars += total_cents//100
    total_cents = total_cents % 100

    return data.Price(total_dollars, total_cents)


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: Calculates the area of a rectangle
    # TODO: Input(s): rectangle - a Rectangle object
    # TODO: Output: The area of the rectangle as a float
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    return width*height


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: Finds all books written by a specific author
    # TODO: Input(s): author - a string with the author's name  books - a list of Book objects
    # TODO: Output: A list of books written by that author
    result = []
    for book in books:
        if author in book.authors:
            result.append(book)
    return result


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: Finds the smallest circle that encloses a rectangle
    # TODO: Input(s): rectangle - a Rectangle object
    # TODO: Output: A new Circle object with the center and radius
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x)/2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y)/2

    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y

    radius = math.sqrt(width**2 + height**2)/2

    center = data.Point(center_x, center_y)
    return data.Circle(center, radius)


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: Finds employees who make less than the average pay
    # TODO: Input(s): employees - a list of Employee objects
    # TODO: Output: A list of names of employees with below average pay
    if len(employees)==0:
        return []

    total = 0
    for employee in employees:
        total += employee.pay_rate

    average = total/len(employees)

    result = []
    for employee in employees:
        if employee.pay_rate < average:
            result.append(employee.name)
    return result
