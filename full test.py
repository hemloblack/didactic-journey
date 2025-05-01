number = 0
sum = 0
aa = []
while True:
    try:
        number = (int(input("enter posetive number:")))
        if number > 0:
            aa.append(number)
            sum += number
        else:

            print("pleas  dont enter number negetive! ")
            break
    except ValueError:
        print("error!!!!!!!!!!!!!!!!!!!!!!!!")
odd = 0
even = 0
for i in aa:
    print("Calculate the square", i, i*i)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even numbers:", even, "Number of odd numbers", odd)
print("sum of all number", sum)
print("full list", aa)
