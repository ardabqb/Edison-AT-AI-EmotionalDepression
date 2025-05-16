from deepface import DeepFace #Analyze Face Emotion or Face Sentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #Sentiment Depression Analyzer
import speech_recognition as sp_human #Speech real-time using Microphone
import pyaudio #Speech real-time using Microphone
import pyttsx3 #Audio or Sound of Edison
#from sentiment import SentimentAnalysis #Analyz diseas #Release V 2 Pro Edison Paid #ClosedSource
#import hippocrates #Questioner mental health #Release V 2 Pro Edison Paid #ClosedSource



print("----------------------------------------------------\n")

programname= "Edison AT"
version= "Beta Version 1.0.0"
devdate= "Developed date: 31 January 2022"
devby= "Developed by Ananda Rauf Maududi"
print(programname)
print(version)
print(devdate)
print(devby)

print("----------------------------------------------------\n")

class SoundEdison():
    def soundedison():
        engine = pyttsx3.init()
        engine.say("Hello")
        engine.say("Im Edison")
        engine.say("Your Depression Assistant")
        engine.say("Can i help you?")
        engine.runAndWait()

        spech_human_on = sp_human.Recognizer()

        with sp_human.Microphone() as human_say:
            print('Waiting Microphone On.....')
            spech_human_on.adjust_for_ambient_noise(human_say,duration=1)
            print('Edison listening.....')
            edison_listen = spech_human_on.listen(human_say)
            print('Edison listening.....')

            try:
                print("Edison has been listen")
                text_edison = spech_human_on.recognize_google(edison_listen,language='en-US')
                print('Edison listen:{}'.format(text_edison))
            except Exception as ex:
                print(ex)
                print("Im so sorry")
                print("I can not hear")
                print("Please typing")

                #engine = pyttsx3.init()
                #engine.say("Im so sorry")
                #engine.say("I can not hear")
                #engine.say("Please try again")
                

        
        human_typing= input("Human answer is:")
        
        
        if text_edison or human_typing=='yes':
            engine.say("What is your problem?")
            
            print("Can you change gender?")
            engine.say("Sure")
            engine.say("I can")
            engine.say("Please Choose Gender")
            engine.say("If Male typing number one")
            engine.say("If Female typing number zero")
            engine.say("Im waiting you for choose")
            engine.runAndWait()

        elif text_edison or human_typing=='no':
            engine = pyttsx3.init()
            engine.say("Okay")
            engine.say("No problem")
            engine.say("I will learn to understand you next time")
            engine.say("Thanks for using")
            engine.say("Nice to meet you")
            engine.say("Have a good day")
            engine.say("Good bye")
            engine.runAndWait()

        else:
            exit()


SoundEdison.soundedison()

cho_gender=int(input("Talk Edison or Exit? T(0(Female) and 1(Male)) E(2-9):"))

if cho_gender==0:
    engine = pyttsx3.init()
    gender_ed = engine.getProperty('voices')
    engine.setProperty('voice',gender_ed[cho_gender].id)
    engine.say("Hello")
    engine.say("Im Edison")
    engine("Your Depression Assistant")
    engine.say("What is your problem?")
    print("Please check my status voice mental health")
    engine.say("Okay")
    engine.say("Please wait")
    engine.runAndWait()




elif cho_gender==1:
    engine = pyttsx3.init()
    gender_ed = engine.getProperty('voices')
    engine.setProperty('voice',gender_ed[1].id)
    engine.say("Hello")
    engine.say("Im Edison")
    engine.say("Your Depression Assistant")
    engine.say("What is your problem?")
    print("Please check my status voice mental health")
    engine.say("Okay")
    engine.say("Please wait")
    engine.runAndWait()

else:
    exit()

       



#class FaceAn():
    #def facean(self):
        #database is folder data model face emotion
        #an_emot = DeepFace.stream("database", model_name='DeepFace') #Analyze Emotion from face with using library DeepFace
        #print(an_emot)

#FaceAn.facean()

class SpeechAn():
    def speechan():
        #Initiliaze Recognizer real-time with using Microphone PC
        sp_recog_on = sp_human.Recognizer()

        with sp_human.Microphone() as human_source:
            print('Waiting Microphone On.....')
            sp_recog_on.adjust_for_ambient_noise(human_source,duration=1)
            print('Edison listening.....')
            ed_listen = sp_recog_on.listen(human_source)
            print('Edison listening.....')

            try:
                print("Edison has been listen.....")
                text_ed = sp_recog_on.recognize_google(ed_listen,language='en-US')
                print('Edison listen:{}'.format(text_ed))
            except Exception as ex:
                print(ex)
                print("Im so sorry")
                print("I can not hear your problem")
                print("Please try again")

            depres_human = [str(text_ed)]
            an_dep = SentimentIntensityAnalyzer()

            for i in depres_human():

                dep_result = an_dep.polarity_scores(i)
                print(dep_result)


SpeechAn.speechan()
                
            
            
        
        









