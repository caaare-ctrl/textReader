# Too tired to read? Build a python script that takes a PDF file, identifies the text and converts the text to speech.
# Effectively creating a free audiobook.
# AI text-to-speech has come so far. They can sound more lifelike than a real audiobook.
# Using what you've learnt about HTTP requests, APIs and Python scripting, create a program that can convert PDF files to speech.
# You right want to choose your own Text-To-Speech (TTS) API. But here are some you can consider:
from gtts import gTTS
from io import BytesIO
import tkinter as tk
from tkinter import filedialog
import PyPDF2
from playsound import playsound
mp3_fp = BytesIO()

def readText(filename):
    text = ""
    pdf = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdf)
    pageNum = pdfReader.numPages
    for i in range(pageNum):
        pageObj = pdfReader.getPage(i)
        text += pageObj.extractText()
    audio = gTTS(text=text.strip(), lang='en', tld="co.uk")
    audio.save("result.mp3")
    playsound("result.mp3")

def UploadAction():
    filename = filedialog.askopenfilename(title="Upload Your PDF File")
    if filename:
        root.destroy()
        readText(filename)

root = tk.Tk()
root.title("Welcome to PDF Text Reader!")
root.geometry("300x200")
button = tk.Button(root, text='Upload Your PDF', command=UploadAction)
button.pack()
root.mainloop()

