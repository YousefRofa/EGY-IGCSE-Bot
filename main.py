import nextcord as discord
from nextcord.ext import commands
from nextcord.utils import get
from server_functions import isModerator, hasRole_id, isfat7i, is_banned
from server_bases import rules_msg, server_roles_msg, server_roles_buttons, case_msg, warn_msg,\
    server_rules, session_roles_buttons, session_roles_msg, subject_roles_msgs, subject_roles_buttons, welcome_msg, warning_details
from server_data import server_channels, server_roles_data
import pymongo
import datetime, time
import requests
import os
from pytesseract import pytesseract
import io
from PIL import Image


TOKEN = os.environ.get("TOKEN")
MONGODB_LINK =  'mongodb+srv://Yousefrofa:Nodanaro842006@egy-igcse-bot.orccawa.mongodb.net/?retryWrites=true&w=majority'  # os.environ.get("MONGODB_LINK")
path_to_tesseract = r"./.apt/usr/share/tesseract-ocr/4.00/tessdata"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
cluster = pymongo.MongoClient(MONGODB_LINK)

GUILD_ID = 967997831690465290

# Events on starting the bot


async def set_roles():
    server_roles_channel = bot.get_channel(server_channels['roles_server-roles'])
    messages = await server_roles_channel.history(limit=1).flatten()
    await messages[0].edit(view=server_roles_buttons())
    session_roles_channel = bot.get_channel(server_channels['roles_session-roles'])
    messages = await session_roles_channel.history(limit=1).flatten()
    await messages[0].edit(view=session_roles_buttons())
    subject_roles_channel = bot.get_channel(server_channels['roles_subjects-roles'])
    messages = await subject_roles_channel.history().flatten()
    for message in messages:
        await message.edit(view=subject_roles_buttons(str(message.embeds[0].title)))


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("DM to contact mods!"))
    await set_roles()
    print("Bot ready as {0.user}".format(bot))


@bot.event
async def on_member_join(member):
    channel = await member.create_dm()
    await channel.send(embeds=welcome_msg)

# Moderators actions


@bot.slash_command(description="Oxembllah h5leh y5ras 5ales (mods only)")
async def mute(interaction: discord.Interaction,
               user: discord.Member =
                    discord.SlashOption(name="member",
                                        description="User to mute", required=True),
               reason: str=discord.SlashOption(name="reason", description="El sabab?", required=True)):
    if isModerator(interaction.user):
        if await is_banned(user, interaction.guild):
            await interaction.send("User is banned from the server", ephemeral=True)
            return
        mute_role = discord.utils.get(interaction.guild.roles, id=server_roles_data['muted'])
        if hasRole_id(user, mute_role.id):
            await interaction.send("User is already muted", ephemeral=True)
            return
        if isModerator(user):
            await interaction.send("You cant mute a mod yasta", ephemeral=True)
            return
        if isfat7i(user):
            await interaction.send("3ayz t3mli ana mute?? :(", ephemeral=True)
            return
        await interaction.response.defer()

        db = cluster['Behavior']
        if not user.name in db.list_collection_names():
            db.create_collection(f'{user.name}#{user.discriminator}')
        collection = db[f'{user.name}#{user.discriminator}']

        collection.insert_one({'Date': datetime.datetime.utcnow(), 'Case': 'Mute', 'Reason': reason,
                               'Moderator': f'{interaction.user.name}#{interaction.user.discriminator}'})

        await user.add_roles(mute_role)
        log_channel = bot.get_channel(server_channels['server_info_moderators-actions'])
        last_ban_msg = await log_channel.history(limit=1).flatten()
        case_no = int(last_ban_msg[0].embeds[0].title.split()[1][1:])+1
        await log_channel.send(embed=case_msg("Mute", case_no, user, interaction.user, reason))
        await interaction.send("5aleto y5ras 5ales, 2y 5dma yabaaa")
    else:
        await interaction.send(f"You are not a mod :P", ephemeral=True)


@bot.slash_command(description="H5leh yrg3 ytklm tani (mods only)")
async def unmute(interaction: discord.Interaction,
               user: discord.Member =
                    discord.SlashOption(name="member",
                                        description="User to mute", required=True),
               reason: str=discord.SlashOption(name="reason", description="El sabab?", required=False)):
    if isModerator(interaction.user):
        mute_role = discord.utils.get(interaction.guild.roles, id=server_roles_data['muted'])
        if not hasRole_id(user, mute_role.id):
            await interaction.send("User is not muted", ephemeral=True)
            return
        if await is_banned(user, interaction.guild):
            await interaction.send("User is banned from the server", ephemeral=True)
            return
        await interaction.response.defer()
        await user.remove_roles(mute_role)
        log_channel = bot.get_channel(server_channels['server_info_moderators-actions'])
        last_ban_msg = await log_channel.history(limit=1).flatten()
        case_no = int(last_ban_msg[0].embeds[0].title.split()[1][1:])+1
        await log_channel.send(embed=case_msg("Unmute", case_no, user, interaction.user, reason))
        await interaction.send("5aleto yrg3 ytklm tani, 2y 5dma yabaaa")
    else:
        await interaction.send(f"You are not a mod :P", ephemeral=True)


@bot.slash_command(description="Htl3o bara el server (mods only)")
async def kick(interaction: discord.Interaction,
               user: discord.Member =
                    discord.SlashOption(name="member",
                                        description="User you to kick", required=True),
               reason: str=discord.SlashOption(name="reason", description="El sabab?", required=True)):
    if isModerator(interaction.user):
        if await is_banned(user, interaction.guild):
            await interaction.send("User is banned from the server", ephemeral=True)
            return
        if isModerator(user):
            await interaction.send("You cant kick a mod yasta", ephemeral=True)
            return
        if isfat7i(user):
            await interaction.send("3ayz t3mly ana kick?? :(", ephemeral=True)
            return
        await interaction.response.defer()

        db = cluster['Behavior']
        if not user.name in db.list_collection_names():
            db.create_collection(f'{user.name}#{user.discriminator}')
        collection = db[f'{user.name}#{user.discriminator}']

        collection.insert_one({'Date': datetime.datetime.utcnow(), 'Case': 'Kick', 'Reason': reason,
                               'Moderator': f'{interaction.user.name}#{interaction.user.discriminator}'})

        log_channel = bot.get_channel(server_channels['server_info_moderators-actions'])
        last_ban_msg = await log_channel.history(limit=1).flatten()
        case_no = int(last_ban_msg[0].embeds[0].title.split()[1][1:])+1
        await log_channel.send(embed=case_msg("Kick", case_no, user, interaction.user, reason))
        await user.kick(reason=reason)
        await interaction.send("Tl3to bara el server, 2y 5dma yabaaa")
    else:
        await interaction.send(f"You are not a mod :P", ephemeral=True)


@bot.slash_command(description="Hdelo timeout 3asal (for mods)")
async def timeout(interaction: discord.Interaction,
                  user: discord.Member = discord.SlashOption(name="user", description="User to timeout",
                                                             required=True),
                  time_: str = discord.SlashOption(name="duration",
                                                   description="Duration of timeout (e.g. 1d5h)",
                                                   required=True),
                  reason: str = discord.SlashOption(name="reason", description="el sabab?", required=True)):
    if await is_banned(user, interaction.guild):
        await interaction.send("User is banned from the server", ephemeral=True)
        return
    if isModerator(user):
        await interaction.send(f"You cant timeout a mod yasta", ephemeral=True)
        return
    await interaction.response.defer()

    db = cluster['Behavior']
    if not user.name in db.list_collection_names():
        db.create_collection(f'{user.name}#{user.discriminator}')
    collection = db[f'{user.name}#{user.discriminator}']

    collection.insert_one({'Date': datetime.datetime.utcnow(), 'Case': 'Timeout', 'Reason': reason,
                           'Moderator': f'{interaction.user.name}#{interaction.user.discriminator}'})

    seconds = 0
    if "d" in time_:
        seconds += int(time_.split("d")[0]) * 86400
        time_ = time_.split("d")[1]
    if "h" in time_:
        seconds += int(time_.split("h")[0]) * 3600
        time_ = time_.split("h")[1]
    if "m" in time_:
        seconds += int(time_.split("m")[0]) * 60
        time_ = time_.split("m")[1]
    if "s" in time_:
        seconds += int(time_.split("s")[0])
    if seconds == 0:
        await interaction.send("You can't timeout for zero seconds!", ephemeral=True)
        return
    await user.edit(timeout=discord.utils.utcnow() + datetime.timedelta(seconds=seconds))
    human_readable_time = f"{seconds // 86400}d {(seconds % 86400) // 3600}h {(seconds % 3600) // 60}m {seconds % 60}s"
    log_channel = bot.get_channel(server_channels['server_info_moderators-actions'])
    last_ban_msg = await log_channel.history(limit=1).flatten()
    case_no = int(last_ban_msg[0].embeds[0].title.split()[1][1:])+1
    until = f"<t:{int(time.time()) + seconds}> (<t:{int(time.time()) + seconds}:R>)"
    await log_channel.send(embed=case_msg("Timeout", case_no, user, interaction.user, reason,human_readable_time, until))
    await interaction.send(f"timed out {user.mention} until {until}")


@bot.slash_command(description="H4eel el timeout mno (mods only)")
async def untimeout(interaction: discord.Interaction,
               user: discord.Member =
                    discord.SlashOption(name="member",
                                        description="User to untimeout", required=True),
               reason: str=discord.SlashOption(name="reason", description="El sabab?", required=False)):
    if isModerator(interaction.user):
        if await is_banned(user, interaction.guild):
            await interaction.send("User is banned from the server", ephemeral=True)
            return
        if not user._timeout:
            await interaction.send("User is not timed out", ephemeral=True)
            return
        await interaction.response.defer()
        await user.edit(timeout=None)
        log_channel = bot.get_channel(server_channels['server_info_moderators-actions'])
        last_ban_msg = await log_channel.history(limit=1).flatten()
        case_no = int(last_ban_msg[0].embeds[0].title.split()[1][1:])+1
        await log_channel.send(embed=case_msg("Untimeout", case_no, user, interaction.user, reason))
        await interaction.send("mb2a4 timed out 5las, 2y 5dma yabaaa")
    else:
        await interaction.send(f"You are not a mod :P", ephemeral=True)


@bot.slash_command(description="Hadelo ban el server (mods only)")
async def ban(interaction: discord.Interaction,
               user: discord.Member =
                    discord.SlashOption(name="member",
                                        description="User you to ban", required=True),
               reason: str=discord.SlashOption(name="reason", description="El sabab?", required=True),
              delete_message_days: int = discord.SlashOption(name="delete_messages",
            choices={"Don't Delete Messages": 0, "Delete Today's Messages": 1, "Delete 3 Days of Messages": 3, 'Delete 1 Week of Messages': 7},
                                                             default=0, description="Duration of messages from the user to delete (defaults to zero)", required=True)):
    if isModerator(interaction.user):
        if await is_banned(user, interaction.guild):
            await interaction.send("User is banned from the server", ephemeral=True)
            return
        if isModerator(user):
            await interaction.send("You cant ban a mod yasta", ephemeral=True)
            return
        if isfat7i(user):
            await interaction.send("3ayz t3mly ana ban?? :(", ephemeral=True)
            return
        await interaction.response.defer()

        db = cluster['Behavior']
        if not user.name in db.list_collection_names():
            db.create_collection(f'{user.name}#{user.discriminator}')
        collection = db[f'{user.name}#{user.discriminator}']

        collection.insert_one({'Date': datetime.datetime.utcnow(), 'Case': 'Ban', 'Reason': reason,
                               'Moderator': f'{interaction.user.name}#{interaction.user.discriminator}'})

        log_channel = bot.get_channel(server_channels['server_info_moderators-actions'])
        last_ban_msg = await log_channel.history(limit=1).flatten()
        case_no = int(last_ban_msg[0].embeds[0].title.split()[1][1:])+1
        await log_channel.send(embed=case_msg("Ban", case_no, user, interaction.user, reason))
        await interaction.guild.ban(user, delete_message_days=delete_message_days)
        await interaction.send("2deto ban mn el server, 2y 5dma yabaaa")
    else:
        await interaction.send(f"You are not a mod :P", ephemeral=True)


@bot.slash_command(description="H4eel el ban mno el server (mods only)")
async def unban(interaction: discord.Interaction,
               user: discord.Member =
                    discord.SlashOption(name="member",
                                        description="User you to unban", required=True),
               reason: str=discord.SlashOption(name="reason", description="El sabab?", required=False)):
    if isModerator(interaction.user):
        if await is_banned(user, interaction.guild):
            await interaction.response.defer()
            log_channel = bot.get_channel(server_channels['server_info_moderators-actions'])
            last_ban_msg = await log_channel.history(limit=1).flatten()
            case_no = int(last_ban_msg[0].embeds[0].title.split()[1][1:])+1
            await log_channel.send(embed=case_msg("Unban", case_no, user, interaction.user, reason))
            await interaction.guild.unban(user)
            await interaction.send("4elt mno el ban, 2y 5dma yabaaa")
        else:
            if isModerator(user):
                await interaction.send("You cant unban a mod yasta", ephemeral=True)
                return
            await interaction.send("user is not banned!", ephemeral=True)
    else:
        await interaction.send(f"You are not a mod :P", ephemeral=True)


@bot.slash_command(description="Hdelo klmtan kda (mods only)")
async def warn(interaction: discord.Interaction,
               user: discord.Member =
                    discord.SlashOption(name="member",
                                        description="User you to warn", required=True),
               reason: str=discord.SlashOption(name="reason", description="El sabab?", required=True)):
    if isModerator(interaction.user):
        if await is_banned(user, interaction.guild):
            await interaction.send("User is banned from the server", ephemeral=True)
            return
        if isModerator(user):
            await interaction.send("You cant warn a mod yasta", ephemeral=True)
            return
        if isfat7i(user):
            await interaction.send("3ayz t3mly ana warn?? :(", ephemeral=True)
            return

        db = cluster['Behavior']
        if not f'{user.name}#{user.discriminator}' in db.list_collection_names():
            db.create_collection(f'{user.name}#{user.discriminator}')
        collection = db[f'{user.name}#{user.discriminator}']

        collection.insert_one({'Date': datetime.datetime.utcnow(), 'Case': 'Warn', 'Reason': reason, 'Moderator': f'{interaction.user.name}#{interaction.user.discriminator}'})

        warnings_channel = bot.get_channel(server_channels['moderation_warnings'])
        await warnings_channel.send(embed=warning_details(interaction.user, user, reason, datetime.datetime.utcnow()))

        await user.send(warn_msg(interaction.user, reason))
        await interaction.send("Warned them 5las, 2y 5dma yabaa", ephemeral=True)
    else:
        await interaction.send(f"You are not a mod :P", ephemeral=True)


@bot.slash_command(description="Show user past history (mods only)")
async def history(interaction: discord.Interaction,
               user: discord.Member =
                    discord.SlashOption(name="member",
                                        description="User you to unban", required=True)):
    if isModerator(interaction.user):
        db = cluster['Behavior']
        if not f'{user.name}#{user.discriminator}' in db.list_collection_names():
            await interaction.send("User has no previous history.")
            return
        collection = db[f'{user.name}#{user.discriminator}']
        message = f'```{user} History\n\n'
        for activity in collection.find():
            message += f'Case : {activity["Case"]}\nReason : {activity["Reason"]}\nModerator : {activity["Moderator"]}\nDate : {activity["Date"]}\n\n'
        await interaction.send(message+'```')
    else:
        await interaction.send(f"You are not a mod :P", ephemeral=True)

# Commands


@bot.slash_command(description="Send server rules (mods only)")
async def set_server_rules(interaction: discord.Interaction):
    if isModerator(interaction.user):
        await interaction.channel.send(embeds=rules_msg)
        await interaction.send("Done!", ephemeral=True)
    else:
        await interaction.send("You have to be a mod to perform this action", ephemeral=True)


@bot.slash_command(description="Send session rules (mods only)")
async def set_session_roles(interaction: discord.Interaction):
    if isModerator(interaction.user):
        await interaction.channel.send(embeds=session_roles_msg, view=session_roles_buttons())
        await interaction.send("Done!", ephemeral=True)
    else:
        await interaction.send("You have to be a mod to perform this action", ephemeral=True)


@bot.slash_command(description="Send server roles (mods only)")
async def set_server_roles(interaction: discord.Interaction):
    if isModerator(interaction.user):
        await interaction.channel.send(embeds=server_roles_msg, view=server_roles_buttons())
        await interaction.send("Done!", ephemeral=True)
    else:
        await interaction.send("You have to be a mod to perform this action", ephemeral=True)


@bot.slash_command(description="Send subject roles (mods only)")
async def set_subject_roles(interaction: discord.Interaction):
    if isModerator(interaction.user):
        await interaction.channel.send(embed=subject_roles_msgs['title'])
        await interaction.channel.send(embed=subject_roles_msgs['Mathematics & Sciences'], view=subject_roles_buttons("maths and sciences"))
        await interaction.channel.send(embed=subject_roles_msgs['Languages'], view=subject_roles_buttons("Languages"))
        await interaction.channel.send(embed=subject_roles_msgs['Humanities & Social Sciences'], view=subject_roles_buttons("Humanities and social sciences"))
        await interaction.channel.send(embed=subject_roles_msgs['Computer Subjects'], view=subject_roles_buttons("Computer Subjects"))
        await interaction.send("Done!", ephemeral=True)
    else:
        await interaction.send("You have to be a mod to perform this action", ephemeral=True)


@bot.slash_command(description="Mention a server rule")
async def rule(interaction: discord.Interaction,
               rule_number: int = discord.SlashOption(name="rule_number",
                                                      description="The number of the rule you want to mention", required=True, min_value=1, max_value=6)):
    rule_mention = server_rules[rule_number]+f'\n\nAll server rules are mentioned in <#{server_channels["server_info_rules"]}>'
    await interaction.send(rule_mention)


@bot.slash_command(description="Send messages in server channels (mods only)")
async def send(interaction: discord.Interaction,
                content: str = discord.SlashOption(name="content", description="the message content to be sent", required=True),
                channel: discord.abc.GuildChannel = discord.SlashOption(name="channel", description="the channel to send the message in", required=False),
                embed: bool = discord.SlashOption(name="embed", description="send message in embed form", required=False)):
    if isModerator(interaction.user):
        if channel == None:
            channel = interaction.channel
        if embed == True:
            embed = discord.Embed.from_dict(
                eval("{'color': 5111808, 'type': 'rich', " + f"'description': '{content}'" + "}"))
            await channel.send(embed=embed)
        else:
            await channel.send(content)
        embed = discord.Embed.from_dict(eval("{'color': 5111808, 'type': 'rich', "+f"'description': '{content}'"+"}"))
        data_channel = bot.get_channel(991088800065261618)  # the bot-messaging channel
        await data_channel.send(content=f'Message sent in {channel.mention} by {interaction.user}', embed=embed)
        await interaction.send("Done", ephemeral=True)
    else:
        await interaction.send("You have to be a mod to perform this action", ephemeral=True)


@bot.slash_command(description="delete")
async def delete(interaction: discord.Interaction,
                 limit: int=discord.SlashOption(name="number", description="number of messages to delete", required=True)):
    fetchMessage = await interaction.channel.history(limit=limit).flatten()
    for m in fetchMessage:
        await m.delete()
    await interaction.send("Deleted my messages :(", ephemeral=True)


@bot.slash_command(description='Find the past paper with the mark scheme')
async def findpaper(interaction: discord.Interaction,
                    query: str = discord.SlashOption(name="query", description="Search query", required=False),
                    img: discord.Attachment = discord.SlashOption(name="image",
                                                                     description="Image to find the paper of",
                                                                     required=False)):
    if img:
        response = requests.get(img.url, stream=True)
        img = Image.open(io.BytesIO(response.content))
        context = pytesseract.image_to_string(img).replace("\n", " ").replace("  ", "").replace("  ", "")
    elif query:
        context = ' '.join(query)
    else:
        await interaction.send('You have to set either a query or an image', ephemeral=True)
        return
    response = requests.get(f"https://paper.sc/search/?as=json&query={context}").json()
    if len(response['list']) == 0:
        await interaction.send("No results found in past papers. Try changing your query for better results.")
    else:
        embed = discord.Embed(title="Potential Match",
                              description="Found a question paper matching your question!",
                              colour=discord.Colour.blurple())
        for number, item in enumerate(response['list']):
            if not len(item['related']) == 0:
                embed.add_field(name="Subject", value=item['doc']['subject'], inline=True)
                embed.add_field(name="Paper", value=item['doc']['paper'], inline=True)
                embed.add_field(name="Session", value=item['doc']['time'], inline=True)
                embed.add_field(name="Variant", value=item['doc']['variant'], inline=True)
                embed.add_field(name="QP Link", value=f"https://paper.sc/doc/{item['doc']['_id']}", inline=True)
                embed.add_field(name="MS Link", value=f"https://paper.sc/doc/{item['related'][0]['_id']}",
                                inline=True)
                if number == 2:
                    await interaction.send(embed=embed)
                    return
        await interaction.send(embed=embed)

# Actions when a message is sent


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    guild = bot.get_guild(GUILD_ID)
    mod_mail_channel = get(guild.text_channels, id=server_channels['moderation_mod-mail'])

    # Mod mail
    if not message.guild:
        threads_names_ids = [[thread.name, thread.id] for thread in mod_mail_channel.threads]
        for thread in threads_names_ids:
            if thread[0] == str(message.author.id):
                thread = mod_mail_channel.get_thread(thread[1])
                if message.content:
                    await thread.send(message.content)
                for attachment in message.attachments:
                    await thread.send(file=await attachment.to_file())
                return
        embed = discord.Embed(colour=discord.Colour.dark_blue(), title=f'Mail sent by {message.author}', description=message.content)
        mail = await mod_mail_channel.send(embed=embed)
        await mail.create_thread(name=f'{message.author.id}')
        await message.reply("Your message has been sent to the EGY-IGCSE moderators! Any mod reply will be conveyed to you by DM.")
        return

    if type(message.channel) == discord.Thread:
        if message.channel.parent == mod_mail_channel:
            user_id = int(str(message.channel))
            user = bot.get_user(user_id)
            if message.content:
                await user.send(content=message.content)
            for attachment in message.attachments:
                await user.send(file=await attachment.to_file())
            return


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Invalid command. Try using** `help` **to figure out commands!**")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Please pass in all requirements.**')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**You dont have all the requirements or permissions for using this command :angry:**")

bot.run(TOKEN)
