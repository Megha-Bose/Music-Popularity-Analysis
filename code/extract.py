from fycharts.SpotifyCharts import SpotifyCharts
import requests
import webbrowser
import time

url = 'https://spotifycharts.com/regional/global/weekly/'

file1 = open('weeks.txt', 'r')
cnt = 276
for line in file1:
    url_temp = url+line.split("\n")[0]+"/download"
    print(url_temp)
    webbrowser.open(url_temp)
    time.sleep(2)
