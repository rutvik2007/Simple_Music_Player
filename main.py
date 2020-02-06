import os
from tkinter.filedialog import askdirectory
from pprint import *
import pygame
from mutagen import File
from tkinter import *
from mutagen.id3 import *
root = Tk()
root.minsize(500,500)


listofsongs = []
realnames = []
v = StringVar()
songlabel = Label(root,textvariable=v,width=35)
index = 0
def directorychooserinit():

	directory = filedialog.askdirectory()
	os.chdir(directory)

	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			realdir = os.path.realpath(files)
			listofsongs.append(realdir)
			audio = ID3(realdir)
			print(audio['TIT2'])
			realnames.append(audio['TIT2'][0])

	pygame.mixer.init()

directorychooserinit()
print(listofsongs,len(listofsongs))

def directorychooser(event):

	directory = filedialog.askdirectory()
	os.chdir(directory)
	lst1=[]
	lst2=[]
	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			realdir = os.path.realpath(files)
			lst2.append(realdir)
			audio = ID3(realdir)
			lst1.append(audio['TIT2'][0])
	for items in lst1:
		listbox.insert(END,items)
	realnames.extend(lst1)
	listofsongs.extend(lst2)


def nextsong(event):
	global index
	if (index<len(listofsongs)-1):
		index += 1
	else:
		index=len(listofsongs)-1
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	print(listofsongs[index])
	updatelabel()

def pausesong(event):
	pygame.mixer.music.pause()


def prevsong(event):
	global index
	index -= 1
	if(index<=0):
		index=0
	pygame.mixer.music.load(listofsongs[index])
	pygame.mixer.music.play()
	updatelabel()

def stopsong(event):
	pygame.mixer.music.stop()
	v.set("")

def updatelabel():
	global index
	v.set("Now playing: "+realnames[index])

label=Label
label = Label(root,text='Music Player')
label.pack()

listbox = Listbox(root,)
listbox.pack()

#listofsongs.reverse()


for items in realnames:
	listbox.insert(END,items)

#listofsongs.reverse()

nextbutton = Button(root,text = 'Next Song')

nextbutton.pack()
directorybutton=Button(root,text='Load more songs')
directorybutton.pack()
previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()

stopbutton = Button(root,text='Stop Music')
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
directorybutton.bind("<Button-1>",directorychooser)
songlabel.pack()
root.mainloop()
