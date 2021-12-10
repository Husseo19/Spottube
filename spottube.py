# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:54:51 2021

@author: Hussein Abbas
"""
import re, spotipy , os , pytube , time
from spotipy.oauth2 import SpotifyClientCredentials
from googlesearch import search

client_credentials_manager = SpotifyClientCredentials(client_id="7e59e51e03584e6e81433e3af71eb260",
                                                      client_secret="66ac298749e640c994abddef4bf4a474")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

list_for_youtube = []
list_for_google = []
destination = None
def Spotify_link():
    playlist_link = input("Please Enter the playlist you want to download:")
    pattern = "https://open.spotify.com/playlist/(.*?)\?si="
    substring = re.search(pattern, playlist_link).group(1)
    counter = 0;
    total = 0;
    tracks = sp.playlist_tracks(substring, fields=None, limit=100, offset=0, market=None)
    for item in tracks['items']:
        track = item['track']
        counter += 1
        total += 1
        print(counter,")" , track['name'] + ' - ' + track['artists'][0]['name']) 
        list_for_google.append(track['name'] + ' - ' + track['artists'][0]['name'] + " official audio youtube")
    print("Total songs to download is" , total)

def Google_search():
    print("Searching for youtube links...")
    for i in range(len(list_for_google)):
        query = (list_for_google[i]) 
    # to search
        for j in search(query, tld="co.in",num=10, stop=1, pause=0):
            list_for_youtube.append(j)
    
def Youtube_downloader():
    for i in range(len(list_for_youtube)):
        time.sleep(1)
        yt = pytube.YouTube(list_for_youtube[i])

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
  
        # download the file
        out_file = video.download(output_path=destination)
  
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
  
        # result of success
        print(yt.title + " has been successfully downloaded.")
        
def main():
    Spotify_link()
    user_input = input("Do you want to continue? (Y/N)")
    destination = input("Enter the destination (leave blank for current directory): ")
    while True:
        if user_input in ("Y", "y"):
            Google_search()
            Youtube_downloader()
            break
        elif user_input in ("N", "n"):
            break
        else:
            user_input = input("Please enter correct input (Y/N)")


    
   
main()




#https://open.spotify.com/playlist/7ymVT8WlZr8BgAssxD9knB?si=1b47800ed23b46fb

