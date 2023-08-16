# PresonalAssistance
Developed a Python-based personal assistant that efficiently streamlined daily tasks and provided enhanced productivity. Leveraged natural language processing and machine learning techniques to enable voice-controlled interactions for different tasks.

Code Explained:

# Import necessary libraries
import speech_recognition as sr  # Library for recognizing speech
import os  # Library to interact with the operating system
import pyttsx3  # Library for text-to-speech conversion
import webbrowser  # Library to open web browsers

# Function to convert text to speech
def say(text):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.say(text)  # Set the text that will be spoken
    engine.runAndWait()  # Run the speech synthesis engine and wait for completion

# Function to take user's voice input
def TakeCommand():
    r = sr.Recognizer()  # Create an instance of the speech recognizer
    with sr.Microphone() as source:  # Use the microphone as the audio source
        r.pause_threshold = 1  # Set the pause threshold before considering audio complete
        audio = r.listen(source)  # Listen to the audio input
        try:
            query = r.recognize_google(audio, language="en-in")  # Convert audio to text using Google API
            print(f"User Said: {query}")  # Print the user's input
            return query
        except Exception as e:
            return "Sorry, an error occurred."

# Main execution
if __name__ == '__main__':
    print('PyCharm')  # Print a message
    
    # Use the say function to speak a welcome message
    say("Welcome Prathamesh.........I am Your Personal Assistant")

# Continuous loop to keep the program running and listening for user commands
while True:
    print("Listening.............")  # Print a message indicating listening
    
    # Use the TakeCommand function to get user's voice input
    query = TakeCommand()
    
    # List of predefined websites to open
    sites = [
        ["youtube", "https://www.youtube.com"],
        ["Google", "https://www.google.com"],
        # ... (similar entries for other websites)
    ]
    
    # Check if user's query matches predefined website commands and open the website
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} sir...")  # Speak the action
            webbrowser.open(site[1])  # Open the website using the webbrowser library
