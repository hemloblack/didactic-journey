number = [2, 4, 8, 16, 32, 64, 77]  # لیست عددی تعریف شده

for i in range(len(number)):  # حلقه از 0 تا تعداد عناصر لیست اجرا می‌شود
    number[i] *= 2  # مقدار هر عدد در لیست را دو برابر می‌کند
    print(number[i])  # مقدار جدید هر عدد را چاپ می‌کند

print(len(number))  # تعداد عناصر لیست را چاپ می‌کند
