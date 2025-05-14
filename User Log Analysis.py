def check_access(user_scores):
    for index, score in enumerate(user_scores, start=1):
        if 0 <= score <= 9:
            level = "Access Level: Low"
        elif 10 <= score <= 15:
            level = "Access Level: Medium"
        elif 16 <= score <= 20:
            level = "Access Level: High"
        else:
            level = "Invalid score"

        print(f"User {index}: {level}")

# لیست امتیازها
scores = [5, 12, 17, 21, -3]

# اجرای تابع
check_access(scores)
