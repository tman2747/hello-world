# "!=" is not equal to "==" means equal to
whatisit = 3 * (2 - 1) == 4 - 1
print(whatisit)

# Boolean values True and False always need to be capitalized and do not have quotation marks.
my_baby_bool = "true"

print(type(my_baby_bool))

my_baby_bool_two = True

print(type(my_baby_bool_two))

# if statements

if 2 == 2 + 4 - 2 - 2:
    print("apple")


# is it dave checker
def dave_check(user_name):
    if user_name == "Dave":
        return "Get off my computer Dave!"
    if user_name == "angela_catlady_87":
        return "I know it is you Dave! Go away!"


# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

print(dave_check(user_name))


# Relational operators:
# Greater than: >
# Less than: <
# Greater than or equal to: >=
# Less than or equal to: <=

def age_checker(age):
    if age >= 21:
        return "can drink"
    if age < 21:
        return "cant drink"


Tristonsage = 22

print(age_checker(Tristonsage))


def greater_than(x, y):
    if x > y:
        return x
    if y > x:
        return y
    if x == y:
        return "These numbers are the same"


x = 3
y = 3

print(greater_than(x, y))


def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"
    if credits < 120:
        return "You dont have enough credits to graduate."


tristons_credits = 129
tristons_gpa = 1.95
print(graduation_reqs(tristons_credits))


# boolean Operators: and, or, not

def graduation_reqs(credits, gpa):
    if credits >= 120 and gpa >= 2:
        return "You have enough credits to graduate!"
    if credits < 120 or gpa < 2:
        return "You dont have a high enough GPA or enough Credits to graduate"



print(graduation_reqs(tristons_credits, tristons_gpa))

def graduation_mailer(credits,gpa):
    if credits >= 120 or gpa >= 2:
        return "This is an example for sending a email to someone that has a high enough gpa or enough credits aka Triston came up with this text :P"
print(graduation_mailer(tristons_credits,tristons_gpa))

# else statements:

def graduation_reqs(credits, gpa):
    if credits >= 120 and gpa >= 2:
        return "You have enough credits to graduate!"
    else:
        return "You do not meet the GPA or the credit requirement for graduation."
print(graduation_reqs(tristons_credits,tristons_gpa))

# else if statements:

def grade_converter(gpa):
    if gpa >= 4:
        return "A"
    elif gpa >= 3:
        return "B"
    elif gpa >= 2:
        return "C"
    elif gpa >= 1:
        return "D"
    else:
        return "F"
print(grade_converter(tristons_gpa))

# Try and Except Statements: still confused on this one :D
def raises_value_error():
  raise ValueError
try:
  raises_value_error()
except ValueError:
    print("You raised a ValueError!")