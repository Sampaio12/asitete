import spotipy
from logic.config import Client_ID, Client_Secret, Redirect_URI, scope
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth




class Spotify:
    def __init__(self):
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope, client_id=Client_ID, client_secret=Client_Secret, redirect_uri=Redirect_URI))

    def spotify_play(self,query):
        try:
            results = self.sp.search(q=query, limit=1)
            self.sp.start_playback(uris=[results['tracks']['items'][0]['uri']])
            return
        except:
            return
        
    def get_title(self, comm):
        try:
            results = self.sp.search(q=comm, limit=1)
            return results['tracks']['items'][0]['name']
        except:
            return

    def volume_up(self):
        try:
            vol = self.sp.current_playback()['device']['volume_percent']
            if vol < 100:
                vol += 10
                self.sp.volume(vol)
                return vol
            else:
                return vol
        except:
            return

    def volume_down(self):
        try:
            vol = self.sp.current_playback()['device']['volume_percent']
            if vol > 0:
                vol -= 10
                self.sp.volume(vol)
                return vol
            else:
                return vol
        except:
            return
    def pause(self):
        try:
            self.sp.pause_playback()
        except:
            return
    def resume(self):
        try:
            self.sp.start_playback()
        except:
            return

