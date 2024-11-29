import random 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from MPXMusic import app

WELCOME = [
    "https://i.postimg.cc/9MKRx6DB/1.png",
    "https://i.postimg.cc/jqnJWS13/2.png",
    "https://i.postimg.cc/8cvFxZWg/3.png",
    "https://i.postimg.cc/NM52ksjM/4.png",
    "https://i.postimg.cc/RVrJwz5S/5.png",
    "https://i.postimg.cc/gkvXDBmv/6.png",
    "https://i.postimg.cc/3x1yM4yN/7.png",
    "https://i.postimg.cc/8zNFnBzx/8.png",
    "https://i.postimg.cc/jjjDRxNX/9.png",
    "https://i.postimg.cc/fbgJLGfh/10.png",
    "https://i.postimg.cc/FRMzb06W/11.png",
    "https://i.postimg.cc/Qt9VWffK/12.png",
    "https://i.postimg.cc/MZBv6rch/13.png",
    "https://i.postimg.cc/90yMLr5W/14.png",
    "https://i.postimg.cc/bNjdsHkd/15.png",
]

#--------------------------

MUST_JOIN = "MPXStore"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(random.choice(WELCOME),caption=f"ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !\n\nɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ , ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ʏᴏᴜ ᴊᴏɪɴᴇᴅ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Jᴏɪɴ!", url="https://t.me/MPXStore"),]]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_ᴊᴏɪɴ ᴄʜᴀᴛ {MUST_JOIN}")