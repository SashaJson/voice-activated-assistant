import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print(words)
    os.system('say ' + words)


talk('Hi')


def cmd():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('I am listening to you')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print('You said: ' + task)
    except sr.UnknownValueError:
        talk('I do not understand you')
        task = cmd()

    return task


def make_some_thing(task):
    if 'open this repository in website GitHub' in task:
        task('Already opening')
        url = 'https://github.com/SashaJson/voice-activated-assistant'
        webbrowser.open(url)
    elif 'stop' in task:
        talk('Okay!')
        sys.exit()
