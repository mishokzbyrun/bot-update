from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="List of products")],
    [KeyboardButton(text="Make order"), KeyboardButton(text="Confirm")]
], resize_keyboard=True, input_field_placeholder="Make your choice")


inlineMain = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")],
    [InlineKeyboardButton(text="Google", url="https://google.com")],
    
])


