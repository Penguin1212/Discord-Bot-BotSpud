import os
import configparser

def make_prawini():
    config_name = 'praw'
    file_name = os.path.join(os.path.dirname(__file__), config_name + '.ini')
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'check_for_updates':'True',
        'comment_kind':'t1',
        'message_kind':'t4',
        'redditor_kind':'t2',
        'submission_kind':'t3',
        'subreddit_kind':'t5',
        'trophy_kind':'t6',
        'oauth_url':'https://oauth.reddit.com',
        'reddit_url':'https://www.reddit.com',
        'short_url':'https://redd.it'
    }
    with open(file_name, 'w') as prawini:
        config.write(prawini)
    return
