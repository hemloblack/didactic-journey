try:
    score=int(input("نمره خود راوارد کنید:"))
    if score<10:
        print("ضعیف")
    elif 10<=score<=14:
        print("قابل قبول")
    elif 15<=score<=17:
        print("خوب")
    elif 18<=score<=20:
        print("خیلی خوب")
    else:print("عدد وارد شده نا معتبر است")
    
except ValueError:
    print("وروودی نا معتبر!!!!")