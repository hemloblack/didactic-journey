def check_access(score):
    if 0<=score<=9:
        level="Access Level: Low"
    elif 10<=score<=15:
      level="Access Level: Medium"
    elif 16<=score<=20:
        level="Access Level: High"
    else: level="Invalid score"
    return level

print(check_access(int(input("ente score:"))))