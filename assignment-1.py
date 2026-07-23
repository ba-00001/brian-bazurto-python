"""Assignment 1 - Python Basics: Profile Card Builder.

Five sections, each adding one new idea on top of the last:
variables and types, input and maths, type conversion, formatted output,
and finally a profile card that uses all of it together.
"""

# Kept in one place at the top so both age calculations use the same year.
# If I hardcoded 2026 in two spots I'd eventually update one and not the other.
current_year = 2026


# ---------------------------------------------------------------------------
# Section 1: Variables and Types
# ---------------------------------------------------------------------------
print("--- Section 1: Variables and Types ---")

# One variable of each of the four basic types.
name = "Alex Rivera"  # str  - text, so it goes in quotes
age = 27  # int   - whole number, no decimal point
height = 5.9  # float - has a decimal point, so Python stores it differently
is_student = True  # bool  - only ever True or False, no quotes

# type() reports what Python decided each value is. Printing the value next to
# its type makes it obvious that 27 and "27" would NOT be the same thing.
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# ---------------------------------------------------------------------------
# Section 2: User Input and Math
# ---------------------------------------------------------------------------
print()  # blank line so the sections don't run into each other
print("--- Section 2: User Input and Math ---")

user_name = input("What is your name? ")
birth_year = input("What year were you born? ")

# input() always hands back a string, even when the person typed digits.
# So birth_year is the text "1998", not the number 1998, and subtracting it
# from an int would raise:
#   TypeError: unsupported operand type(s) for -: 'int' and 'str'
# int() converts the text into a number first, which makes the maths legal.
approximate_age = current_year - int(birth_year)

# f-string: the f before the quote lets me drop variables straight into the
# text inside {}, instead of gluing strings together with +.
print(f"Hi, {user_name}! You are approximately {approximate_age} years old.")


# ---------------------------------------------------------------------------
# Section 3: Type Conversion and f-strings
# ---------------------------------------------------------------------------
print()
print("--- Section 3: Type Conversion and f-strings ---")

# float() rather than int() here because these should accept decimals.
# Reading it inside out: input() asks and returns text, float() converts it.
first_number = float(input("Enter a number: "))
second_number = float(input("Enter another number: "))

# Both are numbers now, so * means multiply. If they were still strings this
# would either fail or do something strange like repeating the text.
product = first_number * second_number

# Note that typing a whole number like 4 prints back as 4.0 - float() turned
# it into a decimal.
print(f"{first_number} × {second_number} = {product}")


# ---------------------------------------------------------------------------
# Section 4: Formatted Receipt
# ---------------------------------------------------------------------------
print()
print("--- Section 4: Formatted Receipt ---")

# No input() in this section - everything comes from variables.
item = "Python textbook"
price = 29.99
quantity = 2

# The total is worked out from the variables rather than typed in, so changing
# the price or quantity above updates the receipt without touching this line.
total = price * quantity

print("===========================")
print("        RECEIPT")
print("===========================")
# The spaces after the colons line the values up into a column.
print(f"Item:      {item}")
# :.2f forces exactly two decimal places, so 29.99 stays 29.99 and a price
# like 30.0 would print as 30.00 instead of looking wrong for money.
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("===========================")


# ---------------------------------------------------------------------------
# Section 5: Mini-Project - Profile Card
# ---------------------------------------------------------------------------
print()
print("--- Section 5: Profile Card ---")

# Five separate questions. Each input() waits for Enter before moving on.
profile_name = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("Tell me one fun fact about yourself: ")

# Converting straight away this time instead of storing the text and
# converting later - fewer places to forget.
profile_birth_year = int(input("What year were you born? "))

# The assignment says to work the age out rather than ask for it directly.
profile_age = current_year - profile_birth_year

print()
print("╔══════════════════════════════╗")
print(f"      PROFILE: {profile_name}")
print("╚══════════════════════════════╝")
# Labels padded to the same width so the values start in the same column.
print(f"Hometown:   {hometown}")
print(f"Hobby:      {hobby}")
print(f"Fun fact:   {fun_fact}")
print(f"Age:        {profile_age}")
