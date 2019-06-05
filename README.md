# Discord-Bot-BotSpud

___WELCOME___

BotSpud is a bot I have been working on for a little more than 2 months.

A porject while I learn to code in Python, but after changing the dsicord.py to the re-write version I found that a lot of the code I had been using (for voice commands) did not work with the re-write of discord.py. Most of the command like: 

join, leave, pause, resume, stop, and play were supported for the most part and can be found in the re-write documentation.

Commands like queue (to queue new songs before the one playing has finished) and next (to play the next queued song even before
the one playing has finished) did not seem to be supported and there was nothing about these command in the docuentation. 

I also could not find any tutorials or help online like I could before the re-write.

If you look through the code in 'Bot_Spud.py' you will see I have made all the above commands with some twists on them, but they work.

I am not taking credit for any of this because all I did was look through the documentation of a few imports and used them the way they work to solve a problem and anyone could do this.

The point of this is to supply others with a fairly big bot as an example of how things could be done.

Exaples:

This can also be used as a base to a bot and people could add cogs for new command as need.

Could be used as a very customizable discord bot more so than a regular discord bot.

Use:

To use the code you must have a few things installed on you computer 

1. Python (latest version)

2. pip so projects needed for the bot to run correctly can be downloaded

3. FFmpeg (https://ffmpeg.org/)

When these are all installed you can then download the ZIP from here and unpack it on your computer making sure all the files are inside the same folder. 

Then once that is complete you can use the 'start.bat' to run the bot this will use pip to install all the projects needed and then run the bot.

If everything above is done correctly it should run and ask for a few inputs for setup (Make sure to read the instructions.txt file if needed)

===========================================================================

___IMPORTS___

This bot was made using the latest version of python (V: 3.7) along with the latest version of all imported Python projects.

------------------------------------------------------------------------

from discord.ext import commands

from discord.utils import get

from discord import FFmpegPCMAudio

from os import system

from termcolor import colored, cprint

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

------------------------------------------------------------------------

Some of these will need to be installed using pip

discord.py is the voice version.





























