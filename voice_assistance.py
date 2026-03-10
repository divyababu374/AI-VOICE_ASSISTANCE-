import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
import datetime
import os
import ollama

recognizer = sr.Recognizer()

# Speak function
def speak(text):

    print("Assistant:", text)

    tts = gTTS(text=text, lang="en")
    tts.save("voice.mp3")

    playsound("voice.mp3")

    os.remove("voice.mp3")


# AI function using Ollama
def ask_ai(question):

    response = ollama.chat(
        model="phi3",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return response["message"]["content"]

#listen function
def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command

    except:

        return None

def run_voice_assistant():

    speak("Hello Divya, I am your AI assistant")

    while True:

        command = input("You: ")

        if command == "exit":
            speak("Goodbye")
            break

        response = ask_ai(command)

        speak(response)

# Greeting
speak("Hello Divya. I am your AI voice assistant. How can I help you?")


while True:

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        command = command.lower()

        print("You said:", command)

    except:

        speak("Sorry I could not understand")

        continue


    if "hello" in command:

        speak("Hello Divya")


    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%H:%M")

        speak("The time is " + current_time)


    elif "open google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")


    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")


    elif "search" in command:

        speak("What should I search")

        with sr.Microphone() as source:

            audio = recognizer.listen(source)

        try:

            query = recognizer.recognize_google(audio)

            speak("Searching for " + query)

            webbrowser.open(
                "https://www.google.com/search?q=" + query
            )

        except:

            speak("I could not understand the search")


    elif "exit" in command or "stop" in command:

        speak("Goodbye Divya")

        break


    else:

        ai_answer = ask_ai(command)

        speak(ai_answer)