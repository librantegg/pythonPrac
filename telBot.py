#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import datetime
import json
from telebot import types

bot = telebot.TeleBot('1881110774:AAEXuS-JIFkYsMvcXPmWu_Mb_HZS3JRLx78')


chtuka = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
	msg = bot.send_message(message.chat.id, "Input your reminder:...")
	bot.register_next_step_handler(msg, process_text_step)


def process_text_step(message):
		chtuka["message_id"] = message.id
		chtuka["message_text"] = message.text
		msg = bot.reply_to(message, "Print time interval in minutes")
		bot.register_next_step_handler(msg, process_time_step)


def process_time_step(message):
		minutes = message.text
		if not minutes.isdigit():
			msg = bot.reply_to(message, 'Time should be a number.')
			bot.register_next_step_handler(msg, process_time_step)
			return
		chtuka["time"] = minutes
		with open("napomni.json", 'a') as my_file:
			json.dump(chtuka, my_file)
		bot.reply_to(message, 'Your reminder is noted')


# @bot.message_handler(func=lambda message: True)<
# def send_confirmation(message):
# 	try:
# 		chtuka = {}
# 		chtuka["message_id"] = message.id
# 		chtuka["message_text"] = message.text
# 		chtuka["time_to_pend"] = datetime.datetime.now().timestamp()
# 		# chtuka["time_to_pend_2"] = time_to_pend
# 		print(chtuka)
# 		with open("napomni.json", 'w') as my_file:
# 			json.dump(chtuka, my_file)
# 		bot.reply_to(message, "Your reminder is noted")
# 	except Exception as e:
# 		bot.reply_to(message, 'oooops')


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message)



# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling()



# {
# 	"message_id": "",
#  	"message_text": "",
#  	"time_to_pend": ""
# }

# {'content_type': 'text',
#  'id': 16,
#  'message_id': 16,
#  'from_user': {
# 	 'id': 912316680,
# 	 'is_bot': False,
# 	 'first_name': 'Вова',
# 	 'username': 'vladimireho',
# 	 'last_name': 'Бабулехин',
# 	 'language_code': 'en',
# 	 'can_join_groups': None,
# 	 'can_read_all_group_messages': None,
# 	 'supports_inline_queries': None},
#  'date': 1625785408,
#  'chat': {
# 	 'id': 912316680,
# 	 'type': 'private',
# 	 'title': None, 'username': 'vladimireho', 'first_name': 'Вова', 'last_name': 'Бабулехин', 'photo': None, 'bio': None,
# 	 'description': None, 'invite_link': None, 'pinned_message': None,
# 	 'permissions': None, 'slow_mode_delay': None, 'message_auto_delete_time': None,
# 	 'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None,
# 	 'location': None},
# 	 'forward_from': None,
# 	 'forward_from_chat': None,
# 	 ' forward_from_message_id': None,
# 	 'forward_signature': None,
# 	 'forward_sender_name': None,
# 	 'forward_date': None, 'reply_to_message': None,
# 	 'via_bot': None, 'edit_date': None,
# 	 'media_group_id': None,
# 	 'author_signature': None,
# 	 'text': '/start',
# 	 'entities': [<telebot.types.MessageEntity object at 0x7ff52b193850>],
# 	 'caption_entities': None,
# 	 'audio': None,
# 	 'document': None,
# 	 'photo': None,
# 	 'sticker': None,
# 	 'video': None,
# 	 'video_note': None,
# 	 'voice': None,
# 	 'caption': None,
# 	 'contact': None,
# 	 'location': None,
# 	 'venue': None,
# 	 'animation': None,
# 	 'dice': None,
# 	 'new_chat_member': None,
# 	 'new_chat_members': None,
# 	 'left_chat_member': None,
# 	 'new_chat_title': None,
# 	 'new_chat_photo': None,
# 	 'delete_chat_photo': None,
# 	 'group_chat_created': None,
# 	 'supergroup_chat_created': None,
# 	 'channel_chat_created': None,
# 	 'migrate_to_chat_id': None,
# 	 'migrate_from_chat_id': None,
# 	 'pinned_message': None,
# 	 'invoice': None,
# 	 'successful_payment': None,
# 	 'connected_website': None,
# 	 'reply_markup': None,
# 	 'json':
# 		 {
# 		 'message_id': 16,
# 		 'from':
# 			 {
# 			 'id': 912316680,
# 			 'is_bot': False,
# 			 'first_name': 'Вова',
# 			 'last_name': 'Бабулехин',
# 			 'username': 'vladimireho',
# 			 'language_code': 'en'
# 			 },
# 		 'chat':
# 		 {
# 		 	'id': 912316680, '
# 		 	first_name': 'Вова',
# 		 	'last_name': 'Бабулехин',
# 		 	'username': 'vladimireho',
# 		 	'type': 'private'
# 		 },
# 		 'date': 1625785408,
# 		 'text': '/start',
# 		 'entities':
# 			 [{'offset': 0,
# 			 'length': 6,
# 			 'type': 'bot_command'}]
# 	 	}
#  }




