import pyttsx3  # importing a text to speach library
import speech_recognition as sr
import datetime  # importing module for getting the date and time
import wikipedia  # importing the wikipedia module

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
        "complete his small tasks, give important information.")


def greeting():
    """
Jarvis needs to greet me according to the right time.
    """
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        speak(" A very Good Morning, Sir !")
    elif 12 <= hour <= 16:
        speak(" A very Good Afternoon, Sir !")
    elif 16 <= hour <= 20:
        speak(" A very Good Evening, Sir !")
    elif 20 <= hour <= 5:
        speak(" Sir its night time, please take rest.")
    speak("Sir, your today's schedule is really busy. ")


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
        query = r.recognize_google(audio, language="en-UK")  # uses the google API to convert the audio to text.
        print(f"Your command Sir : {query}\n")
    except Exception as e:  # if jarvis is unable to understand my command throw the following message
        print("Sir I'm sorry, but can you please repeat what you just said ....")
        return "None"
    return query


# Main function (so that speak function in the main function executes only in this python file).
if __name__ == '__main__':
    greeting()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on the query
        if 'wikipedia' in query:
            speak("Sir looking for you, just hold on ....")  # Jarvis searching in the wikipedia
            query = query.replace("wikipedia", "")  # replacing the text "wikipedia" with blank
            results = wikipedia.summary(query, sentence=2)
