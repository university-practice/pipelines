import re

def remove_personal_data(text):
    pattern = r'\b[А-ЯЁ]\.\s?[А-ЯЁ]\.\s?[А-ЯЁ][а-яё]+\b|\b[А-ЯЁ][а-яё]+\s[А-ЯЁ]\.\s?[А-ЯЁ]\.\b|\b[А-ЯЁ]\.\s?[А-ЯЁ]\.\s?[А-ЯЁ][а-яё]+\d*\b'

    lines = text.split('\n')
    
    cleaned_lines = [line for line in lines if not re.search(pattern, line)]
    
    cleaned_text = '\n'.join(cleaned_lines)

    return cleaned_text

text = """
ТЕХНОЛОГИЙ1
Ю. С. Сашина1, В. О. Чертухин1, Е. С. Гаранина1, В. В. Линьков1

Литература
1. Инсульт. Руководство для врачей. М. : Медицинское информационное агентство, 2014. - 400 с. 
2. Нарушения мозгового кровообращения: диагностика, лечение, профилактика / З. А. Суслина [и др.]. - М. : МЕДпресс-информ, 2016. - 536 с. 

А.К. Красильникова, д.м.н.1

Материал и методы. Программа поддерживается на кросс платформенных операционных системах

Список литературы:
1. Фетисова И.Н., Малышкина А.И., Зинченко Р.А., Панова И.А., Фетисов Н.С., Рокотянская Е.А. Прогностическое значение полиморфизма генов системы гемостаза и генов, контролирующих тонус сосудистой стенки у беременных женщин с гипертензивными расстройствами различного генеза, Ярославль, 2022.
"""

cleaned_text = remove_personal_data(text)
print(cleaned_text)
