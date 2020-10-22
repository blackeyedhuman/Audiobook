import os
from os import path
from glob import glob
import pyttsx3
import PyPDF2
import keyboard
import PySimpleGUI as sg
from tkinter import Tk   
from tkinter.filedialog import askopenfilename

# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

def main_menu_start():
    layout = [[sg.Text("Hi, are you starting a new book?")],
            [sg.Button('Yes'), sg.Button('No')]]

    window = sg.Window('Audiobook', layout)

    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == 'Yes':
        print("Choose the pdf of your choice : ")
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        writeBook(filename)
        writeCache(0)
        
    # Finish up by removing from the screen
    print("Let's get started!")
    window.close()

#read pg number
def readBook():
    f = open("/home/venkatesh/Documents/GitHub/audiobook/bookPath.txt", "r")
    to_return = f.read()
    f.close()
    return to_return

def writeBook(path):
    f = open("/home/venkatesh/Documents/GitHub/audiobook/bookPath.txt", "w")
    f.write(path)
    print("The book path has been stored!")
    f.close()
    return

def readCache():
    f = open("/home/venkatesh/Documents/GitHub/audiobook/cache.txt", "r")
    if os.stat("/home/venkatesh/Documents/GitHub/audiobook/cache.txt").st_size == 0:
        to_return = 0
    else:
        to_return = f.read()
    f.close()
    return int(to_return)

#write pg number
def writeCache(page):
    f = open("/home/venkatesh/Documents/GitHub/audiobook/cache.txt", "w")
    f.write(str(page))
    print("The bookmark has been cached!")
    f.close()
    return

#play the pdf
def audioBook(page_number):
    page_number = page_number
    speaker = pyttsx3.init()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate-60)
    #book_ext = find_ext(".", "pdf") 
    #print(book_ext)
    path = readBook()
    book = open(path, 'rb') #pdf.pdf
    pdfReader = PyPDF2.PdfFileReader(book)
    lastPage = pdfReader.getNumPages()
    
    while(1):
        if lastPage <= page_number:
            break
        cache_pg = page_number
        page = pdfReader.getPage(page_number)
        writeCache(cache_pg)
        page_number = page_number + 1
        text = page.extractText()
        def onWord(name, location, length):
            print('word', name, location, length)
            if keyboard.is_pressed("esc"):
                speaker.stop()
            speaker.connect('started-word', onWord)
        speaker.say(text)
        speaker.runAndWait()
    
    writeCache(page_number)

def main():

    main_menu_start()
    startFrom = readCache()
    audioBook(startFrom)

if __name__ == '__main__':
    main()