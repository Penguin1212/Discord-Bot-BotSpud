import configparser
import os
import json

config = configparser.RawConfigParser()



def config_l():
    config.read('Other/config.ini')
    print("Config:: \n")
    print("Bot Token = " + config.get('var', 'bottoken'))
    print("Auto Role = " + config.get('var', 'autorole'))
    print("Command Prefix = " + config.get('var', 'prefix'))
    print("Currency Name = " + config.get('var', 'currencyname'))
    print("Starting Balance = " + config.get('var', 'startbalance'))
    print("Minimum Till Loan = " + config.get('var', 'loanminimum'))
    print("Display What Bot Is Playing = " + config.get('var', 'botplaying'))
    print("\nFeatures:")
    print("Reddit = " + config.get('features', 'reddit'))
    print("Insult = " + config.get('features', 'insult'))
    print("")
    input("__Press ENTER to proceed__")
    print("\n")


def save_ini():
    with open('Other/config.ini', 'w') as configsave:
        config.write(configsave)
    print("DONE!")
    input("__Press ENTER to proceed__")
    print('\n')
    return


def config_e():
    global AMOUNT, MINLOAN
    config.read('Other/config.ini')
    AMOUNT = config.getint('DEFAULT', 'startbalance')
    MINLOAN = config.getint('DEFAULT', 'loanminimum')
    config.read('Other/config.ini')
    print("\nAnswer with Y or N\n")

    def tk():
        global option_token
        option_token = input("Change Token? : ")
        if option_token == '':
            tk()

    tk()

    def ar():
        global option_autorole
        option_autorole = input("Change Auto Role? : ")
        if option_autorole == '':
            ar()

    ar()

    def pf():
        global option_prefix
        option_prefix = input("Change Prefix? : ")
        if option_prefix == '':
            pf()

    pf()

    def cn():
        global option_currency
        option_currency = input("Change Currency Name? : ")
        if option_currency == '':
            cn()
    cn()

    def am():
        global option_startamount
        option_startamount = input("Change The Starting Amount? : ")
        if option_startamount == '':
            am()
    am()

    def al():
        global option_minloan
        option_minloan = input("Change Minimum Loan Amount? : ")
        if option_minloan == '':
            al()
    al()


    def bp():
        global option_botplaying
        option_botplaying = input("Change what the bot is playing? : ")
        if option_botplaying == '':
            bp()
    bp()


    if option_token.upper() == 'Y':
        def ch_tk():
            global change_token
            change_token = input("What is the new bot token: ")
            if change_token == '':
                ch_tk()

        ch_tk()
        config.set('var', 'bottoken', change_token)

    if option_autorole.upper() == 'Y':
        def ch_ar():
            global change_autorole
            change_autorole = input('What is the new auto role: ')
            if change_autorole == '':
                ch_ar()

        ch_ar()
        config.set('var', 'autorole', change_autorole)

    if option_prefix.upper() == 'Y':
        def ch_pf():
            global change_prefix
            change_prefix = input('What is the new prefix: ')
            if change_prefix == '':
                ch_pf()

        ch_pf()
        config.set('var', 'prefix', change_prefix)

    if option_currency.upper() == 'Y':
        def ch_cn():
            global change_currency
            change_currency = input('What is the new currency name: ')
            if change_currency == '':
                ch_cn()

        ch_cn()
        config.set('var', 'currencyname', change_currency)

    if option_startamount.upper() == 'Y':
        def ch_am():
            global change_startamount
            change_startamount = input('What is the new bank starting amount: ')
            if change_startamount == '':
                ch_am()

        ch_am()
        config.set('var', 'startbalance', change_startamount)

    if option_minloan.upper() == 'Y':
        def ch_al():
            global change_minloan, change_startamount
            change_minloan = input('What is the new minimum amount before able to apply for a loan: ')
            if change_minloan == '':
                ch_al()

        ch_al()
        config.set('var', 'loanminimum', change_minloan)

    if option_botplaying.upper() == 'Y':
        def ch_bp():
            global change_botplaying
            change_botplaying = input('What should the bot say it is playing: ')
            if change_botplaying == '':
                ch_bp()

        ch_bp()
        config.set('var', 'botplaying', change_botplaying)

    print('\nOne second while I make changes to the config for you!')
    save_ini()

def balance_l():
    with open('Other/amounts.json') as f:
        banks = json.load(f)
    print('\n')
    print(banks)
    print('\n')
    input("__Press ENTER to proceed__")


def dis_ena():
    config.read('Other/config.ini')
    REDDIT = config.getboolean('features', 'reddit')
    INSULT= config.getboolean('features', 'insult')


    def chan():
        if REDDIT is True:
            change = input("Would you like to disable the Reddit feature? (Y/N):")
            if change == "":
                chan()
            elif change.upper() == "Y":
                config.set('features', 'reddit', 'False')
                save_ini()

        if REDDIT is False:
            change = input("Would you like to enable the Reddit feature? (Y/N):")
            if change == "":
                chan()
            elif change.upper() == "Y":
                config.set('features', 'reddit', 'True')
                save_ini()

        if INSULT is True:
            change = input("Would you like to disable the Insult feature? (Y/N):")
            if change == "":
                chan()
            elif change.upper() == "Y":
                config.set('features', 'insult', 'False')
                save_ini()

        if INSULT is False:
            change = input("Would you like to enable the Insult feature? (Y/N):")
            if change == "":
                chan()
            elif change.upper() == "Y":
                config.set('features', 'insult', 'True')
                save_ini()
    chan()



def enable_reddit():
    config = configparser.RawConfigParser()
    config.read('Other/config.ini')
    config.set('features', 'reddit', 'True')
    with open('Other/config.ini', 'w') as configsave:
        config.write(configsave)

    print("The for Reddit command was enabled")


def reddit_in():

    reddit_infile = os.path.isfile("./Other/reddit_info.ini")
    if reddit_infile:
        print("\nThe 'reddit_info.ini' inside the 'Other' folder needs to be deleted before you can input new bot info")
        return


    print("\nNone of this information leaves your computer\n")

    print("Help on these questions can be found in the Instructions.txt inside the other "
          "folder where you placed the bot on your computer\n")


    def client_id():
        global option_cid
        option_cid = input("Bots Client ID : ")
        if option_cid == '':
            client_id()

    client_id()


    def client_secret():
        global option_csec
        option_csec = input("Bots Client Secret : ")
        if option_csec == '':
            client_secret()

    client_secret()


    def username():
        global option_UN
        option_UN = input("Username : ")
        if option_UN == '':
            username()

    username()


    def password():
        global option_pass
        option_pass = input("Password : ")
        if option_pass == '':
            password()

    password()

    config['DEFAULT'] = {
        '# This is you reddit bot information\n'
        'client_id': option_cid,
        'client_secret': option_csec,
        'username': option_UN,
        'password': option_pass,
    }

    with open("Other/reddit_info.ini", 'w') as redditini:
        config.write(redditini)

    print("\nReddit info saved\n")

    enable_reddit()
