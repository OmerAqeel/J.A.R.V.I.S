import pyttsx3  # importing a text to speach library
import speech_recognition as sr
import datetime  # importing module for getting the date and time
import wikipedia  # importing the wikipedia module
import webbrowser  # to open any website on the browser

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
        speak(" A very Good Morning Mr Omer !")
    elif 12 <= hour <= 16:
        speak(" A very Good Afternoon Mr Omer !")
    elif 16 <= hour <= 20:
        speak(" A very Good Evening Mr Omer !")
    elif 20 <= hour <= 5:
        speak(" Sir its night time, please take rest.")
    speak("How can I help you Sir ..... ")


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
            speak("Yes Sir, wikipedia is opened. What do you want to know ?")  # Jarvis searching in the wikipedia
            query = takeCommand().lower()
            query = query.replace("I want to know about", "")
            results = wikipedia.summary(query, sentences=2)  # summarizes the info into 2 sentences
            print(results)  # prints the wiki results about the anything I have asked jarvis for.
            speak(f"Sir according to wikipedia, {results}")
        elif "open youtube" in query:
            speak("Of course Sir, your command is my wish !")
            webbrowser.open("https://www.youtube.com")
        elif "university portal" in query:
            speak("Of course Sir, your command is my wish !")
            webbrowser.open(
                "https://login.navigate.navitas.com/ENTERPRISE/index/login?SAMLRequest"
                "=fVPLbtswELznKwLdbT0i2zVhCXCdPgy4tmCrPfTGUOuGgESy3FXi%2Fn1JSWmcohUvApYzszPL1Qp5Uxu2bulRHeFnC0g3t"
                "%2B5cmloh6y6zoLWKaY4SmeINICPBTusvO5ZMI2asJi10HfxFG2dxRLAktepp2%2FssOOw%2F7A6ftvt5HMcwv3uIovOMp8vZ"
                "%2FBy%2F4xUkszSaJ8u7NF0s4mUV8575DSw6mSxwqoMWYgtbhcQVuXKUJJMomSSLMl6yNGVJ%2FL3HFYPx91JVUv0Y9"
                "%2FvQg5B9LstiUhxOZS"
                "%2Byfsmx0QrbBuwJ7JMU8PW4y4JHIoMsDPlF4lTxJ0kcp0I3ITemloJ7XuhnFYqeHeSd6MrXWJfD5v8TWYXXqFeeYXvnfntfaNfiV1f356O2DafxkL4iq8m5gzLjJ4sEioI%2FKuu61s8bC5wgC8i2znHv423XN3aGrYKq2zE3J4IL3W50Y7iV6J8OLlzQkP01%2FzV8U7uFOcI5H90pwYTHuXLhPs%2FaVv6NQbjepeUKjbY0jO2f4r3rcMR2fvNyff3D5L8B",
                )
