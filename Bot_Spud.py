from __future__ import unicode_literals
from First_Run import ftime, input_config
from makepraw import make_prawini
from start_options import config_l, config_e, balance_l, dis_ena, reddit_in
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
from termcolor import colored, cprint
from pytz import timezone
import youtube_dl
import urbandictionary
import discord
import json
import os
import random
import configparser
import webbrowser
import praw
import urllib3
import time
import datetime
import sys
import shutil


Other_infile = os.path.isdir("./Other")
if Other_infile is False:
    os.mkdir("Other")

config = configparser.RawConfigParser()

STARTOP = False

config_infile = os.path.isfile("./Other/config.ini")

if config_infile is True:
    config.read('Other/config.ini')
    STARTOP = config.getboolean('DEFAULT', 'startoptions')

def main():
    global amounts, players, queues

    config = configparser.RawConfigParser()


    file_txt_there = os.path.isfile("./Other/Instructions.txt")

    if file_txt_there is False:
        ftime()

    print("give me a second while I get everything ready...\n")

    file_configthere = os.path.isfile("./Other/config.ini")
    if file_configthere is False:
        input_config()

    reddit_infile = os.path.isfile("./Other/reddit_info.ini")
    if reddit_infile is False:
        cprint("WARNING: THE COMMAND FOR REDDIT WILL NOT WORK BECAUSE NO INFO WAS PROVIDED. HELP CAN BE FOUND IN "
               "INSTRUCTIONS.TXT\n", 'green')
        config.read('Other/config.ini')
        config.set('features', 'reddit', 'False')
        with open('Other/config.ini', 'w') as configsave:
            config.write(configsave)


    config.read('Other/config.ini')
    TOKEN = config.get('var', 'bottoken')
    BOT_PREFIX = config.get('var', 'prefix')
    AUTO_ROLE = config.get('var', 'autorole')
    CURRENCY_NAME = config.get('var', 'currencyname')
    START_BALANCE = config.getint('var', 'startbalance')
    MINFOR_LOAN = config.getint('var', 'loanminimum')
    BOT_PLAYING = config.get('var', 'botplaying')
    CHANNEL_MUSIC = config.getint('var', 'channeltextid')

    if TOKEN == '' or TOKEN == 'NULL':
        print("No Token from the bot has been entered")
        input("Press ENTER to close bot")
        quit()

    if BOT_PREFIX == '':
        BOT_PREFIX = config.get('DEFAULT', 'prefix')

    if AUTO_ROLE == '':
        AUTO_ROLE = config.get('DEFAULT', 'autorole')

    if CURRENCY_NAME == '':
        CURRENCY_NAME = config.get('DEFAULT', 'currencyname')

    if START_BALANCE == '':
        START_BALANCE = config.getint('DEFAULT', 'startbalance')

    if MINFOR_LOAN == '':
        MINFOR_LOAN = config.getint('DEFAULT', 'loanminimum')

    if BOT_PLAYING == '':
        BOT_PLAYING = config.get('DEFAULT', 'botplaying')

    if CHANNEL_MUSIC == '':
        CHANNEL_MUSIC = config.get('DEFAULT', 'channeltextid')


    bot = commands.Bot(command_prefix=BOT_PREFIX)
    bot.remove_command('help')


    amounts = {}
    players = {}
    queues = {}


    def _save():
        with open('Other/amounts.json', 'w+') as f:
            json.dump(amounts, f)
            print("just took a dump")




    # When the bot executes this stuff

    @bot.event
    async def on_ready():
        global amounts, data, config
        config.read('Other/config.ini')
        print("Logged in as: " + bot.user.name + "\n")
        game = discord.Game(BOT_PLAYING)
        await bot.change_presence(status=discord.Status.online, activity=game)
        file_there = os.path.isfile("./Other/amounts.json")

        def make_json(amounts):
            with open("Other/amounts.json", 'w') as f:
                json.dump(amounts, f)
                print("amounts is ready!\n")

        if file_there is True:
            with open("Other/amounts.json") as f:
                amounts = json.load(f)
                print("I see the 'amounts.json' file and loaded it\n")
        else:
            print("Did not see 'amounts.json' making it now...\n")
            amounts = {}
            make_json(amounts)
        print("Everything is looking good...\n")
        print("------------------LOG--------------------")


# When a message is sent in the discord what is done

    @bot.event
    async def on_message(message):
        log = open('Other/Log.txt', 'a')
        tz = timezone('US/Eastern')
        c_time = datetime.datetime.now(tz)
        id = message.author.id
        user = message.author.name
        msg = message.content
        if message.author == bot.user:
            return
        cprint("<" + c_time.strftime("%I:%M%p") + f"> {user}: {msg}", 'red')
        try:
            log.write("<" + c_time.strftime("%a, %m/%d/%Y %I:%M:%S%p") + f"> {user}(id:{id}): {msg}\n")
        except:
            log.write("<" + c_time.strftime("%a, %m/%d/%Y %I:%M:%S%p") + f"> {user}(id:{id}): *Emoji*\n")
        log.close

        await bot.process_commands(message)


# When a new member joins what is done (being fixed )

    @bot.event
    async def on_member_join(member):
        role = get(member.guild.roles, name=AUTO_ROLE)
        await member.add_roles(role)
        print(f'{member} Joined the server, {role} given to them')


# custome help command

    @bot.command(pass_context=True)
    async def help(ctx):
        print("Sent Help")
        author = ctx.message.author

        embed = discord.Embed(
            colour=discord.Colour.orange()
        )
        embed.set_author(name="Help (Prefix = " + "'" + BOT_PREFIX + "'" + " )")
        embed.add_field(name='register', value='Do before anything else! This will make you a bank account | '
                                               'aliases = [reg]', inline=False)
        embed.add_field(name='balance', value='Shows your account balance | aliases = [bal, b]', inline=False)
        embed.add_field(name='transfer', value='Give currency to others when you suck ass | aliases = [pay, give]',
                        inline=False)
        embed.add_field(name='roll', value='Roll some dice brotha | !roll [999999] [2-999999999999] | aliases = []',
                        inline=False)
        embed.add_field(name='apply_loan', value='Apply for a loan! Guess a number between 1-100 (60 sec cooldown) | '
                                                 'aliases = [apply, loan, al]', inline=False)
        embed.add_field(name='reddit', value='Get posts from reddit | reddit [subreddit] [HOT/NEW] [1-8] | '
                                             'aliases = [red, rd]', inline=False)
        embed.add_field(name='insult', value='You mad bro? | insult @[user] | aliases = [in]', inline=False)
        embed.add_field(name='urbandic', value='Get a random Urban dictionary word | aliases = [ud]', inline=False)
        embed.add_field(name='changes', value='Most recent changes done to the bot', inline=False)
        embed.add_field(name='ahelp', value='Helps admins with admin specific commands | Admin use only', inline=False)
        embed.add_field(name='vhelp', value='Helps anyone with voice commands', inline=False)

        await author.send(embed=embed)
        print("Sent Help")


# Register for a bank account

    @bot.command(pass_context=True, brief="DO THIS BEFORE ANYTHING ELSE! (ONLY ONCE)", aliases=['reg'])
    async def register(ctx):
        id = str(ctx.message.author.id)
        if id not in amounts:
            amounts[id] = START_BALANCE
            await ctx.send(ctx.message.author.mention + ", You are now registered")
            print(id + " just made an account")
            print("have to take a dump")
            _save()
        else:
            await ctx.send(ctx.message.author.mention + ", You already have an account")
            print(id + " just tried to make an account, but already had one")


# Checks balance of bank account

    @bot.command(pass_context=True, brief="Shows your balance", aliases=['bal', 'b'])
    # @commands.cooldown(1, 30, commands.BucketType.user) this is the cooldown
    async def balance(ctx):
        id = str(ctx.message.author.id)
        if id in amounts:
            await ctx.send(ctx.message.author.mention + " has {} ".format(amounts[id]) + CURRENCY_NAME + " in the bank")
            print("Checked balance of " + id)
        else:
            await ctx.send("You do not have an account")
            print("Tried to check balance, but no account")


# Transfer money to other discord users

    @bot.command(pass_context=True, brief="Transfer " + CURRENCY_NAME + " to others '!transfer @user [amount]'",
                 aliases=['pay', 'give'])
    async def transfer(ctx, other: discord.Member, amount: int):
        primary_id = str(ctx.message.author.id)
        other_id = str(other.id)
        if primary_id not in amounts:
            await ctx.send(ctx.message.author.mention + ", You do not have an account '!reg'")
            print('Tried to send ' + CURRENCY_NAME + ', but no account')
        elif other_id not in amounts:
            await ctx.send("The other party does not have an account tell them to type '!reg'")
            print("Tried to send " + CURRENCY_NAME + " but the other person did not have an account")
        elif amounts[primary_id] < amount:
            await ctx.send(ctx.message.author.mention + ", You cannot afford this transaction")
            print(primary_id + " tried to send " + CURRENCY_NAME + ", but they did not have enough ")
        else:
            amounts[primary_id] -= amount
            amounts[other_id] += amount
            await ctx.send("Transaction complete")
            print(primary_id + " sent " + CURRENCY_NAME + " to " + other_id)
        print("have to take a dump")
        _save()


# Roll command

    @bot.command(pass_context=True, brief="Rolling for " + CURRENCY_NAME +
                                          " is no joke! '!roll [999999] [2-999999999999]'")
    @commands.cooldown(1, 25, commands.BucketType.user)
    async def roll(ctx, dice_amount: int, sides: int):
        config.read('Other/config.ini')
        spam = config.getboolean('features', 'notneededmsg')
        Rostate = config.getboolean('features', 'roll')

        if Rostate is False:
            print("Not Enabled")
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return

        if dice_amount > 999999:
            print("Dice limit hit")
            if spam:
                await ctx.send(f"{ctx.message.author.mention}, you went over the dice amount limit of 999999")
            return
        if sides > 999999999999:
            print("Side limit hit")
            if spam:
                await ctx.send(f"{ctx.message.author.mention}, you went over the dice side limit of 999999999999")
            return
        if sides == 1:
            print("One sided dice")
            if spam:
                await ctx.send(f"{ctx.message.author.mention}, Not point to rolling a 1 sided dice")

        run_l1 = True
        dice_a1 = dice_amount
        total = 0
        dice_track = []
        while run_l1:
            if dice_a1 != 0:
                dice_roll = random.randint(1, sides)
                dice_track.append(dice_roll)
                dice_a1 -= 1
            else:
                run_l1 = False

        for roll_num in dice_track:
            total += roll_num

        print(f"{ctx.message.author.mention} Rolled {dice_amount} dice with {sides} sides each. Total: {total}")

        try:
            await ctx.send(f"{ctx.message.author.mention} Rolled {dice_amount} dice with {sides} sides each. "
                           f"With a total of {total}")
        except:
            if spam:
                await ctx.send("I'm a computer I know, but that's a lot for even me!")
            print("Character limit hit")

# apply for a loan min. game

    @bot.command(pass_context=True, brief="Apply for a loan! Guess a number between 1-100 "
                                          "(60 sec cooldown)",
                 aliases=['apply', 'loan', 'al'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def apply_loan(ctx, guess: int):
        if MINFOR_LOAN > START_BALANCE:
            await ctx.send("ERROR(Code: 1): Bot is now offline! Please contact an admin about this")
            quit()
        randnum = random.randint(10, 90)
        randplus = float(randnum + 10)
        randmin = float(randnum - 10)
        id = str(ctx.message.author.id)
        if amounts[id] < MINFOR_LOAN:
            print(id + " Is trying to take a loan out: " + str(randmin) + " - " + str(randnum) + " + " + str(randplus)
                  + " Guess: " + str(guess))
            if guess > randmin and guess < randplus:
                if guess == randnum:
                    loan = random.randint(5000, 10000)
                    amounts[id] += loan
                    await ctx.send(ctx.message.author.mention + "Get 100% of loan: "
                                  + str(loan))
                    print(id + " just took a large loan out!")
                    _save()
                elif guess > randmin and guess < randnum:
                    percent = float(guess - randmin)
                    decimal = float(percent / 10)
                    loan = random.randint(1000, 10000)
                    total = int(loan * decimal)
                    print("amount loan: " + str(loan) + "*" + str(decimal) + '=' + str(total))
                    print(str(total))
                    amounts[id] += int(total)
                    await ctx.send(ctx.message.author.mention + " Number: " + str(randnum) + " Guess: " +
                                  str(guess) + " Total loan: " + str(loan) + " You get: " + str(total))
                    print(id + " just took part of a loan out")
                    _save()
                elif guess < randplus and guess > randnum:
                    percent = float(randplus - guess)
                    decimal = float(percent / 10)
                    loan = random.randint(1000, 10000)
                    total = int(loan * decimal)
                    print("amount loan: " + str(loan) + "*" + str(decimal) + '=' + str(total))
                    print(str(total))
                    amounts[id] += int(total)
                    await ctx.send(ctx.message.author.mention + " Number: " + str(randnum) + " Guess: " +
                                  str(guess) + " Total loan: " + str(loan) + " You get: " + str(total))
                    print(id + " just took part of a loan out")
                    _save()
            else:
                await ctx.send(ctx.message.author.mention + " Loan request failed")
                print(id + " did not guess right")
        elif amounts[id] >= MINFOR_LOAN:
            await ctx.send(ctx.message.author.mention + " They won't even talk to you about a loan")
            print(id + " just tried to take a loan out, but got denied")


# reddit api to pull posts from reddit. This command uses the reddit API more for personal use and open source software

    @bot.command(brief="This is FOR REDDIT!",
                 aliases=['red', 'rd'])
    @commands.cooldown(1, 60, commands.BucketType.default)
    async def reddit(ctx, sub: str, sort: str, limit: int):
        author = ctx.message.author
        config.read('Other/config.ini')
        spam = config.getboolean('features', 'notneededmsg')
        Rstate = config.getboolean('features', 'reddit')
        do_dm = config.getboolean('features', 'dmredditinfo')
        if Rstate is False:
            print("Not Enabled")
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return

        config.read('Other/reddit_info.ini')
        CLIENTID = config.get('DEFAULT', 'client_id')
        CLIENTSECRET = config.get('DEFAULT', 'client_secret')
        USERNAME = config.get('DEFAULT', 'username')
        PASSWORD = config.get('DEFAULT', 'password')

        file_ini_there = os.path.isfile("praw.ini")
        if file_ini_there is False:
            print("O SHIT! someone wants stuff from reddit, give me a second I need to make something...")
            make_prawini()
            print("Okay we good now")
        if limit > 8:
            print("Someone tried to request more than 8")
            await ctx.send("Limit of 8, you requested " + str(limit) + " please re-enter the input")
            return
        config.read('Other/config.ini')
        reddit = praw.Reddit(client_id=CLIENTID,  # This is setting up the reddit instance
                             client_secret=CLIENTSECRET,
                             username=USERNAME,
                             password=PASSWORD,
                             user_agent='Spud')
        if sort.upper() == "HOT":
            limit += 2
            subreddit = reddit.subreddit(sub)
            hot_reddit = subreddit.hot(limit=limit)
            limit -= 2
            print("I need to get " + str(limit) + " things from reddit!")
            if do_dm is True:
                await author.send("Link: https://www.reddit.com/r/" + sub)
                await author.send("Sort by: HOT")
            elif do_dm is False:
                await ctx.send("Link: https://www.reddit.com/r/" + sub)
                await ctx.send("Sort by: HOT")
            num_lab = 0
            for submission in hot_reddit:
                if not submission.stickied:
                    num_lab += 1
                    print("I got : " + str(num_lab))
                    if do_dm is True:
                        await author.send(str(num_lab) + ": Link: https://www.reddit.com/r/{}/comments/{}/, Title: '{}'"
                                                         "".format(submission.subreddit,
                                                                   submission.id,
                                                                   submission.title))
                    elif do_dm is False:
                        await ctx.send(str(num_lab) + ": Link: https://www.reddit.com/r/{}/comments/{}/, Title: '{}'"
                                                         "".format(submission.subreddit,
                                                                   submission.id,
                                                                   submission.title))
        elif sort.upper() == "NEW":
            subreddit = reddit.subreddit(sub)
            new_reddit = subreddit.new(limit=limit)
            print("I need to get " + str(limit) + " things from reddit!")
            if do_dm is True:
                await author.send("Link: https://www.reddit.com/r/" + sub)
                await author.send("Sort by: HOT")
            elif do_dm is False:
                await ctx.send("Link: https://www.reddit.com/r/" + sub)
                await ctx.send("Sort by: HOT")
            num_lab = 0
            for submission in new_reddit:
                if not submission.stickied:
                    num_lab += 1
                    print("I got : " + str(num_lab))
                    if do_dm is True:
                        await author.send(str(num_lab) + ": Link: https://www.reddit.com/r/{}/comments/{}/, Title: '{}'"
                                                         "".format(submission.subreddit,
                                                                   submission.id,
                                                                   submission.title))
                    elif do_dm is False:
                        await ctx.send(str(num_lab) + ": Link: https://www.reddit.com/r/{}/comments/{}/, Title: '{}'"
                                                         "".format(submission.subreddit,
                                                                   submission.id,
                                                                   submission.title))
        time.sleep(0.5)


# insult api randome insult at user

    @bot.command(brief="You mad bro?", aliases=['in'])
    async def insult(ctx, person: str):
        config.read('Other/config.ini')
        Istate = config.getboolean('features', 'insult')
        spam = config.getboolean('features', 'notneededmsg')
        if Istate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return
        print("Someone is pissed off LuL")
        http = urllib3.PoolManager()
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        test = http.request('GET', 'https://insult.mattbas.org/api/insult')
        await ctx.send(person + ", " + str(test.data, "utf-8"))


# pulls random word a definition from urban dic.

    @bot.command(brief="Random Urban Dictionary word '/ud'", aliases=['ud'])
    async def urbandic(ctx):
        config.read('Other/config.ini')
        Ustate = config.getboolean('features', 'insult')
        spam = config.getboolean('features', 'notneededmsg')
        if Ustate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return
        ran = urbandictionary.random()
        limit = 1
        print("Asking urbandictionary.com for a word and def.")
        for r in ran:
            while limit != 0:
                await ctx.send("Word: " + r.word + " | " + "Def: " + r.definition)
                limit -= 1


# very simplified blackjack game to earn currency

    @bot.command(brief="", aliases=['ca'])
    async def cards(ctx):
        config.read('Other/config.ini')
        Cstate = config.getboolean('features', 'cards')
        spam = config.getboolean('features', 'notneededmsg')
        if Cstate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return

        '''
        Make it so users can play against each other
        make so they can add more
        add some console printouts
        add users name
        add money when playing against bot
        change timing if feel needs it
        '''

        card_list = {
            "2 of Clubs": 2,
            "2 of Diamonds": 2,
            "2 of Hearts": 2,
            "2 of Spades": 2,
            "3 of Clubs": 3,
            "3 of Diamonds": 3,
            "3 of Hearts": 3,
            "3 of Spades": 3,
            "4 of Clubs": 4,
            "4 of Diamonds": 4,
            "4 of Hearts": 4,
            "4 of Spades": 4,
            "5 of Clubs": 5,
            "5 of Diamonds": 5,
            "5 of Hearts": 5,
            "5 of Spades": 5,
            "6 of Clubs": 6,
            "6 of Diamonds": 6,
            "6 of Hearts": 6,
            "6 of Spades": 6,
            "7 of Clubs": 7,
            "7 of Diamonds": 7,
            "7 of Hearts": 7,
            "7 of Spades": 7,
            "8 of Clubs": 8,
            "8 of Diamonds": 8,
            "8 of Hearts": 8,
            "8 of Spades": 8,
            "9 of Clubs": 9,
            "9 of Diamonds": 9,
            "9 of Hearts": 9,
            "9 of Spades": 9,
            "10 of Clubs": 10,
            "10 of Diamonds": 10,
            "10 of Hearts": 10,
            "10 of Spades": 10,
            "Jack of Clubs": 10,
            "Jack of Diamonds": 10,
            "Jack of Hearts": 10,
            "Jack of Spades": 10,
            "Queen of Clubs": 10,
            "Queen of Diamonds": 10,
            "Queen of Hearts": 10,
            "Queen of Spades": 10,
            "King of Clubs": 10,
            "King of Diamonds": 10,
            "King of Hearts": 10,
            "King of Spades": 10,
            "Ace of Clubs": 11,
            "Ace of Diamonds": 11,
            "Ace of Hearts": 11,
            "Ace of Spades": 11
        }

        player_card1 = random.choice(list(card_list.keys()))
        player_card2 = random.choice(list(card_list.keys()))
        dealer_card1 = random.choice(list(card_list.keys()))
        dealer_card2 = random.choice(list(card_list.keys()))
        px = card_list[player_card1]
        py = card_list[player_card2]
        dx = card_list[dealer_card1]
        dy = card_list[dealer_card2]

        p_total = px + py
        d_total = dx + dy

        print("Dealing Cards")

        time.sleep(1)
        await ctx.send("You:  " + str(player_card1) + "  +  " + str(player_card2) + "  Total:  " + str(p_total))

        time.sleep(1)
        await ctx.send("Dealer:  " + str(dealer_card1) + "  +  " + str(dealer_card2) + "  Total:  " + str(d_total))


# this will have the bot join the channel you are in

    @bot.command(pass_context=True, brief="Makes the bot join your channel", aliases=['j', 'jo'])
    async def join(ctx):
        config.read('Other/config.ini')
        Vstate = config.getboolean('features', 'discordvoice')
        spam = config.getboolean('features', 'notneededmsg')
        restrict = config.getboolean("features", 'restrictvoice')
        if Vstate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return
        if restrict is True:
            if ctx.channel.id == CHANNEL_MUSIC:
                channel = ctx.message.author.voice.channel
                if not channel:
                    print("User tried to request voice bot, but was not in a voice channel")
                    if spam:
                        await ctx.send("You are not connected to a voice channel")
                        return
                    else:
                        return
                voice = get(bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                await voice.disconnect()
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                    print(f"The bot has moved to {channel}")
                else:
                    voice = await channel.connect()
                    print(f"The bot has connected to {channel}")
                if spam:
                    await ctx.send(f"Joined {channel}")
            else:
                print("Wrong text channel")
                if spam:
                    await ctx.send("This command is restricted to a specific text channel (Not this one)")
                return
        elif restrict is False:
            channel = ctx.message.author.voice.channel
            if not channel:
                print("User tried to request voice bot, but was not in a voice channel")
                if spam:
                    await ctx.send("You are not connected to a voice channel")
                    return
                else:
                    return
            voice = get(bot.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
            await voice.disconnect()
            if voice and voice.is_connected():
                await voice.move_to(channel)
                print(f"The bot has moved to {channel}")
            else:
                voice = await channel.connect()
                print(f"The bot has connected to {channel}")
            if spam:
                await ctx.send(f"Joined {channel}")
        else:
            return


# this will have the bot leave the current voice channel

    @bot.command(pass_context=True, brief="Makes the bot leave your channel", aliases=['l', 'le', 'lea'])
    async def leave(ctx):
        config.read('Other/config.ini')
        Vstate = config.getboolean('features', 'discordvoice')
        spam = config.getboolean('features', 'notneededmsg')
        restrict = config.getboolean("features", 'restrictvoice')
        if Vstate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return
        if restrict is True:
            if ctx.channel.id == CHANNEL_MUSIC:
                channel = ctx.message.author.voice.channel
                voice = get(bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_connected():
                    print(f"The bot has left {channel}")
                    await voice.disconnect()
                    if spam:
                        await ctx.send(f"Left {channel}")
                else:
                    print("Bot was told to leave a voice channel, but was not in a voice channel")
                    if spam:
                        await ctx.send("Don't think I am in a voice channel")
            else:
                print("Wrong text channel")
                if spam:
                    await ctx.send("This command is restricted to a specific text channel (Not this one)")
                return
        elif restrict is False:
            channel = ctx.message.author.voice.channel
            voice = get(bot.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                print(f"The bot has left {channel}")
                await voice.disconnect()
                if spam:
                    await ctx.send(f"Left {channel}")
            else:
                print("Bot was told to leave a voice channel, but was not in a voice channel")
                if spam:
                    await ctx.send("Don't think I am in a voice channel")
        else:
            return


# this will play music from a youtube, spotify, soundcloud, ect.  urls

    @bot.command(pass_context=True, brief="This will play a song 'play [url]'", aliases=['pl'])
    async def play(ctx, url: str):


        config.read('Other/config.ini')
        Vstate = config.getboolean('features', 'discordvoice')
        spam = config.getboolean('features', 'notneededmsg')
        quiet_d = config.getboolean("features", 'quietdownload')
        restrict = config.getboolean("features", 'restrictvoice')


        if Vstate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return


        def check_queue():
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                still_q = length - 1
                try:
                    first_file = os.listdir(DIR)[0]
                except:
                    print("No more queued song(s)\n")
                    return
                main_location = os.path.dirname(os.path.realpath(__file__))
                song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
                if length != 0:
                    print("Playing next queued\n")
                    print(f"Songs still in queue: {still_q}\n")
                    song_there = os.path.isfile("song.mp3")
                    if song_there:
                        os.remove("song.mp3")
                    shutil.move(song_path, main_location)
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            name = file
                            os.rename(file, 'song.mp3')
                    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.07
                else:
                    return
            elif Queue_infile is False:
                print("End\n")


        if restrict is True:
            if ctx.channel.id == CHANNEL_MUSIC:
                song_there = os.path.isfile("song.mp3")
                try:
                    if song_there:
                        os.remove("song.mp3")
                        queues.clear()
                        print("\nRemoved current song file\n")
                        Queue_infile = os.path.isdir("./Queue")
                        Queue_folder = "./Queue"
                        if Queue_infile is True:
                            print("removed old Queue folder\n")
                            shutil.rmtree(Queue_folder)
                except PermissionError:
                    print("Trying to delete song file, but it's being played\n")
                    await ctx.send("ERROR: Music playing, use stop command to play new song")
                    return
                if spam:
                    await ctx.send("Getting everything ready, playing audio soon")
                voice = get(bot.voice_clients, guild=ctx.guild)
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'quiet': quiet_d,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                try:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        print("Downloading audio now\n")
                        ydl.download([url])
                except:
                    dir_path = os.path.dirname(os.path.realpath(__file__))
                    print("FALLBACK: youtube-dl not supported, searching spotify now (This is normal if spotify URL)\n")
                    system("spotdl -f " + '"' + dir_path + '"' + " -s " + url)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        name = file
                        os.rename(file, 'song.mp3')
                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07
                if spam:
                    nname = name.rsplit("-", 2)
                    await ctx.send(f"Playing: {nname[0]} - {nname[1]}")
                print("Playing\n")
            else:
                print("Wrong text channel")
                if spam:
                    await ctx.send("This command is restricted to a specific text channel (Not this one)")
                return


        elif restrict is False:
            song_there = os.path.isfile("song.mp3")
            try:
                if song_there:
                    os.remove("song.mp3")
                    queues.clear()
                    print("\nRemoved current song file\n")
            except PermissionError:
                print("Trying to delete song file, but it's being played\n")
                await ctx.send("ERROR: Music playing use stop command to play new song")
                return
            if spam:
                await ctx.send("Getting everything ready, playing audio soon")
            voice = get(bot.voice_clients, guild=ctx.guild)
            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': quiet_d,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            except:
                dir_path = os.path.dirname(os.path.realpath(__file__))
                print("FALLBACK: youtube-dl not supported, searching spotify now (This is normal)\n")
                system("spotdl -f " + '"' + dir_path + '"' + " -s " + url)
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    name = file
                    os.rename(file, 'song.mp3')
            voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.07
            if spam:
                nname = name.rsplit("-", 2)
                await ctx.send(f"Playing: {nname[0]} - {nname[1]}")
            print("Playing\n")


        else:
            return


# this will pause the currently playing music

    @bot.command(pass_context=True, brief="Pauses the music that is playing", aliases=['pa'])
    async def pause(ctx):
        config.read('Other/config.ini')
        Vstate = config.getboolean('features', 'discordvoice')
        spam = config.getboolean('features', 'notneededmsg')
        restrict = config.getboolean("features", 'restrictvoice')
        if Vstate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return

        if restrict is True:
            if ctx.channel.id == CHANNEL_MUSIC:
                voice = get(bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_playing():
                    print("Music is being paused")
                    voice.pause()
                    if spam:
                        await ctx.send("Music has been paused")
                else:
                    print("Tried to pause not playing music")
                    if spam:
                        await ctx.send("Don't think there is music playing")
            else:
                print("Wrong text channel")
                if spam:
                    await ctx.send("This command is restricted to a specific text channel (Not this one)")
                return
        elif restrict is False:
            voice = get(bot.voice_clients, guild=ctx.guild)
            if voice and voice.is_playing():
                print("Music is being paused")
                voice.pause()
                if spam:
                    await ctx.send("Music has been paused")
            else:
                print("Tried to pause not playing music")
                if spam:
                    await ctx.send("Don't think there is music playing")
        else:
            return


# this will resume the currently paused music

    @bot.command(pass_context=True, brief="this will resume the currently paused music", aliases=['res'])
    async def resume(ctx):
        config.read('Other/config.ini')
        Vstate = config.getboolean('features', 'discordvoice')
        spam = config.getboolean('features', 'notneededmsg')
        restrict = config.getboolean("features", 'restrictvoice')
        if Vstate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return

        if restrict is True:
            if ctx.channel.id == CHANNEL_MUSIC:
                voice = get(bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_paused():
                    print("Music is being resumed")
                    voice.resume()
                    if spam:
                        await ctx.send("Music has been resumed")
                else:
                    print("Tried to play unpaused music")
                    if spam:
                        await ctx.send("Don't think the music is paused")
            else:
                print("Wrong text channel")
                if spam:
                    await ctx.send("This command is restricted to a specific text channel (Not this one)")
                return
        elif restrict is False:
            voice = get(bot.voice_clients, guild=ctx.guild)
            if voice and voice.is_paused():
                print("Music is being resumed")
                voice.resume()
                if spam:
                    await ctx.send("Music has been resumed")
            else:
                print("Tried to play unpaused music")
                if spam:
                    await ctx.send("Don't think the music is paused")
        else:
            return


# This will stop the currently playing music

    @bot.command(pass_context=True, brief="This will stop the currently playing music", aliases=['st'])
    async def stop(ctx):
        global queues
        queues.clear()
        config.read('Other/config.ini')
        Vstate = config.getboolean('features', 'discordvoice')
        spam = config.getboolean('features', 'notneededmsg')
        restrict = config.getboolean("features", 'restrictvoice')
        if Vstate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return

        Queue_infile = os.path.isdir("./Queue")
        Queue_folder = "./Queue"
        if Queue_infile is True:
            shutil.rmtree(Queue_folder)


        if restrict is True:
            if ctx.channel.id == CHANNEL_MUSIC:
                voice = get(bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_playing():
                    print("Music is being stopped")
                    voice.stop()
                    if spam:
                        await ctx.send("Music has been stopped")
                else:
                    print("tried to stop not playing music")
                    if spam:
                        await ctx.send("Don't think the music is played")
            else:
                print("Wrong text channel")
                if spam:
                    await ctx.send("This command is restricted to a specific text channel (Not this one)")
                return
        elif restrict is False:
            voice = get(bot.voice_clients, guild=ctx.guild)
            if voice and voice.is_playing():
                print("Music is being stopped\n")
                voice.stop()
                if spam:
                    await ctx.send("Music has been stopped")
            else:
                print("tried to stop not playing music\n")
                if spam:
                    await ctx.send("Don't think the music is played")
        else:
            return


# Queues up a song

    @bot.command(pass_context=True, brief="Queues up a song", aliases=['qu', 'q'])
    async def queue(ctx, url: str):


        config.read('Other/config.ini')
        Vstate = config.getboolean('features', 'discordvoice')
        spam = config.getboolean('features', 'notneededmsg')
        quiet_d = config.getboolean("features", 'quietdownload')
        restrict = config.getboolean("features", 'restrictvoice')

        if Vstate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return


        if restrict is True:
            if ctx.channel.id == CHANNEL_MUSIC:
                Queue_infile = os.path.isdir("./Queue")
                if Queue_infile is False:
                    os.mkdir("Queue")
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                length += 1
                add_queue = True
                while add_queue:
                    if length in queues:
                        length += 1
                    else:
                        add_queue = False
                        queues[length] = [length]
                queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{length}.%(ext)s")
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'quiet': quiet_d,
                    'outtmpl': queue_path,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                try:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        print("Downloading song audio now\n")
                        ydl.download([url])
                except:
                    dir_path = os.path.abspath(os.path.realpath("Queue"))
                    print("FALLBACK: youtube-dl not supported, searching spotify now (This is normal if spotify URL)\n")
                    system(f"spotdl -ff song{length} -f " + '"' + dir_path + '"' + " -s " + url)
                if spam:
                    await ctx.send("Adding song " + str(length) + " to the queue" )
                print("Song added to Queue\n")
            else:
                print("Wrong text channel")
                if spam:
                    await ctx.send("This command is restricted to a specific text channel (Not this one)")
                return


        elif restrict is False:
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is False:
                os.mkdir("Queue")
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            length += 1
            add_queue = True
            while add_queue:
                if length in queues:
                    length += 1
                else:
                    add_queue = False
                    queues[length] = [length]
            queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{length}.%(ext)s")
            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': quiet_d,
                'outtmpl': queue_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    print("Downloading song audio now\n")
                    ydl.download([url])
            except:
                dir_path = os.path.abspath(os.path.realpath("Queue"))
                print("FALLBACK: youtube-dl not supported, searching spotify now (This is normal if spotify URL)\n")
                system(f"spotdl -ff song{length} -f " + '"' + dir_path + '"' + " -s " + url)
            if spam:
                await ctx.send("Adding song " + str(length) + " to the queue")
            print("Song added to Queue\n")


        else:
            return


# This will skip to next song (In testing right now)

    @bot.command(pass_context=True, brief="This will skip to next song (In beta right now)", aliases=['skip',
                                                                                                      'sk',
                                                                                                      'nex'])
    async def next(ctx):
        config.read('Other/config.ini')
        Vstate = config.getboolean('features', 'discordvoice')
        spam = config.getboolean('features', 'notneededmsg')
        restrict = config.getboolean("features", 'restrictvoice')


        if Vstate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return


        if restrict is True:
            if ctx.channel.id == CHANNEL_MUSIC:
                voice = get(bot.voice_clients, guild=ctx.guild)
                Queue_infile = os.path.isdir("./Queue")
                if Queue_infile is True:

                    DIR = os.path.abspath(os.path.realpath("Queue"))
                    length = len(os.listdir(DIR))
                    still_q = length - 1
                    try:
                        first_file = os.listdir(DIR)[0]
                        if voice and voice.is_playing():
                            print("Next queued song requested (current stopped)\n")
                            voice.stop()
                            if spam:
                                await ctx.send("Playing next queued song")
                        else:
                            print("Tried to play next queued song, but failed")
                            if spam:
                                await ctx.send("Don't think the music is played")
                            return
                        song_there = os.path.isfile("song.mp3")
                        if song_there:
                            try:
                                os.remove("song.mp3")
                            except PermissionError:
                                return
                    except:
                        print("No more songs in queue")
                        if spam:
                            await ctx.send("No more songs queued")
                        return
                elif Queue_infile is False:
                    print("No Queue was made")
                    if spam:
                        await ctx.send("No songs were queued")
                    return
            else:
                print("Wrong text channel")
                if spam:
                    await ctx.send("This command is restricted to a specific text channel (Not this one)")
                return


        elif restrict is False:
            voice = get(bot.voice_clients, guild=ctx.guild)
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                still_q = length - 1
                try:
                    first_file = os.listdir(DIR)[0]
                    if voice and voice.is_playing():
                        print("Next queued song requested (current stopped)\n")
                        voice.stop()
                        if spam:
                            await ctx.send("Playing next queued song")
                    else:
                        print("Tried to play next queued song, but failed")
                        if spam:
                            await ctx.send("Don't think the music is played")
                        return
                    song_there = os.path.isfile("song.mp3")
                    if song_there:
                        try:
                            os.remove("song.mp3")
                        except PermissionError:
                            return
                except:
                    print("No more songs in queue")
                    if spam:
                        await ctx.send("No more songs queued")
                    return
            elif Queue_infile is False:
                print("No Queue was made")
                if spam:
                    await ctx.send("No songs were queued")
                return

        else:
            return


# Changes volume (in testing right now) *Disabled*

    @bot.command(pass_context=True, brief="Changes volume (in testing right now) *Disabled*", aliases=['vol'])
    async def volume(ctx, percent:int):
        print("Being developed, does not do anything right now")
        return
        config.read('Other/config.ini')
        Vstate = config.getboolean('features', 'discordvoice')
        spam = config.getboolean('features', 'notneededmsg')
        restrict = config.getboolean("features", 'restrictvoice')
        if Vstate is False:
            if spam:
                await ctx.send("This is feature is disabled at this time")
            return
        level = 0
        level = float(percent/100)
        print(f"New Volume: {percent}% ({level}))")
        if restrict is True:
            if ctx.channel.id == CHANNEL_MUSIC:
                voice = get(bot.voice_clients, guild=ctx.guild)
                if voice and voice.is_playing():
                    print("Volume has been changed")
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = int(level)
                    if spam:
                        await ctx.send("Volume has been chaned")
                else:
                    print("Tried to change volume but no playing music")
                    if spam:
                        await ctx.send("Don't think there is music playing")
            else:
                if spam:
                    await ctx.send("Please join the correct channel")
                return
        elif restrict is False:
            voice = get(bot.voice_clients, guild=ctx.guild)
            if voice and voice.is_playing():
                print("Volume has been changed")
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = level
                if spam:
                    await ctx.send("Volume has been chaned")
            else:
                print("Tried to change volume but no playing music")
                if spam:
                    await ctx.send("Don't think there is music playing")
        else:
            return


# Change log

    @bot.command(pass_context=True)
    async def changes(ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour=discord.Colour.orange()
        )
        embed.set_author(name="Change Log 4.5 (Autorole fix, emoji errors, logging times set to EST, "
                              "New ROll command, add to config.ini, diable roll command)")
        embed.add_field(name='Summary', value="Autorole works as should giving new users a set role | if an emoji "
                                              "is typed into the discord an error is not thrown | logging timestamps "
                                              "now set in EST | Roll command has been re-written | new option in "
                                              "config.ini (Recommend deleting you're current one) | the Roll command "
                                              "can now be diabled in config.ini"
                        , inline=False)
        embed.add_field(name='Change1', value="The autorole feature of the bot is not working! had not looked into the "
                                              "new way of doing this until now. When a new user joins your server "
                                              "should give role set in confing.ini",
                        inline=False)
        embed.add_field(name='Change2', value="Emoji errors in the console are no more the bot can figure them out now",
                        inline=False)
        embed.add_field(name='Change3', value="Inside the Log.txt the time stamps are now EST not a random time the "
                                              "code picked. This time can not be change from EST as of now",
                        inline=False)
        embed.add_field(name='Change4', value="The roll command has been re-written instead of only being able to roll"
                                              " 4 dice at a time the roll command can now roll 999999 dice with "
                                              "999999999999 sides at one time these limits are hard set inside the code"
                                              "Could be more but will slow the bot down",
                        inline=False)
        embed.add_field(name='Change5', value="New options in Config.ini would recommend you delete the one currently "
                                              "in your Other folder so the bot can generate a new one "
                                              "with the new options",
                        inline=False)
        embed.add_field(name='Change6', value="The roll command can now be disabled inside of the config.ini file. "
                                              "this is the new option",
                        inline=False)
        embed.add_field(name='Known Issues', value="Not any that are known if found let me know",
                        inline=False)
        embed.add_field(name='Total lines', value="was: 2066 | is: 1967 ", inline=False)

        print("Send changes")

        await author.send(embed=embed)


# test command

    @bot.command(pass_context=True)
    async def test(ctx, url: str):
        print("test works")


# This is loading cogs (commands from different files)

    for cog in os.listdir(".\\cogs"):
        if cog.endswith(".py"):
            try:
                print(cog)
                cog = f"cogs.{cog.replace('.py', '')}"
                bot.load_extension(cog)
                print("Cog Loaded\n")
            except Exception as e:
                print(f'{cog} can not be loaded\n')
                raise e

    bot.run(TOKEN)


# amounts_infile = os.path.isfile("./Other/amounts.json")

time.sleep(2)
if STARTOP is True:

    def start_run():


        def _saveini():
            with open('Other/config.ini', 'w') as configsave:
                config.write(configsave)


        print("\nHit 'ENTER' to start bot\n")
        print("Enter 'E' to open config.ini")
        print("Enter 'B' to look at bank accounts")
        print("Enter 'I' to open instructions")
        print("Enter 'L' to open Logs")
        print("Enter 'S' to turn this off")
        print("Enter 'R' to input reddit info")
        print("Enter 'C' to clear screen")
        what_do = input('\nwhat do? : ')


        if what_do == '':
            print("")
            main()
        elif what_do.upper() == 'E':
            print("Close the pop up window file when finished to continue")
            osCommandString = "notepad.exe Other/config.ini"
            os.system(osCommandString)
            start_run()
        elif what_do.upper() == 'C':
            _ = system('cls')
            start_run()
        elif what_do.upper() == 'I':
            print("Close the pop up window file when finished to continue")
            osCommandString = "notepad.exe Other/Instructions.txt"
            os.system(osCommandString)
            start_run()
        elif what_do.upper() == 'L':
            print("Close the pop up window file when finished to continue")
            osCommandString = "notepad.exe Other/Log.txt"
            os.system(osCommandString)
            start_run()
        elif what_do.upper() == 'B':
            balance_l()
            start_run()
        elif what_do.upper() == 'S':
            config.set('DEFAULT', 'startoptions', 'False')
            _saveini()
            print("Config changed")
            main()
        elif what_do.upper() == 'R':
            reddit_in()
            start_run()
        else:
            start_run()

    system('cls')
    start_run()


elif STARTOP is False:
    system('cls')
    main()
