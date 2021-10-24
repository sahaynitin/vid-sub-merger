@Client.on_message(pyrogram.filters.command("help"))
async def help(bot, message, cb=False):
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, message)
      if fsub == 400:
        return
    me = await bot.get_me()
    button = [[
        InlineKeyboardButton(f'🏡 Home', callback_data='back'),
        InlineKeyboardButton(f'👲 About', callback_data='about')
        ],[
        InlineKeyboardButton(f'👥 Source', url='https://t.me/tellybots_digital'),
        InlineKeyboardButton(f'⛔ Close', callback_data='close')
        ]]
    reply_markup = InlineKeyboardMarkup(button)
    if cb:
        await message.message.edit(
            text=Script.HELP_USER.format(bot_name=me.mention(style='md')),
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
    else:
        await message.reply_text(
            text=Script.HELP_USER.format(bot_name=me.mention(style='md')),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        )


@Client.on_message(pyrogram.filters.command("start"))
async def start(bot, message, cb=False):
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, message)
      if fsub == 400:
        return
    me = await bot.get_me()
    owner = await bot.get_users(Config.OWNER_ID)
    owner_username = owner.username if owner.username else 'AsmSafone'
    button = [[
        InlineKeyboardButton(f'💡 Help', callback_data='help'),
        InlineKeyboardButton(f'👲 About', callback_data="about")
        ],[
        InlineKeyboardButton(f'🥰 Source', url='https://github.com/Tellybots/vid-sub-merger'),
        InlineKeyboardButton(f'⛔ Close', callback_data="close")
        ]]
    reply_markup = InlineKeyboardMarkup(button)
    if cb:
        await message.message.edit(
            text=Script.START_TEXT.format(user_mention=message.from_user.mention, bot_name=me.mention(style='md'), bot_owner=owner.mention(style="md")), 
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
    else:
        await message.reply_text(
            text=Script.START_TEXT.format(user_mention=message.from_user.mention, bot_name=me.mention(style='md'), bot_owner=owner.mention(style="md")), 
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        ) 


@Client.on_message(pyrogram.filters.command("about"))
async def about(bot, message, cb=False):
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, message)
      if fsub == 400:
        return
    me = await bot.get_me()
    button = [[
        InlineKeyboardButton(f'🏡 Home', callback_data='back'),
        InlineKeyboardButton(f'❔ Help', callback_data='help')
        ],[
        InlineKeyboardButton(f'👥 Update Channel', url='https://t.me/Tellybots_4u'),
        InlineKeyboardButton(f'⛔ Close', callback_data="close")
        ]]
    reply_markup = InlineKeyboardMarkup(button)
    if cb:
        await message.message.edit(
            text=Script.ABOUT.format(bot_name=me.mention(style='md')),
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
    else:
        await message.reply_text(
            text=Script.ABOUT.format(bot_name=me.mention(style='md')),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        )
