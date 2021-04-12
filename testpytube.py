#Este codigo sirve para descargar videos de YT con una libreria de python
#Primero instalamos la libreria 
#pip install pytube

#Importamos el modulo pytube
import pytube
#crear una variable donde almacenamos la URL del video
video_url = input("Inserte la URL del video: ")
#crear la variable que lleva el medoso youtube
youtube = pytube.YouTube(video_url)
#definimos el formato de descarga como mp4 y en que resolucion
#“720p”, “480p”, “360p”, “240p”, “144p”
#video = youtube.streams.get_by_resolution("480p")
video = youtube.streams.first()
#descargamos el video en una direccion, si no se 
#especifica entonces se descarga en la carpeta
#del archivo
video.download()
#video.download(r'C:Documentos')