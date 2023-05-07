from spotipy.oauth2 import SpotifyOAuth
import spotipy


# Spotify API'ye erişim anahtarınızı buraya girin
client_id = 'CLİENT_İD'
client_secret = 'CLİENT_SECRET' #Spotify dev platformundan apinin özelliklerinden alıcaksın
redirect_uri = 'http://localhost:8000/callback/'



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='user-read-recently-played'))


results = sp.current_user_recently_played(limit=1)
track_name = results['items'][0]['track']['name']
artist_name = results['items'][0]['track']['artists'][0]['name']
caption = f"{track_name} - {artist_name}"

print(caption)

# Burdaki Caption verisini kendi programınızda apiler aracığılıyla istediğiniz uygulamaya yazdırabilirsin. İnstagrama yazdırcak arkaşalar Selenium kullanması daha mantıklı instagramAPI instabot modülleri düzgün çalışmıyor.