r = int(input('Radius: '))
sign = '*'



#---------------------------------------------------------------
while True: 
    slon = input('Kupi slona.   ')
    if slon == 'pokupaju':
        break

siamese = 'Leah'
for letter in siamese:
    print(letter)

#----------------------------------------------------------------
cats = ['seamis', 'black', 'white', 'maincoon', 'red', 'red','red','red','red','red','red']
count = 0
for cat in cats:
    if cat == 'red':
        count += 1
print(count)   

#---------------------------------------------------------
list_ = []
print(type(list_))
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 5:
        print(number)
        break

#---------------------------------------------
for y in range(10):
    for x in range(10):
        print(x, end=" ")
    print()

#----------------------------------------------
n = float(input('Enter a number: '))
x = 0
while x < n:
    x += 1
    s = n * (n + 1) / 2
print(s)

#-----------------------------------------------
x = 0
count = 0
while x <= 5:
    number = float(input('Enter a number: '))
    if number.is_integer():
        count += 1
print(count)

#----------------------------------
x = 0

while x <= 10:
    print(x)
    x += 1  # same as x = x + 1

while True:
    print("Ctrl+C - TO STOP!!!!!")
    break