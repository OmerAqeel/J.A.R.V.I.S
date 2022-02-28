import pyttsx3  # importing a text to speach library
import speech_recognition as sr
import datetime  # importing module for getting the date and time
import wikipedia  # importing the wikipedia module
import webbrowser  # to open any website on the browser

from Bots import *
from Links import *
from personal import *
from Reminders import *
from shuttingDown import jarvisCloseCommands

# Factory function to get reference to pyttsx3 and as I am on Mac, I will NSSpeachSynthesizer TTS engine.
engine = pyttsx3.init('nsss')
# outputs the voices available in the computer.
voices = engine.getProperty('voices')

# checking for the best voice for jarvis -----> print(voices[0].id)

# setting the voice for the
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """
This function takes in the string that jarvis will speak
    :param audio:
    """
    engine.say(audio)
    engine.runAndWait()


def JarvisInfo():
    """
This function tells the important info about Jarvis when called.
    """
    speak(
        "Hi, I am Jarvis. I am a personal Assistant of Mr Omer Aqeel. He has programmed me to receive his commands, "
        "complete his small tasks, give important information, remind him about his daily task that he has set for "
        "himself. I also manage his whatsapp messages, his emails etc. Mr "
        "Omer has other ideas in his mind for me, which I'm really excited for. Anyways it was nice meeting you, "
        "see you next time!")


def greeting():
    """
Jarvis needs to greet me according to the right time. Also reminds me of the reminders
    """
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        speak(" A very Good Morning Mr Omer !")
    elif 12 <= hour <= 16:
        speak(" A very Good Afternoon Mr Omer !")
    elif 16 <= hour <= 20:
        speak(" A very Good Evening Mr Omer !")
    elif 20 <= hour:
        speak(" Sir its night time, please take rest.")
    speak("How may I help you Sir?")
    if num_Reminders >= 5:  # If I have typed in more than 5 reminders or 5 for myself in the text file, Jarvis will let me know about it.
        speak(f"By the way sir, you have a really busy schedule today. I have {num_Reminders} reminders for you. Let me remind them to you sir.")
        speak(f"{readReminders}")


x = "not done"


def takeCommand():
    """
This function takes in my command through microphone and returns the command as a string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:  # use the default microphone as the audio source
        print("I am Listening sir .....")
        r.pause_threshold = 1  # Allows me to take at most 1 second pause b/w my phrases.
        audio = r.listen(source)

    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language="en-IN")  # uses the google API to convert the audio to text.
        print(f"Your command Sir : {query}\n")
    except Exception as e:  # if jarvis is unable to understand my command throw the following message
        print("Sir I'm sorry, but can you please repeat what you just said ....")
        return "None"
    return query


def openResources():
    webbrowser.open(geeksForgeeks)
    webbrowser.open(stackOverflow)
    webbrowser.open(youtube)
    webbrowser.open(W3schools)


# Main function (so that speak function in the main function executes only in this python file).
if __name__ == '__main__':
    greeting()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on the query
        if "yourself" in query:
            JarvisInfo()
            speak("Sir if that was it, do you want me to leave ?")
            query = takeCommand().lower()
            if "yes" in query:
                speak("Alright sir! Have a good day.")
                break
            else:
                pass
        if query in jarvisCloseCommands:                #Commanding Jarvis to stop running.
            speak("Ok sir, shutting down. I'll see you later, have a great day")
            break
        if 'wikipedia' in query:
            speak(
                "Yes Sir, wikipedia is opened now. What exactly you want me to look for?")  # Jarvis searching in the wikipedia
            query = takeCommand().lower()
            query = query.replace("look for", "")
            results = wikipedia.summary(query, sentences=2)  # summarizes the info into 2 sentences
            print(results)  # prints the wiki results about the anything I have asked jarvis for.
            speak(f"Sir according to wikipedia, {results}")
        elif "open youtube" in query:
            speak("Of course Sir, your command is my wish ! ")
            webbrowser.open(youtube)
        elif "google" in query:
            speak(f"Opening google for you sir.")
            webbrowser.open(google)
        elif "resources" in query:
            speak(f"Opening all the resources for you sir.")
            openResources()
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "reminders" in query:
            if num_Reminders != 0 and num_Reminders < 5:
                speak(f"Yes sir, you have {num_Reminders} reminders.")
                speak(f"{readReminders}")
            else:
                speak("No sir, there is nothing for you in the reminders.")
        elif "university portal" in query:
            speak("Of course Sir, do you want me to log in for you ?")
            query = takeCommand().lower()
            if "no" in query:
                webbrowser.open(university)
            elif "yes" in query:
                speak("Here you go sir ")
                runUniversityBot(usernameStr, passwordStr)
