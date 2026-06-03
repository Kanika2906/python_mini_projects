import datetime
import webbrowser
import random
import os

jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Python is my favorite snake.",
            "Debugging is like being a detective."
        ]
quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Keep learning and keep building.",
    "Every expert was once a beginner."
]

def wishme():
    r = int(datetime.datetime.now().hour)
    if r>=0 and r<12:
        p = "Good Morning!"
    elif r>=12 and r<18:
        p = "Good Afternoon!"
    else:
        p = "Good Evening!"
    print(f"Hello, {p}")
    print("I am your Personal Chatbot !")
    

if __name__ == "__main__":
    wishme()
    while True:
        query = input("How may I help you.").lower()
        
        if "time" in query:
            print("Current time is :")
            print(datetime.datetime.now().strftime("%H:%M:%S"))

        elif "joke" in query:
            print(random.choice(jokes))
        
        elif "quote" in query:
            print(random.choice(quotes))

        elif "calculator" in query:
            os.system("calc")

        elif "google" in query:
            print("Opening Google...")
            webbrowser.open("www.google.com")
        
        elif "youtube" in query:
            print("Opening Youtube...")
            webbrowser.open("www.youtube.com")
        
        elif 'chatgpt' in query:
            webbrowser.open("chatgpt.com")

        elif "exit" in query or "stop" in query:
            print("Exiting..")
            break

        else:
            print("Sorry, out of my reach")