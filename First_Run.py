import configparser
import webbrowser


def make_txt():
    instruction = open('Other/Instructions.txt', 'w+')
    instruction.write("___WELCOME___\n"
                       "Hello and welcome to this discord bot! This might seem like a lot, but trust me it is not!!!\n"
                       "I will walk you through everything you will need to get this bot up and running!\n"
                       "Once you launch the bot again it will ask you to enter a few different things "
                       "(Bot Token, Auto Give Role, Command Prefix, Currency Name, Starting Balance, and Amount "
                       "to be able to apply for a loan)\n"
                       "\n"
                       "\n"
                       "___EXPLANATION___\n"
                       "Bot Token - Can be found here = https://discordpy.readthedocs.io/en/rewrite/discord.html \n"
                       "Auto Give Role - Is the default role in your server. When a new user joins your discord the "
                       "bot will give them that role on it's own (make sure to enter exactly what the role is. It's "
                       "case-sensitive \n"
                       "Command Prefix - What symbol comes before a command such as: ('/', '!') only enter one\n"
                       "Currency Name - The name you want your currency to be (EX: Penguins, Coffey Cups, or Coins) it can "
                       "be anything you would like it to be\n"
                       "Start Balance - Is the balance you want when a new bank account is made this can be any amount "
                       "(NO DECIMALS) whatever you think is fair\n"
                       "Loan Minimum Amount - This is the minimum amount someone can have in their bank account "
                       "before they are "
                       "allowed to apply for a loan using the command. This amount must be equal to or less than the Starting "
                       "amount or balance\n"
                       "\n"
                       "\n"
                       "___FALLBACK___\n"
                       "Config.ini fallback values (Default values NULL=Bot will not work without it):\n"
                       "Bot Token = NULL\n"
                       "Command Prefix = !\n"
                       "Auto Role = Test Role\n"
                       "Currency Name = Money\n"
                       "Bank Starting Balance = 1000\n"
                       "Minimum Loan = 100\n"
                       "Bot Playing = With Humans\n"
                       "\n"
                       "\n"
                       "___FEATURES___\n"
                       "You can now disable/enable a few features such as:\n"
                       "The Reddit command\n"
                       "The DMRedditInfo (This will dictate if the bot gives the pulled reddit information to the user "
                       "via their DMs or in chat room they requested it in)\n"
                       "The Insult command\n"
                       "The Cards command\n"
                       "The Discord voice commands\n"
                       "The Restricted voice (If voice commands should only be allowed in a specific text channel)"
                       "The Not Needed msg (This is spam control this will limit the response from the bot to only needed "
                       "messages)\n"
                       "The Quiet Download (If False will display the song downloading/If True will hide the song "
                       "downloading)\n"
                       "\n"
                       "\n"
                       "___OPTIONS___\n"
                       ">>MAKING MESSAGE 'Start Options' COME BACK:\n"
                       "Locate 'config.ini file should be in the 'Other' folder thats located where the bot files are.\n"
                       "You can open it with notepad or notepad++ (I would use notepad++)\n"
                       "Then change 'startoptions' under the 'default' section to 'True'\n"
                       "If you can not figure it out just delete the 'config.ini' file (will have to re-enter variables)\n"
                       ">>RESTRICT VOICE COMMANDS TO ONLY ONE TEXT CHANNEL\n"
                       "The bot offers a feature to only allow the voice control commands in a text channel of your choice\n"
                       "To enable this feature open the 'config.ini' file (location is described above)\n"
                       "Under the 'features' change 'restrictvoice' to 'True'\n"
                       "Then under the 'var' section delete the 4 zeros next to 'ChannelTextId' then paste the text channel id you want the "
                       "voice commands to work in.\n"
                       "How To get channel IDs: https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord#get-the-channel-id-of-the-discord-text-channel \n"
                       "EX:\n"
                       "ChannelTextId = 576477347507863562\n"
                       "restrictvoice = True"
                       "\n"
                       "\n"
                       "___REDDIT___\n"
                       "This section will explain how to get the for reddit command to work\n"
                       "First you will need a reddit bot for this to work. To get one log in to any reddit account\n"
                       "Then click preferences in the top right then you should see an 'apps' tab near the top click that\n"
                       "Then click the button that says 'create another app', name the bot, select the 'script' option, "
                       "type up a description, and then fill in the URLs any URL will work for those\n"
                       "After this your bot should show up in the list click the edit button you will need two keys from "
                       "the bot\n"
                       "Right under the name of the bot should see a key (ex: tadDgDrUW-wvcn) this is the client ID\n"
                       "The last key you will need is the one labeled 'SECRET' (ex: Dpwt_noa8S2YBgpa_uox4mFNqv6) "
                       "This is the client secret\n"
                       "The last two things you will need is your account username and password that the reddit bot you just made "
                       "is associated with\n"
                       "To input this so the discord bot can use it make sure that in the 'config.ini' under the "
                       "DEFAULT section that 'startoptions' is True (This can be set to False after you input the bot info)\n"
                       "Now when you restart the bot there will be a list of options press 'r' then hit ENTER "
                       "Then input the information as labeled\n"
                       "This will save the reddit bot info to your computer and turn the for Reddit command on"
                       "\n"
                       "\n"
                       "___ERROR CODES___\n"
                       "1 = In Config 'loanminimum' is larger than 'startbalance' FIX: Edit config with notepad or Notepad++"
                       "to make 'startbalance' larger than 'loanminimum'\n"
                       "If a green warning saying the for reddit command will not work: see REDDIT section for help"
                       "\n"
                       "\n"
                       "___END___\n"
                       "I would recommend getting the program notepad++ to open the files in the 'Other' folder.\n"
                       "Notepad++ download link: https://notepad-plus-plus.org/download/v7.7.html \n"
                       "If you delete this file the bot will ask if you have launched it before so keep this file here\n")
    instruction.close()


def ftime():
    global first_time
    first_time = input("Is this the first time you have launched 'Bot_Spud.exe'?(Y/N): ")
    if first_time.upper() == 'Y':
        make_txt()
        print("\nI have made an 'Instructions.txt' and placed it in the same directory as me.\n\n"
              "Read that then re-launch the bot\n")
        want_quit = input("Close bot and read 'Instructions.txt'(Y/N): ")
        if want_quit.upper() == 'Y':
            webbrowser.open('instructions.txt')
            quit()
        else:
            return
    elif first_time.upper() == 'N':
        make_txt()
        return
    elif first_time.upper() == '':
        ftime()
    ftime()


def input_config():

    print("I see there is no 'Config.json' please enter the following, so I can make a new one:\n")

    def tk():
        global TOKEN
        TOKEN = input("*Enter bot Token:")
        if TOKEN == '':
            print("\rThis is Required\n")
            tk()
    tk()

    def ar():
        global AUTO_ROLE
        AUTO_ROLE = input("Enter role to automatically give new people(Must be exact name): ")
        if AUTO_ROLE == '':
            print("\rPlease enter a value\n")
            ar()
    ar()

    def pf():
        global PREFIX
        PREFIX = input("Enter command prefix(only one): ")
        if PREFIX == '':
            print("\rPlease enter a value\n")
            pf()
    pf()

    def cn():
        global CURREN
        CURREN = input("Enter the name of your currency: ")
        if CURREN == '':
            print("\rPlease enter a value\n")
            cn()
    cn()

    def am():
        global AMOUNT, CURREN
        AMOUNT = input("Enter the amount of " + CURREN + " a new account should start with: ")
        if AMOUNT == '':
            print("\rPlease enter a value\n")
            am()
    am()

    def al():
        global APPLY
        APPLY = input("Enter the minimum amount before able to apply for a loan: ")
        if APPLY == '':
            print("\rPlease enter a value\n")
            al()
    al()

    def bp():
        global PLAYING
        PLAYING = input("Enter what the bot will appear to be playing: ")
        if PLAYING == '':
            print("\rPlease enter a value\n")
            bp()
    bp()

    make_config()


def make_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        '# Do not edit DEFAULT values\n'
        'BotToken': 'NULL',
        'AutoRole': 'User',
        'Prefix': '!',
        'CurrencyName': 'Money',
        'StartBalance': '1000',
        'LoanMinimum': '100',
        'BotPlaying': 'With Humans',
        'ChannelTextId': '0000',
        'StartOptions': 'True',
    }
    config['var'] = {
        '# Make sure that you read Instructions.txt before editing below this\n'
        'BotToken': TOKEN,
        'AutoRole': AUTO_ROLE,
        'Prefix': PREFIX,
        'CurrencyName': CURREN,
        'StartBalance': AMOUNT,
        'LoanMinimum': APPLY,
        'BotPlaying': PLAYING,
        '# If you need to enter text channel id see instructions.txt on a how-to\n'
        'ChannelTextId': '0000',
    }
    config['features'] = {
        '# Make sure to capitalize the True or False when editing\n'
        'Roll': 'True',
        'Reddit': 'False',
        'DMRedditInfo': 'False',
        'Insult': 'True',
        'Urbandic': 'True',
        'Cards': 'True',
        'DiscordVoice': 'True',
        'RestrictVoice': 'False',
        'NotNeededMSG': 'True',
        'QuietDownload': 'False',
    }
    with open("Other/config.ini", 'w') as configini:
        config.write(configini)
    print("\nConfig has been made! \n\n"
          +
          "Now looking for 'amounts.json'...\n")
