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

def read_text(filename):
    text = ""
    pdf = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdf)
    pageNum = pdfReader.numPages
    for i in range(pageNum):
        pageObj = pdfReader.getPage(i)
        text += pageObj.extractText()
        return text

def audio(text):
    audio = gTTS(text=text.strip(), lang='en', tld="co.uk")
    print("Your Audio is Processing...")
    audio.save("result.mp3")
    playsound("result.mp3")
    print("Done, Hope you will enjoy!")


def upload_action():
    filename = filedialog.askopenfilename(title="Upload Your PDF File")
    if filename:
        root.destroy()
        text = read_text(filename)
        audio(text)

root = tk.Tk()
root.title("Welcome to PDF Text Reader!")
root.geometry("300x200")
button = tk.Button(root, text='Upload Your PDF', command=upload_action)
button.pack()
root.mainloop()

