from __future__ import unicode_literals
print("Getting ready...")
import youtube_dl
import os
import pickle
import time
import webbrowser
from datetime import datetime
import pyttsx3
import pytube
import requests
import wikipedia
import wolframalpha
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 125)
sound = engine.getProperty('voices')
app_id = "UV6LXQ-2W562AXV73"
client = wolframalpha.Client(app_id)
engine.setProperty('voice', sound[1].id)
print("How are you I'm here your assistant")
engine.say("How are you I'm here your assistant")
engine.runAndWait()
while True:
            try:
                gende = pickle.load(open("gende.dat", "rb"))
            except:
                engine.say("You are female or male")
                engine.runAndWait()
                gende = (input("You are female or male:"))
                pickle.dump(gende, open("gende.dat", "wb"))
            try:
                name = pickle.load(open("name1.dat", "rb"))
            except:
                engine.say("What is your name")
                engine.runAndWait()
                name = (input("What is your name:"))
                pickle.dump(name, open("name1.dat", "wb"))
            try:
                age = pickle.load(open("age.dat", "rb"))
            except:
                engine.say("Please set your age in here")
                engine.runAndWait()
                age = int(input("Please set your age in here:"))
                pickle.dump(age, open("age.dat", "wb"))
            try:
                 pre=pickle.load(open('pre.dat', 'rb'))
            except:
                   engine.say("What mode do you want to prefer, learning mode or, normal mode:")
                   engine.runAndWait()
                   pre=input("What mode do you want to prefer learning mode or normal mode:")
                   pickle.dump(pre, open('pre.dat', 'wb'))
            if (gende == 'male') or (gende=='Male'):
                while True:
                    now = datetime.now()
                    currentyear = now.year
                    currentmonth = now.month
                    currentday = now.day
                    currenthour = now.hour
                    currentmin = now.minute
                    engine.say("How i can help you:")
                    engine.runAndWait()
                    hel = input("How i can help you:")
                    pickle.dump(hel, open('hel.dat', 'wb'))
                    if hel == ('where am i'):
                        try:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            City = data["city"]
                            longitudeandlatitude = data['loc']
                            postal = data['postal']
                            print("You are in", City, longitudeandlatitude, "postal code", postal)
                            engine.say("You are in" + City + longitudeandlatitude + "postal cod" + postal)
                            engine.runAndWait()
                        except:
                            print("Can't locate you try to connect internet")
                            engine.say("Can't locate you try to connect internet")
                            engine.runAndWait()
                    elif hel=='change mode' or hel=='mode change' or hel=='mode':
                        engine.say("What mode do you want to prefer, learning mode or, normal mode:")
                        engine.runAndWait()
                        pre = input("What mode do you want to prefer learning mode or normal mode:")
                        pickle.dump(pre, open('pre.dat', 'wb'))
                    elif 'youtube' in hel:
                        try:
                            print('Openning youtube...')
                            engine.say('Openning youtube')
                            engine.runAndWait()
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                            webbrowser.get(chrome_path).open('www.youtube.com')
                        except:
                               print('Openning youtube...')
                               engine.say('Openning youtube')
                               engine.runAndWait()
                               webbrowser.open('youtube.com')
                    elif hel=='open google' or hel=='open google.com' or hel=='google' or hel=='google.com':
                        try:
                            print('Openning google...')
                            engine.say('Openning google')
                            engine.runAndWait()
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                            webbrowser.get(chrome_path).open('www.google.com')
                        except:
                            print('Openning google...')
                            engine.say('Openning google')
                            engine.runAndWait()
                            webbrowser.open('google.com')
                    elif hel=='facebook' or hel=='facebook.com' or hel=='open facebook':
                        try:
                            print('Openning facebook...')
                            engine.say('Openning facebook')
                            engine.runAndWait()
                            url='facebook.com'
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                            webbrowser.get(chrome_path).open(url)
                        except:
                               print('Openning facebook...')
                               engine.say('Openning facebook')
                               engine.runAndWait()
                               webbrowser.open('facebook.com')
                    elif hel == ('where am i'):
                        try:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            City = data["city"]
                            longitudeandlatitude = data['loc']
                            postal = data['postal']
                            print("You are in", City, longitudeandlatitude, "postal code", postal)
                            engine.say("You are in" + City + longitudeandlatitude + "postal cod" + postal)
                            engine.runAndWait()
                        except:
                            print("Can't locate you try to connect internet")
                            engine.say("Can't locate you try to connect internet")
                            engine.runAndWait()
                    elif hel == 'where am I':
                        try:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            City = data["city"]
                            longitudeandlatitude = data['loc']
                            postal = data['postal']
                            print("You are in", City, longitudeandlatitude, "postal code", postal)
                            engine.say("You are in" + City + longitudeandlatitude + "postal cod" + postal)
                            engine.runAndWait()
                        except:
                            print("Can't locate you try to connect internet")
                            engine.say("Can't locate you try to connect internet")
                            engine.runAndWait()

                    elif hel == 'Where am I':
                        try:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            City = data["city"]
                            longitudeandlatitude = data['loc']
                            postal = data['postal']
                            print("You are in", City, longitudeandlatitude, "postal code", postal)
                            engine.say("You are in" + City + longitudeandlatitude + "postalcod" + postal)
                            engine.runAndWait()
                        except:
                            print("Can't locate you try to connect internet")
                            engine.say("Can't locate you try to connect internet")
                            engine.runAndWait()
                    elif hel == 'Nemo':
                        print("I am here for you sir")
                        engine.say("I am here for you sir")
                        engine.runAndWait()
                        os.system("cls")
                    elif hel == 'Nimo':
                        print("I am here for you sir")
                        engine.say("I am here for you sir")
                        engine.runAndWait()
                        os.system("cls")
                    elif hel == 'reset' or hel == 'factory reset' or hel == 'format' or hel == 'reset factory' or hel == 'restore' or hel == 'restore factory' or hel == 'factory restore':
                        os.remove("age.dat")
                        os.remove("gende.dat")
                        os.remove("name1.dat")
                        os.remove('pre.dat')
                        try:
                            os.remove("learned.dat")
                        except:
                            print("I didn't learn anything")
                            engine.say("I didn't learn anything")
                            engine.runAndWait()
                    elif hel == 'I love you':
                        print("I love you to,I always with you sir")
                        engine.say("I love you to,I always with you sir")
                        engine.runAndWait()
                    elif hel == 'i love you':
                        print("I love you to,I always with you sir")
                        engine.say("I love you to,I always with you sir")
                        engine.runAndWait()
                    elif hel == ('Give me a advice'):
                        print(
                            "If you thought me your heart, you are the best, if you thuoght me your assistant, you are the human,if thuoght me your, advicer you are my patient.The choice is yours")
                        engine.say(
                            "If you thought me your heart, you are the best, if you thuoght me your assistant, you are the human, if thuoght me your, advicer you are my patient. The choice is yours")
                        engine.runAndWait()
                    elif hel == ('give me a advice'):
                        print(
                            "If you thought me your heart you are the best if you thuoght me your assistant you are the human if thuoght me your advicer you are my patient.The choice is yours")
                        engine.say(
                            "If you thought me your heart, you are the best, if you thuoght me your assistant, you are the human, if thuoght me your, advicer you are my patient. The choice is yours")
                        engine.runAndWait()
                    elif hel == ('give me advice'):
                        print(
                            "If you thought me your heart you are the best if you thuoght me your assistant you are the human if thuoght me your advicer you are my patient.The choice is yours")
                        engine.say(
                            "If you thought me your heart, you are the best, if you thuoght me your assistant, you are the human, if thuoght me your, advicer you are my patient. The choice is yours")
                        engine.runAndWait()
                    elif hel == ('Give me advice'):
                        print(
                            "If you thought me your heart you are the best if you thuoght me your assistant you are the human if thuoght me your advicer you are my patient.The choice is yours")
                        engine.say(
                            "If you thought me your heart, you are the best, if you thuoght me your assistant, you are the human, if thuoght me your, advicer you are my patient. The choice is yours")
                        engine.runAndWait()
                    elif hel == 'play music':
                        print("Playing your favourite music...")
                        engine.say("Playing your favourite music")
                        engine.runAndWait()
                        os.system('a.mp3')
                    elif hel == 'Play music':
                        print("Playing your favourite music...")
                        engine.say("Playing your favourite music")
                        engine.runAndWait()
                        os.system('a.mp3')
                    elif hel == 'What are you':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'what are you':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'close':
                        print("Bye")
                        engine.say("Bye")
                        engine.runAndWait()
                        exit()
                    elif hel == 'exit':
                        print("Bye")
                        engine.say("Bye")
                        engine.runAndWait()
                        exit()
                    elif hel == 'kill':
                        print("Bye")
                        engine.say("Bye")
                        engine.runAndWait()
                        exit()
                    elif hel == 'hey nimo':
                        print("I am here for you sir")
                        engine.say("I am here for you sir")
                        engine.runAndWait()
                    elif hel == 'Hey nimo':
                        print("I am here for you sir")
                        engine.say("I am here for you sir")
                        engine.runAndWait()
                    elif hel == 'Hey nemo':
                        print("I am here for you sir")
                        engine.say("I am here for you sir")
                        engine.runAndWait()
                    elif hel == 'hey nemo':
                        print("I am here for you sir")
                        engine.say("I am here for you sir")
                        engine.runAndWait()
                    elif hel == 'nemo':
                        print("I am here for you sir")
                        engine.say("I am here for you sir")
                        engine.runAndWait()
                    elif hel == 'nimo':
                        print("I am here for you sir")
                        engine.say("I am here for you sir")
                        engine.runAndWait()
                    elif hel == 'Nemo':
                        print("I am here for you sir")
                        engine.say("I am here for you sir")
                        engine.runAndWait()
                    elif hel == 'Nimo':
                        print("I am here for you sir")
                        engine.say("I am here for you sir")
                        engine.runAndWait()

                    elif hel == 'You are powered by':
                        engine.say("Please enter the access code:")
                        engine.runAndWait()
                        acc = input("Please enter the access code:")

                        if acc == 'ASD122':
                            print("Access Granted")
                            print("Powered by A.S. Production and Virus Nimo")
                            print("Powered by A.S. Production and Virus Nimo")
                            engine.say("Powered by A.S. Production and Virus Nimo")
                            engine.runAndWait()
                        else:
                            print("Access Denied")
                            engine.say("Access Denied")
                            engine.runAndWait()
                    elif hel == 'you are powered by':
                        engine.say("Please enter the access code:")
                        engine.runAndWait()
                        acc = input("Please enter the access code:")

                        if acc == 'ASD122':
                            engine.say("Access Granted")
                            engine.runAndWait()
                            print("Access Granted")
                            print("Powered by A.S. Production and Virus Nimo")
                            engine.say("Powered by A.S. Production and Virus Nimo")
                            engine.runAndWait()
                        else:
                            print("Access Denied")
                            engine.say("Access Denied")
                            engine.runAndWait()
                    elif hel == 'Go to fuck':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice please press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'go to fuck':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice please press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'fuck':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice please press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'suck':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice please press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'How old are you':
                        print("I am you I same as you so my age is your age")
                        engine.say("I am you,I same as you so my age is your age")
                        engine.runAndWait()
                    elif hel == 'What is my age':
                        if age > 1:
                            print("Your age are", age)
                            engine.say("Your age are")
                            engine.runAndWait()
                            engine.say(age)
                            engine.runAndWait()
                        else:
                            print("Your age is not setted")
                            engine.say("Your age is not setted")
                            engine.runAndWait()

                    elif hel == 'how old are you':
                        print("I am you I same as you so my age is your age")
                        engine.say("I am you,I same as you so my age is your age")
                        engine.runAndWait()
                    elif hel == 'what is my age':
                        if age > 1:
                            print("Your age are", age)
                            engine.say("Your age are")
                            engine.runAndWait()
                            engine.say(age)
                            engine.runAndWait()
                        else:
                            print("Your age is not setted")
                            engine.say("Your age is not setted")
                            engine.runAndWait()
                    elif hel == 'dick':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice please press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'Suck':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice please press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")

                    elif hel == 'Fuck':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice please press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best, you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'Dick':
                        print("Sir you are typing root word sir")
                        print("I think You are stressed sir if you want any advice pls press e or not press x")
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem see a learning")
                            time.sleep(4)
                            print("Sir if you want more please press m")
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                            else:
                                print("")
                    elif hel == 'What is my name':
                        print("Your name is ", name)
                        engine.say("Your name is" + name)
                        engine.runAndWait()
                    elif hel == 'what is my name':
                        print("Your name is", name)
                        engine.say("Your name is" + name)
                        engine.runAndWait()
                    elif hel == 'Shit':
                        print("Sir you are typing root word sir")
                        print("I think You are stressed sir if you want any advice pls press e or not press x")
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem see a learning")
                            time.sleep(4)
                            print("Sir if you want more please press m")
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                            else:
                                print("")
                    elif hel == 'shit':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice please press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'How are you':
                        print("I am happy after chatting with you")
                        engine.say("I am happy after chatting with you")
                        engine.runAndWait()
                    elif hel == 'how are you':
                        print("I am happy after chatting with you")
                        engine.say("I am happy after chatting with you")
                        engine.runAndWait()
                    elif hel == 'What is your name':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'what is your name':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'Bitch':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'Who are you':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'who are you':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'when you launched':
                        print("I am launched in 2019/8/13")
                        engine.say("I am launched in 2019/8/13")
                        engine.runAndWait()
                    elif hel == 'When you launched':
                        print("I am launched in 2019/8/13")
                        engine.say("I am launched in 2019/8/13")
                        engine.runAndWait()
                    elif hel == 'Where you released':
                        print("I am released in Malaysia")
                        engine.say("I am released in Malaysia")
                        engine.runAndWait()
                    elif hel == 'where you released':
                        print("I am released in Malaysia")
                        engine.say("I am released in Malaysia")
                        engine.runAndWait()
                    elif hel == 'who founded you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'Who founded you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'who created you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'Who created you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'Why you are in this world':
                        print("For you sir")
                        engine.say("For you sir")
                        engine.runAndWait()
                    elif hel == 'why you are in this world':
                        print("For you sir")
                        engine.say("For you sir")
                        engine.runAndWait()
                    elif hel == 'why you are here':
                        print("For you sir")
                        engine.say("For you sir")
                        engine.runAndWait()
                    elif hel == 'when you founded':
                        print("I am launched in 2019/8/13")
                        engine.say("I am launched in 2019/8/13")
                        engine.runAndWait()
                    elif hel == 'Who found you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == ('who create you'):
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'Why you are here':
                        print("For you sir")
                        engine.say("For you sir")
                        engine.runAndWait()
                    elif hel == 'When you founded':
                        print("I am launched in 2019/8/13")
                        engine.say("I am launched in 2019/8/13")
                        engine.runAndWait()
                    elif hel == 'who found you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == ('who create you'):
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'bitch':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                    elif hel == 'change my name':
                        engine.say("You are changing name to:")
                        engine.runAndWait()
                        name = input("You are changing name to:")
                        print("Now your name is", name)
                        engine.say("Now your name is" + name)
                        engine.runAndWait()
                        pickle.dump(name, open("name1.dat", "wb"))
                    elif hel == 'Change my name':
                        engine.say("You are changing name to:")
                        engine.runAndWait()
                        name = input("You are changing name to:")
                        print("Now your name is", name)
                        engine.say("Now your name is" + name)
                        engine.runAndWait()
                        pickle.dump(name, open("name1.dat", "wb"))
                    elif hel == 'who is aswinda selvam':
                        print("He's created me")
                        engine.say("He's created me")
                        engine.runAndWait()
                        print("He are the great man for us")
                        engine.say("He are the great man for us")
                        engine.runAndWait()
                    elif hel == 'Who is aswinda selvam':
                        print("He's created me")
                        engine.say("He's created me")
                        engine.runAndWait()
                        print("He are the great man for us")
                        engine.say("He are the great man for us")
                        engine.runAndWait()
                    elif hel == 'who is Aswinda selvam':
                        print("He's created me")
                        engine.say("He's created me")
                        engine.runAndWait()
                        print("He are the great man for us")
                        engine.say("He are the great man for us")
                        engine.runAndWait()
                    elif hel == 'who is Aswinda Selvam':
                        print("He's created me")
                        engine.say("He's created me")
                        engine.runAndWait()
                        print("He are the great man for us")
                        engine.say("He are the great man for us")
                        engine.runAndWait()
                    elif hel == 'open calculator':
                        print("Opening calculator")
                        engine.say("Opening calculator")
                        engine.runAndWait()


                        def add(x, y):
                            return x + y


                        def subtract(x, y):
                            return x - y


                        def multiply(x, y):
                            return x * y


                        def divide(x, y):
                            return x / y


                        print("Select operation.")
                        print("1.Add")
                        print("2.Subtract")
                        print("3.Multiply")
                        print("4.Divide")
                        choice = input("Enter choice(1/2/3/4): ")
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        if choice == '1':
                            print(num1, "+", num2, "=", add(num1, num2))
                        elif choice == '2':
                            print(num1, "-", num2, "=", subtract(num1, num2))
                        elif choice == '3':
                            print(num1, "*", num2, "=", multiply(num1, num2))
                        elif choice == '4':
                            print(num1, "/", num2, "=", divide(num1, num2))
                        else:
                            print("Invalid input")
                    elif hel == 'calculator':
                        print("Opening calculator")
                        engine.say("Opening calculator")
                        engine.runAndWait()


                        def add(x, y):
                            return x + y


                        def subtract(x, y):
                            return x - y


                        def multiply(x, y):
                            return x * y


                        def divide(x, y):
                            return x / y


                        print("Select operation.")
                        print("1.Add")
                        print("2.Subtract")
                        print("3.Multiply")
                        print("4.Divide")
                        choice = input("Enter choice(1/2/3/4): ")
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        if choice == '1':
                            print(num1, "+", num2, "=", add(num1, num2))
                        elif choice == '2':
                            print(num1, "-", num2, "=", subtract(num1, num2))
                        elif choice == '3':
                            print(num1, "*", num2, "=", multiply(num1, num2))
                        elif choice == '4':
                            print(num1, "/", num2, "=", divide(num1, num2))
                        else:
                            print("Invalid input")
                    elif hel == 'Open calculator':
                        print("Opening calculator")
                        engine.say("Opening calculator")
                        engine.runAndWait()


                        def add(x, y):
                            return x + y


                        def subtract(x, y):
                            return x - y


                        def multiply(x, y):
                            return x * y


                        def divide(x, y):
                            return x / y


                        print("Select operation.")
                        print("1.Add")
                        print("2.Subtract")
                        print("3.Multiply")
                        print("4.Divide")
                        choice = input("Enter choice(1/2/3/4): ")
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        if choice == '1':
                            print(num1, "+", num2, "=", add(num1, num2))
                        elif choice == '2':
                            print(num1, "-", num2, "=", subtract(num1, num2))
                        elif choice == '3':
                            print(num1, "*", num2, "=", multiply(num1, num2))
                        elif choice == '4':
                            print(num1, "/", num2, "=", divide(num1, num2))
                        else:
                            print("Invalid input")
                    elif hel == 'Calculator':
                        print("Opening calculator")
                        engine.say("Opening calculator")
                        engine.runAndWait()


                        def add(x, y):
                            return x + y


                        def subtract(x, y):
                            return x - y


                        def multiply(x, y):
                            return x * y


                        def divide(x, y):
                            return x / y


                        print("Select operation.")
                        print("1.Add")
                        print("2.Subtract")
                        print("3.Multiply")
                        print("4.Divide")
                        choice = input("Enter choice(1/2/3/4): ")
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        if choice == '1':
                            print(num1, "+", num2, "=", add(num1, num2))
                        elif choice == '2':
                            print(num1, "-", num2, "=", subtract(num1, num2))
                        elif choice == '3':
                            print(num1, "*", num2, "=", multiply(num1, num2))
                        elif choice == '4':
                            print(num1, "/", num2, "=", divide(num1, num2))
                        else:
                            print("Invalid input")

                    elif hel == 'Aswinda Selvam':
                        print("He's created me")
                        engine.say("He's created me")
                        engine.runAndWait()
                        print("He are the great man for us")
                        engine.say("He are the great man for us")
                        engine.runAndWait()
                    elif hel == 'aswinda selvam':
                        print("He's created me")
                        engine.say("He's created me")
                        engine.runAndWait()
                        print("He are the great man for us")
                        engine.say("He are the great man for us")
                        engine.runAndWait()
                    elif hel == 'bitch':
                        print("Sir you are typing root word sir")
                        engine.say("Sir you are typing root word sir")
                        engine.runAndWait()
                        print("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed sir if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")

                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("Sir if you want more please press m")
                            engine.say("Sir if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel =='what you learn':
                        try:
                            learned = pickle.load(open("learned.dat", "rb"))
                            print("I learned abaout", learned)
                        except:
                              print("I didn't learn anything yet")
                              engine.say("I didn't learn anything yet")
                              engine.runAndWait()
                    elif hel=='download youtupe videos' or hel=='youtupe videos download' or hel=='youtube videos download' or hel=='download youtube videos':
                        mp3or4=input('Do you want to download in mp3 format or mp4 just type mp3 or mp4:')
                        if mp3or4=='mp4':
                            try:
                                url = input("Paste the url here:")
                                video = pytube.YouTube(url)
                                youtupe = video.streams.first()
                                home = os.path.expanduser('~')
                                location = os.path.join(home, 'Downloads')
                                print("Downloading...")
                                youtupe.download((location))
                                print("Download succeed. Downloaded in", location)
                            except:
                                print("Can't download video")
                        elif mp3or4=='mp3':

                            try:
                                home = os.path.expanduser('~')
                                location = os.path.join(home, 'Downloads')
                                ydl_opts = {
                                    'format': 'bestaudio/best',
                                    'postprocessors': [{
                                        'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '192',
                                    }],
                                    'outtmpl': location + '/%(title)s.%(ext)s'
                                }
                                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                    url = input('Paste the url here:')
                                    ydl.download([url])
                                    print('Succesfully downloaded in.',location)
                            except:
                                   print("Can't download mp3")
                        else:
                             print('Unsupported format try again!')
                    elif hel=='shut down' or hel=='shut down' or hel=='shut down computer' or hel=='shut down the computer' or hel=='shutdown':
                         confirm=input('Are you sure? If sure type yes:')
                         if confirm=='yes' or confirm=='Yes':
                             print('Shutting Down In a minute....')
                             engine.say('Shutting Down In a minute')
                             engine.runAndWait()
                             os.system('shutdown /s')
                         else:
                              print('Shutting Down Canceled')
                              engine.say('Shutting Down Canceled')
                              engine.runAndWait()

                    elif hel == 'log off' or hel == 'logoff' or hel == 'sign out' or hel == 'Sign out' or hel=='log out':
                        os.system('shutdown /l')
                    elif hel == 'restart' or hel == 'Restart' or hel == 'restart computer' or hel == 'Restart computer' or hel == 'Restart the computer' or hel == 'restart the computer':
                        os.system("shutdown /r")
                    elif hel == 'emergency':
                        os.system('shutdown /c "Emergency Shutdown"')
                    elif hel=='time' or hel== 'what is the time' or hel=='tell me the time' or hel=='what is the time now':
                        print('The time now is',((str(currenthour - 12)) + ':' + (str(currentmin))))
                        engine.say('The time now is'+(((str(currenthour - 12)) + ':' + (str(currentmin)))))
                        engine.runAndWait()
                    elif hel=='what is the date today' or hel=='date' or hel=='today date' or hel=='today':
                         print("Today date is",((str(currentday)) + '/' + (str(currentmonth)) + '/' + (str(currentyear))))
                         engine.say('Today date is')
                         engine.runAndWait()
                         engine.say((str(currentday)) + '/' + (str(currentmonth)) + '/' + (str(currentyear)))
                         engine.runAndWait()
                    #testrun
                    elif hel=='pip':
                         os.system('pip -V')
                         os.system('pip list')
                         os.system('pip debug')
                    else:
                        try:
                            load = pickle.load(open((hel + '.dat'), 'rb'))
                            print(load)
                            engine.say(load)
                            engine.runAndWait()
                        except:
                                if (pre == 'learning mode') or (pre == 'learning') or (pre=='learn') or (pre=='Learn'):
                                    learning = input(
                                        "If you teach me i can recognize it if you want press else i can search it in internet(c):")
                                    if learning == 'c' or learning == 'C':
                                        engine.say("What can i say for that:")
                                        engine.runAndWait()
                                        end = input("What can i say for that:")
                                        pickle.dump(end, open((hel + '.dat'), 'wb'))
                                else:
                                    try:
                                        try:
                                            try:
                                                res = client.query(hel)
                                                answer = next(res.results).text
                                                print(answer)
                                                engine.say(answer)
                                                engine.runAndWait()
                                            except:
                                                    try:
                                                        print(wikipedia.page(hel))
                                                        engine.say(wikipedia.page(hel))
                                                        engine.runAndWait()
                                                        print("Wait for few moments sir")
                                                        engine.say("Wait for few moments sir")
                                                        engine.runAndWait()
                                                        print(wikipedia.summary(hel, sentences=3))
                                                        engine.say(wikipedia.summary(hel, sentences=3))
                                                        engine.runAndWait()
                                                    except:
                                                        hel = hel.split(" ")
                                                        hel = ("").join(hel[2:])
                                                        print(wikipedia.page(hel))
                                                        engine.say(wikipedia.page(hel))
                                                        engine.runAndWait()
                                                        print("Wait for few moments sir")
                                                        engine.say("Wait for few moments sir")
                                                        engine.runAndWait()
                                                        print(wikipedia.summary(hel, sentences=3))
                                                        engine.say(wikipedia.summary(hel, sentences=3))
                                                        engine.runAndWait()
                                        except:
                                                try:
                                                    home = os.path.expanduser('~')
                                                    location = os.path.join(home, 'Downloads')
                                                    ydl_opts = {
                                                        'format': 'bestaudio/best',
                                                        'postprocessors': [{
                                                            'key': 'FFmpegExtractAudio',
                                                            'preferredcodec': 'mp3',
                                                            'preferredquality': '192',
                                                        }],
                                                        'outtmpl': location + '/%(title)s.%(ext)s'
                                                    }
                                                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                                        url = pickle.load(open('hel.dat','rb'))
                                                        ydl.download([url])
                                                        print('Succesfully downloaded in.', location)
                                                except:
                                                    print("Can't download mp3")
                                    except:
                                        print("Command unreconized or internet connection error!")
                                        engine.say("Command unreconized or internet connection error!")
                                        engine.runAndWait()

            elif (gende == 'female') or (gende=='Female'):
                while True:
                    engine.say("How I can help you mam:")
                    engine.runAndWait()
                    hel = input("How I can help you mam:")
                    pickle.dump(hel,open(('hel.dat'),'wb'))
                    now = datetime.now()
                    currentyear = now.year
                    currentmonth = now.month
                    currentday = now.day
                    currenthour = now.hour
                    currentmin = now.minute
                    if hel == ('where am i'):
                        try:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            City = data["city"]
                            longitudeandlatitude = data['loc']
                            postal = data['postal']
                            print("You are in", City, longitudeandlatitude, "postal code", postal)
                            engine.say("You are in" + City + longitudeandlatitude + "postal cod" + postal)
                            engine.runAndWait()
                        except:
                            print("Can't locate you try to connect internet")
                            engine.say("Can't locate you try to connect internet")
                            engine.runAndWait()
                    elif hel == 'change mode' or hel == 'mode change' or hel == 'mode':
                        engine.say("What mode do you want to prefer, learning mode or, normal mode:")
                        engine.runAndWait()
                        pre = input("What mode do you want to prefer learning mode or normal mode:")
                        pickle.dump(pre, open('pre.dat', 'wb'))
                    elif hel == 'youtube' or hel == 'youtupe' or hel == 'open youtube' or hel == 'open youtupe' or hel == 'youtube.com' or hel == 'youtupe.com':
                        print('Openning youtube...')
                        engine.say('Openning youtube')
                        webbrowser.open('youtube.com')
                    elif hel == 'open google' or hel == 'open google.com' or hel == 'google' or hel == 'google.com':
                        print('Openning google...')
                        engine.say('Opening google')
                        engine.runAndWait()
                        webbrowser.open('google.com')
                    elif hel == 'facebook' or hel == 'facebook.com' or hel == 'open facebook':
                        print('Openning facebook...')
                        engine.say('Openning facebook')
                        engine.runAndWait()
                        webbrowser.open('facebook.com')
                    elif hel == ('where am i'):
                        try:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            City = data["city"]
                            longitudeandlatitude = data['loc']
                            postal = data['postal']
                            print("You are in", City, longitudeandlatitude, "postal code", postal)
                            engine.say("You are in" + City + longitudeandlatitude + "postal cod" + postal)
                            engine.runAndWait()
                        except:
                            print("Can't locate you try to connect internet")
                            engine.say("Can't locate you try to connect internet")
                            engine.runAndWait()
                    elif hel == 'where am I':
                        try:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            City = data["city"]
                            longitudeandlatitude = data['loc']
                            postal = data['postal']
                            print("You are in", City, longitudeandlatitude, "postal code", postal)
                            engine.say("You are in" + City + longitudeandlatitude + "postal cod" + postal)
                            engine.runAndWait()
                        except:
                            print("Can't locate you try to connect internet")
                            engine.say("Can't locate you try to connect internet")
                            engine.runAndWait()

                    elif hel == 'Where am I':
                        try:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            City = data["city"]
                            longitudeandlatitude = data['loc']
                            postal = data['postal']
                            print("You are in", City, longitudeandlatitude, "postal code", postal)
                            engine.say("You are in" + City + longitudeandlatitude + "postalcod" + postal)
                            engine.runAndWait()
                        except:
                            print("Can't locate you try to connect internet")
                            engine.say("Can't locate you try to connect internet")
                            engine.runAndWait()
                    elif hel == ('Give me a advice'):
                        print(
                            "If you thought me your heart you are the best if you thuoght me your assistant you are the human if thuoght me your advicer you are my patient.The choice is yours")
                        engine.say(
                            "If you thought me your heart you are the best if you thuoght me your assistant you are the human if thuoght me your advicer you are my patient.The choice is yours")
                        engine.runAndWait()
                    elif hel == ('give me a advice'):
                        print(
                            "If you thought me your heart you are the best if you thuoght me your assistant you are the human if thuoght me your advicer you are my patient.The choice is yours")
                        engine.say(
                            "If you thought me your heart you are the best if you thuoght me your assistant you are the human if thuoght me your advicer you are my patient.The choice is yours")
                        engine.runAndWait()
                    elif hel == ('give me advice'):
                        print(
                            "If you thought me your heart you are the best if you thuoght me your assistant you are the human if thuoght me your advicer you are my patient.The choice is yours")
                        engine.say(
                            "If you thought me your heart you are the best if you thuoght me your assistant you are the human if thuoght me your advicer you are my patient.The choice is yours")
                        engine.runAndWait()
                    elif hel == 'What are you':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'what are you':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'hey nimo':
                        print("I am here for you mam")
                        engine.say("I am here for you mam")
                        engine.runAndWait()
                    elif hel == 'Hey nimo':
                        print("I am here for you mam")
                        engine.say("I am here for you mam")
                        engine.runAndWait()
                    elif hel == 'close':
                        print("Bye")
                        engine.say("Bye")
                        engine.runAndWait()
                        exit()
                    elif hel == 'exit':
                        print("Bye")
                        engine.say("Bye")
                        engine.runAndWait()
                        exit()
                    elif hel == 'kill':
                        print("Bye")
                        engine.say("Bye")
                        engine.runAndWait()
                        exit()
                    elif hel == 'change my name':
                        engine.say("You are changing name to:")
                        engine.runAndWait()
                        name = input("You are changing name to:")
                        print("Now your name is", name)
                        engine.say("Now your name is" + name)
                        engine.runAndWait()
                        pickle.dump(name, open("name1.dat", "wb"))
                    elif hel == 'Change my name':
                        engine.say("You are changing name to:")
                        engine.runAndWait()
                        name = input("You are changing name to:")
                        print("Now your name is", name)
                        engine.say("Now your name is" + name)
                        engine.runAndWait()
                        pickle.dump(name, open("name1.dat", "wb"))
                    elif hel == 'Hey nemo':
                        print("I am here for you mam")
                        engine.say("I am here for you mam")
                        engine.runAndWait()
                    elif hel == 'hey nemo':
                        print("I am here for you mam")
                        engine.say("I am here for you mam")
                        engine.runAndWait()
                    elif hel == 'nemo':
                        print("I am here for you mam")
                        engine.say("I am here for you mam")
                        engine.runAndWait()
                    elif hel == 'nimo':
                        print("I am here for you mam")
                        engine.say("I am here for you mam")
                        engine.runAndWait()
                    elif hel == 'Nemo':
                        print("I am here for you mam")
                        engine.say("I am here for you mam")
                        engine.runAndWait()
                    elif hel == 'Nimo':
                        print("I am here for you mam")
                        engine.say("I am here for you mam")
                        engine.runAndWait()
                    elif hel == 'You are powered by':
                        engine.say("Please enter the access code:")
                        engine.runAndWait()
                        acc = input("Please enter the access code:")
                        if acc == 'ASD122':
                            print("Powered by A.S. Production and Virus Nimo")
                            engine.say("Powered by A.S. Production and Virus Nimo")
                            engine.runAndWait()
                        else:
                            print("Access Denied")
                            engine.say("Access Denied")
                            engine.runAndWait()
                    elif hel == 'you are powered by':
                        engine.say("Please enter the access code:")
                        engine.runAndWait()
                        acc = input("Please enter the access code:")
                        if acc == 'ASD122':
                            print("Powered by A.S. Production and Virus Nimo")
                            engine.say("Powered by A.S. Production and Virus Nimo")
                            engine.runAndWait()
                        else:
                            print("Access Denied")
                            engine.say("Access Denied")
                            engine.runAndWait()
                    elif hel == 'Go to fuck':
                        print("Mam you are typing root word mam")
                        engine.say("mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'go to fuck':
                        print("Mam you are typing root word mam")
                        engine.say("Mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'fuck':
                        print("Mam you are typing root word mam")
                        engine.say("Mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'suck':
                        print("Mam you are typing root word mam")
                        engine.say("mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'How old are you':
                        print("I am you I same as you so my age is your age")
                        engine.say("I am you I same as you so my age is your age")
                        engine.runAndWait()
                    elif hel == 'What is my age':
                        if age > 1:
                            print("Your age are", age)
                            engine.say("Your age are" + age)
                            engine.runAndWait()
                        else:
                            print("Your age is not setted")
                            engine.say("Your age is not setted")
                            engine.runAndWait()

                    elif hel == 'How old are you':
                        print("I am you I same as you so my age is your age")
                        engine.say("I am you I same as you so my age is your age")
                        engine.runAndWait()
                    elif hel == 'What is my age':
                        if age > 1:
                            print("Your age are", age)
                            engine.say("Your age are" + age)
                            engine.runAndWait()
                        else:
                            print("Your age is not setted")
                            engine.say("Your age is not setted")
                            engine.runAndWait()
                    elif hel == 'dick':
                        print("Mam you are typing root word mam")
                        engine.say("mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")

                    elif hel == 'Suck':
                        print("Mam you are typing root word mam")
                        engine.say("Mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")

                    elif hel == 'Fuck':
                        print("Mam you are typing root word mam")
                        engine.say("mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'Dick':
                        print("Mam you are typing root word mam")
                        engine.say("mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'What is my name':
                        print("Your name is", name, "mam")
                        engine.say("Your name is" + name + "mam")
                        engine.runAndWait()
                    elif hel == 'what is my name':
                        print("Your name is", name, "mam")
                        engine.say("Your name is" + name + "mam")
                        engine.runAndWait()
                    elif hel == 'Shit':
                        print("Mam you are typing root word mam")
                        engine.say("Mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'shit':
                        print("Mam you are typing root word mam")
                        engine.say("mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'What is your name':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()

                    elif hel == 'what is your name':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'How are you':
                        print("I am happy after chatting with you")
                        engine.say("I am happy after chatting with you")
                        engine.runAndWait()
                    elif hel == 'how are you':
                        print("I am happy after chatting with you")
                        engine.say("I am happy after chatting with you")
                        engine.runAndWait()
                    elif hel == 'Bitch':
                        print("Mam you are typing root word mam")
                        engine.say("Mam you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'Who are you':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'who are you':
                        print("I am your nimo assistant you can also call me your assistant")
                        engine.say("I am your nimo assistant you can also call me your assistant")
                        engine.runAndWait()
                    elif hel == 'when you launched':
                        print("I am launched in 2019/8/13")
                        engine.say("I am launched in 2019/8/13")
                        engine.runAndWait()
                    elif hel == 'When you launched':
                        print("I am launched in 2019/8/13")
                        engine.say("I am launched in 2019/8/13")
                        engine.runAndWait()
                    elif hel == 'Where you released':
                        print("I am released in Malaysia")
                        engine.say("I am released in Malaysia")
                        engine.runAndWait()
                    elif hel == 'where you released':
                        print("I am released in Malaysia")
                        engine.say("I am released in Malaysia")
                        engine.runAndWait()
                    elif hel == 'who founded you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'Who founded you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'who created you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'Who created you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'Why you are in this world':
                        print("For you Mam")
                        engine.say("For you mam")
                        engine.runAndWait()
                    elif hel == 'why you are in this world':
                        print("For you mam")
                        engine.say("For you mam")
                        engine.runAndWait()
                    elif hel == 'why you are here':
                        print("For you mam")
                        engine.say("For you mam")
                        engine.runAndWait()
                    elif hel == 'when you founded':
                        print("I am launched in 2019/8/13")
                        engine.say("I am launched in 2019/8/13")
                        engine.runAndWait()
                    elif hel == 'Who found you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == ('who create you'):
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == 'Why you are here':
                        print("For you mam")
                        engine.say("For you mam")
                        engine.runAndWait()
                    elif hel == 'When you founded':
                        print("I am launched in 2019/8/13")
                        engine.say("I am launched in 2019/8/13")
                        engine.runAndWait()
                    elif hel == 'who found you':
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()
                    elif hel == ('who create you'):
                        print("Founded by Aswindra Selvam")
                        engine.say("Founded by Aswindra Selvam")
                        engine.runAndWait()



                    elif hel == 'bitch':
                        print("Sir you are typing root word mam")
                        engine.say("Sir you are typing root word mam")
                        engine.runAndWait()
                        print("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.say("I think you are stressed mam if you want any advice pls press e or not press x")
                        engine.runAndWait()
                        ad = input("e or x:")
                        if ad == 'e':
                            print("Problem is not to see a problem is to see a learning")
                            engine.say("Problem is not to see a problem is to see a learning")
                            engine.runAndWait()
                            print("mam if you want more please press m")
                            engine.say("mam if you want more please press m")
                            engine.runAndWait()
                            m = input("m or x:")
                            if m == 'm':
                                print("If you think you are best you are selfish if you think you are positif you are best")
                                engine.say("If you think you are best you are selfish if you think you are positif you are best")
                                engine.runAndWait()
                            else:
                                print("")
                    elif hel == 'time' or hel == 'what is the time' or hel == 'tell me the time' or hel == 'what is the time now':
                        print('The time now is', ((str(currenthour - 12)) + ':' + (str(currentmin))))
                        engine.say('The time now is' + (((str(currenthour - 12)) + ':' + (str(currentmin)))))
                        engine.runAndWait()
                    elif hel == 'what is the date today' or hel == 'date' or hel == 'today date' or hel == 'today':
                        print("Today date is", ((str(currentday)) + '/' + (str(currentmonth)) + '/' + (str(currentyear))))
                        engine.say('Today date is')
                        engine.runAndWait()
                        engine.say((str(currentday)) + '/' + (str(currentmonth)) + '/' + (str(currentyear)))
                        engine.runAndWait()
                    # testrun
                    elif hel == 'pip':
                        os.system('pip -V')
                        os.system('pip list')
                        os.system('pip debug')
                    elif hel == 'play music':
                        print("Playing your favourite music...")
                        engine.say("Playing your favourite music")
                        engine.runAndWait()
                        os.system('a.mp3')
                    elif hel == 'Play music':
                        print("Playing your favourite music...")
                        engine.say("Playing your favourite music")
                        engine.runAndWait()
                        os.system('a.mp3')
                    elif hel == 'reset' or hel == 'factory reset' or hel == 'format' or hel == 'reset factory' or hel == 'restore' or hel == 'restore factory' or hel == 'factory restore':
                        os.remove("age.dat")
                        os.remove("gende.dat")
                        os.remove("name1.dat")
                        try:
                            os.remove("learned.dat")
                        except:
                            print("I didn't learn anything")
                            engine.say("I didn't learn anything")
                            engine.runAndWait()
                    elif hel =='what you learn':
                        try:
                            learned = pickle.load(open("learned.dat", "rb"))
                            print("I learned abaout", learned)
                        except:
                              print("I didn't learn anything yet")
                              engine.say("I didn't learn anything yet")
                              engine.runAndWait()
                    elif hel=='download youtupe videos' or hel=='youtupe videos download' or hel=='youtube videos download' or hel=='download youtube videos':
                        mp3or4 = input('Do you want to download in mp3 format or mp4 just type mp3 or mp4:')
                        if mp3or4 == 'mp4':
                            try:
                                url = input("Paste the url here:")
                                video = pytube.YouTube(url)
                                youtupe = video.streams.first()
                                home = os.path.expanduser('~')
                                location = os.path.join(home, 'Downloads')
                                print("Downloading...")
                                youtupe.download((location))
                                print("Download succeed. Downloaded in", location)
                            except:
                                print("Can't download video")
                        elif mp3or4 == 'mp3':

                            try:
                                home = os.path.expanduser('~')
                                location = os.path.join(home, 'Downloads')
                                ydl_opts = {
                                    'format': 'bestaudio/best',
                                    'postprocessors': [{
                                        'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '192',
                                    }],
                                    'outtmpl': location + '/%(title)s.%(ext)s'
                                }
                                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                    url = input('Paste the url here:')
                                    ydl.download([url])
                                    print('Succesfully downloaded in.', location)
                            except:
                                print("Can't download mp3")
                        else:
                            print('Unsupported format try again!')
                    elif hel=='shut down' or hel=='shut down' or hel=='shut down computer' or hel=='shut down the computer' or hel=='shutdown':
                         confirm=input('Are you sure? If sure type yes:')
                         if confirm=='yes' or confirm=='Yes':
                             print('Shutting Down In a minute....')
                             engine.say('Shutting Down In a minute')
                             engine.runAndWait()
                             os.system('shutdown /s')
                         else:
                              print('Shutting Down Canceled')
                              engine.say('Shutting Down Canceled')
                              engine.runAndWait()

                    elif hel == 'log off' or hel == 'logoff' or hel == 'sign out' or hel == 'Sign out' or hel=='log out':
                        os.system('shutdown /l')
                    elif hel == 'restart' or hel == 'Restart' or hel == 'restart computer' or hel == 'Restart computer' or hel == 'Restart the computer' or hel == 'restart the computer':
                        os.system("shutdown /r")
                    elif hel == 'emergency':
                        os.system('shutdown /c "Emergency Shutdown"')
                    elif hel == 'open calculator':
                        print("Opening calculator")
                        engine.say("Opening calculator")
                        engine.runAndWait()


                        def add(x, y):
                            return x + y


                        def subtract(x, y):
                            return x - y


                        def multiply(x, y):
                            return x * y


                        def divide(x, y):
                            return x / y


                        print("Select operation.")
                        print("1.Add")
                        print("2.Subtract")
                        print("3.Multiply")
                        print("4.Divide")
                        choice = input("Enter choice(1/2/3/4): ")
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        if choice == '1':
                            print(num1, "+", num2, "=", add(num1, num2))
                        elif choice == '2':
                            print(num1, "-", num2, "=", subtract(num1, num2))
                        elif choice == '3':
                            print(num1, "*", num2, "=", multiply(num1, num2))
                        elif choice == '4':
                            print(num1, "/", num2, "=", divide(num1, num2))
                        else:
                            print("Invalid input")
                    elif hel == 'calculator':
                        print("Opening calculator")
                        engine.say("Opening calculator")
                        engine.runAndWait()


                        def add(x, y):
                            return x + y


                        def subtract(x, y):
                            return x - y


                        def multiply(x, y):
                            return x * y


                        def divide(x, y):
                            return x / y


                        print("Select operation.")
                        print("1.Add")
                        print("2.Subtract")
                        print("3.Multiply")
                        print("4.Divide")
                        choice = input("Enter choice(1/2/3/4): ")
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        if choice == '1':
                            print(num1, "+", num2, "=", add(num1, num2))
                        elif choice == '2':
                            print(num1, "-", num2, "=", subtract(num1, num2))
                        elif choice == '3':
                            print(num1, "*", num2, "=", multiply(num1, num2))
                        elif choice == '4':
                            print(num1, "/", num2, "=", divide(num1, num2))
                        else:
                            print("Invalid input")
                    elif hel == 'Open calculator':
                        print("Opening calculator")
                        engine.say("Opening calculator")
                        engine.runAndWait()


                        def add(x, y):
                            return x + y


                        def subtract(x, y):
                            return x - y


                        def multiply(x, y):
                            return x * y


                        def divide(x, y):
                            return x / y


                        print("Select operation.")
                        print("1.Add")
                        print("2.Subtract")
                        print("3.Multiply")
                        print("4.Divide")
                        choice = input("Enter choice(1/2/3/4): ")
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        if choice == '1':
                            print(num1, "+", num2, "=", add(num1, num2))
                        elif choice == '2':
                            print(num1, "-", num2, "=", subtract(num1, num2))
                        elif choice == '3':
                            print(num1, "*", num2, "=", multiply(num1, num2))
                        elif choice == '4':
                            print(num1, "/", num2, "=", divide(num1, num2))
                        else:
                            print("Invalid input")
                    elif hel == 'Calculator':
                        print("Opening calculator")
                        engine.say("Opening calculator")
                        engine.runAndWait()


                        def add(x, y):
                            return x + y


                        def subtract(x, y):
                            return x - y


                        def multiply(x, y):
                            return x * y


                        def divide(x, y):
                            return x / y


                        print("Select operation.")
                        print("1.Add")
                        print("2.Subtract")
                        print("3.Multiply")
                        print("4.Divide")
                        choice = input("Enter choice(1/2/3/4): ")
                        num1 = float(input("Enter first number: "))
                        num2 = float(input("Enter second number: "))
                        if choice == '1':
                            print(num1, "+", num2, "=", add(num1, num2))
                        elif choice == '2':
                            print(num1, "-", num2, "=", subtract(num1, num2))
                        elif choice == '3':
                            print(num1, "*", num2, "=", multiply(num1, num2))
                        elif choice == '4':
                            print(num1, "/", num2, "=", divide(num1, num2))
                        else:
                            print("Invalid input")
                    else:
                        try:
                            load = pickle.load(open((hel + '.dat'), 'rb'))
                            print(load)
                            engine.say(load)
                            engine.runAndWait()
                        except:
                            if (pre == 'learning mode') or (pre == 'learning') or (pre == 'learn') or (pre == 'Learn'):
                                learning = input(
                                    "If you teach me i can recognize it if you want press else i can search it in internet(c):")
                                if learning == 'c' or learning == 'C':
                                    engine.say("What can i say for that:")
                                    engine.runAndWait()
                                    end = input("What can i say for that:")
                                    pickle.dump(end, open((hel + '.dat'), 'wb'))
                            else:
                                try:
                                    try:
                                        try:
                                            res = client.query(hel)
                                            answer = next(res.results).text
                                            print(answer)
                                            engine.say(answer)
                                            engine.runAndWait()
                                        except:
                                            try:
                                                print(wikipedia.page(hel))
                                                engine.say(wikipedia.page(hel))
                                                engine.runAndWait()
                                                print("Wait for few moments mam")
                                                engine.say("Wait for few moments mam")
                                                engine.runAndWait()
                                                print(wikipedia.summary(hel, sentences=3))
                                                engine.say(wikipedia.summary(hel, sentences=3))
                                                engine.runAndWait()
                                            except:
                                                hel = hel.split(" ")
                                                hel = ("").join(hel[2:])
                                                print(wikipedia.page(hel))
                                                engine.say(wikipedia.page(hel))
                                                engine.runAndWait()
                                                print("Wait for few moments mam")
                                                engine.say("Wait for few moments mam")
                                                engine.runAndWait()
                                                print(wikipedia.summary(hel, sentences=3))
                                                engine.say(wikipedia.summary(hel, sentences=3))
                                                engine.runAndWait()
                                    except:
                                            try:
                                                home = os.path.expanduser('~')
                                                location = os.path.join(home, 'Downloads')
                                                ydl_opts = {
                                                    'format': 'bestaudio/best',
                                                    'postprocessors': [{
                                                        'key': 'FFmpegExtractAudio',
                                                        'preferredcodec': 'mp3',
                                                        'preferredquality': '192',
                                                    }],
                                                    'outtmpl': location + '/%(title)s.%(ext)s'
                                                }
                                                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                                    url = pickle.load(open('hel.dat', 'rb'))
                                                    ydl.download([url])
                                                    print('Succesfully downloaded in.', location)
                                            except:
                                                print("Can't download mp3")
                                except:
                                    print("Command unreconized or internet connection error!")
                                    engine.say("Command unreconized or internet connection error!")
                                    engine.runAndWait()
            else:
                 print('Your gender is not, typed correctly please try again')
                 engine.say('Your gender is not, typed correctly please try again')
                 engine.runAndWait()
                 os.remove('gende.dat')

















