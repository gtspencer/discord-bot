# This example requires the 'members' privileged intents

import discord
from discord.ext import commands
import random
import constants

#constants = input('constants')
#importlib.import_module(constants)



weeeeeeebs = """Omg hai ___^ I’m anon-san and I absolutely luuuv @__@ anime <3 and my fav is naurto!!! Okies so anyways, im going to tell you about the BEST day of my life when I met my hot husband sasuke!! <333333333 OMFGZ HE WAS SOOOOO FREAKIN KAWAII IN PERSON!!! Supa kawaii desu!!!!!!!! ^___________________________________^

When I walked onto Tokyo street =____=I looked up and saw…SASUKE!!!!!!!!!!!!!!! <33333333333333333333333333333333333333333333333333333333333333!!!! “ KONNICHIWA OMGZZZZZZZZZZZZZZZZ SUPA SUPA SUPA KAWAII SASUKE-SAMA!!!!!” I yelled n____n then he turned chibi then un-chibi!! he looked at me [O.O;;;;;;;;;;;] and then he saw how hot I am *___* he grabbed my hand and winked ~_^ then pulled me behind a pocky shop o_o and started to kiss me!!!!!! [OMG!!! HIS TOUNGE TASTED LIKE RAMEN!!! RLY!! >.> <.< >.< (O) (O) (O)] then I saw some baka fat bitch watching us and I could tell she was undressing him with her eyes!!!!!!! [ -___________-;;;;; OMG I COULDN’T BELIEVE IT EITHER!!! (ò_ó) (ò_ó) (ò_ó)] so I yelled “UH UH BAKA NEKO THAT’S MY MAN WHY DON’T YOU GO HOOK UP WITH NARUTO CAUSE SASUKE-SAMA LOVES ME!!! (ò_ó)” then sasuke held me close =^= and said he would only ever love me and kissed me again!!!!!!! ** (O)/ then we went to his apartment and banged all night long and made 42 babies and they all became ninjas!!!!!!!!!!!!!!! Nyaaaaa!!! (^___<) ^______________;;;;;;;;;;;;;;;;"""

#intents = discord.Intents.default()

#bot = commands.Bot(command_prefix='!', description=constants.description, intents=intents)
bot = discord.Client()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for guild in bot.guilds:
        print (guild.members)
        #for member in guild.members:
            #print (member + " in " + guild)
        #print (guild.name)


@bot.command()
async def animelove69420(ctx):
    await ctx.send("""nick's alter ego.  shhhhh.....""")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def rant(ctx):
    await ctx.send("""Listen you hairy gay lesbain man lover blanket rubbish bin man i could beet you in fortnitee for $7000 because i have aimbot $5000 computer i bet u don't have anyone take care you or love you. I bet you fat gay mum collects rubbish and eats it! I will end you and throw you out of my window in a 1v4 i will find your ugly lesbain dad and clap him with a hand and my $700 renegaide raider aimbot account level 10000 i bet you are a chav roadman that only plays this gaynite game and doesnt go school. I bet you don't even see big girls with no clothes on lol lamo. I'll laugh wehn you are homeless on the street begging for v bucks for renegaide raider.""")

@bot.command()
async def connor(ctx):
    await ctx.send(constants.connor_string)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def spencer(ctx):
    await ctx.send('The commentor above me is lame ^^^')

@bot.command()
async def natasha(ctx):
    await ctx.send('natasha is a sexy little minx')

@bot.command()
async def uwu(ctx):
    await ctx.send(weeeeeeebs)

@bot.command()
async def nick(ctx):
    await ctx.send('daddy ;)')

@bot.command()
async def reilly(ctx):
    await ctx.send('pew pew')

@bot.command()
async def liam(ctx):
    await ctx.send("""I don’t know who you are. I don’t know what you want. If you are looking for ransom I can tell you I don’t have money, but what I do have are a very particular set of skills. Skills I have acquired over a very long career. Skills that make me a nightmare for people like you. If you let my daughter go now that’ll be the end of it. I will not look for you, I will not pursue you, but if you don’t, I will look for you, I will find you and I will kill you.""")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@cool.command(name="nick")
async def _nick(ctx):
    await ctx.send('nick will never be cool')

#@bot.event
async def on_message(message):
    if "Good bot" in message.content:
        await message.channel.send('Bad person')

bot.run('ODE0NjMyNDM3MzU0MDcwMDE2.YDgrlA.bk35ES2V2U1S3-gUUrUZ2aQ-BPg')
