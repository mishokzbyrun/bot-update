from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import requests
import os
import random

cars = ["AUDI", "BMW", "Tesla", "Dodge", "Mersedes", "Kia", "Renault"]
menu = ["catalog", "basket", "cancel"]


async def reply_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url="https://youtube.com"))
    return keyboard.adjust(3).as_markup()

async def inline_menu():
    keyboard = InlineKeyboardBuilder()
    for item in menu:
        keyboard.add(InlineKeyboardButton(text=item, callback_data=f"item_{item.lower()}"))
    return keyboard.adjust(2).as_markup()

def get_random_duck():
    endpoint = "https://random-d.uk/api/random"
    response = requests.get(endpoint)
    data = response.json()
    return data['url']

def get_random_memasik():
    folder_path = 'memasiki' 
    
    try:
        files = os.listdir(folder_path)
    except FileNotFoundError:
        return "Folder 'memasiki' not found."

    images = [file for file in files if file.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    
    if not images:
        return "No images found in the 'memasiki' folder."
    random_image = random.choice(images)
    image_path = os.path.join(folder_path, random_image)
    return image_path