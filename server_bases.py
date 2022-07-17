import nextcord as discord
from nextcord.utils import get
from server_data import server_roles_data, session_roles_data, subject_roles_data
from server_functions import hasRole_id

rules_msg = [discord.Embed(colour=5111808, title="**EGY-IGCSE Discord Server rules**", description=
                 " As a member of this server you have to **agree** to [Discord Terms of Service](https://discord.com/terms)"
                 " and [Community Guidelines](https://discord.com/guidelines), serious action will be taken against any violation to these rules results"
        ),
            discord.Embed(colour=5111808, title='**1. Be respectful**', description=
                 "profanity use in this server should be minimally used and not used towards others, Respect all users under all conditions and treat others the way "
                 "you want to be treated. **All** forms of racism, discrimination and offencive jokes involving religion,"
                 " , gender and races are prohibited from this server, any type of harassment and inappropriate content and other NSFW material are also prohibited"
        ),
            discord.Embed(colour=5111808, title="**2. No offensive/inappropriate name, bio and profile picture**", description=
                     "Nick name, bio and profile pictures also fall under rule 1, You will be asked to change your name or picture if Moderators find them inappropriate."
        ),
            discord.Embed(colour=5111808, title="**3. Discussions in appropriate channels**", description=
                     "Keep the discussions in a channel topic related, avoid asking any subject related questions in general channels and take private conversations to dm."
        ),
            discord.Embed(colour=5111808, title="**4. Mentions**", description=
                     "Avoid mentioning moderators or specific members without proper reason. This includes replying to a message multiple times."
        ),
            discord.Embed(colour=5111808, title="**5. No spam**", description=
                     "No spam of any kind is allowed in any of the server channels except in <#991127999279800440>."
                     " This includes posting links, images, videos and general texts"
        ),
            discord.Embed(colour=5111808, title="**6. No piracy**", description=
                     "No piracy is allowed. This includes but is not limited to, torrenting, uploading, downloading, and sharing of copyrighted material."
            ),
            discord.Embed(colour=5111808, description=
                    "Moderators will take actions against any violation of these rules. You can get muted, banned,"
                    " timed out or kicked if you encouraged any violation to the rules. Please mention the mods if you witnessed any. \\n Thank you :)"
            ),
]

server_rules = {
    1: '**1. Be respectful**\nProfanity use in this server should be minimally used and not used towards others,'
       ' Respect all users under all conditions and treat others the way you want to be treated. All forms of racism,'
       ' discrimination and offencive jokes involving religion, , gender and races are prohibited from this server,'
       ' any type of harassment and inappropriate content and other NSFW material are also prohibited',
    2: '**2. No offensive/inappropriate name,bio and profile picture**\n'
       ' Nick name, bio and profile pictures also fall under rule 1,'
       ' You will be asked to change your name or picture if Moderators find them inappropriate.',
    3: '**3. Discussions in appropriate channels**\nKeep the discussions in a channel topic related,'
       ' avoid asking any subject related questions in general channels and take private conversations to dm.',
    4: '**4. Mentions**\nAvoid mentioning moderators or specific members without proper reason.'
       ' This includes replying to a message multiple times.',
    5: '**5. No spam**\nNo spam of any kind is allowed in any of the server channels except in <#991127999279800440>.'
       ' This includes posting links, images, videos and general texts',
    6: '**6. No piracy**\nNo piracy is allowed. '
       'This includes but is not limited to, torrenting, uploading, downloading, and sharing of copyrighted material.'
}

server_roles_msg = [discord.Embed(colour=discord.Colour.greyple(), title="**EGY-IGCSE Server roles**"
        ),
                discord.Embed(colour=discord.Colour.blurple(), title='**Announcements 📢**', description="If you assigned yourself this rule then you will receive a notification everytime"
                                                          "there is an announcement in <#991112179661148190>"
        ),
                discord.Embed(colour=discord.Colour.blurple(), title='**Announcements-off 🔇**', description="If you assigned yourself this rule then you will not receive a notification for"
                                                          "server announcements in <#991112179661148190>, but you will recieve a notifaction from normal pings/mentions."
        ),
                discord.Embed(colour=discord.Colour.blurple(), title='**Server-Mute 🔕**', description="If you assigned yourself this rule then you will receive no notification **under "
                                                          "any case**, You wont get mentioned personally and you wont be able to view server channel (You will be able to view this "
                                                          "channel only and un-assign this role at anytime)"
        ),      discord.Embed(colour=discord.Colour.blurple(), description='Choose a role using the buttons under this message')
                    ]

session_roles_msg = [discord.Embed(colour=discord.Colour.greyple(), title="**EGY-IGCSE Session roles**"
                                   ),
                    discord.Embed(colour=discord.Colour.blurple(),
                                  description="Choose the sessions which you will set exams in, and if you had sat any exams in previous session click on IG Alumni."

        ),
                     discord.Embed(colour=discord.Colour.blurple(),
                                   description="You can acquire more than one session role and to remove one of them re-press it's corresponding button.")
                     ]

subject_roles_msgs = {
    'title': discord.Embed(colour=discord.Colour.greyple(), title="**EGY-IGCSE Subject roles**"),
    'maths and sciences': discord.Embed(
        colour=discord.Colour.blurple(),
        title="Mathematics & Sciences",
        description='**1** : Biology\n**2** : Chemistry\n**3** : Physics\n**4** : Mathematics\n**5** : Psychology\n'),
    'Languages': discord.Embed(
        colour=discord.Colour.blurple(),
        title="Languages",
        description='**1** : Arabic\n**2** : French\n**3** : German\n**4** : English First Language\n'
                    '**5** : English Literature\n**6** : English as a second language\n'),
    'Humanities and social sciences': discord.Embed(
        colour=discord.Colour.blurple(),
        title="Humanities & Social Sciences",
        description='**1** : Accounting\n**2** : Business Studies\n**3** : Economics\n**4** : Environmental Management'
                    '\n**5** : Global Perspectives\n**6** : History'),
    'Computer Subjects': discord.Embed(
        colour=discord.Colour.blurple(),
        title="Computer Subjects",
        description='**1** : Computer Science\n**2** : ICT\n'),
}

welcome_msg = [discord.Embed(title="**سلام عليكم ورحمة الله وبركاتوووووو**",
        description="Al Salam Alaikum w ra7amt Allah w barakato - Mesa Mesa 3leko ya agd3 el so7ab."
                                        "\nWelcome to EGY-IGCSE. 5watak fy Allah w fel IGCSE").set_image("https://media.giphy.com/media/lJJtzOQJMnPmE3EjNc/giphy.gif"),
              discord.Embed(description="Bos yabny w ya benty, mafe4 7d yenkr en el yom ely d5lna feh el IG kan aktr 7aga nadmaneen 3leha, "
                                        "w ba2ena kolena ma4yeen 3al 7etan. Bs al 7amdulilah rabena satar.\n"
                                        "El kalam kal 2aty, mfe4 a7san lel masry mn a5oh el masry- w 3omrena ma nensa 7abayebna el ely fel 5aleeg "
                                        "-w gomhoreyet el IG kolaha 4ahedat 3la past papers tho3baneya w manaheg 8er ba4areya w ayam soda zy sawad 3yon Abo Nanci."),
              discord.Embed(title="**خدمات الزعامة**",
                  description="Akeed enta hates2al nfsk, 'y3ny asebny mn el hunood 3al youtube w ad5ol hena leh, ana mostafeed eh'\n"
                                        "Esm3 b2a yabn 3amy el 4o8l el gamed ely 3mk Adel Shakal hywfrholak"),
              discord.Embed(title="Kol mwad IG hna",
                  description="Ay mada 3ndk, swa2 chemistry, biology wla enta mn bto3 'ques quel ya la buini' e7na mawgooden w hnwafarlak kol egabat as2eltak f kol el mawad"),
              discord.Embed(title="Ngblk markscheme 2y so2al l7d 3andak",
                  description="Tb3n e7na yama zhe2na mn PMT w GCE Guide w Save My Exams. F El Z3ama gablak mn el a5er."
                                        " Erz3 screenshot el so2al f 2y channel w m3aha el command w 3mk hygeblak el markscheme l7ad 3andak").set_image("https://i.im.ge/2022/07/12/u48xTG.png"),
              discord.Embed(description="W tab3an b2a, mab2a4 ebn balady lw ma2oltelak4 en e7na agd3 nas, el mohem enta t3ala bs w e7na hno2af f dahrak w nesandak.\n"
                                        "W lw 3ndk ay 7aga, hezely wa7da DM hna w ana bnafsy ***El Z3ama*** **Adel Shakal** hawasal el resala l el Mods f asr3 wa2t \n"
                                        "W 3la kalam el 4a3er  *'لو قلبك جايبك, تعالى و هات حبايابك.'*")]


def warn_msg(moderator, reason):
    msg = f"""Hello,
    You have been warned in EGY-IGCSE for  '{reason}'
    We focus on maintaining a safe and secure environment for our community, and your account was flagged by the our server mods for violations of 
    our rules and Discords Community Guidelines (https://discord.com/guidelines).
    Please mindful your further actions in the server, If the behavior continues, we may take further action on your account.
    - {moderator}"""
    return msg


def case_msg(case_type, case_no, user, mod, reason=None, duration=None, time=None):
    embed = discord.Embed(colour=discord.Colour.dark_blue(), title=f'**Case #{case_no}   |   [{case_type}]**')
    embed.add_field(name="User:", value=str(user), inline=False)
    embed.add_field(name="Moderator:", value=mod.mention, inline=False)
    if reason:
        embed.add_field(name="Reason:", value=reason, inline=False)
    if time:
        embed.add_field(name="Duration:", value=duration, inline=False)
        embed.add_field(name="Until:", value=time, inline=False)
    return embed


def warning_details(user, mod, reason, time):
    embed = discord.Embed(colour=discord.Colour.dark_red(), title=f'{user.name}#{user.discriminator} warned')
    embed.add_field(name="Moderator: ", value=mod.mention, inline=False)
    embed.add_field(name="Reason: ", value=reason, inline=False)
    embed.add_field(name="Time: ", value=time, inline=False)
    return embed


def server_roles_buttons():
    view = discord.ui.View(timeout=None)
    Announcements_btn = discord.ui.Button(label='Announcements', style=discord.ButtonStyle.blurple)
    Announcements_off_btn = discord.ui.Button(label='Announcements off', style=discord.ButtonStyle.blurple)
    Server_mute_btn = discord.ui.Button(label='Server Mute', style=discord.ButtonStyle.blurple)

    async def remove_all_server_roles(user: discord.Member):
        for role in server_roles_data.values():
            if hasRole_id(user, role):
                await user.remove_roles(get(user.guild.roles, id=role))

    async def Announcements_Callback(interaction: discord.Interaction):
        await remove_all_server_roles(interaction.user)
        await interaction.user.add_roles(get(interaction.guild.roles, id=server_roles_data['announcements']))
        await interaction.response.send_message('You successfully opted the Announcements role!', ephemeral=True)

    async def Announcements_off_Callback(interaction: discord.Interaction):
        await remove_all_server_roles(interaction.user)
        await interaction.user.add_roles(get(interaction.guild.roles, id=server_roles_data['announcements-off']))
        await interaction.response.send_message('You successfully opted the Announcements-off role!', ephemeral=True)

    async def Server_mute_Callback(interaction: discord.Interaction):
        await remove_all_server_roles(interaction.user)
        await interaction.user.add_roles(get(interaction.guild.roles, id=server_roles_data['server-mute']))
        await interaction.response.send_message('You successfully opted the Server-Mute role!', ephemeral=True)

    Announcements_btn.callback = Announcements_Callback
    Announcements_off_btn.callback = Announcements_off_Callback
    Server_mute_btn.callback = Server_mute_Callback

    view.add_item(Announcements_btn)
    view.add_item(Announcements_off_btn)
    view.add_item(Server_mute_btn)

    return view


def session_roles_buttons():
    view = discord.ui.View(timeout=None)
    IGalumni_btn = discord.ui.Button(label='IG Alumni', style=discord.ButtonStyle.blurple)
    ON2022_btn = discord.ui.Button(label='O/N 2022', style=discord.ButtonStyle.blurple)
    FM2023_btn = discord.ui.Button(label='F/M 2023', style=discord.ButtonStyle.blurple)
    MJ2023_btn = discord.ui.Button(label='M/J 2023', style=discord.ButtonStyle.blurple)
    ON2023_btn = discord.ui.Button(label='O/N 2023', style=discord.ButtonStyle.blurple)
    FM2024_btn = discord.ui.Button(label='F/M 2024', style=discord.ButtonStyle.blurple)

    async def IGalumni_Callback(interaction: discord.Interaction):
        if hasRole_id(interaction.user, session_roles_data['IG Alumni']):
            await interaction.user.remove_roles(get(interaction.user.guild.roles, id=session_roles_data['IG Alumni']))
            await interaction.response.send_message('You successfully un-opted the IG Alumni role!', ephemeral=True)
        else:
            await interaction.user.add_roles(get(interaction.user.guild.roles, id=session_roles_data['IG Alumni']))
            await interaction.response.send_message('You successfully opted the IG Alumni role!', ephemeral=True)

    async def ON2022_Callback(interaction: discord.Interaction):
        if hasRole_id(interaction.user, session_roles_data['O/N 2022']):
            await interaction.user.remove_roles(get(interaction.user.guild.roles, id=session_roles_data['O/N 2022']))
            await interaction.response.send_message('You successfully un-opted the O/N 2022 role!', ephemeral=True)
        else:
            await interaction.user.add_roles(get(interaction.user.guild.roles, id=session_roles_data['O/N 2022']))
            await interaction.response.send_message('You successfully opted the O/N 2022 role!', ephemeral=True)

    async def FM2023_Callback(interaction: discord.Interaction):
        if hasRole_id(interaction.user, session_roles_data['F/M 2023']):
            await interaction.user.remove_roles(get(interaction.user.guild.roles, id=session_roles_data['F/M 2023']))
            await interaction.response.send_message('You successfully un-opted the F/M 2023 role!', ephemeral=True)
        else:
            await interaction.user.add_roles(get(interaction.user.guild.roles, id=session_roles_data['F/M 2023']))
            await interaction.response.send_message('You successfully opted the F/M 2023 role!', ephemeral=True)

    async def MJ2023_Callback(interaction: discord.Interaction):
        if hasRole_id(interaction.user, session_roles_data['M/J 2023']):
            await interaction.user.remove_roles(get(interaction.user.guild.roles, id=session_roles_data['M/J 2023']))
            await interaction.response.send_message('You successfully un-opted the M/J 2023 role!', ephemeral=True)
        else:
            await interaction.user.add_roles(get(interaction.user.guild.roles, id=session_roles_data['M/J 2023']))
            await interaction.response.send_message('You successfully opted the M/J 2023 role!', ephemeral=True)

    async def ON2023_Callback(interaction: discord.Interaction):
        if hasRole_id(interaction.user, session_roles_data['O/N 2023']):
            await interaction.user.remove_roles(get(interaction.user.guild.roles, id=session_roles_data['O/N 2023']))
            await interaction.response.send_message('You successfully un-opted the O/N 2023 role!', ephemeral=True)
        else:
            await interaction.user.add_roles(get(interaction.user.guild.roles, id=session_roles_data['O/N 2023']))
            await interaction.response.send_message('You successfully opted the O/N 2023 role!', ephemeral=True)

    async def FM2024_Callback(interaction: discord.Interaction):
        if hasRole_id(interaction.user, session_roles_data['F/M 2024']):
            await interaction.user.remove_roles(get(interaction.user.guild.roles, id=session_roles_data['F/M 2024']))
            await interaction.response.send_message('You successfully un-opted the F/M 2024 role!', ephemeral=True)
        else:
            await interaction.user.add_roles(get(interaction.user.guild.roles, id=session_roles_data['F/M 2024']))
            await interaction.response.send_message('You successfully opted the F/M 2024 role!', ephemeral=True)

    IGalumni_btn.callback = IGalumni_Callback
    ON2022_btn.callback = ON2022_Callback
    FM2023_btn.callback = FM2023_Callback
    MJ2023_btn.callback = MJ2023_Callback
    ON2023_btn.callback = ON2023_Callback
    FM2024_btn.callback = FM2024_Callback

    view.add_item(IGalumni_btn)
    view.add_item(ON2022_btn)
    view.add_item(FM2023_btn)
    view.add_item(MJ2023_btn)
    view.add_item(ON2023_btn)
    view.add_item(FM2024_btn)

    return view


def subject_roles_buttons(subjects_type):
    view = discord.ui.View(timeout=None)
    if subjects_type == 'Mathematics & Sciences':
        Biology_btn = discord.ui.Button(label='1', style=discord.ButtonStyle.blurple)
        Chemistry_btn = discord.ui.Button(label='2', style=discord.ButtonStyle.blurple)
        Physics_btn = discord.ui.Button(label='3', style=discord.ButtonStyle.blurple)
        Mathematics_btn = discord.ui.Button(label='4', style=discord.ButtonStyle.blurple)
        Psychology_btn = discord.ui.Button(label='5', style=discord.ButtonStyle.blurple)

        async def Biology_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['maths and sciences']['Biology']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['maths and sciences']['Biology']))
                await interaction.response.send_message('You successfully un-opted the Biology role!', ephemeral=True)
            else:
                await interaction.user.add_roles(get(interaction.user.guild.roles, id=subject_roles_data['maths and sciences']['Biology']))
                await interaction.response.send_message('You successfully opted the Biology role!', ephemeral=True)

        async def Chemistry_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['maths and sciences']['Chemistry']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['maths and sciences']['Chemistry']))
                await interaction.response.send_message('You successfully un-opted the Chemistry role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['maths and sciences']['Chemistry']))
                await interaction.response.send_message('You successfully opted the Chemistry role!', ephemeral=True)

        async def Physics_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['maths and sciences']['Physics']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['maths and sciences']['Physics']))
                await interaction.response.send_message('You successfully un-opted the Physics role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['maths and sciences']['Physics']))
                await interaction.response.send_message('You successfully opted the Physics role!', ephemeral=True)

        async def Mathematics_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['maths and sciences']['Mathematics']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['maths and sciences']['Mathematics']))
                await interaction.response.send_message('You successfully un-opted the Mathematics role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['maths and sciences']['Mathematics']))
                await interaction.response.send_message('You successfully opted the Mathematics role!', ephemeral=True)

        async def Psychology_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['maths and sciences']['Psychology']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['maths and sciences']['Psychology']))
                await interaction.response.send_message('You successfully un-opted the Psychology role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['maths and sciences']['Psychology']))
                await interaction.response.send_message('You successfully opted the Psychology role!', ephemeral=True)

        Biology_btn.callback = Biology_Callback
        Chemistry_btn.callback = Chemistry_Callback
        Physics_btn.callback = Physics_Callback
        Mathematics_btn.callback = Mathematics_Callback
        Psychology_btn.callback = Psychology_Callback

        view.add_item(Biology_btn)
        view.add_item(Chemistry_btn)
        view.add_item(Physics_btn)
        view.add_item(Mathematics_btn)
        view.add_item(Psychology_btn)

        return view

    if subjects_type == 'Languages':
        Arabic_btn = discord.ui.Button(label='1', style=discord.ButtonStyle.blurple)
        French_btn = discord.ui.Button(label='2', style=discord.ButtonStyle.blurple)
        German_btn = discord.ui.Button(label='3', style=discord.ButtonStyle.blurple)
        English_First_Language_btn = discord.ui.Button(label='4', style=discord.ButtonStyle.blurple)
        English_Literature_btn = discord.ui.Button(label='5', style=discord.ButtonStyle.blurple)
        ESL_btn = discord.ui.Button(label='6', style=discord.ButtonStyle.blurple)

        async def Arabic_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['languages']['Arabic']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['Arabic']))
                await interaction.response.send_message('You successfully un-opted the Arabic role!', ephemeral=True)
            else:
                await interaction.user.add_roles(get(interaction.user.guild.roles, id=subject_roles_data['languages']['Arabic']))
                await interaction.response.send_message('You successfully opted the Arabic role!', ephemeral=True)

        async def French_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['languages']['French']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['French']))
                await interaction.response.send_message('You successfully un-opted the French role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['French']))
                await interaction.response.send_message('You successfully opted the French role!', ephemeral=True)

        async def German_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['languages']['German']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['German']))
                await interaction.response.send_message('You successfully un-opted the German role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['German']))
                await interaction.response.send_message('You successfully opted the German role!', ephemeral=True)

        async def English_First_Language_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['languages']['English First Language']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['English First Language']))
                await interaction.response.send_message('You successfully un-opted the English First Language role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['English First Language']))
                await interaction.response.send_message('You successfully opted the English First Language role!', ephemeral=True)

        async def English_Literature_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['languages']['English Literature']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['English Literature']))
                await interaction.response.send_message('You successfully un-opted the English Literature role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['English Literature']))
                await interaction.response.send_message('You successfully opted the English Literature role!', ephemeral=True)

        async def ESL_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['languages']['English as a second language']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['English as a second language']))
                await interaction.response.send_message('You successfully un-opted the English as a second language role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['languages']['English as a second language']))
                await interaction.response.send_message('You successfully opted the English as a second language role!', ephemeral=True)

        Arabic_btn.callback = Arabic_Callback
        French_btn.callback = French_Callback
        German_btn.callback = German_Callback
        English_First_Language_btn.callback = English_First_Language_Callback
        English_Literature_btn.callback = English_Literature_Callback
        ESL_btn.callback = ESL_Callback

        view.add_item(Arabic_btn)
        view.add_item(French_btn)
        view.add_item(German_btn)
        view.add_item(English_First_Language_btn)
        view.add_item(English_Literature_btn)
        view.add_item(ESL_btn)

        return view

    if subjects_type == 'Humanities & Social Sciences':
        Accounting_btn = discord.ui.Button(label='1', style=discord.ButtonStyle.blurple)
        Business_Studies_btn = discord.ui.Button(label='2', style=discord.ButtonStyle.blurple)
        Economics_btn = discord.ui.Button(label='3', style=discord.ButtonStyle.blurple)
        Environmental_Management_btn = discord.ui.Button(label='4',
                                                       style=discord.ButtonStyle.blurple)
        Global_Perspectives_btn = discord.ui.Button(label='5', style=discord.ButtonStyle.blurple)
        History_btn = discord.ui.Button(label='6', style=discord.ButtonStyle.blurple)

        async def Accounting_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['Humanities and social sciences']['Accounting']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['Accounting']))
                await interaction.response.send_message('You successfully un-opted the Accounting role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['Accounting']))
                await interaction.response.send_message('You successfully opted the Accounting role!', ephemeral=True)

        async def Business_Studies_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['Humanities and social sciences']['Business Studies']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['Business Studies']))
                await interaction.response.send_message('You successfully un-opted the Business Studies role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['Business Studies']))
                await interaction.response.send_message('You successfully opted the Business Studies role!', ephemeral=True)

        async def Economics_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['Humanities and social sciences']['Economics']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['Economics']))
                await interaction.response.send_message('You successfully un-opted the Economics role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['Economics']))
                await interaction.response.send_message('You successfully opted the Economics role!', ephemeral=True)

        async def Environmental_Management_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['Humanities and social sciences']['Environmental Management']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['Environmental Management']))
                await interaction.response.send_message('You successfully un-opted the Environmental Management role!',
                                                        ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['Environmental Management']))
                await interaction.response.send_message('You successfully opted the Environmental Management role!',
                                                        ephemeral=True)

        async def Global_Perspectives_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['Humanities and social sciences']['Global Perspectives']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['Global Perspectives']))
                await interaction.response.send_message('You successfully un-opted the Global Perspectives role!',
                                                        ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['Global Perspectives']))
                await interaction.response.send_message('You successfully opted the Global Perspectives role!',
                                                        ephemeral=True)

        async def History_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['Humanities and social sciences']['History']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['History']))
                await interaction.response.send_message('You successfully un-opted the History role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Humanities and social sciences']['History']))
                await interaction.response.send_message('You successfully opted the History role!', ephemeral=True)

        Accounting_btn.callback = Accounting_Callback
        Business_Studies_btn.callback = Business_Studies_Callback
        Economics_btn.callback = Economics_Callback
        Environmental_Management_btn.callback = Environmental_Management_Callback
        Global_Perspectives_btn.callback = Global_Perspectives_Callback
        History_btn.callback = History_Callback

        view.add_item(Accounting_btn)
        view.add_item(Business_Studies_btn)
        view.add_item(Economics_btn)
        view.add_item(Environmental_Management_btn)
        view.add_item(Global_Perspectives_btn)
        view.add_item(History_btn)

        return view

    if subjects_type == 'Computer Subjects':
        Computer_Science_btn = discord.ui.Button(label='1', style=discord.ButtonStyle.blurple)
        ICT_btn = discord.ui.Button(label='2', style=discord.ButtonStyle.blurple)

        async def Computer_Science_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['Computer subjects']['Computer Science']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Computer subjects']['Computer Science']))
                await interaction.response.send_message('You successfully un-opted the Computer Science role!', ephemeral=True)
            else:
                await interaction.user.add_roles(get(interaction.user.guild.roles, id=subject_roles_data['Computer subjects']['Computer Science']))
                await interaction.response.send_message('You successfully opted the Computer Science role!', ephemeral=True)

        async def ICT_Callback(interaction: discord.Interaction):
            if hasRole_id(interaction.user, subject_roles_data['Computer subjects']['ICT']):
                await interaction.user.remove_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Computer subjects']['ICT']))
                await interaction.response.send_message('You successfully un-opted the ICT role!', ephemeral=True)
            else:
                await interaction.user.add_roles(
                    get(interaction.user.guild.roles, id=subject_roles_data['Computer subjects']['ICT']))
                await interaction.response.send_message('You successfully opted the ICT role!', ephemeral=True)

        Computer_Science_btn.callback = Computer_Science_Callback
        ICT_btn.callback = ICT_Callback

        view.add_item(Computer_Science_btn)
        view.add_item(ICT_btn)

        return view