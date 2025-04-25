fruits=["apple","orange","strawberries"]
print (fruits[0])
fruits[1]="benana"#جایگزین کردن بر اسا اندیس
print(fruits)
fruits.append("coconat")#اضافه کردن به ارایه
fruits.remove("strawberries") #حذف بر اساس اسم
del fruits[1]#حذف بر اساس اندیس
print (fruits)

#تمرین بعدی با ارایه
animal=["tiger","shampanze","elphent"]
animal.append("grizly")
animal.remove("tiger")
print(animal)

#تمرین ارایه بعدی
number=[11,25,64,17,90]
number[1]=33
number.append(23)
del number[2]
print(number)