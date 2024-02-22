from fun.ListenJs import Listen
from fun.Speak import speak,wishMe
#from fun.SpeakHotWord import speak
from fun.Filter import Filter,RunCode
from fun.Apps import OpenCloseApp
from fun.GetingWindows import get_current_window_title
from fun.SaveFile import create_file_with_index
from fun.ExecCode import ExecCode

#from Online.DataOnline import Online_Scraper
from Online.Chatg4f import GPT
from Online.Basic import ChromeCode, YoutubeCode
from Online.WhatsApp import whatsappmessage
from Mistral2 import Mistral7B
from Online.EmailSender import EmailSender
from Online.WebsiteInfo import WebsiteInfo

from mtranslate import translate
import pyperclip
import random
import pyautogui
from time import sleep

from Online.Chatg4f import messages as gms
from Mistral2 import messages as mms




KnowApps={"Google Chrome":ChromeCode,
          "YouTube":YoutubeCode}
GoodMsg= ["Command executed, sir.",
       "What's the next move, sir?",
       "Task completed, sir.",
       "What's on the agenda, sir?",
       "Mission accomplished, sir.",
       "Ready for the next challenge, sir.",
       "All set, sir.",
       "Awaiting further instructions, sir.",
       "Next step, sir?",
       "Task fulfilled, sir.",
       "What's the plan, sir?",
       "Ready and waiting, sir.",
       "What's the next objective, sir?",
       "Task completed successfully, sir.",
       "What's the next mission, sir?"]

sleep_mode = False
writting_mode = False

if __name__ == "__main__":
    wishMe()
    while True:        
        query = Listen().lower() 
        query = translate(query,"en","auto")
        Sq = query.split(" ")[0]
        #print(Sq)
        query = query.removeprefix("jarvis")

        CURRENT_APP = " "
        CURRENT_APP_NAME = " "
        SELECTED_NAME = " "
        try:
            CURRENT_APP = get_current_window_title()
            CURRENT_APP_NAME = CURRENT_APP.split(" - ")[-1]
            SELECTED_NAME = CURRENT_APP.split(" - ")[-2]
        except:
            CURRENT_APP = " "
            CURRENT_APP_NAME = " "
            SELECTED_NAME = " "
        if CURRENT_APP_NAME in KnowApps:
            Func_= KnowApps[CURRENT_APP_NAME]
            Output = Func_(query)
            if Output != False:
                print(Output)
                pyautogui.hotkey(*Output)
                continue
        if SELECTED_NAME in KnowApps:
            Func_= KnowApps[SELECTED_NAME]
            Output = Func_(query)
            if Output != False:
                print(Output)
                pyautogui.hotkey(*Output)
                continue
        
        if "quit the program" in query:
            speak("Shutting down sir...")
            break
        
        
        elif "send mail" in query or "send email" in query or "send an email" in query or "send a mail" in query:
            speak("Sir please provide me the reciver mail id")
            reciver = str(input("Reciver mail id:"))
            speak("What will be subject of mail.")
            sub = Listen()
            speak("Will i generate it by my self or you will provide some input")
            ans = Listen().lower()
            if "i will provide" in ans or "i will describe" in ans:
                mes = Listen()
            else :
                speak("Generating the Email...")
                mes = GPT(f"{sub}***Generate a plain message so i send it to email. Do not write any subject, reciver mail id or anything else. Just a plain email message body ***")
                mes = Filter(mes)
            speak("Sending Email...")
            EmailSender(reciver,sub,mes)
            if EmailSender:
                speak("Message sent successfully...")
            else:
                speak("Some error occur sir.")
        elif "scan this website" in query or "read this website" in query:
            
            speak("OK SIR I AM SCANING THE WEBSITE")
            url = "" 
            for i in range(5):
                pyautogui.press('f6')
                print("done scanning")
                sleep (1)
                pyautogui.hotkey("Ctrl","c")
                sleep(1)
                url= pyperclip.paste()
                print("pasing data")
                    
                if "htt" in url:
                    break
                else:
                    sleep (1)
            mms.append({"role":"system","content":f"{WebsiteInfo(url)}"})
            speak("ok sir i have scaned the website ask me anything about it.")
        
            
        elif "read my selection" in query or "read my selected text" in query :
            speak("Sure sir. Loading your selected text")
            pyautogui.hotkey("ctrl","c")
            sleep(1) 
            selected_text = pyperclip.paste()
            speak(selected_text)
        elif "copy data from my clipboard" in query or "copy my clipboard" in query or "read clipboard" in query or "copy data" in query or "copy selected text" in query:
            pyautogui.hotkey("ctrl","c")
            speak("ok just give me a second")
            jo = pyperclip.paste()
            gms.append({"role":"system","content":f"{jo}***I had copied this data from the clipboard.***"})
            mms.append({"role":"system","content":f"{jo}***I had copied this data from the clipboard.***"})
            speak("Data copied successfully sir...")
     
        elif "send message in whatsapp" in query or "send message" in query:
            for _ in range(1):
                speak("Whom will I send message sir... Please write the name...")
                name = str(input("Please write the name of Reciver: "))
                speak("What should I write sir...")
                sleep(1)
                msg = Listen()
                whatsappmessage(name,msg)
        elif "go to sleep" in query:
                speak("Ok sir. I am going to sleep but you can call me just say wake up and i will be there for you.")
                sleep_mode = True
                            
                while sleep_mode:
                    query = Listen().lower()
                    if "wake up" in query:
                        speak("I am awake now. How can i help you sir.")
                        sleep_mode = False
        elif "write here" in query or "start writing mode" in query:
            speak("Writting mode on but you can stop it by saying stop writing")
            writting_mode = True
            while writting_mode:
                wri = Listen()
                if "stop writing" in wri or "stop writing" in wri:
                    speak("Writting mode off")
                    writting_mode = False
                else:
                    print("working")
                    pyautogui.typewrite(wri)
                    print("Done")
        elif "scroll up" in query:
            pyautogui.scroll(20)
        elif "scroll down" in query:
            pyautogui.scroll(-20)
        elif "jarvis" == Sq:
            responce = GPT(f"{query}")
            code = RunCode(responce)
            if code!=None:
                if "from Online.Image_Generation import" in code or "import" not in code:
                    try:
                        exec(code)
                        create_file_with_index(query,code)
                        speak("Done Sir....")
                    except:
                        speak("Some error occur sir...")
                else:
                    Done=ExecCode(code)
                    create_file_with_index(query,code)
                    print(Done)
                    if Done:
                        speak(random.choice(GoodMsg))
                    else:
                        for i in range(3):
                            with open(r"error.log", "r") as f:
                                res = f.read()
                                if res != "":
                                    GPT(f"{res} /n" + "**fix this and write full code again. with different approach**")
                                    code = Filter(code)
                                    if code==None:
                                        break
                                    Done=ExecCode(code)
                                    if Done==True:
                                        break
                                else:
                                    break
                        speak("Sorry sir i Can't Do that")
            
            else:
                speak(responce)
        
        elif "open" in query or "close" in query:
            OpenCloseApp(query)
        else :
            gms.append({"role": "user", "content": query})
            reply=Mistral7B(query +" ***reply like tony stark jarvis in less words and don't write code***")
            speak(reply)

            """web=Online_Scraper(query)
            if web!=None:
                speak(web)
            else:
            """