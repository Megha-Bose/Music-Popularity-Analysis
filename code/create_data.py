

from fycharts.SpotifyCharts import SpotifyCharts
import requests
import webbrowser
import time
import pandas as pd
import json

file_name = 'weeks/regional-global-weekly-'
data_songs = {}
file1 = open('ascending_weeks.txt', 'r')
cnt = 0
for line in file1:
    cnt += 1
    fileN = file_name+line.split("\n")[0]+".csv"
    print(fileN)
    df = pd.read_csv(fileN)
    for i in range(len(df)):
        if i == 0:
            continue
        position = df.loc[i][0]
        song = df.loc[i][1]
        artist = df.loc[i][2]
        streams = df.loc[i][3]
        url = df.loc[i][4]
        if song in data_songs and artist == data_songs[song]['artist']:
            data_songs[song]['data'].append({
                'week': line.split("--")[0],
                'streams': streams,
                'position': position
            })
        else:
            data_songs[song] = {
                'artist': artist,
                'url': url,
                'data': []
            }
            data_songs[song]['data'].append({
                'week': line.split("--")[0],
                'streams': streams,
                'position': position
            })


with open("spotifycharts_data.json", "w") as outfile:
    json.dump(data_songs, outfile, indent=2)
