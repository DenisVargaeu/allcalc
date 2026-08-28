def check (score):
    if score >= 90:
        grade = "Excellent"
    elif score >= 75:
        grade = "Very Good"
    elif score >= 50:
        grade = "Good"
    elif score >= 0:
        grade = "Faild"
    else:
        grade = "Invalid score"
    print (f"Score {score} is {grade}")
