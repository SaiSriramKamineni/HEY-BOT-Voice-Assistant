import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_current_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_current_date():
    now = datetime.datetime.now()
    return now.day, now.month, now.year

def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour

    if 4 <= hour < 12:
        greeting = "Good Morning Sir!"
    elif 12 <= hour < 16:
        greeting = "Good Afternoon Sir!"
    elif 16 <= hour < 24:
        greeting = "Good Evening Sir!"
    else:
        greeting = "Good Night Sir, See You Tomorrow"

    speak(greeting)
    speak("HEY BOT at your service sir, please tell me how may I help you.")

def take_screenshot():
    img = pyautogui.screenshot()
    img_path = os.path.join(os.path.expanduser("~"), "Pictures", "screenshot.png")
    img.save(img_path)
    return img_path

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that. Please say that again.")
        return "None"
    except sr.RequestError:
        speak("Sorry, my speech service is down. Please try again later.")
        return "None"

    return query.lower()

if __name__ == "__main__":
    wishme()
    while True:
        query = take_command()

        if "time" in query:
            current_time = get_current_time()
            speak(f"The current time is {current_time}")
            print(f"The current time is {current_time}")

        elif "date" in query:
            day, month, year = get_current_date()
            speak(f"The current date is {day} {month} {year}")
            print(f"The current date is {day}/{month}/{year}")

        elif "who are you" in query:
            speak("I'm HEY BOT, your desktop voice assistant.")
            print("I'm HEY BOT, your desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query or "good" in query:
            speak("Glad to hear that sir!")
            print("Glad to hear that sir!")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(result)
                print(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for your query. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find any results for your query.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")

        elif "open youtube" in query:
            wb.open("https://www.youtube.com")

        elif "open google" in query:
            wb.open("https://www.google.com")

        elif "open stack overflow" in query:
            wb.open("https://www.stackoverflow.com")

        elif "play music" in query:
            music_dir = os.path.join(os.path.expanduser("~"), "Music")
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
            else:
                speak("No music files found in your Music directory.")

        elif "open chrome" in query:
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        elif "search on chrome" in query:
            speak("What should I search?")
            search_query = take_command()
            if search_query != "None":
                wb.get(chrome_path).open_new_tab(f"https://www.google.com/search?q={search_query}")

        elif "remember that" in query:
            speak("What should I remember?")
            data = take_command()
            if data != "None":
                with open("data.txt", "w") as file:
                    file.write(data)
                speak(f"You asked me to remember: {data}")

        elif "do you remember anything" in query:
            try:
                with open("data.txt", "r") as file:
                    remembered_data = file.read()
                speak(f"You told me to remember: {remembered_data}")
            except FileNotFoundError:
                speak("I don't have anything to remember.")

        elif "screenshot" in query:
            img_path = take_screenshot()
            speak(f"I've taken a screenshot. Please check your Pictures folder. Saved as {img_path}")

        elif "offline" in query:
            speak("Going offline. Goodbye, sir!")
            print("Going offline. Goodbye, sir!")
            break
