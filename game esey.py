import random
ghaechi=1
kaghaz=2
sang=3
round=random.randint(1,3)
javab=input("1=sang \n 2=kaghaz \n 1=ghaechi")
if round==javab:
    print("مساوی")
elif javab==ghaechi and round==kaghaz:
    print("شما قیچی اوردید و بردید")
elif javab==kaghaz and round==sang:
    print("شماکاغذ اوردید و بردید")
elif javab==sang and round==ghaechi:
    print("شما سنگ اوردید و بردید")
elif javab==kaghaz and round==ghaechi:
    print("شماکاغذ اوردید و باختید")
elif javab==kaghaz and round==sang:
    print("شماکاغذ اوردید و بردید")