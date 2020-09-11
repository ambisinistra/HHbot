import pandas as pd
from collections import OrderedDict

MIN_HEADER_LEN = 5
MAX_HEADER_LEN = 120
MIN_SECTIONS = 2
MAX_SECTIONS = 10

def build_vacancy_text(number_in_db : int, df : pd.DataFrame):
    cell = df.iloc[number_in_db]

    vacancy_text = ""
    vacancy_text += cell["name"] + "\n"
    vacancy_text += cell["employer.name"] + "\n"
    vacancy_text += cell["area.name"] + "\n\n"

    full_text = cell["description"]
    segments = return_first_items(segmentation_by_terminals(full_text=full_text))
    if not segments.keys():
        return ('')
    for header in segments.keys():
        vacancy_text += header + ":"
        vacancy_text += "\n".join(segments[header]) + "\n\n"

    vacancy_text += "Страница компании" + "\n"
    vacancy_text += cell["employer.alternate_url"] + "\n\n"
    vacancy_text += "Страница вакансии" + "\n"
    vacancy_text += cell["alternate_url"]

    return vacancy_text

def strip_for_all(list_of_str : list, func=str.strip, sensfull_length=4):
    return [func(elem) for elem in list_of_str if len(elem) >= sensfull_length]

def return_first_items(input_dict : OrderedDict):
    try:
        first_out_key = list(input_dict.keys())[0]
    except KeyError:
        return OrderedDict()
    try:
        first_inn_key = list(input_dict[first_out_key].keys())[0]
    except KeyError:
        return OrderedDict()
    return (input_dict[first_out_key][first_inn_key])

def segmentation_by_terminals(full_text : str, terminals=["**"], small_terminals=["*", r"\-", "\n"]):
    # trying cut full text in segments [T,h,T,h,T], where h - headear, T - text
    # then evaluate quality of cutting

    segmentations_variants = OrderedDict()

    #TODO: Check results by different terminals
    for terminal in terminals:
        segmentations_variants[terminal] = OrderedDict()
        segments = full_text.split(terminal)
        segments = strip_for_all(segments)

        for sub_terminal in small_terminals:
            segmentations_variants[terminal][sub_terminal] = OrderedDict()
            max_sections = 0

            for i in range(len(segments)):
                sub_segments = segments[i].split(sub_terminal)
                sub_segments = strip_for_all(sub_segments)
                if len(sub_segments) >= MIN_SECTIONS:
                    if i > 0:
                        if MIN_HEADER_LEN <= len(segments[i-1]) <= MAX_HEADER_LEN:
                            segmentations_variants[terminal][sub_terminal][segments[i-1]] = sub_segments
                            if len(sub_segments) > max_sections:
                                max_sections = len(sub_segments)
                    elif i == 0:
                        segmentations_variants[terminal][sub_terminal]["headless"] = sub_segments

            if not segmentations_variants[terminal][sub_terminal]:
                del segmentations_variants[terminal][sub_terminal]
            if max_sections >= MAX_SECTIONS:
                del segmentations_variants[terminal][sub_terminal]

        if not segmentations_variants[terminal]:
            del segmentations_variants[terminal]

    return (segmentations_variants)