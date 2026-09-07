from .i18n import I18n
def check (score, language ):
    i18n = I18n(language)
    if score >= 90:
        grade = i18n.get("grade.exel")
    elif score >= 75:
        grade = i18n.get("grade.very.good")
    elif score >= 50:
        grade = i18n.get("grade.good")
    elif score >= 0:
        grade = i18n.get("grade.faild")
    else:
        grade = i18n.get("grade.invalid")
    print (f"{i18n.get('grade.score')} {score} {i18n.get('grade.is')} {grade}")#SCORE = grade.score IS = grade.is
    return 
