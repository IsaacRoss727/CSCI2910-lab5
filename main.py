from ossapi import Ossapi
import requests
import json
from ossapi import models
import re

#id is an int and cliend_secret is a string
#Scrapped compare uesrs because of time contraints.

api = Ossapi(id, client_secret)

def get_user_info(username):
    user_id = api.user(username).id
    user_string = ""
    user_info_username = api.user(username).username 
    user_string += f"Username: {user_info_username}\n"
    user_global_rank = api.user(username).statistics.global_rank
    user_string += f"Global rank: {user_global_rank}\n"
    user_country_rank = api.user(username).statistics.country_rank
    user_country = api.user(username).country.name
    user_string += f"Country: {user_country}\nCountry Rank: {user_country_rank}\n"
    user_level = api.user(username).statistics.level.current
    user_string += f"Level: {user_level}\n"
    user_playtime = api.user(username).statistics.play_time
    user_string += f"Total Playtime: {round(user_playtime/60/60)} hours\n"
    user_performace_points = api.user(username).statistics.pp
    user_string += f"Total PP: {user_performace_points}\n"
    user_info_acc = api.user(username).statistics.hit_accuracy
    user_string += f"Hit accuracy: {round(user_info_acc,2)}%\n"
    user_info_top_play_id = api.user_scores(user_id, "best")[0].best_id
    top_play_id = user_info_top_play_id
    user_top_play = api.score("osu", top_play_id)
    user_top_play_beatmapset = api.beatmapset(user_top_play.beatmap)
    user_top_play_beatmap = api.beatmap(user_top_play.beatmap)
    user_string += f"Top Play: {user_top_play.pp}pp on {user_top_play_beatmapset.artist} - {user_top_play_beatmapset.title} [{user_top_play_beatmap.version}] mapped by {api.user(user_top_play_beatmap.user_id).username} with {round(user_top_play.accuracy*100,2)}% accuracy."
    return user_string

def get_recent_score(username):
    user_string = ''
    user_id = api.user(username).id
    user_recent_score = api.user_scores(user_id, include_fails=False, type="recent")[0]
    user_string += f"Recent score for {api.user(user_id).username}: {user_recent_score.beatmapset.artist} - {user_recent_score.beatmapset.title} [{user_recent_score.beatmap.version}]\n{user_recent_score.pp}PP\n300 Count: {user_recent_score.statistics.count_300}\n100 Count: {user_recent_score.statistics.count_100}\n50 Count: {user_recent_score.statistics.count_50}\nMisses: {user_recent_score.statistics.count_miss}"
    return user_string

print("Welcome to the osu! API demo!\nPlease select an option!\n")
user_choice = input("1. Get user info\n2. View a user's recent score\nWhich option would you like to select?: ")
if user_choice == "1":
    username_choice = input("Which user would you like to get the info of?: ")
    print(get_user_info(username_choice))
elif user_choice == "2":
    username_choice = input("Which user would you like to get recent score of?: ")
    print(get_recent_score(username_choice))
else:
    print("Please go back and select a correct option!")


