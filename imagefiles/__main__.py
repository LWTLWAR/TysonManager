import openai
import sys
import os
import logging
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOGGER = logging.getLogger(__name__)

# Bot details from environment
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "hgbotsupportgroup")
BOT_OWNER_ID = int(os.getenv("OWNER_ID", "5147671960"))  # Default to a placeholder; replace as needed

if not (API_ID and API_HASH and BOT_TOKEN):
    LOGGER.error("API_ID, API_HASH, and BOT_TOKEN must be set in environment variables.")
    sys.exit(1)

HgBots = Client("TestingBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Check Python path for debugging
print("Python Path:", sys.path)

@HgBots.on_message(filters.command("start"))
async def start_cmd(client, message):
# Check if the start command was sent in a group or private chat
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        # Increment the chat count only if this is a new group
        

        buttons = [
            [InlineKeyboardButton(text="🚑 Support", url=f"https://t.me/{SUPPORT_CHAT}"),
             InlineKeyboardButton(text="📢 Updates", url="https://t.me/hgbotsupdates")]
        ]

        reply_markup = InlineKeyboardMarkup(buttons)

        try:
            await message.reply_photo(
                photo="https://files.catbox.moe/evi5o3.jpg",
                caption="⚡ 𝙏𝙔𝙎𝞞𝙉 𝞛𝘼𝙉𝘼𝙂𝙀𝙍⚡ was working perfectly !!",
                reply_markup=reply_markup
            )
        except Exception as e:
            LOGGER.error(f"Error handling start command in group: {e}")
            await message.reply_text("An error occurred. Please try again later.")

    else:
        # Start message for private chat
        buttons = [
            [InlineKeyboardButton(text="Aᴅᴅ ᴍᴇ➕️", url="https://t.me/TysonGrangerXBot?startgroup=true")],
            [InlineKeyboardButton(text="⚜️Hᴇʟᴘ", callback_data="help_menu")],
            [InlineKeyboardButton(text="🛐Cʀᴇᴀᴛᴏʀ ", url="https://t.me/Ikiyo_kyokasiugetsu"),
             InlineKeyboardButton(text="🧡About ", callback_data="about")],
            [InlineKeyboardButton(text="🚑 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
             InlineKeyboardButton(text="📢 Uᴘᴅᴀᴛᴇꜱ", url="https://t.me/hgbotsupdates")]
        ]

        reply_markup = InlineKeyboardMarkup(buttons)
        first_name = message.from_user.first_name if message.from_user else "there"
        
        try:
            await message.reply_photo(
                photo="https://files.catbox.moe/pru1zv.jpg",
                caption=f"""──「  𝙏𝙔𝙎𝞞𝙉 𝞛𝘼𝙉𝘼𝙂𝙀𝙍 」──

𝐇𝐞𝐥𝐥𝐨, {message.from_user.first_name} !
𝐈 𝐚𝐦 𝐚 🕊𝐀𝐧𝐢𝐦𝐞-𝐭𝐡𝐞𝐦𝐞𝐝 𝐚𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐠𝐫𝐨𝐮𝐩 𝐦𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐦𝐚𝐧𝐲 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬⚔️.
• `10` 𝐮𝐬𝐞𝐫𝐬, 𝐚𝐜𝐫𝐨𝐬𝐬 `100` 𝐜𝐡𝐚𝐭𝐬.

➛ 𝐓𝐚𝐩 "𝐇𝐞𝐥𝐩" 𝐛𝐞𝐥𝐨𝐰 𝐭𝐨 𝐞𝐱𝐩𝐥𝐨𝐫𝐞 𝐦𝐲 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬.""",                
                reply_markup=reply_markup
            )
        except Exception as e:
            LOGGER.error(f"Error handling start command in private chat: {e}")
            await message.reply_text("An error occurred. Please try again later.")


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os

# Define the photo URL and text for the alive message
animation = "https://files.catbox.moe/hwf2lh.mp4"

@HgBots.on_message(filters.command("alive") & filters.group)
async def awake(client, message):
    # Alive message text
    alive_message = f"**♡ I am Alive and working! ⚡**\n\n"
    alive_message += "**♡ I'm working with awesome speed!**\n\n"
    alive_message += "**♡ Version : 2.0 LATEST**\n\n"
    alive_message += "**♡ My Developer :** [HgBots](t.me/HEMANTHGAMING_1K)\n\n"
    alive_message += f"**♡ Python Version :** {os.sys.version}\n\n"
    alive_message += "**♡ Telethon Version :** 1.23.0\n\n"
    
    # Buttons for support and updates
    buttons = [
        [InlineKeyboardButton("𝐒𝐔𝐏𝐏𝐎𝐑𝐓🙂", url="https://t.me/hgbotsupportgroup"),
         InlineKeyboardButton("𝐔𝐏𝐃𝐀𝐓𝐄", url="https://t.me/hgbotsupdates")]
    ]
    
    # Send the alive message with the photo and buttons
    await message.reply_animation(
        animation,
        caption=alive_message,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# Ban storage
banned_users = {}  # Maps user_id to (ban_expiry, reason)

# Check Python path for debugging
print("Python Path:", sys.path)

# Command Handlers

@HgBots.on_message(filters.command("start"))
async def start_cmd(client, message):
# Check if the start command was sent in a group or private chat
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        # Increment the chat count only if this is a new group
        
        buttons = [
            [InlineKeyboardButton(text="🚑 Support", url=f"https://t.me/{SUPPORT_CHAT}"),
             InlineKeyboardButton(text="📢 Updates", url="https://t.me/hgbotsupdates")]
        ]

        reply_markup = InlineKeyboardMarkup(buttons)

        try:
            await message.reply_photo(
                photo="https://files.catbox.moe/evi5o3.jpg",
                caption="⚡ƤƛƖƝ⚡ was working perfectly !!",
                reply_markup=reply_markup
            )
        except Exception as e:
            LOGGER.error(f"Error handling start command in group: {e}")
            await message.reply_text("An error occurred. Please try again later.")

    else:
        # Start message for private chat
        buttons = [
            [InlineKeyboardButton(text="Aᴅᴅ ᴍᴇ➕️", url="https://t.me/TysonGrangerXBot?startgroup=true")],
            [InlineKeyboardButton(text="⚜️Hᴇʟᴘ", callback_data="help_menu")],
            [InlineKeyboardButton(text="🛐Cʀᴇᴀᴛᴏʀ ", url="https://t.me/Ikiyo_kyokasiugetsu"),
             InlineKeyboardButton(text="🧡About ", callback_data="about")],
            [InlineKeyboardButton(text="🚑 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
             InlineKeyboardButton(text="📢 Uᴘᴅᴀᴛᴇꜱ", url="https://t.me/hgbotsupdates")]
        ]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        first_name = message.from_user.first_name if message.from_user else "there"

        try:
            await message.reply_photo(
                photo="https://files.catbox.moe/pru1zv.jpg",
                caption=f"""──「 ƤƛƖƝ 」──

𝐇𝐞𝐥𝐥𝐨, {message.from_user.first_name} !
𝐈 𝐚𝐦 𝐚 🕊𝐀𝐧𝐢𝐦𝐞-𝐭𝐡𝐞𝐦𝐞𝐝 𝐚𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐠𝐫𝐨𝐮𝐩 𝐦𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡 𝐦𝐚𝐧𝐲 𝐩𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬⚔️.
• `10` 𝐮𝐬𝐞𝐫𝐬, 𝐚𝐜𝐫𝐨𝐬𝐬 `100` 𝐜𝐡𝐚𝐭𝐬.

➛ 𝐓𝐚𝐩 "𝐇𝐞𝐥𝐩" 𝐛𝐞𝐥𝐨𝐰 𝐭𝐨 𝐞𝐱𝐩𝐥𝐨𝐫𝐞 𝐦𝐲 𝐟𝐞𝐚𝐭𝐮𝐫𝐞𝐬.""",                
                reply_markup=reply_markup
            )
        except Exception as e:
            LOGGER.error(f"Error handling start command in private chat: {e}")
            await message.reply_text("An error occurred. Please try again later.")



@HgBots.on_message(filters.command("help"))
async def help_cmd(client, message):
    # Check if the help command was sent in a group or private chat
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        # Group help message
        buttons = [
            [InlineKeyboardButton(text="Check help in pm", url=f"http://t.me/PainXrobot?start=help_")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await message.reply_animation(
            animation="https://files.catbox.moe/zpjtsy.mp4",
            caption="Hey, check my help features in PM!",
            reply_markup=reply_markup
        )
    else:
        # Private help message
        help_text = """
**Hey there, I'm [*⚡𝙏𝙔𝙎𝞞𝙉⚡*!](https://files.catbox.moe/zpjtsy.mp4)
To make me functional, make sure I have enough rights in your group.
Helpful commands:
- /start: Starts me!
- /help: Shows this message with more details.
- /donate: Info on supporting me and my creator.
If you have questions or bug reports, contact @hgbotsupportgroup.
List of all available Modules:**
"""

        help_buttons = [
            [InlineKeyboardButton(text="help menu", callback_data="help_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(help_buttons)

        await message.reply_text(help_text, reply_markup=reply_markup)

@HgBots.on_callback_query(filters.regex("about"))
async def about_callback(client, callback_query):
    about_text = """
**───「 [ 𝙏𝙔𝙎𝞞𝙉 ](https://t.me/TysonGrangerXBot) 」───

Hey 👋 I'm ⚔️ [ 𝙏𝙔𝙎𝞞𝙉 ](https://t.me/TysonGrangerXBot), your friendly Naruto-themed group management bot. 🐉

I'm designed to help you manage your groups with ease and a touch of anime flair! 

🎏 Features:
♡ I restrict users, greet with messages, set rules, and stop spam.
♡ I warn, ban, tag or kick users.
♡ I keep notes and reply to keywords.
♡ I check admin permissions before acting.

⚠️ Note : If you find any error's contact [Support Chat !](https://t.me/hgbotsupportgroup)

───────────────────**
"""
    buttons = [
        [InlineKeyboardButton(text="✨Developer", url=f"http://t.me/hemanthgaming_1k"),
         InlineKeyboardButton(text="⚔️Owner", url=f"http://t.me/King_Of_Alone_Dark_World")]
]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.answer()
    await callback_query.message.edit_text(about_text, reply_markup=reply_markup)
    
@HgBots.on_callback_query(filters.regex("help_menu"))
async def help_menu_callback(client, callback_query):
    logging.info("help_menu_callback triggered")

    help_buttons = [
         [InlineKeyboardButton(text="Aᴅᴍɪɴ", callback_data="help_admin"),
          InlineKeyboardButton(text="Afk", callback_data="help_afk")],
         [InlineKeyboardButton(text="Bᴀɴ", callback_data="help_ban"),
          InlineKeyboardButton(text="Cʜᴀᴛɢᴘᴛ", callback_data="help_chatbot")],
         [InlineKeyboardButton(text="Dᴇᴠ", callback_data="help_dev"),
          InlineKeyboardButton(text="Games", callback_data="help_games")],
         [InlineKeyboardButton(text="Iɴꜰᴏ", callback_data="help_info"),
         InlineKeyboardButton(text="Tᴇʟᴇɢʀᴀᴘʜ", callback_data="help_telegraph")],
        [InlineKeyboardButton(text="Back ⬅️", callback_data="back_to_start")]
    ]

    reply_markup = InlineKeyboardMarkup(help_buttons)

    try:
        await callback_query.answer()
        logging.info("Answered callback query")

        await callback_query.message.edit_text(
            """
            **Hey there, I'm [*⚡𝙏𝙔𝙎𝞞𝙉⚡*!](https://files.catbox.moe/umdyo3.jpg)
            To make me functional, make sure I have enough rights in your group.
            Helpful commands:
            - /start: Starts me!
            - /help: Shows this message with more details.
            - /donate: Info on supporting me and my creator.
            If you have questions or bug reports, contact @hgbotsupportgroup.
            List of all available Modules:**
            """,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        logging.info("Edited message with help menu")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

@HgBots.on_callback_query(filters.regex("help_afk"))
async def help_afk_callback(client, callback_query):
    afk_help_text = """
*── 🤖Afk Commands ──*
/afk - Use This in groups
"""
    back_button = [[InlineKeyboardButton("Back to Help Menu", callback_data="help_menu")]]
    reply_markup = InlineKeyboardMarkup(back_button)

    await callback_query.answer()
    await callback_query.message.edit_text(afk_help_text, reply_markup=reply_markup)

@HgBots.on_callback_query(filters.regex("help_games"))
async def help_games_callback(client, callback_query):
    games_help_text = """
*── 🎮Games Commands ──*
/dice or /dice [1-6] - Play a dice game with the given number
/ball or /ball [1-5] - Play basketball game with the given number
/dart or /dart [1-6] - Play a dart game with the given number
/lol or /lol [1-5] - Play a laugh emoji game with the given number
"""
    back_button = [[InlineKeyboardButton("Back to Help Menu", callback_data="help_menu")]]
    reply_markup = InlineKeyboardMarkup(back_button)

    await callback_query.answer()
    await callback_query.message.edit_text(games_help_text, reply_markup=reply_markup)

@HgBots.on_callback_query(filters.regex("help_info"))
async def help_info_callback(client, callback_query):
    info_help_text = """
*── ❓Info Commands ──*
/info - Get information about your user account.
/id - Get your user ID.
"""
    back_button = [[InlineKeyboardButton("Back to Help Menu", callback_data="help_menu")]]
    reply_markup = InlineKeyboardMarkup(back_button)

    await callback_query.answer()
    await callback_query.message.edit_text(info_help_text, reply_markup=reply_markup)

@HgBots.on_callback_query(filters.regex("help_chatbot"))
async def help_chatbot_callback(client, callback_query):
    chatbot_help_text = """
*── 🔍Chatgpt Commands ──*
/ask <question> - Ask the AI a question.
"""
    back_button = [[InlineKeyboardButton("Back to Help Menu", callback_data="help_menu")]]
    reply_markup = InlineKeyboardMarkup(back_button)

    await callback_query.answer()
    await callback_query.message.edit_text(chatbot_help_text, reply_markup=reply_markup)

@HgBots.on_callback_query(filters.regex("help_telegraph"))
async def help_telegraph_callback(client, callback_query):
    telegraph_help_text = """
*── 📜Telegraph Commands ──*
/tm - Reply to a image or file to get telegraph link.
"""
    back_button = [[InlineKeyboardButton("Back to Help Menu", callback_data="help_menu")]]
    reply_markup = InlineKeyboardMarkup(back_button)

    await callback_query.answer()
    await callback_query.message.edit_text(telegraph_help_text, reply_markup=reply_markup)

@HgBots.on_callback_query(filters.regex("help_ban"))
async def help_ban_callback(client, callback_query):
    ban_help_text = """
*── ❓Ban Commands ──*
/ban - Reply to a user or give user id to ban user.
/unban - Reply to a user or give user id to unban user.
"""
    back_button = [[InlineKeyboardButton("Back to Help Menu", callback_data="help_menu")]]
    reply_markup = InlineKeyboardMarkup(back_button)

    await callback_query.answer()
    await callback_query.message.edit_text(ban_help_text, reply_markup=reply_markup)

@HgBots.on_callback_query(filters.regex("help_admin"))
async def help_admin_callback(client, callback_query):
    admin_help_text = """
*── ❓Admin Commands ──*
/promote - Get information about your user account.
/demote - Get your user ID.
"""
    back_button = [[InlineKeyboardButton("Back to Help Menu", callback_data="help_menu")]]
    reply_markup = InlineKeyboardMarkup(back_button)

    await callback_query.answer()
    await callback_query.message.edit_text(admin_help_text, reply_markup=reply_markup)

@HgBots.on_callback_query(filters.regex("help_dev"))
async def help_dev_callback(client, callback_query):
    dev_help_text = """
*── ❓Dev Commands ──*
/logs - Get information about your user account.
/gban - Get your user ID.
/stats - Get bots stats
"""
    back_button = [[InlineKeyboardButton("Back to Help Menu", callback_data="help_menu")]]
    reply_markup = InlineKeyboardMarkup(back_button)

    await callback_query.answer()
    await callback_query.message.edit_text(dev_help_text, reply_markup=reply_markup)

@HgBots.on_callback_query(filters.regex("back_to_menu"))
async def back_to_menu_callback(client, callback_query):
    await help_menu_callback(client, callback_query)

@HgBots.on_callback_query(filters.regex("back_to_start"))
async def back_to_start_callback(client, callback_query):
    # Call the start command function again to show the start message
    await start_cmd(client, callback_query.message)
        

import asyncio
from datetime import datetime, timedelta
from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions, Message

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Dictionary to store banned users: {user_id: {"reason": reason, "expires_at": datetime, "message_id": message_id}}
banned_users = {}


@HgBots.on_message(filters.command("ban"))
async def ban_cmd(client: Client, message: Message):
    # Check if the command is used in a group chat
    if message.chat.type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await message.reply_text("This command can only be used in groups.")
        return

    # Verify the user has admin or owner privileges
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
        await message.reply_text("You must be an admin or owner to use this command.")
        return

    # Proceed with the ban logic
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("❗Reply to a user or give user id to /ban <user_id | @username | reply_to_user> [reason]")
        return

    # Check for the target user
    target_user = None
    reason = "No reason provided" if len(message.command) < 3 else " ".join(message.command[2:])

    # If the command is a reply, use the replied user's ID
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        # If a user ID or username is provided
        target_user_input = message.command[1]
        
        # Check if the input is a user ID (pure number)
        if target_user_input.isdigit():
            target_user_id = int(target_user_input)
            try:
                target_user = await client.get_users(target_user_id)
            except Exception as e:
                await message.reply_text(f"Error: {e}")
                return
        elif target_user_input.startswith('@'):
            # Handle the case where the input is a username
            target_user_input = target_user_input[1:]  # Remove '@' symbol
            try:
                target_user = await client.get_users(target_user_input)
            except Exception as e:
                await message.reply_text(f"Error: {e}")
                return
        else:
            await message.reply_text("Invalid input! Please provide a valid user ID, username, or reply to a user.")
            return

    # Ban the target user
    if target_user:
        user_id = target_user.id
        banned_users[user_id] = {"reason": reason, "expires_at": None}  # None for permanent ban

        try:
            await client.ban_chat_member(message.chat.id, user_id)

            # Inline keyboard buttons
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("✅Unban", callback_data=f"unban_{user_id}"),
                 InlineKeyboardButton("❌Cancel", callback_data="cancel")]
            ])

            # Send GIF with the ban message and inline buttons
            gif_url = "https://files.catbox.moe/7rhbh4.mp4"  # Replace with actual GIF URL
            await client.send_animation(
                chat_id=message.chat.id,
                animation=gif_url,
                caption=f"❗Banned User {target_user.mention}   •Ban Status : Permanent  •Reason : {reason}",
                reply_markup=keyboard
            )
            print(f"Banned user {target_user.mention} permanently for: {reason}")
        except Exception as e:
            await message.reply_text(f"Failed to ban user: {e}")
            print(f"Failed to ban user {user_id}: {e}")


async def unban_after_delay(client: Client, chat_id: int, user_id: int, expires_at: datetime):
    # Calculate time remaining until unban
    delay = (expires_at - datetime.now()).total_seconds()
    await asyncio.sleep(delay)

    # Unban the user if they are still in banned_users
    if user_id in banned_users:
        del banned_users[user_id]
        try:
            await client.unban_chat_member(chat_id, user_id)
        except Exception as e:
            print(f"Error unbanning user {user_id}: {e}")


@HgBots.on_message(filters.command("unban"))
async def unban_cmd(client: Client, message: Message):
    # Check if the command is used in a group chat
    if message.chat.type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await message.reply_text("This command can only be used in groups.")
        return

    # Verify the user has admin or owner privileges
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
        await message.reply_text("You must be an admin or owner to use this command.")
        return

    # Proceed with the unban logic
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("❗Reply to a user or give user id to /unban <user_id | @username | reply_to_user>")
        return

    # Check for the target user
    target_user = None

    # If the command is a reply, use the replied user's ID
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        # If a user ID or username is provided
        target_user_input = message.command[1]
        
        # Check if the input is a user ID (pure number)
        if target_user_input.isdigit():
            target_user_id = int(target_user_input)
            try:
                target_user = await client.get_users(target_user_id)
            except Exception as e:
                await message.reply_text(f"Error: {e}")
                return
        elif target_user_input.startswith('@'):
            # Handle the case where the input is a username
            target_user_input = target_user_input[1:]  # Remove '@' symbol
            try:
                target_user = await client.get_users(target_user_input)
            except Exception as e:
                await message.reply_text(f"Error: {e}")
                return
        else:
            await message.reply_text("Invalid input! Please provide a valid user ID, username, or reply to a user.")
            return

    # Unban the target user
    if target_user:
        user_id = target_user.id

        # Check if the user is in the banned list
        if user_id in banned_users:
            del banned_users[user_id]
            try:
                await client.unban_chat_member(message.chat.id, user_id)
                await message.reply_text(f"User {target_user.id} has been unbanned.")
                print(f"Unbanned user {target_user.id}")
            except Exception as e:
                await message.reply_text(f"Failed to unban user: {e}")
                print(f"Failed to unban user {user_id}: {e}")
        else:
            await message.reply_text("User is not currently banned.")

@HgBots.on_callback_query()
async def callback_handler(client, callback_query):
    data = callback_query.data
    
    if data.startswith("unban_"):
        user_id = int(data.split("_")[1])
        try:
            await client.unban_chat_member(callback_query.message.chat.id, user_id)
            await callback_query.message.edit_text(f"User {user_id} has been unbanned.")
        except Exception as e:
            await callback_query.message.reply_text(f"Failed to unban user: {e}")
    elif data == "cancel":
        await callback_query.message.edit_text("Ban action canceled.")

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import RPCError, BadRequest
import html
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OWNER_ID = 5147671960

# Decorators
def bot_admin(func):
    async def wrapper(client, message):
        chat_member = await client.get_chat_member(message.chat.id, client.me.id)
        
        if chat_member.status != "administrator":
            await message.reply("I need to be an admin to do that.")
            return
        
        bot_member = await client.get_chat_member(chat_id, bot_user_id)
        bot_permissions = chat_member.privileges
        if not (bot_permissions.can_promote_members and bot_permissions.can_restrict_members):
            await message.reply("I need the proper permissions (promote, restrict members) to do that.")
            return
            return await func(client, message)
            return wrapper

def can_promote(func):
    async def wrapper(client, message):
        chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
        if chat_member.can_promote_members or chat_member.status == "creator":
            return await func(client, message)
        else:
            await message.reply("You need promotion permissions to use this command.")
    return wrapper

# Helper function to extract user ID
async def extract_user(message, args):
    if message.reply_to_message:
        return message.reply_to_message.from_user.id
    elif len(args) > 1 and args[1].isdigit():
        return int(args[1])
    return None

@bot_admin
@can_promote
@HgBots.on_message(filters.command("promote") & filters.user(OWNER_ID) & filters.group)
async def promote(client, message):
    chat_id = message.chat.id  # Obtain chat_id from the message object
    bot_user_id = client.me.id  # Example bot user ID setup; adjust if needed
    bot_member = await client.get_chat_member(chat_id, bot_user_id)
    if bot_member.privileges.can_manage_messages:
        args = message.text.split()
        user_id = await extract_user(message, args)
    
    if not user_id:
        return await message.reply("You need to specify a user or reply to their message.")

    try:
        user_member = await client.get_chat_member(message.chat.id, user_id)
        bot_member = await client.get_chat_member(message.chat.id, client.me.id)

        # Ensure user is not already an admin
        if user_member.status in ["administrator", "creator"]:
            return await message.reply("This user is already an admin.")
        
        # Prevent promoting the bot itself
        if user_id == client.me.id:
            return await message.reply("I cannot promote myself; an admin needs to do it.")
        
        bot_member = await client.get_chat_member(chat_id, bot_user_id)
        if bot_member.privileges.can_manage_messages:
            await client.promote_chat_member(
            message.chat.id,
            user_id,
            can_delete_messages=bot_member.can_delete_messages,
            can_invite_users=bot_member.can_invite_users,
            can_restrict_members=bot_member.can_restrict_members,
            can_pin_messages=bot_member.can_pin_messages,
        )
        
        await message.reply(f"Successfully promoted {user_member.user.first_name}!")
        
        # Logging the promotion
        log_message = (
            f"<b>{html.escape(message.chat.title)}:</b>\n"
            f"#PROMOTED\n"
            f"<b>Admin:</b> {html.escape(message.from_user.first_name)}\n"
            f"<b>User:</b> {html.escape(user_member.user.first_name)}"
        )
        logger.info(log_message)

    except BadRequest as err:
        if "USER_NOT_MUTUAL_CONTACT" in err.MESSAGE:
            await message.reply("I can't promote someone who isn't in the group.")
        else:
            await message.reply(f"An error occurred while promoting: {err.MESSAGE}")

@bot_admin
@can_promote    
@HgBots.on_message(filters.command("demote") & filters.user(OWNER_ID) & filters.group)
async def demote(client: Client, message: Message):
    args = message.text.split()
    user_id = await extract_user(message, args)

    if not user_id:
        return await message.reply("You need to specify a user or reply to their message.")

    try:
        user_member = await client.get_chat_member(message.chat.id, user_id)

        # Check if user is the creator
        if user_member.status == "creator":
            return await message.reply("Cannot demote the chat creator.")

        # Check if user is already not an admin
        if user_member.status != "administrator":
            return await message.reply("This user is not an admin.")

        # Demote the user by revoking all privileges
        await client.promote_chat_member(
            message.chat.id,
            user_id,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
        )
        
        await message.reply(f"Successfully demoted {user_member.user.first_name}!")

        # Logging the demotion
        log_message = (
            f"<b>{html.escape(message.chat.title)}:</b>\n"
            f"#DEMOTED\n"
            f"<b>Admin:</b> {html.escape(message.from_user.first_name)}\n"
            f"<b>User:</b> {html.escape(user_member.user.first_name)}"
        )
        logger.info(log_message)

    except BadRequest as err:
        if "CHAT_ADMIN_REQUIRED" in err.MESSAGE:
            await message.reply("I lack the necessary permissions to demote this user.")
        else:
            await message.reply(f"Could not demote. Error: {err.MESSAGE}")

from pyrogram import Client, filters
from pyrogram.types import Message

@HgBots.on_message(filters.command("info"))
async def info_cmd(client, message: Message):
    # Determine the target user (by reply, user ID, username, or the sender)
    user = None

    # Case 1: Reply to a message
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    # Case 2: User ID provided
    elif len(message.command) > 1 and message.command[1].isdigit():
        user_id = int(message.command[1])
        user = await client.get_users(user_id)
    # Case 3: Username provided
    elif len(message.command) > 1:
        username = message.command[1].lstrip('@')
        user = await client.get_users(username)
    # Case 4: No other user specified, use the sender
    else:
        user = message.from_user

    # Generate the user info text
    user_info_text = (
        f"*── User Info ──*\n"
        f"• **Mention:** [{user.first_name}](tg://user?id={user.id})\n"
        f"• **ID:** `{user.id}`\n"
        f"• **First Name:** {user.first_name}\n"
        f"• **Last Name:** {user.last_name if user.last_name else 'N/A'}\n"
        f"• **Username:** @{user.username if user.username else 'N/A'}\n"
        f"• **Language:** {user.language_code if user.language_code else 'N/A'}\n"
        f"• **Status: Active**"
    )

    try:
        # Fetch user profile photos
        profile_photos = client.get_chat_photos(user.id)

        # Use async for to retrieve the first available profile photo
        async for photo in profile_photos:
            profile_photo_id = photo.file_id
            await message.reply_photo(profile_photo_id, caption=user_info_text)
            break  # Exit after the first photo

        # If no profile photo was sent, send only the text
        else:
            await message.reply_text(user_info_text)

    except Exception as e:
        LOGGER.error(f"Error sending user info: {e}")
        await message.reply_text("Failed to retrieve user info. Please try again later.")

@HgBots.on_message(filters.command("id"))
async def id_cmd(client, message):
    user_id_text = ""
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        group_id = message.chat.id
        user_id_text = f"""
*── User ID ──*
• User ID: `{user.id}`
• First Name: {user.first_name}
• Last Name: {user.last_name if user.last_name else 'N/A'}
• Username: @{user.username if user.username else 'N/A'}
• Group ID: `{group_id}`
"""
    elif message.entities and message.entities[0].type == "mention":
        mentioned_user = message.entities[0].user
        group_id = message.chat.id
        user_id_text = f"""
*── User ID ──*
• User ID: `{mentioned_user.id}`
• First Name: {mentioned_user.first_name}
• Last Name: {mentioned_user.last_name if mentioned_user.last_name else 'N/A'}
• Username: @{mentioned_user.username if mentioned_user else 'N/A'}
• Group ID: `{group_id}`
"""
    else:
        chat_id = message.text.split()[1] if len(message.command) > 1 else None
        if chat_id:
            try:
                chat = await client.get_chat(chat_id)
                user_id_text = f"""
*── Chat ID ──*
• This Chat's ID: `{chat.id}`
• Title: {chat.title if chat.title else 'N/A'}
"""
            except Exception as e:
                LOGGER.error(f"Error fetching chat with ID {chat_id}: {e}")
                await message.reply_text("Could not retrieve group info for that ID.")
                return
        else:
            group_id = message.chat.id
            user_id_text = f"""
*── Chat ID ──*
• This Chat's ID: `{group_id}`
"""

    try:
        await message.reply_text(user_id_text)
    except Exception as e:
        LOGGER.error(f"Error sending user/group ID: {e}")
        await message.reply_text("Failed to retrieve information. Please try again later.")



@HgBots.on_message(filters.command("ask"))
async def ask_cmd(client, message):
    user_query = message.text.split(" ", 1)[1] if len(message.command) > 1 else ""

    if not user_query:
        await message.reply_text("Please provide a question after the /ask command.")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4 if you have access
            messages=[{"role": "user", "content": user_query}]
        )
        
        answer = response.choices[0].message['content']
        await message.reply_text(answer)
    
    except Exception as e:
        LOGGER.error(f"Error with ChatGPT API: {e}")
        await message.reply_text("❌ Failed to get a response from ChatGPT. Please try again later.")


import requests
import os
from telegraph import Telegraph
from pyrogram import filters


TMP_DOWNLOAD_DIRECTORY = "./"

def upload_to_catbox(file_path):
    url = "https://catbox.moe/user/api.php"
    
    with open(file_path, 'rb') as f:
        files = {'fileToUpload': f}
        data = {'reqtype': 'fileupload'}
        
        try:
            response = requests.post(url, files=files, data=data)
            LOGGER.info(f"Catbox response status: {response.status_code}")
            LOGGER.info(f"Catbox response text: {response.text}")

            if response.status_code == 200 and "https" in response.text:
                return response.text.strip()  # Catbox returns the URL as plain text
            else:
                LOGGER.error(f"Failed to upload to Catbox: {response.text}")
                return None
        except Exception as e:
            LOGGER.error(f"Error during Catbox upload: {e}")
            return None

@HgBots.on_message(filters.command("tm") & filters.reply)
async def catbox_upload(client, message):
    if message.reply_to_message.photo or message.reply_to_message.document:
        msg = await message.reply_text("📤 Uploading to Catbox...")

        # Step 1: Download the media file
        try:
            file_path = await client.download_media(message.reply_to_message, TMP_DOWNLOAD_DIRECTORY)
            LOGGER.info(f"File downloaded to: {file_path}")
        except Exception as e:
            await msg.edit_text(f"❌ Failed to download file: {e}")
            return

        if not os.path.exists(file_path):
            await msg.edit_text("❌ Download failed or file does not exist.")
            return

        # Step 2: Upload to Catbox.moe
        LOGGER.info(f"Uploading to Catbox: {file_path}")
        catbox_url = upload_to_catbox(file_path)

        # Inline button for the support chat
        buttons = [[InlineKeyboardButton(text="🚑 Support Chat", url=f"https://t.me/{SUPPORT_CHAT}")]]
        reply_markup = InlineKeyboardMarkup(buttons)

        if catbox_url:
            # Step 3: Send the Catbox link directly with support button
            await msg.edit_text(f"✅ Uploaded to Catbox\n{catbox_url}", disable_web_page_preview=True, reply_markup=reply_markup)
        else:
            await msg.edit_text("❌ Upload failed: Unable to upload to Catbox.", reply_markup=reply_markup)

        # Step 4: Clean up the downloaded file
        if os.path.exists(file_path):
            os.remove(file_path)
            LOGGER.info(f"Temporary file removed: {file_path}")
    else:
        await message.reply_text("⚠️ Please reply to an image or document to upload to Catbox.")

from pyrogram import Client, filters
import random

@HgBots.on_message(filters.command("dice"))
async def dice_game(client, message):
    if message.forward_from:  # Check if the message is forwarded
        return

    input_str = message.text.split(" ", 1)
    if len(input_str) > 1:
        input_int = int(input_str[1])
    else:
        input_int = random.randint(1, 6)

    if input_int < 1 or input_int > 6:
        await message.reply("Please use a number between 1 and 6.")
        return

    # Use send_dice to send the dice emoji
    r = await message.reply("🎲")  # Sending the dice emoji for the game
    try:
        while True:
            # Simulating dice roll result here, as pyrogram doesn't have reply_dice
            roll = random.randint(1, 6)  # Random dice value between 1 and 6
            if roll == input_int:
                await r.edit(f"🎲 You rolled a {roll}, and it matches your input!")
                break
            await r.edit(f"🎲 Rolled a {roll}. Try again!")
            await asyncio.sleep(1)  # Sleep to simulate delay before next roll
    except Exception as e:
        print(f"Error: {e}")
        pass

@HgBots.on_message(filters.command("dart"))
async def dart_game(client, message):
    if message.forward_from:  # Check if the message is forwarded
        return

    input_str = message.text.split(" ", 1)
    if len(input_str) > 1:
        input_int = int(input_str[1])
    else:
        input_int = random.randint(1, 6)

    if input_int < 1 or input_int > 6:
        await message.reply("Please use a number between 1 and 6.")
        return

    # Use send_dice to send the dice emoji with dart
    r = await message.reply("🎯")  # Dart emoji for the game
    try:
        while True:
            roll = random.randint(1, 6)  # Random dice value between 1 and 6
            if roll == input_int:
                await r.edit(f"🎯 You hit {roll}, and it matches your input!")
                break
            await r.edit(f"🎯 Dart hit {roll}. Try again!")
            await asyncio.sleep(1)  # Sleep to simulate delay before next roll
    except Exception as e:
        print(f"Error: {e}")
        pass

@HgBots.on_message(filters.command("ball"))
async def basketball_game(client, message):
    if message.forward_from:  # Check if the message is forwarded
        return

    input_str = message.text.split(" ", 1)
    if len(input_str) > 1:
        input_int = int(input_str[1])
    else:
        input_int = random.randint(1, 5)

    if input_int < 1 or input_int > 5:
        await message.reply("Please use a number between 1 and 5.")
        return

    # Use send_dice to send the dice emoji with basketball
    r = await message.reply("🏀")  # Basketball emoji for the game
    try:
        while True:
            roll = random.randint(1, 5)  # Random dice value between 1 and 5
            if roll == input_int:
                await r.edit(f"🏀 You scored {roll}, and it matches your input!")
                break
            await r.edit(f"🏀 Ball hit {roll}. Try again!")
            await asyncio.sleep(1)  # Sleep to simulate delay before next roll
    except Exception as e:
        print(f"Error: {e}")
        pass

@HgBots.on_message(filters.command("lol"))
async def lol_game(client, message):
    if message.forward_from:  # Check if the message is forwarded
        return

    input_str = message.text.split(" ", 1)
    if len(input_str) > 1:
        input_int = int(input_str[1])
    else:
        input_int = random.randint(1, 5)

    if input_int < 1 or input_int > 5:
        await message.reply("Please use a number between 1 and 5.")
        return

    # Use send_dice to send the dice emoji with laughing face
    r = await message.reply("😂")  # Laughing face emoji for the game
    try:
        while True:
            roll = random.randint(1, 5)  # Random dice value between 1 and 5
            if roll == input_int:
                await r.edit(f"😂 You got {roll}, and it matches your input!")
                break
            await r.edit(f"😂 Rolled a {roll}. Try again!")
            await asyncio.sleep(1)  # Sleep to simulate delay before next roll
    except Exception as e:
        print(f"Error: {e}")
        pass

from pyrogram import Client, filters, enums
from pyrogram.types import Message, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserAdminInvalid
import re
import asyncio

# Function to check if user is admin or owner
async def is_admin_or_owner(client, chat, user_id):
    try:
        user = await client.get_chat_member(chat.id, user_id)
        if user.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
            return True
        return False
    except Exception:
        return False

@HgBots.on_message(filters.command("kick"))
async def kick(client, message: Message):
    if not await is_admin_or_owner(client, message.chat, message.from_user.id):
        await message.reply("You must be an admin or the group owner to use this command.")
        return

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        try:
            await client.ban_chat_member(message.chat.id, user_id)
            await message.reply(f"Kicked {message.reply_to_message.from_user.first_name} from the group.")
        except Exception as e:
            await message.reply(f"Failed to kick user: {e}")
    else:
        await message.reply("Please reply to the message of the user you want to kick.")

@HgBots.on_message(filters.command("pin"))
async def pin(client, message: Message):
    if not await is_admin_or_owner(client, message.chat, message.from_user.id):
        await message.reply("You must be an admin or the group owner to use this command.")
        return

    if message.reply_to_message:
        try:
            await message.reply_to_message.pin()
            await message.reply("**📌Pinned the message.**")
        except Exception as e:
            await message.reply(f"Failed to pin message: {e}")
    else:
        await message.reply("Please reply to the message you want to pin.")

@HgBots.on_message(filters.command("unpin"))
async def unpin(client, message: Message):
    if not await is_admin_or_owner(client, message.chat, message.from_user.id):
        await message.reply("You must be an admin or the group owner to use this command.")
        return

    if message.reply_to_message:
        try:
            await message.reply_to_message.unpin()
            await message.reply("**📌Unpinned the message.**")
        except Exception as e:
            await message.reply(f"Failed to unpin message: {e}")
    else:
        await message.reply("Please reply to the message you want to unpin.")

@HgBots.on_message(filters.command("del"))
async def delete_message(client, message: Message):
    if not await is_admin_or_owner(client, message.chat, message.from_user.id):
        await message.reply("You must be an admin or the group owner to use this command.")
        return

    if message.reply_to_message:
        try:
            await message.reply_to_message.delete()
            await message.reply("**✅Deleted the replied message.**")
        except Exception as e:
            await message.reply(f"Failed to delete message: {e}")
    else:
        await message.reply("Please reply to the message you want to delete.")

from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserAdminInvalid
import asyncio

# Function to check if the user is an admin or owner
async def is_admin_or_owner(client, chat, user_id):
    try:
        user = await client.get_chat_member(chat.id, user_id)
        if user.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
            return True
        return False
    except Exception:
        return False

@HgBots.on_message(filters.command("purge") & filters.group)
@bot_admin
async def purge(client: Client, message: Message):
    if not await is_admin_or_owner(client, message.chat, message.from_user.id):
        await message.reply("You need to be an admin or the group owner to use this command.")

    # Ensure the command is replying to a message
    if not message.reply_to_message:
        return await message.reply("You need to reply to a message to use this command.")

    # Get the replied-to message's ID
    reply_message_id = message.reply_to_message.message_id

    try:
        # Get all messages in the chat after the replied message
        messages_to_delete = []
        async for msg in client.get_chat_history(message.chat.id, from_message_id=reply_message_id + 1):
            messages_to_delete.append(msg.message_id)

        # Add the replied message itself to the deletion list if necessary
        messages_to_delete.append(reply_message_id)

        # Delete the collected messages
        await client.delete_messages(message.chat.id, messages_to_delete)
        
        # Inform the user
        await message.reply(f"Successfully purged all messages below the replied message.")

    except Exception as e:
        await message.reply(f"An error occurred while purging messages: {str(e)}")

# Warn command with coroutine fix
user_warnings = {}  # Global variable to track user warnings

@HgBots.on_message(filters.command("warn"))
async def warn(client, message: Message):
    if not await is_admin_or_owner(client, message.chat, message.from_user.id):
        await message.reply("You must be an admin or the group owner to use this command.")
        return

    if not message.reply_to_message:
        await message.reply("Please reply to the message of the user you want to warn.")
        return

    user_id = message.reply_to_message.from_user.id
    user_warnings[user_id] = user_warnings.get(user_id, 0) + 1

    if user_warnings[user_id] >= 3:
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply(f"{message.reply_to_message.from_user.first_name} has been banned after 3 warnings.")
        user_warnings[user_id] = 0  # Reset warnings after banning
    else:
        await message.reply(f"{message.reply_to_message.from_user.first_name} has received warning #{user_warnings[user_id]}.")

# Other parts of the code remain unchanged
@HgBots.on_message(filters.command("warns"))
async def check_warns(client, message: Message):
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
        target_user_id = target_user.id
    else:
        if len(message.text.split()) < 2:
            await message.reply("Please reply to a user's message or provide their user ID or username.")
            return

        user_input = message.text.split()[1]
        if user_input.isdigit():
            target_user_id = int(user_input)
        elif user_input.startswith('@'):
            username = user_input[1:]
            try:
                user = await client.get_users(username)
                target_user_id = user.id
            except Exception:
                await message.reply("User not found by username.")
                return
        else:
            await message.reply("Invalid input. Please provide a valid user ID or username.")
            return

    warnings = user_warnings.get(target_user_id, 0)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"❗Remove warning ({warnings})", callback_data=f"remove_warn_{target_user_id}")]
    ])

    await message.reply(f"{target_user.first_name} has {warnings} warning(s).", reply_markup=keyboard)

@HgBots.on_callback_query(filters.regex(r"remove_warn_(\d+)"))
async def remove_warn(client, callback_query):
    match = re.match(r"remove_warn_(\d+)", callback_query.data)
    if match:
        user_id = int(match.group(1))

        if callback_query.from_user.id != user_id and not await is_admin_or_owner(client, callback_query.message.chat, callback_query.from_user.id):
            await callback_query.answer("You don't have permission to remove this warning.", show_alert=True)
            return

        if user_warnings.get(user_id, 0) > 0:
            user_warnings[user_id] -= 1
            await callback_query.answer(f"Warning removed. ({user_warnings[user_id]}/3)")
        else:
            await callback_query.answer("This user has no warnings to remove.")

        await callback_query.edit_message_text(f"User {user_id} has {user_warnings.get(user_id, 0)} warning(s).")
    else:
        await callback_query.answer("Invalid callback data.", show_alert=True)

@HgBots.on_message(filters.command("kickme"))
async def kickme(client, message: Message):
    try:
        bot_member = await client.get_chat_member(message.chat.id, client.me.id)
        if not bot_member.can_restrict_members:
            await message.reply("**I don't have permission to ban members!**")
            return
        
        await client.ban_chat_member(message.chat.id, message.from_user.id)
        await message.reply(f"{message.from_user.first_name} has been kicked from the group!")

        await asyncio.sleep(3600)
        await client.unban_chat_member(message.chat.id, message.from_user.id)
        await message.reply(f"{message.from_user.first_name} has been unbanned and can rejoin the group!")

    except Exception as e:
        await message.reply(f"An error occurred: {e}")

@HgBots.on_message(filters.command("punchme"))
async def punchme(client, message: Message):
    await message.reply("Ouch! You've been punched! 💥")

from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated

# Custom welcome and goodbye messages
welcome_message = "Welcome {user} to the {group_name} Clan⚔️! We're glad to have you here."
goodbye_message = "Goodbye {user}, {group_name} will miss you!"

# Function to send a welcome message
async def send_welcome(client, chat_id, user_first_name, group_name):
    message = welcome_message.format(user=user_first_name, group_name=group_name)
    await client.send_message(chat_id, message)

# Function to send a goodbye message
async def send_goodbye(client, chat_id, user_first_name, group_name):
    message = goodbye_message.format(user=user_first_name, group_name=group_name)
    await client.send_message(chat_id, message)

# Handle both welcome and goodbye messages in a single handler
@HgBots.on_chat_member_updated()
async def handle_user_join_leave(client, update: ChatMemberUpdated):
    # Ensure both old and new chat members exist before accessing their attributes
    if update.old_chat_member and update.new_chat_member:
        chat_id = update.chat.id
        group_name = update.chat.title

        # When a new user joins the chat (status "member")
        if update.new_chat_member.status == "member":
            user_first_name = update.new_chat_member.user.first_name
            await send_welcome(client, chat_id, user_first_name, group_name)

        # When a user leaves the chat (status "left")
        elif update.old_chat_member.status in ("member", "administrator") and update.new_chat_member.status == "left":
            user_first_name = update.old_chat_member.user.first_name
            await send_goodbye(client, chat_id, user_first_name, group_name)

from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions
import asyncio
import json

# Dictionary to track which chats have tagging active (optional: save to a file for persistence)
active_tagging_chats = {}

# Optional: Load active tagging state from a file
try:
    with open('active_tagging_chats.json', 'r') as f:
        active_tagging_chats = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    active_tagging_chats = {}

async def is_admin(client, chat_id, user_id):
    try:
        # Get the user's status in the group
        user = await client.get_chat_member(chat_id, user_id)
        
        # Check if the user is an admin or the group owner
        if user.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
            return True
        return False
    except Exception as e:
        print(f"Error checking admin status: {e}")
        return False


@HgBots.on_message(filters.command("tagall") & filters.group)
async def tagall(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Check if the user is an admin or the group owner
    if not await is_admin(client, chat_id, user_id):
        await message.reply("You need to be an admin to use this command.")
        return

    # Check if tagging is already active
    if active_tagging_chats.get(str(chat_id)):
        await message.reply("Tagging is already active in this group.")
        return

    # Mark tagging as active in this chat
    active_tagging_chats[str(chat_id)] = True
    # Optionally save the active state
    with open('active_tagging_chats.json', 'w') as f:
        json.dump(active_tagging_chats, f)

    await message.reply("Starting to tag all members...")

    # Get all participants
    async for member in client.get_chat_members(chat_id):
        # Stop tagging if /stop command was used
        if not active_tagging_chats.get(str(chat_id)):
            break

        user = member.user
        try:
            if user.username:
                await message.reply(f"@{user.username}")
            else:
                await message.reply(f"[{user.first_name}](tg://user?id={user.id})", disable_web_page_preview=True)
            await asyncio.sleep(1)  # Delay to avoid hitting Telegram's flood limits
        except Exception as e:
            print(f"Error tagging user {user.id}: {e}")

@HgBots.on_message(filters.command("stop") & filters.group)
async def stop(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Check if the user is an admin or the group owner
    if not await is_admin(client, chat_id, user_id):
        await message.reply("You need to be an admin to use this command.")
        return

    # Stop tagging in this chat
    active_tagging_chats[str(chat_id)] = False
    # Optionally save the active state
    with open('active_tagging_chats.json', 'w') as f:
        json.dump(active_tagging_chats, f)

    await message.reply("Tagging has been stopped.")

import random
import html
import json
from pyrogram import filters
from pyrogram.types import Message, MessageEntity

# Dictionary for storing AFK status (load/save from file for persistence)
afk_users = {}

# Load AFK status from file
try:
    with open('afk_users.json', 'r') as f:
        afk_users = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    afk_users = {}

def set_afk(user_id, reason=""):
    afk_users[user_id] = reason
    with open('afk_users.json', 'w') as f:
        json.dump(afk_users, f)

def remove_afk(user_id):
    if user_id in afk_users:
        del afk_users[user_id]
        with open('afk_users.json', 'w') as f:
            json.dump(afk_users, f)
        return True
    return False

def check_afk(user_id):
    return afk_users.get(user_id, None)

@HgBots.on_message(filters.command("afk") & filters.group)
async def afk(client, message: Message):
    args = message.text.split(None, 1)
    user_id = message.from_user.id
    reason = args[1][:100] if len(args) > 1 else ""
    
    set_afk(user_id, reason)
    notice = "\nYour AFK reason was shortened to 100 characters." if len(args) > 1 and len(args[1]) > 100 else ""
    await message.reply(f"{message.from_user.first_name} is now AFK!{notice}")

@HgBots.on_message(filters.group & filters.incoming)
async def no_longer_afk(client, message: Message):
    user_id = message.from_user.id
    
    if remove_afk(user_id):
        options = [
            '{} the pro is back!', '{} why came back!', '{} is here to make trouble!',
            '{} has reincarnated!', '{} is back, but don’t trash the chat!',
            '{} go back!', '{} be gentle to everyone!'
        ]
        response = random.choice(options).format(message.from_user.first_name)
        await message.reply(response)

@HgBots.on_message(filters.group & filters.incoming)
async def reply_afk(client, message: Message):
    entities = message.entities or []
    mentioned_user_ids = set()

    # Collect mentioned users
    for entity in entities:
        if entity.type in [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]:
            user_id = entity.user.id if entity.user else None
            if user_id:
                mentioned_user_ids.add(user_id)

    # Check for AFK status in mentions and replies
    for user_id in mentioned_user_ids:
        reason = check_afk(user_id)
        if reason is not None:
            afk_message = f"{html.escape(message.from_user.first_name)} is AFK."
            if reason:
                afk_message += f"\nReason: <code>{html.escape(reason)}</code>"
            await message.reply(afk_message, disable_web_page_preview=True)

# Register handlers
__handlers__ = [
    (afk, filters.command("afk") & filters.group),
    (no_longer_afk, filters.group & filters.incoming),
    (reply_afk, filters.group & filters.incoming),
]

from pyrogram import Client, filters
from pyrogram.types import Message
from googletrans import Translator, LANGUAGES
import re

# Initialize Translator instance
translator = Translator()

# Function to extract language and text from the command message
def extract_language_and_text(message_text: str):
    pattern = r"^/translate (\w{2}) (.+)"
    match = re.match(pattern, message_text)
    
    if match:
        language = match.group(1)
        text = match.group(2)
        return language, text
    return None, None

# Translation function using googletrans
def translate(text: str, dest_language: str):
    if dest_language not in LANGUAGES:  # Check if language code is valid
        return None
    result = translator.translate(text, dest=dest_language)
    return result.text if result else None

@HgBots.on_message(filters.command("translate"))
async def translate_message(client, message: Message):
    # Extract language and text from the message
    language, text = extract_language_and_text(message.text)
    
    # Check if language and text are correctly extracted
    if language and text:
        if language not in LANGUAGES:
            await message.reply_text(f"Invalid language code '{language}'. Please use a valid 2-letter language code.")
            return
        
        try:
            translated_text = translate(text, language)  # Perform translation
            
            if translated_text:  # Check if translation was successful
                await message.reply_text(translated_text)
            else:
                await message.reply_text("Translation resulted in an empty message. Please try again with different input.")
        
        except Exception as e:
            print(f"Error during translation: {e}")
            await message.reply_text("An error occurred while trying to translate your message.")
    else:
        await message.reply_text("Invalid format. Please use: `/translate <language_code> <text>`")

import os
import io
import random
import glob
import requests
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters  # Change Client to Hgbots

LOGO_LINKS = [
"https://files.catbox.moe/ny65qb.jpg",
"https://files.catbox.moe/p7ee3f.jpg",
"https://files.catbox.moe/09gst5.jpg",
"https://files.catbox.moe/n4kxq2.jpg",
"https://files.catbox.moe/m6u762.jpg",
"https://files.catbox.moe/r4d4m8.jpg",
"https://files.catbox.moe/b5f237.jpg",
"https://files.catbox.moe/1chttp.jpg",
"https://files.catbox.moe/np3u9g.jpg",
"https://files.catbox.moe/4qt0fz.jpg",
"https://files.catbox.moe/0o1dq8.jpg",
"https://files.catbox.moe/317txp.jpg",
"https://files.catbox.moe/sbtzvi.jpg",
"https://files.catbox.moe/hfonlf.jpg",
"https://files.catbox.moe/lk5g8k.jpg",
"https://files.catbox.moe/w0ilyr.jpg",
"https://files.catbox.moe/8u9rfq.jpg"
]

@HgBots.on_message(filters.command("logo") & (filters.private | filters.group))  # Change Client to Hgbots
async def logo_generator(client, message):
    text = message.text.split(' ', 1)
    
    if len(text) < 2:
        await message.reply("**Please provide a text for the logo.**")
        return

    text = text[1]
    await message.reply("**Generating your logo, please wait...**")

    try:
        # Select a random logo background image from LOGO_LINKS
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        
        buttons = [[InlineKeyboardButton(text="🎉Made By ƤƛƖƝ ✨", url=f"https://t.me/PainXrobot")]]
        reply_markup = InlineKeyboardMarkup(buttons)

        # Specify the fixed font path
        font_path = "./imagefiles/logofiles/logofont1.otf"  # Replace 'YourFont.ttf' with the actual font file name
        font = ImageFont.truetype(font_path, 140)
        font_path = os.path.join("imagefiles", "logofiles", "logofont1.otf")

        bbox = draw.textbbox((0, 0), text, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        image_widthz, image_heightz = img.size

        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2
        draw.text((x, y), text, font=font, fill="white", stroke_width=5, stroke_fill="black")

        
        # Save the image as PNG
        output_file = "logo_output.png"
        img.save(output_file, "PNG")

        # Send the logo to the user
        await message.reply_photo(output_file, caption="**Here is your logo! Made By @PainXrobot**", reply_markup=reply_markup)

        # Clean up the file after sending
        if os.path.exists(output_file):
            os.remove(output_file)

    except Exception as e:
        await message.reply(f"Error generating logo: {str(e)}")

import sqlite3
from telegram import Update
from telegram.ext import (
    Application,
    CallbackContext,
    CommandHandler,
    ChatMemberHandler,
    filters,
)
from telegram.helpers import mention_html
from io import BytesIO

# Replace this with the actual user ID of the bot owner
BOT_OWNER_ID = 5147671960  

# Initialize Database
def init_db():
    conn = sqlite3.connect('gban_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gbans (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            reason TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gban_enforcement (
            chat_id INTEGER PRIMARY KEY,
            enforce_gban BOOLEAN DEFAULT 1
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            chat_id INTEGER PRIMARY KEY
        )
    ''')
    conn.commit()
    conn.close()

# Database Functions
def add_group(chat_id):
    conn = sqlite3.connect('gban_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO groups (chat_id) VALUES (?)", (chat_id,))
    conn.commit()
    conn.close()

def remove_group(chat_id):
    conn = sqlite3.connect('gban_data.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM groups WHERE chat_id = ?", (chat_id,))
    conn.commit()
    conn.close()

def get_all_groups():
    conn = sqlite3.connect('gban_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT chat_id FROM groups")
    results = [row[0] for row in cursor.fetchall()]
    conn.close()
    return results

def is_user_gbanned(user_id):
    conn = sqlite3.connect('gban_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM gbans WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def gban_user(user_id, name, reason):
    conn = sqlite3.connect('gban_data.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR REPLACE INTO gbans (user_id, name, reason) VALUES (?, ?, ?)",
        (user_id, name, reason),
    )
    conn.commit()
    conn.close()

def ungban_user(user_id):
    conn = sqlite3.connect('gban_data.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM gbans WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

def get_gban_list():
    conn = sqlite3.connect('gban_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name, reason FROM gbans")
    results = cursor.fetchall()
    conn.close()
    return results

# Bot Owner Check
def is_owner(user_id: int) -> bool:
    return user_id == BOT_OWNER_ID

async def gban(update: Update, context: CallbackContext):
    if not is_owner(update.effective_user.id):
        await update.message.reply_text("You are not authorized to use this command.")
        return

    args = context.args
    if len(args) < 1:
        await update.message.reply_text("Usage: /gban <user_id> [reason]")
        return

    try:
        user_id = int(args[0])
    except ValueError:
        await update.message.reply_text("Invalid user ID. Please provide a valid numerical ID.")
        return

    reason = " ".join(args[1:]) if len(args) > 1 else "No reason provided"

    # Fetch user details
    try:
        user_name = (await context.bot.get_chat(user_id)).first_name
    except Exception as e:
        await update.message.reply_text(f"Error fetching user details: {e}")
        return

    # Add user to the gban list
    gban_user(user_id, user_name, reason)
    await update.message.reply_text(f"User {user_name} (ID: {user_id}) has been globally banned.")

    # Remove gbanned user from all groups
    await remove_gbanned_users_from_all_groups(context)

async def ungban(update: Update, context: CallbackContext):
    if not is_owner(update.effective_user.id):
        await update.message.reply_text("You are not authorized to use this command.")
        return

    args = context.args
    if len(args) < 1:
        await update.message.reply_text("Usage: /ungban <user_id>")
        return

    user_id = int(args[0])
    if not is_user_gbanned(user_id):
        await update.message.reply_text("This user is not globally banned.")
        return

    ungban_user(user_id)
    await update.message.reply_text(f"User with ID {user_id} has been un-gbanned.")

async def gbanlist(update: Update, context: CallbackContext):
    if not is_owner(update.effective_user.id):
        await update.message.reply_text("You are not authorized to use this command.")
        return

    banned_users = get_gban_list()
    if not banned_users:
        await update.message.reply_text("No users are currently gbanned.")
        return

    banfile = "GBanned Users:\n"
    for user_id, name, reason in banned_users:
        banfile += f"User ID: {user_id}\nName: {name}\nReason: {reason}\n\n"

    with BytesIO(banfile.encode()) as output:
        output.name = "gbanlist.txt"
        await update.message.reply_document(document=output, caption="List of globally banned users.")

# Group Tracking
async def track_group_join(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    add_group(chat_id)

async def remove_gbanned_users_from_all_groups(context: CallbackContext):
    bot = context.bot
    gbanned_users = get_gban_list()
    all_groups = get_all_groups()

    for chat_id in all_groups:
        for user_id, name, reason in gbanned_users:
            try:
                await bot.ban_chat_member(chat_id, user_id)
            except Exception:
                continue

# Initialize the Database
init_db()

def main():
    HgBots = Application.builder().token("8109859388:AAEMZHWpYjORT9nwIlI1yj3Vc7JbpjjjIzU").build()

    HgBots.add_handler(CommandHandler("gban", gban))
    HgBots.add_handler(CommandHandler("ungban", ungban))
    HgBots.add_handler(CommandHandler("gbanlist", gbanlist))
    HgBots.add_handler(ChatMemberHandler(track_group_join, filters.ChatMemberHandler.MY_CHAT_MEMBER))

                
    HgBots.run_polling()

import logging
from pyrogram import Client, filters
from pyrogram.types import Message
import sqlite3
from contextlib import closing

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SQLite database setup
DB_NAME = 'bot_data.db'

# Initialize database and tables
def init_db():
    with closing(sqlite3.connect(DB_NAME)) as conn, conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS groups (group_id INTEGER PRIMARY KEY)''')

init_db()

# Database helper functions
def add_user(user_id):
    with closing(sqlite3.connect(DB_NAME)) as conn, conn:
        conn.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))

def add_group(group_id):
    with closing(sqlite3.connect(DB_NAME)) as conn, conn:
        conn.execute("INSERT OR IGNORE INTO groups (group_id) VALUES (?)", (group_id,))

def get_all_users():
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users")
        return [row[0] for row in cursor.fetchall()]

def get_all_groups():
    with closing(sqlite3.connect(DB_NAME)) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT group_id FROM groups")
        return [row[0] for row in cursor.fetchall()]

# Function to check if a user is an admin
def is_admin(user_id):
    # Replace with your bot owner's user ID
    return user_id == 5147671960

# Track users and groups
@HgBots.on_message(filters.text)
async def track_user(client, message: Message):
    user_id = message.from_user.id
    if message.chat.type == "private":
        add_user(user_id)
        logger.info(f"Added user {user_id} to the database.")
    elif message.chat.type == "group":
        add_group(message.chat.id)
        logger.info(f"Added group {message.chat.id} to the database.")

# Broadcast command
@HgBots.on_message(filters.command("broadcast"))
async def broadcast(client, message: Message):
    user_id = message.from_user.id
    if not is_admin(user_id):
        await message.reply("Only the bot owner can send broadcasts.")
        return

    if not message.reply_to_message:
        await message.reply("You need to reply to a message to broadcast it.")
        return

    # Identify the message to broadcast
    message_to_broadcast = message.reply_to_message
    await message.reply("Broadcasting message to all users and groups...")

    # Broadcasting to all users
    users = get_all_users()
    successful_users, failed_users = await send_broadcast(client, users, message_to_broadcast, message.chat.id)

    # Broadcasting to all groups
    groups = get_all_groups()
    successful_groups, failed_groups = await send_broadcast(client, groups, message_to_broadcast, message.chat.id)

    # Summary of broadcast
    summary = f"""
    **Broadcast Summary:**
      ------------------
    - Users Broadcasted: {len(successful_users)}
    - Groups Broadcasted: {len(successful_groups)}
    - Failed Users: {len(failed_users)}
    - Failed Groups: {len(failed_groups)}
    """
    await message.reply(summary)

# Helper function to broadcast to a list of chat IDs
async def send_broadcast(client, recipients, message_to_broadcast, chat_id):
    successful = []
    failed = []
    
    for recipient in recipients:
        try:
            # Send the correct type of message
            if message_to_broadcast.text:
                await client.send_message(recipient, message_to_broadcast.text)
            elif message_to_broadcast.photo:
                await client.send_photo(recipient, photo=message_to_broadcast.photo.file_id, caption=message_to_broadcast.caption or "")
            elif message_to_broadcast.video:
                await client.send_video(recipient, video=message_to_broadcast.video.file_id, caption=message_to_broadcast.caption or "")
            elif message_to_broadcast.audio:
                await client.send_audio(recipient, audio=message_to_broadcast.audio.file_id, caption=message_to_broadcast.caption or "")
            elif message_to_broadcast.document:
                await client.send_document(recipient, document=message_to_broadcast.document.file_id, caption=message_to_broadcast.caption or "")
            else:
                await client.copy_message(recipient, chat_id, message_to_broadcast.message_id)
            successful.append(recipient)
        except Exception as e:
            logger.error(f"Failed to send to {recipient}: {e}")
            failed.append(recipient)
    
    return successful, failed
    

print("Bot was Started")
HgBots.run()
