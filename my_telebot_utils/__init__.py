from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton

group_link = "https://t.me/animator_jobs"
tech_support = "https://t.me/ambisinistra"

def make_moder_keyboard():
    keyboard = InlineKeyboardMarkup()
    
    post_button = InlineKeyboardButton(text="POST", callback_data="post")
    irre_button = InlineKeyboardButton(text="irrelevant", callback_data="irre")
    susp_button = InlineKeyboardButton(text="suspicious", callback_data="susp")
    othe_button = InlineKeyboardButton(text="other", callback_data="othe")
    edit_button = InlineKeyboardButton(text="EDIT", callback_data="edit")
    keyboard.row(post_button)
    keyboard.row(irre_button, susp_button, othe_button)
    keyboard.row(edit_button)
    return (keyboard)

def make_post_keyboard():
    keyboard = InlineKeyboardMarkup()
    post_button = InlineKeyboardButton(text="thank you very much. vacancy has been posted in group channel", url=group_link)
    keyboard.add(post_button)
    return (keyboard)

def make_suspicious_keyboard():
    keyboard = InlineKeyboardMarkup()
    suspicious_button = InlineKeyboardButton(text="thank you very much. vacancy has been marked as suspicious and has not been posted", url=group_link)
    keyboard.add(suspicious_button)
    return (keyboard)

def make_irrelevant_keyboard():
    keyboard = InlineKeyboardMarkup()
    irrelevant_button = InlineKeyboardButton(text="thank you very much. vacancy has been marked as out of the box and has not been posted", url=group_link)
    keyboard.add(irrelevant_button)
    return (keyboard)

def make_edit_keyboard():
    keyboard = InlineKeyboardMarkup()
    edit_info_button = InlineKeyboardButton(text="ENTERED EDIT MODE. Please send me editeded message. In case of any issues or difficulties click here to contact support", url=tech_support)
    edit_undo_button = InlineKeyboardButton(text="CANCEL editing. return to normal mode", callback_data="undo")
    keyboard.row(edit_info_button)
    keyboard.row(edit_undo_button)
    return (keyboard)