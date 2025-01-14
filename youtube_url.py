import youtube_dl

def obtener_urls_playlist(url_playlist):

  ydl_opts = {
      'extract_flat': True,
      'quiet': True
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
      info = ydl.extract_info(url_playlist, download=False)
      return [f'https://www.youtube.com/watch?v={entry["id"]}' for entry in info['entries']]

if __name__ == '__main__':
  url_playlist = 'https://www.youtube.com/playlist?list=PLbpxA68x19evaHfbi_cowKHFEwfCqxUgo'  
  urls = obtener_urls_playlist(url_playlist)
  for url in urls:
      print(url)