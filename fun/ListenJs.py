#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Adding the chrome options to run chrome in background without opening it
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream") 
chrome_options.add_argument("--headless=new")

#Installing the nessasary driver and loading the chrome app
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
#/home/suraj2000/Desktop/Jarvis/Online/voice.html This is the lication of my file so you need to change according to your location
# For example if the new location is /home/suraj2000/Desktop/voice.html then change it like this
#website = r"file:///home/suraj2000/Desktop/voice.html" 
#this file:// is complusary the the location of your voice.html file i.e. /home/suraj2000/Desktop/Jarvis/Online/voice.html

#Going to website which is created by me in Java Script offcourse from Youtube Videos and chat gpt.
website = r"file:///home/suraj2000/Desktop/Jarvis/Online/voice.html"
driver.get(website)

def Listen(language="en-US",PRINT=True):
    if PRINT:
        print("LISTENING ... ")
    language_select = driver.find_element(by=By.ID, value='languageSelect') #selecting the language option box
    language_select.send_keys(language) #giving the language option in the box
    driver.find_element(by=By.ID, value='start').click() #clicking on start recording option
    while True:
        text=driver.find_element(by=By.ID, value='output').text #getting text from output
        if text != "":
            if PRINT:
                print("you said: " + text)
            driver.find_element(by=By.ID, value='end').click() #clicking on stop recording box
            break
    return text #returning output text if it is not empty

if __name__=="__main__":
    lang = "en-US"
# It is the default Language you can change it by jus changing lang
#For Hindi it is "hi-IN" and for Bengla it is "bn-IN"
    Listen(language=lang)  

   