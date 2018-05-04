# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
import os
import requests
URL='https://api.telegram.org/bot460479919:AAHPV8AiwYac0a1HXCcD4V5ET_iEh2SZBdM/setMe'
bot = telebot.TeleBot(config.token)
#@bot.message_handler(commands=["print"])
@bot.message_handler(commands=["start"])
def main(message):
	key=types.InlineKeyboardMarkup(row_width=1)
	but_1=types.InlineKeyboardButton(text="Где проходит", callback_data="Где проходит")
	but_2=types.InlineKeyboardButton(text="Кто спикеры", callback_data="Кто спикеры")
	but_22=types.InlineKeyboardButton(text="Сколько стоит", callback_data="Сколько стоит")
	but_3=types.InlineKeyboardButton(text="Связаться с организатором", url="yandex.ru")
	#key_3.add(but_3)
	key.add(but_1, but_2, but_22, but_3)
	bot.send_message(message.chat.id, "Рады приветствовать Вас! В преддверии главного праздника весны мы организуем самое масштабное событие для ярких, стильных и успешных женщин!")
	bot.send_photo(message.from_user.id,open('E://bot/Photo.PNG','rb'))
	bot.send_message(message.chat.id, "Мы знаем, как сделать Вас счастливыми накануне 8 марта! Психология, отношения, красота, здоровый образ жизни, карьера, открытие собственного бизнеса - мы ответим на все Ваши самые сокровенные и животрепещущие вопросы.", reply_markup=key)
	
k=0
i=0
call=""
keyGlobal=types.InlineKeyboardMarkup(row_width=1)
	#bot.send_message(message.chat.id, "Еще одно сообщение", reply_markup=key_3)

@bot.message_handler(commands=["start"])
@bot.callback_query_handler(func=lambda c:True)
def inlin(c):

	if c.data=="Где проходит":
		key=types.InlineKeyboardMarkup(row_width=1)
		but_1=types.InlineKeyboardButton(text="Как добраться", url="https://yandex.by/maps/213/moscow/?clid=2122681&win=75&mode=search&z=16&text=%D0%A2%D0%B2%D0%B5%D1%80%D1%81%D0%BA%D0%B0%D1%8F%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%2C%207&sll=37.611203%2C55.757972&sspn=0.021243%2C0.007792")
		but_2=types.InlineKeyboardButton(text="Вернуться в гавное меню", callback_data="Вернуться в главное меню")
		key.add(but_1,but_2)
		bot.send_message(c.message.chat.id, "Место проведения \n <a href='https://pp.userapi.com/c830509/v830509886/ed7cf/H8_OMFEL-xI.jpg'>..</a>", parse_mode= "HTML", reply_markup=key)
	elif c.data=="Кто спикеры":
		global keyGlobal
		global call
		key=types.InlineKeyboardMarkup(row_width=1)
		but_1=types.InlineKeyboardButton(text="Принять участие", url="https://t.me/DianaAsryan")
		but_2=types.InlineKeyboardButton(text="Вернуться в гавное меню", callback_data="Вернуться в главное меню")
		but_3=types.InlineKeyboardButton(text="<", callback_data="left")
		but_4=types.InlineKeyboardButton(text=">", callback_data="right")
		key.add(but_1,but_2,but_3,but_4)	
		keyGlobal=key
		call=bot.send_message(c.message.chat.id, text="lisovec <a href='https://pp.userapi.com/c830509/v830509886/ed711/06Aues0mfks.jpg'>..</a>",parse_mode="HTML", reply_markup=key)

	if c.data=="right":
		global i		
		if i>2:
			i=0
		if i==0:
			bot.edit_message_text(chat_id=c.message.chat.id, message_id=call.message_id, text="text a,out \nlisovec\n <a href='https://pp.userapi.com/c830509/v830509886/ed711/06Aues0mfks.jpg'>..</a>",parse_mode="HTML",reply_markup=keyGlobal)
			i=i+1
		elif i==1:
			bot.edit_message_text(chat_id=c.message.chat.id, message_id=call.message_id, text="text 2\n <a href='https://pp.userapi.com/c830509/v830509886/ed718/ed__QklVeU4.jpg'>..</a>",parse_mode="HTML",reply_markup=keyGlobal)
			i=i+1
		elif i==2:
			bot.edit_message_text(chat_id=c.message.chat.id, message_id=call.message_id, text="text 3\n <a href='https://pp.userapi.com/c830509/v830509886/ed7cf/H8_OMFEL-xI.jpg'>..</a>",parse_mode="HTML",reply_markup=keyGlobal)
			i=i+1
			
	elif c.data=="left":		
		if i<0:
			i=2
		if i==0:
			bot.edit_message_text(chat_id=c.message.chat.id, message_id=call.message_id, text="text a,out \nlisovec\n <a href='https://pp.userapi.com/c830509/v830509886/ed711/06Aues0mfks.jpg'>..</a>",parse_mode="HTML",reply_markup=keyGlobal)
			i=i-1
		elif i==1:
			bot.edit_message_text(chat_id=c.message.chat.id, message_id=call.message_id, text="text 2\n <a href='https://pp.userapi.com/c830509/v830509886/ed718/ed__QklVeU4.jpg'>..</a>",parse_mode="HTML",reply_markup=keyGlobal)	
			i=i-1
		elif i==2:
			bot.edit_message_text(chat_id=c.message.chat.id, message_id=call.message_id, text="text 3\n <a href='https://pp.userapi.com/c830509/v830509886/ed7cf/H8_OMFEL-xI.jpg'>..</a> ",parse_mode="HTML",reply_markup=keyGlobal)
			i=i-1	
			
	elif c.data=="Сколько стоит":
		key=types.InlineKeyboardMarkup(row_width=1)
		but_4=types.InlineKeyboardButton(text="VIP", callback_data="VIP" )
		but_5=types.InlineKeyboardButton(text="Basik", callback_data="Basik" )
		but_6=types.InlineKeyboardButton(text="Online", callback_data="Online" )
		but_7=types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="Вернуться в главное меню" )
		key.add(but_4,but_5,but_6,but_7)
		bot.send_message(c.message.chat.id, "ВНИМАНИЕ! Каждую пятницу в 17:00 стоимость билетов увеличивается от 1 000 до 2 000 рублей в зависимости от категории билета.", reply_markup=key)
	elif c.data=="VIP":
		key=types.InlineKeyboardMarkup(row_width=1)
		but_1=types.InlineKeyboardButton(text="Заказать", url="https://t.me/DianaAsryan" )
		but_2=types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="Вернуться в главное меню" )
		key.add(but_1,but_2)
		bot.send_message(c.message.chat.id, "Цена VIP билета \nText\n<a href='https://pp.userapi.com/c830509/v830509886/ed718/ed__QklVeU4.jpg'>..</a>", parse_mode="HTML", reply_markup=key)
	elif c.data=="Basik":
		key=types.InlineKeyboardMarkup(row_width=1)
		but_1=types.InlineKeyboardButton(text="Заказать", url="https://t.me/DianaAsryan" )
		but_2=types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="Вернуться в главное меню" )
		key.add(but_1,but_2)
		bot.send_message(c.message.chat.id, "Цена Basik билета \nText\n<a href='https://pp.userapi.com/c830509/v830509886/ed718/ed__QklVeU4.jpg'>..</a>", parse_mode="HTML", reply_markup=key)
	elif c.data=="Online":
		key=types.InlineKeyboardMarkup(row_width=1)
		but_1=types.InlineKeyboardButton(text="Заказать", url="https://t.me/DianaAsryan" )
		but_2=types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="Вернуться в главное меню" )
		key.add(but_1,but_2)
		bot.send_message(c.message.chat.id, "Цена online билета \nText\n <a href='https://pp.userapi.com/c830509/v830509886/ed718/ed__QklVeU4.jpg'>..</a>", parse_mode="HTML", reply_markup=key)
	elif c.data=="Вернуться в главное меню":
		key=types.InlineKeyboardMarkup(row_width=1)
		but_1=types.InlineKeyboardButton(text="Где проходит", callback_data="Где проходит")
		but_2=types.InlineKeyboardButton(text="Кто спикеры", callback_data="Кто спикеры")
		but_22=types.InlineKeyboardButton(text="Сколько стоит", callback_data="Сколько стоит")
		but_3=types.InlineKeyboardButton(text="Связаться с организатором", url="yandex.ru")
		#key_3.add(but_3)
		key.add(but_1, but_2, but_22, but_3)
		bot.send_message(c.message.chat.id, "Рады приветствовать Вас! В преддверии главного праздника весны мы организуем самое масштабное событие для ярких, стильных и успешных женщин!")
		bot.send_photo(c.message.chat.id,open('E://bot/Photo.PNG','rb'))
		bot.send_message(c.message.chat.id, "Мы знаем, как сделать Вас счастливыми накануне 8 марта! Психология, отношения, красота, здоровый образ жизни, карьера, открытие собственного бизнеса - мы ответим на все Ваши самые сокровенные и животрепещущие вопросы.", reply_markup=key)
	
if __name__ == '__main__':
	bot.polling()
