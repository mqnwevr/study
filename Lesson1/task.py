name = input('Enter your name: ').capitalize()
if name == 'Juku':
    age = int(input('Enter your age: '))
    price = 5
    if age < 0 and age > 100:
        if age < 6:
            ticket = 0
        elif age <= 14:
            ticket = price - (price * 0.8)
        elif age <= 65:
            ticket = price
        else:
            ticket = price - (price * 0.6)
        print('Price for Juku is', ticket, '$')
    else:
        print('Juku, are you sure, that you are', age, 'years old?')
else:
    print('You are not Yuku!')

# -----------------------------------------------------
print('  @..@')
print(' (----)')
print(' (\__/)')
print('^^ "" ^^')

print("""
       @..@
      (----)
     (\__/)
    ^^ "" ^^""")
# -----------------------------------------------------
quantity = 10
print('There are', quantity, 'candies on the table.')
candies = int(input('Take a few candies. '))

while True:
    leftover = quantity - candies

    if candies > quantity:
        print('There are only', quantity, '!')
        candies = int(input('Take a few candies. '))
    else:
        if leftover < 2:
            candy = 'candy'
        else:
            candy = 'candies'

        print('On the table had left', leftover, candy)
        break

# --------------------------------------------------------
name = input('your name ')
greet = 'Hello world! Greetings ' + name + '!'
age = int(input('your age '))
print(greet + 'You are ' + age + ' years old.')
# ---------------------------------------------------------
age = 27
name = 'Marina'
length = 170.1
school = False
print(type(age), type(name), type(length), type(school))
