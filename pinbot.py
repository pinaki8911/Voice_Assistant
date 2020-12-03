import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
import pyowm
import os
import calendar
import smtplib
from pygame import mixer
import speech_recognition as sr

genie="Your wish is my command human!"

mus_path=''
music_dir = 'E:/music'
songs = os.listdir(music_dir)
song_number=0

pc="PASSWORD"

now = datetime.datetime.now()
curr_day=now.day
curr_month=now.month
curr_year=now.year


engine = pyttsx3.init()
vlist = engine.getProperty('voices')
engine.setProperty('voice', vlist[0].id)
volume = engine.getProperty('volume')
#engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 25)


greetings = [ 'hey','hello','hi','heya','Hey', 'Hello', 'Hi','Heya']
question = ['how are you', 'how are you doing']
responses = ["I'm fine human","I'm doing great human!","I am good human!","I'm exactly the way you want me to be human!","I'm awesome my human!","I'm good human! You take very good care of me"]
var1 = ['who made you', 'who created you']
var2 = ['I have been created by Pinaki.','Mr. Pinaki built me']
var3 = ['what time is it', 'what is the time', 'time','tell me the time',"what's the time","the time"]
var4 = ['who are you', 'what is you name',"what's your name","introduce yourself"]
cmd2 = ['play music', 'play songs', 'play a song', 'open music player','change song','play song','song','music']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
mailcmds=['send mail','send email','write mail','write email']
webcmds=['search the web','search on web','open website','open a website','search a url','url','browser','internet']
jokes = ["An 8 year old girl went to her dad, who was working in the yard. She asked him, 'Daddy, what is sex?'The father was surprised that she would ask such a question, but decides that if she is old enough to ask the question, the she is old enough to get a straight answer. He proceeded to tell her all about the birds and the bees'. When he finished explaining, the little girl was looking at him with her mouth hanging open. The father asked her, 'Why did you ask this question? 'The little girl replied, Mom told me to tell you that dinner will be ready in just a couple of secs.","What kind of pig can you ignore at a party? A wild bore.","Is it true that cannibals don't eat clowns because they taste funny?"
'Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live. Patient: What do you mean, 10?, 10 what? Months? Weeks?!", Doctor: Nine.','What did the fish say when he swam into a wall?: Dam','What do you call a can opener that doesn’t work?: A cant opener','What do you call a fish with no eyes?: A fsh','Did you hear about the Italian chef who died?: He pasta-way','What’s the best thing about Switzerland?: I don’t know, but the flag is a big plus.','I invented a new word!: Plagiarism','Did you hear about the claustrophobic astronaut?: He just needed a little space']
websites = ['open youtube','open google','open facebook','open quora','open hackerrank','open codeforces','open instagram','open codechef','open spoj','open udemy','open pramp']
muscmds=['stop music','end song', 'stop the music','stop']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing','bye']
cmd9 = ['thank you','thanks']
repfr9 = ["You're welcome human!", 'Glad i could help you',"Please don't mention it human!","It is my sole duty to serve you human! Please don't thank me."]
calcmds=["calendar","show calendar","view calendar","open calendar"]

day_code={0:'Mon',1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}
month_code={1:'JAN',2:"FEB",3:"MAR",4:"APR",5:"MAY",6:"JUN",7:"JUL",8:"AUG",9:"SEP",10:"OCT",11:"NOV",12:"DEC"}

def speak(words):
    engine.say(words)
    engine.runAndWait()
    
def printSpeak(words):
    print(words)
    speak(words)

def sendEmail(to, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_EMAIL','PASSWORD')
    server.sendmail('YOUR_EMAIL', to, body)
    server.close()

def mail(rec_add):
    try:
        speak("Do You want me to type the mail for you?")
        reply=hear()
        if 'no' in reply:
            speak("Please Compose the body of the mail human!")
            print("Body: ",end='')
            body=input()
        else:
            speak("Kindly tell me what I should type!")
            body = hear()
        speak("Is the mail body up to the mark?")
        ans=hear()
        if ans=='yes':
            sendEmail(rec_add,body)
            speak("Email has been sent!")
        else:
            speak("Sorry for the inconvienience! Let's try again human!")
            mail(rec_add)               
    except Exception as e:
        print(e)
        speak("Sorry i can't send the mail") 
    

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        printSpeak("Good Morning human!")

    elif hour>=12 and hour<17:
        printSpeak("Good Afternoon human!")   

    else:
        printSpeak("Good Evening human!")  
    printSpeak("pinbot at your service.")

def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something human:")
        audio = r.listen(source)
    try:
        print("Comprehending...")
        rec_google=r.recognize_google(audio,language='en-in')
        int_text=rec_google.lower()
        print("humansays: " + rec_google)
    except sr.UnknownValueError as e:
        print(e)
        print("Could not understand audio")
        printSpeak('Could you please say that again human?')
        return hear()
    return int_text    


def calPrint(curr_year,m):
    year_month_cal=calendar.Calendar().monthdayscalendar(curr_year,m)
    for w in range(7):
        if w!=6:
            print(day_code[w],end=" ")
        else:
            print(day_code[w])
    for i in year_month_cal:
        count=0
        for j in i:
            if j!=curr_day or m!=curr_month:
                if j==0:
                    print("   ",end=' ')
                elif j<=9:
                    print("  "+str(j),end=' ')
                else:
                    print(" "+str(j),end=' ')
            else:
                if j==0:
                    print(" <",end='>')
                elif j<=9:
                    print(" <"+str(j),end='>')
                else:
                    print("<"+str(j),end='>')
                
        print()

greet()
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something human:")
        audio = r.listen(source)
    try:
        print("Comprehending...")
        rec_google=r.recognize_google(audio,language='en-in')
        int_text=rec_google.lower()
        print("human says: " + rec_google)
    except sr.UnknownValueError as e:
        print(e)
        print("Could not understand audio")
        printSpeak('Could you please say that again human?')
        continue

    if int_text in greetings:
        reply = random.choice(greetings)
        printSpeak(reply+" human!")


    elif int_text in question:
        reply = random.choice(responses)
        printSpeak(reply)
        
    elif int_text in var1:
        reply = random.choice(var2)
        printSpeak(reply)
        
    elif int_text in cmd9:
        reply=random.choice(repfr9)
        printSpeak(reply)
        
    elif int_text in cmd2:
        speak(genie)
        mixer.init()
        mixer.music.load(os.path.join(music_dir,random.choice(songs)))
        mixer.music.play()

    elif int_text in muscmds:
        speak(genie)
        mixer.init()
        mixer.music.stop()

    elif int_text in calcmds:
        speak(genie)
        print()
        print("           "+str(curr_year))
        for m in range(1,13):
            if m!=curr_month:
                print("            "+month_code[m])
            else:
                print("           <"+month_code[m]+">")
            calPrint(curr_year,m)
            print()
    elif int_text in mailcmds:
        speak("Please type the receiver's email address:")
        print("To: ",end='')
        rec_add=input()
        mail(rec_add)
        
    elif int_text in var4:
        printSpeak('I am pinbot')
        
    elif int_text in websites:
        speak(genie)
        webbrowser.open('www.'+int_text[5:]+'.com')

    elif int_text in webcmds:
        speak(genie)
        printSpeak("Please say what you want to search for: ")
        resp=hear()
        webbrowser.open(resp)
        
    elif int_text in cmd6:
        printSpeak('Bye human! Take care!')
        exit()

    elif 'change' in int_text and 'voice' in int_text:
        speak(genie)
        to_change=engine.getProperty('voice')
        if to_change==vlist[0].id:
            engine.setProperty('voice',vlist[1].id)
        else:
            engine.setProperty('voice',vlist[0].id)
        speak("Voice Changed Successfully!")

    elif 'wikipedia' in int_text:
        speak(genie)
        search=int_text[:int_text.index('wikipedia')]+int_text[int_text.index('wikipedia')+9:]
        try:
            printSpeak(wikipedia.summary(search,sentences=6))
        except Exception as e:
            print(e)

    elif 'search' in int_text and 'google' in int_text:
        speak(genie)
        if 'on google' in int_text:
            int_text=int_text[:int_text.index('on google')]+int_text[int_text.index('on google')+9:]
        else:
            int_text=int_text[:int_text.index('google')]+int_text[int_text.index('google')+6:]
        if 'search' in int_text:
            int_text=int_text[:int_text.index('search')]+int_text[int_text.index('search')+6:]
        webbrowser.open('https://www.google.com/search?q='+int_text)
    elif '*' in int_text:
        printSpeak("Kindly don't use such language human!")
    elif int_text in cmd5:
        speak(genie)
        owm = pyowm.OWM('14b5a16d6cfbf8c7b106e728b56195c7')
        observation = owm.weather_at_place('Hyderabad, IN')
        #observation_list = owm.weather_around_coords(12.972442, 77.580643)
        w = observation.get_weather()
        
        
        print("Status: ",end='')
        print(w.get_detailed_status())
        print("Wind Speed(m/s): ",end='')
        print(w.get_wind()['speed'])
        print('Humidity: ',end='')
        print(w.get_humidity())
        print('Clouds(%): ',end='')
        print(w.get_clouds())
        print('Temperature(Celsius): ',end='')
        print(w.get_temperature('celsius')['temp'])
        
        speak("Status, "+w.get_detailed_status()+", Wind Speed, "+str(w.get_wind()['speed'])+" metres per second, "+"humidity, "+str(w.get_humidity())+', clouds, '+str(w.get_clouds())+' percent,'+', Temperature, '+str(w.get_temperature('celsius')['temp'])+" degree celsius,")

    elif r.recognize_google(audio) in var3:
        printSpeak(now.strftime("The time is %H:%M"))


    elif r.recognize_google(audio) in cmd3:
        speak(genie)
        reply = random.choice(jokes)
        printSpeak(reply)
