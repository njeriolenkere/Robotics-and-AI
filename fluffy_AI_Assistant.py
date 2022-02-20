#fluffy your AI Voice Assistant
#The sole purpose of AI is to develop machines that can perform human tasks
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import webbrowser as wb

#Recognizer that will understand your commands
r = sr.Recognizer()
#The speaker to talk back
speaker = pyttsx3.init()
#The voice speed of the fluffy
speaker.setProperty('rate', 150)
#gets you the details of the current voice
voices = speaker.getProperty('voices')
#converts voices (female[1] or male[0])
speaker.setProperty('voice', voices[1].id)

#upon calling say() fluffy will respond to u in text or audio
def say(audio):
    speaker.say(audio)
    speaker.runAndWait()

def takeCommand():
    try:
        # open the microphone and start recording
        with sr.Microphone() as source:
            print('Listening...')
            # calling speech recogniser to listen to the mic
            voice = r.listen(source)
            # convert voice to text and language selection
            command = r.recognize_google(voice, language='en-uk')
            command = command.lower()
            r.pause_threshold = 0.6
            r.adjust_for_ambient_noise(source)
            #make a wish. Your wish is fluffy's command
            if 'your name' in command:
                say('I am Fluffy. Your friend')
            elif 'play' in command:
                song = command.replace('play', '')
                say('playing' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                #time format- 12hr ("%I:%M %p") or 24hr ("%H:%M")
                time = datetime.datetime.now().strftime("%I o'clock and %M minutes, %p")
                say('The time is' + time)
            elif 'search' in command:
                command = command.replace('search', '')
                url = 'https://www.bing.com/search?q=' + command
                say('Searching' + command)
                wb.get().open(url)
            elif 'joke' in command:
                say(pyjokes.get_joke())
            elif 'goodbye' in command:
                say('Goodbye')
                quit()
            else:
                say('Please repeat again')
    except:
        pass
#to run the loop/power on the AI voice assistant
while True:
    takeCommand()
#inspired by programmingHero[Grandma]

