from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3
import os




Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="#00e500")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red ")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!",fg="green")



root = Tk()
root.title("Downloader")
root.geometry("350x250") #set window
root.columnconfigure(0,weight=1)#set all content in center.



#set window color
#root.configure(bg='blue')

#Ytd Link Label
ytdLabel = Label(root,text="Enter the Link of the Video",font=("Helvetica",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=40,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error
ytdError = Label(root,text="Enter Youtube Link",fg="red",font=("Helvetica",10))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("Helvetica",15))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="#00e500",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error location
locationError = Label(root,text="Enter Location",fg="red",font=("Helvetica",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("Helvetica",15))
ytdQuality.grid()

#combobox
choices = ["720p","144p","MP3"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#donwload btn
downloadbtn = Button(root,text="Donwload",width=10,bg="#00e500",fg="white",command=DownloadVideo)
downloadbtn.grid()

#developer Label
developerlabel = Label(root,text="tatomat",font=("Helvetica",5))
developerlabel.grid()
root.mainloop()


# creates a Tk() object 
root= Tk() 


#threads
threads = []


def startThredProcess():
    myNewThread = threading.Thread(target=onClick)
    threads.append(myNewThread)
    myNewThread.start()

#menu


