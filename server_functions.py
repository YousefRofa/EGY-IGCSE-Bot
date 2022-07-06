import nextcord as discord


def isModerator(member: discord.Member):
    roles = [role.id for role in member.roles]
    if 967998090688753725 in roles:
        return True
    else:
        return False


def hasRole_id(member: discord.Member, role_id):
    roles = [role.id for role in member.roles]
    if role_id in roles:
        return True
    return False


def isfat7i(member: discord.Member):
    if member.id == 991046687042703390:
        return True
    return False


async def is_banned(user, guild):
    try:
        await guild.fetch_ban(user)
        return True
    except discord.NotFound:
        return False
