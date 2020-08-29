import pandas as pd
from find_paragraph_by_terminals import find_paragraph_by_terminals

def build_vacancy_text(number_in_db : int, df : pd.DataFrame, keyword_to_paragraph : dict):
    cell = df.iloc[number_in_db]
    that_was_full_text = False

    vacancy_text = ""
    vacancy_text += cell["name"] + "\n"
    vacancy_text += cell["employer.name"] + "\n"
    vacancy_text += cell["area.name"] + "\n\n"

    responsibility = find_paragraph_by_terminals(cell["description"], cell["snippet.responsibility"], keyword_to_paragraph)
    if responsibility:
        vacancy_text += "Задачи" + "\n"
        vacancy_text += responsibility + "\n\n"
        if len(requirement) == len(cell["description"]):
            that_was_full_text = True

    if (not that_was_full_text):
        requirement = find_paragraph_by_terminals(cell["description"], cell["snippet.requirement"], keyword_to_paragraph)
        if requirement:
            vacancy_text += "Требования" + "\n"
            vacancy_text += requirement + "\n\n"
    
    vacancy_text += "Страница компании" + "\n"
    vacancy_text += cell["employer.alternate_url"] + "\n\n"
    vacancy_text += "Страница вакансии" + "\n"
    vacancy_text += cell["alternate_url"]

    return vacancy_text