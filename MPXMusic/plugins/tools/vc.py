from MPXMusic.utils import MPXBin
from MPXMusic import app
from MPXMusic.utils.inline import close_markup
from MPXMusic.utils.database import get_assistant, get_lang
from pyrogram import filters
from pyrogram.enums import ChatType
from strings import get_string

@app.on_message(
    filters.command(["vc", "vcs", "vcm", "vcms"]) & filters.admin
)
async def vc_members(client, message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")

    # Delete the command message
    await message.delete()

    # Initial message
    msg = await client.send_message(
        chat_id=message.chat.id,
        text="🚫 Fᴇᴛᴄʜɪɴɢ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ʟɪsᴛ... 🎙️"
    )

    userbot = await get_assistant(message.chat.id)
    TEXT = ""

    try:
        async for m in userbot.get_call_members(message.chat.id):
            chat_id = m.chat.id
            username = m.chat.username or "N/A"
            is_muted = "🔇" if bool(m.is_muted and not m.can_self_unmute) else "🔈"

            if m.chat.type != ChatType.PRIVATE:
                title = m.chat.title
            else:
                try:
                    title = (await client.get_users(chat_id)).mention
                except:
                    title = m.chat.first_name or "Unknown"

            TEXT += (
                f"{title} ⟿ <code>{chat_id}</code> ⟿ {is_muted}\n"
                f"└ @{username}"
                "\n\n"
            )

        if len(TEXT) < 4000:
            await msg.edit(
                TEXT or "⚠️ Nᴏ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. 🚫",
                reply_markup=close_markup(_),
            )
        else:
            link = await MPXbin(TEXT)
            await msg.edit(
                f"📄 𝗟𝗶𝗻𝗸 𝗽𝗮𝗿𝗮 𝗹𝗶𝘀𝘁𝗮: {link}",
                disable_web_page_preview=True,
                reply_markup=close_markup(_),
            )
    except ValueError as e:
        await msg.edit("❗ 𝗘𝗿𝗿𝗼𝗿𝗲: 𝗡𝗮̃𝗼 𝗳𝗼𝗶 𝗽𝗼𝘀𝘀𝗶́𝘃𝗲𝗹 𝗰𝗮𝗿𝗿𝗲𝗴𝗮𝗿 𝗮 𝗹𝗶𝘀𝘁𝗮.")