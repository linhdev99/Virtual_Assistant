import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import random
from gtts import gTTS
import wikipedia
from webdriver_manager.chrome import ChromeDriverManager
import playsound as aitalk
import winsound
import pyttsx3
import time

wikipedia.set_lang('vi')
language = {"vietnam": "vi",
            "english": "en"}
path = ChromeDriverManager().install()
soundPath = "sound.mp3"
bossName = "Peter"

alice = pyttsx3.init()
voice = alice.getProperty('voices')
alice.setProperty('voice',voice[1].id)

keywords = {
    "password": ["123","1 2 3", "12 3", "1 23"],
    "google": ["mở google", "google", "open google"],
    "youtube": ["mở youtube", "youtube", "open youtube"],
    "video": ["mở video", "open video"],
    "facebook": ["mở facebook", "facebook", "open facebook"],
    "time": ["giờ", "mấy giờ", "thời gian"],
    "exit": ["bye alice", "thoát ra", "tạm biệt", "tắt chương trình", "dừng lại"],
    "mybk": ["mybk", "my bk", "my b k", "school", "web trường", "trường"],
    "elearning": ["learn", "elearning", "study", "học", "học tập"],
    "hello": ["hello", "hi", "chào", "xin chào"],
    "boring": ["boring", "boringggg", "buồn", "chán"],
    "love": ["love", "i love you", "i love", "love you", "love u", "i love u", "yêu em", "anh yêu em", "thương", "thương em", "cưng cưng", "thương thương", "moah"]
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
    speak("Xin chào, tôi tên là ALICE!", lang="vietnam")
    speak("Hãy đọc mật khẩu...", lang="vietnam")
    query = command(True).lower()
    while not verifyPassword(query):
        speak("Hãy đọc lại mật khẩu...", lang="vietnam")
        query = command(True).lower()
    while True:
        ALICE_Reply_VI()

def ALICE_Reply_VI():
    query = command(False).lower()
    if compareList(keywords["google"], query) == 1:
        visitGoogle()
    # elif compareList(keywords["youtube"], query) == 2:
    #     visitYoutube()
    # elif compareList(keywords["video"], query) == 2:
    #     visitFile("video")
    # elif compareList(keywords["facebook"], query) == 2:
    #     visitFacebook()
    elif compareList(keywords["time"], query) == 1:
        time()
    # elif compareList(keywords["exit"], query) == 2:
    #     speak("ALICE Love Boss very much, See you again!")
    #     quit()
    # elif compareList(keywords["mybk"], query) == 1:
    #     visitMyBK()
    # elif compareList(keywords["elearning"], query) == 1:
    #     visitElearning()
    # elif compareList(keywords["hello"], query) == 1:
    #     visitHello()
    # elif compareList(keywords["boring"], query) == 1:
    #     visitBroing()
    # elif compareList(keywords["love"], query) == 1:
    #     visitLove()
    elif compareList(keywords["exit"], query) == 1:
        speak("ALICE Love Boss very much, See you again!", lang="english")
        quit()
    else:
        speak(f"ALICE does't understand!", lang="english")

def time():
    hour = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    sec = datetime.datetime.now().second
    Time = "Bây giờ là: {hour} giờ {min} phút {sec} giây.".format(hour=hour, min=min, sec=sec)
    speak(Time, lang="vietnam")

def visitGoogle():
    speak("Anh cần tìm gì trên Google??", lang="vietnam")
    search = command(False).lower()
    speak('Okay!', lang="vietnam")
    url = f"https://www.google.com/search?q={search}"
    wb.get().open(url)

def speak(text, lang):
    if 'vietnam' in lang:
        print("A.L.I.C.E: {text}".format(text=text))
        tts = gTTS(text=text, lang=language[lang], slow=False)
        tts.save(soundPath)
        aitalk.playsound(soundPath, winsound.SND_ASYNC | winsound.SND_ALIAS)
        os.remove(soundPath)
    elif 'english' in lang:
        print('A.L.I.C.E: ' + text)
        alice.say(text)
        alice.runAndWait()

def command(isPassword):
    # global isPassword
    c = sr.Recognizer()
    query = ""
    with sr.Microphone() as source:
        print("A.L.I.C.E đang nghe...")
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='vi-VN')
        if isPassword:
            print("{bossName}: {query}".format(bossName=bossName, query="******"))
        else:
            print("{bossName}: {query}".format(bossName=bossName, query=query))
    except sr.UnknownValueError:
        # query = command(isPassword)
        print("Please repeat or typing the command ")
        value = input('You order is: ')
        if value != "":
            query = str(value)
        else:
            query = "hello"
    return query

def verifyPassword(password):
    if compareList(keywords["password"], password) == 1:
        speak("Chào {bossName}, mừng anh quay trở lại!\n Em có thể giúp gì cho anh không?".format(bossName=bossName), lang="vietnam")
        return True
    else:
        speak("Bạn là ai? Hay là boss quên mật khẩu?", lang="vietnam")
        return False
    


if __name__ == "__main__":
    print(chr(27) + "[2J")
    main()
