numbers = [12, 7, 5, 64, 14, 9, 22, 3, 18, 27]
zoj = []
sumzoj = 0
fard = []
sumfard = 0

for i in numbers:
    if i % 2 == 0:
        zoj.append(i * i)#مربع اعداد زوج
        sumzoj += i
    else:
        fard.append(i * i)#مربع اعداد فرد
        sumfard += i

print(zoj, fard)
print(sumzoj)
print(sumfard)
