from PIL import Image
import mutagen
import os
from tkinter.filedialog import askdirectory
print(mutagen.version)
songlist=[]
directory=askdirectory()
os.chdir(directory)
for file in os.listdir(directory):
	if file.endswith(".mp3"):
		file=os.path.join(directory, file)
		#print(file)
		songlist.append(file)
songlist.sort()
metadata=[]
for song in songlist:
	audio=mutagen.File(song,easy=False)
	metadata.append(audio)
for song in metadata:
	#print(type(song.tags['APIC:'].data))
	artwork=song.tags['APIC:'].data
	with open('image.jpg', 'wb') as img:
		img.write(artwork)
		image=Image.open('image.jpg')
		image.show()
