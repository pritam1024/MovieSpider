import speech_recognition as sr
import re
import os

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Tell Me what to search!")
    audio = r.listen(source)

try:
    n=r.recognize_google(audio)
    print("You said :" + n)
    #os.system("speak \"searching for the key,"+n+"\"")
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    exit()
    #n="Google Speech Recognition could not understand audio"
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    exit()
    #n="Could not request results from Google Speech Recognition service; {0}".format(e)
#return n

p=re.compile(n,re.IGNORECASE)
f=open('files.txt','r')
i=0
print('\n')
for m in f:
    l=m
    l=l.strip('\n')
    name=l.split('/')[-1]
    name=name.replace('%20',' ')
    name=name.replace('%28','(')
    name=name.replace('%29',')')
    name=name.replace('mkv','')
    name=name.replace('.',' ')
    name=name.replace('_',' ')
    if re.search(p,name):
        print("-->"+name,'\n')
        print(l)
        print('------------------------------------------------------------------------------')
        print('\n')
        i=1
if i!=1:
    print('Could not find the movie with the name \"'+n+'\"')
f.close()
