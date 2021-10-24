

@pyrogram.Client.on_callback_query(pyrogram.filters.regex('^help$'))
async def help_cb(bot, message):
    await message.answer()
    await help(bot, message, True)


@pyrogram.Client.on_callback_query(pyrogram.filters.regex('^close$'))
async def close_cb(bot, message):
    await message.message.delete()
    await message.message.reply_to_message.delete()


@pyrogram.Client.on_callback_query(pyrogram.filters.regex('^back$'))
async def back_cb(bot, message):
    await message.answer()
    await start(bot, message, True)


@pyrogram.Client.on_callback_query(pyrogram.filters.regex('^about$'))
async def about_cb(bot, message):
    await message.answer()
    await about(bot, message, True)


@pyrogram.Client.on_callback_query(pyrogram.filters.regex('^refreshmeh$'))
async def refreshmeh_cb(bot, message):
    if Config.UPDATES_CHANNEL:
        invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
        try:
            user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), message.from_user.id)
            if user.status == "kicked":
                await message.message.edit(
                    text="Sorry Sir, You are Banned. Contact My [Support Group](https://t.me/safothebot).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await message.message.edit(
                text="**You Still Didn't Join ☹️, Please Join My Updates Channel To Use Me!**\n\nDue to Overload, Only Channel Subscribers Can Use Me!",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Join Updates Channel 🤖", url=invite_link.invite_link)
                        ],
                        [
                            InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await message.message.edit(
                text="Something Went Wrong. Contact My [Support Group](https://t.me/safothebot).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return
    await message.answer()
    await start(bot, message, True)



