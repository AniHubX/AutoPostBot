#    This file is part of the ChannelAutoForwarder distribution (https://github.com/xditya/ChannelAutoForwarder).
#    Copyright (c) 2021 Adiya
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/xditya/ChannelAutoForwarder/blob/main/License> .

from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_ = config("FROM_CHANNEL")
FROM1_ = config("FROM_CHANNEL1")
FROM2_ = config("FROM_CHANNEL2")
TO_ = config("TO_CHANNEL")

FROM1 = [int(i) for i in FROM1_.split()]
FROM2 = [int(i) for i in FROM2_.split()]
FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    anihubx = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    anihubx.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@anihubx.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            await anihubx.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

@anihubx.on(events.NewMessage(incoming=True, chats=FROM1))
async def sender_bH1(event):
    for i in TO:
        try:
            await anihubx.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

@anihubx.on(events.NewMessage(incoming=True, chats=FROM2))
async def sender_bH2(event):
    for i in TO:
        try:
            await anihubx.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

print("Bot has started.")
anihubx.run_until_disconnected()