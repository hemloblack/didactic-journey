def check_level(score):
    if score<10:
        level="ضعیف"
    elif 10<score<15:
        level="متوسط"
    elif score>10:
        level="حرفه ای" 
    else:
        level="داده نا درست"
        
    return level
    
print(check_level(int(input("enter score:"))))