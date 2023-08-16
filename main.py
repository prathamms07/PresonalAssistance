import speech_recognition as sr
import os
import pyttsx3
import webbrowser


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



'''The pyttsx3.init()-
    function initializes a new instance of the speech synthesis engine.
engine.say(text)-
    is used to set the text that will be spoken by the engine. It takes the text parameter as input.
engine.runAndWait() -
    runs the speech synthesis engine and waits for the speech to complete before the function returns.
    Essentially, the say function initializes the speech synthesis engine, sets the desired text to be spoken, 
    and then runs the engine to convert the text to speech'''

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source :
     r.pause_threshold=1
     audio=r.listen(source)
     try:
         query= r.recognize_google(audio, language="en-in")
         print(f"User Said: {query}")
         return query
     except Exception as e:
         return "Sorry Error Occured"

'''Here with the help of the recognizer class of speech recognition we will make new instance of that class as r there
then using microphone class we will access the microphone of the system and will treat it as the source
then we will set the pause_threshold as 1 i.e here we will pause that much seconds before the phrase is considered as complete
 then to take input we used listen to take input from source
 
 then we use recognize_google which is google Web Speech API used for speech input and speech to text output'''

if __name__ == '__main__':
    print('PyCharm')
say("Welcome Prathamesh.........I am Your Personal Assistance")
while True:
 #s=input()

 print("Listening.............")

 query= TakeCommand()
 #say(query)

 sites = [
     ["youtube", "https://www.youtube.com"],
     ["Google", "https://www.google.com"],
     ["Wikipedia", "https://www.wikipedia.org"],
     ["LeetCode", "https://leetcode.com"],
     ["CodeChef", "https://www.codechef.com"],
     ["Coursera", "https://www.coursera.org"],
     ["WhatsApp", "https://web.whatsapp.com"],
     ["Telegram", "https://web.telegram.org"],
     ["InternetLogin", "http://1.1.1.1:8090/httpclient.html"],
     ["Music", "https://open.spotify.com/"]
 ]

 for site in sites:
     if f"Open {site[0]}".lower() in query.lower():
         say(f"Opening {site[0]} sir...")
         webbrowser.open(site[1])



 #say(query)


