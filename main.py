import discord, asyncio, json, typing, urllib, re, os, random, requests, discord.utils
from googletrans import Translator
from discord.utils import get
from discord.ext import commands
from bs4 import BeautifulSoup, SoupStrainer



config = dict()
client = discord.Client()
prefix = '>'
bot = commands.Bot(command_prefix=prefix)
translator = Translator()
lastdel = None
lastauth = None
try:
    with open ('data/config.json') as con_file:
        config = json.load(con_file)
except:
    print('Uh oh!')
    exit(42)

@bot.event
async def on_ready():
    print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")


@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    illegal = False
    if message_id == 702233518444511292:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        if payload.emoji.name == '🔞':
            illegal = True
            role = ''
        if payload.emoji.name == '👴':
            role = discord.utils.get(guild.roles,name='30+')
        if payload.emoji.name == '👨':
            role = discord.utils.get(guild.roles,name='26-30')
        if payload.emoji.name == 'pepeOK':
            role = discord.utils.get(guild.roles,name='22-26')
        if payload.emoji.name == 'PepeHappy':
            role = discord.utils.get(guild.roles,name='18-22')
        if payload.emoji.name == 'PepeHands':
            role = discord.utils.get(guild.roles,name='16-18')
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                if illegal == True:
                    chan = await member.create_dm()
                    await chan.send('You must be 16 or above to be in this server, come back later :)')
                    await member.kick()
                else:
                    await member.add_roles(role)
            else:
                print('member not found owo')

@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    illegal = False
    if message_id == 702233518444511292:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        if payload.emoji.name == '🔞':
            illegal = True
            role = ''
        if payload.emoji.name == '👴':
            role = discord.utils.get(guild.roles,name='30+')
        if payload.emoji.name == '👨':
            role = discord.utils.get(guild.roles,name='26-30')
        if payload.emoji.name == 'pepeOK':
            role = discord.utils.get(guild.roles,name='22-26')
        if payload.emoji.name == 'PepeHappy':
            role = discord.utils.get(guild.roles,name='18-22')
        if payload.emoji.name == 'PepeHands':
            role = discord.utils.get(guild.roles,name='16-18')
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                if illegal == True:
                    await member.kick()
                else:
                    await member.remove_roles(role)
            else:
                print('member not found owo')

@bot.event
async def on_message(message):
    if len(message.raw_mentions) > 3:
        await message.channel.send('You have been muted for trying to mention over 3 people, if this is an error pls message a mod or admin')
        role = get(message.guild.roles, name='Muted')
        await message.author.add_roles(role)
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error,commands.CheckFailure):
        return await ctx.send('You dont have perms to do that')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('This is not a command')

@bot.event
async def on_message_delete(message):
    global lastdel
    global lastauth
    log_channel = 701773703700152361
    chan = bot.get_channel(log_channel)
    embed = discord.Embed()
    embed.add_field(name="Message Content", value=message.content, inline=False)
    embed.add_field(name="Author", value=message.author, inline=False)
    embed.add_field(name="Channel", value=message.channel, inline=False)
    bot.lastauth = message.author
    lastdel = message.content
    lastauth = message.author
    print(str(lastauth) +' said : ' + str(lastdel))
    await chan.send(embed=embed)

"""
@bot.event
async def on_message(message):
    if str(message.channel.id) == "695005243087257600":
        await message.add_reaction("bird_heart:701522966504275980")
"""
@bot.command(pass_context=True)
async def hello_world(ctx):
    print('oof')
    await ctx.message.channel.send('Hey there ' + str(ctx.message.author))

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member = None):
    bangifs = ['https://giphy.com/gifs/ban-banned-salt-bae-Vh2c84FAPVyvvjZJNM','https://giphy.com/gifs/trump-ban-LPHbzPcICc86EVte9C','https://giphy.com/gifs/hammer-super-mario-8-bit-qPD4yGsrc0pdm','https://giphy.com/gifs/H99r2HtnYs492','https://giphy.com/gifs/ban-HXcALJVPgaR4A','https://giphy.com/gifs/dvOwFmfbzmAsI9v2IV','https://giphy.com/gifs/ii-topic-diablo-1zFXgNa44Z904','https://giphy.com/gifs/CybZqG4etuZsA','https://giphy.com/gifs/banned-Qn0LMesNcMHKg']
    if not member:
        await ctx.send('Please specify a member to ban')
        return
    await member.ban()
    embed = discord.Embed(title='Member Banned', description='User banned: ' + str(member.mention))
    await ctx.send(embed=embed)
    await ctx.send(random.choice(bangifs))

@bot.command()
@commands.has_permissions(administrator=True)
async def fban(ctx, member: discord.Member = None):
    bangifs = ['https://giphy.com/gifs/ban-banned-salt-bae-Vh2c84FAPVyvvjZJNM','https://giphy.com/gifs/trump-ban-LPHbzPcICc86EVte9C','https://giphy.com/gifs/hammer-super-mario-8-bit-qPD4yGsrc0pdm','https://giphy.com/gifs/H99r2HtnYs492','https://giphy.com/gifs/ban-HXcALJVPgaR4A','https://giphy.com/gifs/dvOwFmfbzmAsI9v2IV','https://giphy.com/gifs/ii-topic-diablo-1zFXgNa44Z904','https://giphy.com/gifs/CybZqG4etuZsA','https://giphy.com/gifs/banned-Qn0LMesNcMHKg']
    if not member:
        await ctx.send('Please specify a member to ban')
        return
    embed = discord.Embed(title='Member Banned', description='User banned: ' + str(member.mention))
    await ctx.send(embed=embed)
    await ctx.send(random.choice(bangifs))
    await ctx.message.delete()

@bot.command()
async def thot_spotted(ctx, member: discord.Member = None):
    if not member:
        await ctx.send('Please show me the thot to eliminate')
        return
    embed = discord.Embed(title='Thot Spotted!', description='Closing in on {}, the thot cannon is coming out now, 3. 2. 1. FIRE. !!!!!'.format(member.mention))
    embed.set_image(url='https://images-ext-1.discordapp.net/external/l3nJKuY_OL8OK6lLYiI5SLuAjbmJT24diOA1ioa1Qfg/https/i.redd.it/p0ebxenpse911.jpg')
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def translate(ctx):
    totrans = ' '.join(ctx.message.content.split()[1::])
    await ctx.message.delete()
    try:
        transd = translator.translate(totrans, 'en')
        if transd.src == 'en':
            await ctx.send('Message already in english')
        else:
            embed = discord.Embed(title="Translation from {}".format(ctx.message.author), description=" Translated message: {}\n Translated from: {} \n Translated text: {}".format(totrans, transd.src,transd.text))
            await ctx.message.channel.send(embed=embed)
    except Exception as e:
        print(e)

@bot.command(pass_context=True)
async def getusers(ctx):
    rolename = ' '.join(ctx.message.content.split()[1::])
    role = get(ctx.guild.roles, name=rolename)
    rolecount = len(role.members)
    embed = discord.Embed(title='Member count for {}'.format(rolename), description="There is {} people who have this role".format(rolecount), color=0x3399ff)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def sayas(ctx):
    user = ctx.message.mentions[0]
    pfp = user.avatar_url
    username = user.name
    msg = ctx.message.content.split()
    tosend = ' '.join(msg[2::])
    cmd = 'curl -d "username={}&content={}&avatar_url={}" -X POST webhookurl'.format(username,tosend, pfp)
    os.system(cmd)
    await ctx.message.delete()

@bot.command(pass_context=True)
async def get_members(ctx):
    guild = ctx.message.guild
    embed = discord.Embed(title="{0.name}'s Member Count".format(guild), description='This servers member count is : {0.member_count}'.format(guild))
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def belle_delphine(ctx):
    await ctx.send('Youre very motherfucking welcome : https://drive.google.com/drive/folders/1ickRX_UtJ9SqlwZiKFRGCCxNG3kEqY65?usp=sharing')

@bot.command()
async def periodic_table(ctx):
    embed = discord.Embed()
    embed.set_image(url='https://images-ext-1.discordapp.net/external/jlSteCjeeSGjIYRQrMPwTDwFeMP_hePMCqOnktfYKFg/https/cdn.boob.bot/bdsm/7936.jpg')
    await ctx.send(embed=embed)

@bot.command()
async def server_info(ctx):
    g = ctx.message.guild
    img = g.icon_url
    print(img)
    vc_cnt = len(g.voice_channels)
    txt_cnt = len(g.text_channels)
    mem_cnt = g.member_count
    role_cnt = len(g.roles)
    creation = g.created_at.date()
    server_id = g.id
    embed = discord.Embed(title='Info on {}'.format(g.name), description='''
                                                                            Voice Channel Count = {}\n
                                                                            Text Channel Count = {}\n
                                                                            Member Count = {}\n
                                                                            Role Count = {}\n
                                                                            Created At = {}\n
                                                                            Server ID = {}
                                                                            '''.format(vc_cnt, txt_cnt, mem_cnt, role_cnt, creation, server_id))
    embed.set_thumbnail(url=str(img))   
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_role('Moderator')
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    if reason == None:
        await ctx.send('The user {} has been kicked'.format(member))
        return
    else:
        await ctx.send('The user {} was kicked for the reason {}'.format(reason))

@bot.command(pass_context=True)
@commands.has_role('Admin')
async def testadmin(ctx):
    await ctx.send('Only people with admin should be able to run this ')

@bot.command(pass_context=True)
@commands.has_role('Beginner Mod')
async def mute(ctx, member: discord.Member):
    role = get(ctx.guild.roles, name='Muted')
    if role is None:
        await ctx.send('Please create a Muted role')
        return 
    if not member:
        await ctx.send('PLease specify a member to mute')
        return  
    await member.add_roles(role)
    await ctx.send('{} has been muted'.format(member.mention))

@bot.command(pass_context=True)
@commands.has_role('Beginner Mod')
async def unmute(ctx, member: discord.Member):
    role = get(ctx.guild.roles, name='Muted')
    await member.remove_roles(role)
    await ctx.send(f'{member.mention} has been unmuted')

@bot.command(pass_context=True)
@commands.has_role('Beginner Mod')
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    await ctx.send(f'{ctx.author.mention} cleared {limit} messages')
    

@bot.command(pass_context=True)
async def peen_size(ctx, member: discord.Member = None):
    if member == None:
        await ctx.send('Whos peen size you trynna measure homeboy')
        return
    if str(member) == 'nemo#3499':
        size = 12
    elif str(member) == 'F.O.E Dabbi#1287':
        size = 1
    else:
        size = random.randint(1,10)
    embed = discord.Embed(title=f"{member}'s peen size", description=f'Peen size in number form: **{size}** Inches\nIn image form: 8{"--" * int(size)}')
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def snipe(ctx):
    global lastdel
    print(lastdel)

    if lastdel == None:
        await ctx.send('Couldnt find a last message')
    else:
        embed = discord.Embed(title='SNIPER', description=f'Message sniped : {lastdel}\nMessage From : {lastauth}')
        embed.set_thumbnail(url='https://i.ytimg.com/vi/3qA8lv4lmTE/hqdefault.jpg')
        await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def gethelp(ctx):
    mod_embed = discord.Embed(title='Moderation commands', color=0x00ffcc)
    mod_embed.add_field(name="Ban", value="*[Minimum role is Admin]* \nDesc: This command bans people \nUsage: `>ban @member`", inline=False)
    mod_embed.add_field(name="Kick", value="*[Minumum role is Moderator]* \nDesc: This command kicks people\nUsage : `>kick @member`", inline=False)
    mod_embed.add_field(name="Mute", value="*[Minimum Role is Beginner mod]*\nDesc: This command mutes people\nUsage : `>mute @member` ", inline=False)
    mod_embed.add_field(name="Unmute", value="*[Minimum Role is Beginner mod]*\nDesc: This command unmutes people\nUsage : `>unmute @member` ", inline=False)
    mod_embed.add_field(name="Clean", value="*[Minimum Role is Beginner mod]*\nDesc : This command deletes x messages\nUsage : `>clean x`", inline=False)   
    fun_embed = discord.Embed(title='Fun commands', color=0xff00ff)
    fun_embed.add_field(name='Thot Spot', value="Desc: This command detects thots and eliminates them\nUsage: `>thot_spotted @member`", inline=False)
    fun_embed.add_field(name="Translate", value="Desc: Translates a message, with auto lang detection\nUsage: `>translate message to translate`", inline=False)
    fun_embed.add_field(name='Say as', value="Desc: Say something as another user! (overuse will result in command stripped from you)\nUsage `>sayas @member to_say`", inline=False)
    fun_embed.add_field(name="Belle Delphine Worship", value='Desc: Send a link of some top tier Belle Delphine images\nUsage: `>belle_delphine`', inline=False)
    fun_embed.add_field(name="Periodic table of kink", value="Desc: Get the periodic table of the kink\nUsage: `>periodic_table`", inline=False)
    info_embed = discord.Embed(title="Info Commands", color=0x99ffcc)
    info_embed.add_field(name='Get Help', value='Desc: Show this message \nUsage: `>gethelp`', inline=False)
    info_embed.add_field(name="Get Users",value='Desc: get the users of a specific role\nUsage `>getusers rolename`', inline=False)
    info_embed.add_field(name='Member count', value='Desc: get server member count\nUsage: `>get_members`', inline=False)
    info_embed.add_field(name='Server Info', value='Desc: get some info on the server\nUsage: `>server_info`', inline=False)
    await ctx.send(embed=mod_embed)
    await ctx.send(embed=fun_embed)
    await ctx.send(embed=info_embed)
bot.run(config['token'])
