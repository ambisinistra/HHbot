import html2text
import requests
import pandas as pd

response = requests.get("https://api.hh.ru/vacancies?text='motion designer'&period=5").json()

def vacancy_keyword_check(keyword : str, df : pd.DataFrame, period = 5):
    response = requests.get("https://api.hh.ru/vacancies?text='{}'&period={}".format(keyword, period)).json()
    found = response["found"]
    pages = response["pages"]

    if (found <= 0):
        return (df)

    for page in range(pages + 1):
        response = requests.get("https://api.hh.ru/vacancies?text='{}'&period={}&page={}".format(keyword, period, page)).json()
        for i in range(len(response["items"])):
            temp_df = pd.DataFrame.from_dict(pd.json_normalize(response["items"][i]))
            if temp_df["id"].iloc[0] not in set(df["id"]):   #checking for not adding same id's that we have
                df = pd.concat([df, temp_df])  #that work reaaaaaly slow
    
    return (df)

def is_nan_or_empty(a : str):
    if (a != a):
        return (True)
    else:
        return (not bool(a))

def update_vacancies_description(df : pd.DataFrame, html=html2text.HTML2Text()):
    for i in range(len(df)):
        if (df["have full descript"].iloc[i] != df["have full descript"].iloc[i]):  #checking for NaN
            id = df["id"].iloc[i]
            vacancy = requests.get("https://api.hh.ru/vacancies/"+ id).json()
            df["description"].iloc[i] = html.handle(vacancy["description"])
            df["have full descript"].iloc[i] = 1
            df["under consideration"].iloc[i] = 0
            df["checked"].iloc[i] = 0
            if not is_nan_or_empty(df["snippet.requirement"].iloc[i]):
                df["snippet.requirement"].iloc[i] = html.handle(df["snippet.requirement"].iloc[i])
            if not is_nan_or_empty(df["snippet.responsibility"].iloc[i]):
                df["snippet.responsibility"].iloc[i] = html.handle(df["snippet.responsibility"].iloc[i])

    return (df)