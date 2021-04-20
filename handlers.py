import os
from telegram.ext import CommandHandler, MessageHandler, Filters

from settings import WELCOME_MESSAGE, TELEGRAM_SUPPORT_CHAT_ID

def start(update, context):
    update.message.reply_text(WELCOME_MESSAGE)

    user_info = update.message.from_user.to_dict()

    context.bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=f"""
📞 Connected {user_info}.
        """,
    )


def forward_to_chat(update, context):
    """{ 
        'message_id': 5, 
        'date': 1605106546, 
        'chat': {'id': 49820636, 'type': 'private', 'username': 'danokhlopkov', 'first_name': 'Daniil', 'last_name': 'Okhlopkov'}, 
        'text': 'TEST QOO', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
        'from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'username': 'danokhlopkov', 'language_code': 'en'}
    }"""
    update.message.forward(chat_id=TELEGRAM_SUPPORT_CHAT_ID)


def forward_to_user(update, context):
    """{
        'message_id': 10, 'date': 1605106662, 
        'chat': {'id': -484179205, 'type': 'group', 'title': '☎️ SUPPORT CHAT', 'all_members_are_administrators': True}, 
        'reply_to_message': {
            'message_id': 9, 'date': 1605106659, 
            'chat': {'id': -484179205, 'type': 'group', 'title': '☎️ SUPPORT CHAT', 'all_members_are_administrators': True}, 
            'forward_from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'danokhlopkov': 'okhlopkov', 'language_code': 'en'}, 
            'forward_date': 1605106658, 
            'text': 'g', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 
            'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
            'from': {'id': 1440913096, 'first_name': 'SUPPORT', 'is_bot': True, 'username': 'lolkek'}
        }, 
        'text': 'ggg', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 
        'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
        'from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'username': 'danokhlopkov', 'language_code': 'en'}
    }"""
    {
  "update_id": 471632444,
  "message": {
    "message_id": 3299,
    "date": 1613904069,
    "chat": {
      "id": -392720014,
      "type": "group",
      "title": "test",
      "all_members_are_administrators": true
    },
    "reply_to_message": {
      "message_id": 3297,
      "date": 1613904018,
      "chat": {
        "id": -392720014,
        "type": "group",
        "title": "test",
        "all_members_are_administrators": true
      },
      "forward_date": 1613904018,
      "text": "пп",
      "entities": [],
      "caption_entities": [],
      "photo": [],
      "new_chat_members": [],
      "new_chat_photo": [],
      "delete_chat_photo": false,
      "group_chat_created": false,
      "supergroup_chat_created": false,
      "channel_chat_created": false,
      "forward_sender_name": "Daniil Okhlopkov",
      "from": {
        "id": 1018878145,
        "first_name": "999",
        "is_bot": true,
        "username": "9999"
      }
    },
    "text": "аппп",
    "entities": [],
    "caption_entities": [],
    "photo": [],
    "new_chat_members": [],
    "new_chat_photo": [],
    "delete_chat_photo": false,
    "group_chat_created": false,
    "supergroup_chat_created": false,
    "channel_chat_created": false,
    "from": {
      "id": 49820636,
      "first_name": "Daniil",
      "is_bot": false,
      "last_name": "Okhlopkov",
      "username": "okhlopkov",
      "language_code": "en"
    }
  }
}
    )


def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.chat_type.private, forward_to_chat))
    dp.add_handler(MessageHandler(Filters.chat(TELEGRAM_SUPPORT_CHAT_ID) & Filters.reply, forward_to_user))
    return dp
