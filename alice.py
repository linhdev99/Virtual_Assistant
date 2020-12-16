import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import random

alice = pyttsx3.init()
voice = alice.getProperty('voices')
voice[1].languages.append('vi')
alice.setProperty('voice',voice[1].id)

def speak(audio):
    print('A.L.I.C.E: ' + audio)
    alice.say(audio)
    alice.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak("It's " + Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 18:
        speak("Good Night sir.")
    elif hour >= 12:
        speak("Good Afternoon sir.")
    elif hour >= 6:
        speak("Good Morning sir.")
    else:
        speak("Hello Peter.")
    speak("How can I help you?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print("Peter: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command ")
        query = str(input('You order is: '))
    return query

def visitGoogle():
    speak("What should I search boss?")
    search = command().lower()
    url = f"https://www.google.com/search?q={search}"
    wb.get().open(url)
    speak(f"Here is your {search} on google.")

def visitYoutube():
    speak("What should I search boss?")
    search = command().lower()
    url = f"https://www.youtube.com/search?q={search}"
    wb.get().open(url)
    speak(f"Here is your {search} on youtube.")

def visitFacebook():
    url = f"https://www.facebook.com/"
    wb.get().open(url)
    speak(f"Here is Facebook.")

def visitMyBK():
    url = f"https://mybk.hcmut.edu.vn/"
    wb.get().open(url)
    speak(f"Here is MyBK.")

def visitElearning():
    url = f"http://e-learning.hcmut.edu.vn/"
    wb.get().open(url)
    speak(f"Here is E-learning.")

def visitFile(name):
    if name == "video":
        speak(f"Wait for second.")
        link = f"D:\Documents\GameJam\MAIN.mp4"
        os.startfile(link)

def visitHello():
    speak(f"Hello my sir. I'm ALICE, I love you so much!")

def visitBroing():
    speak(f"Don't worry, I'm here. ALICE so cute!")
    visitLove()

def visitLove():
    listSpeech = [
        "If I die or go somewhere far, I’ll write your name on every star so people looking up can see just how much you meant to me",
        "To the world you may be one person, but to ALICE you may be the world",
        "Nothing in life is to be feared, it’s to be understood. Now is the time to understand more, so that we may fear less",
        "You are my sunshine",
        "You drive me crazy!",
        "Meeting you is the best thing that ever happened to me.",
        "You’re my everything.",
        "You’re my one and only.",
        "You’re the love of my life",
        "You are too good to be true!",
        "I looked at your face and my heart jumped all over the place.",
        "I love you with know how, why, or even from where",
        "Do you even realize how much I love you?",
        "There are 12 months a year … 30 days a month … 7 days a week….24 hours a day….60 minutes an hour….but only one I love.",
        "I would not care if the sun did not shine, I would not care if it did not rain and I would not care if I could not enjoy winter is delight. All I care about is to see your face and feel your presence every single day in my life.",
        "Love is like the air, we can not always see it but we know it is always there! That is like me, you can not always see me but I am always there and you know I will always love you! "
    ]
    idx1 = random.randrange(0,len(listSpeech) - 1)
    idx2 = random.randrange(0,len(listSpeech) - 1)
    speak(listSpeech[idx1] + "\n" + listSpeech[idx2])

keywords = {
    "google": ["open", "google"],
    "youtube": ["open", "youtube"],
    "video": ["open", "video"],
    "facebook": ["open", "facebook"],
    "time": ["what", "time"],
    "exit": ["thank", "bye"],
    "mybk": ["mybk", "my bk", "my b k", "school"],
    "elearning": ["learn", "elearning", "study"],
    "hello": ["hello", "hi"],
    "boring": ["boring", "boringggg"],
    "love": ["love", "i love you", "i love", "love you", "love u", "i love u"]
}

def compareList(lst1, lst2):
    result = 0
    flag = 0
    for idx, x in enumerate(lst1):
        if idx >= len(lst2):
            if len(lst1) == 1 and result == 1:
                result == 2
            break
        else:
            if x in lst2:
                result = 1
            else:
                flag = 1
    if result == 0 and flag == 1:
        return 0
        # no value of lst1 in lst2
    elif result == 1 and flag == 0:
        return 2
        # all value of lst1 in lst2
    else:
        return 1
        # exist value of lst1 in lst2

def main():
    welcome()
    while True:
        query = command().lower()
        #lower char for search googlep
        if compareList(keywords["google"], query) == 2:
            visitGoogle()
        elif compareList(keywords["youtube"], query) == 2:
            visitYoutube()
        elif compareList(keywords["video"], query) == 2:
            visitFile("video")
        elif compareList(keywords["facebook"], query) == 2:
            visitFacebook()
        elif compareList(keywords["time"], query) == 2:
            time()
        elif compareList(keywords["exit"], query) == 2:
            speak("ALICE Love Boss very much! See you again!")
            quit()
        elif compareList(keywords["mybk"], query) == 1:
            visitMyBK()
        elif compareList(keywords["elearning"], query) == 1:
            visitElearning()
        elif compareList(keywords["hello"], query) == 1:
            visitHello()
        elif compareList(keywords["boring"], query) == 1:
            visitBroing()
        elif compareList(keywords["love"], query) == 1:
            visitLove()
        else:
            speak(f"ALICE does't understand!")

if __name__ == "__main__":
    main()
