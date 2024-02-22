#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:38:39 2024

@author: suraj2000
"""
import g4f
import nest_asyncio

nest_asyncio.apply()

messages = [
    {"role": "system", "content": "You the latest J.A.R.V.I.S. AI, designed by Suraj Shaw with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, random, mouse, keyboard, datetime, PyQt5, etc."},
    {"role": "system", "content": "You are operating on a Ubuntu 23.10 system"},
    {"role": "user", "content": "Open Google Chrome."},
    {"role": "assistant", "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
    {"role": "user", "content": "Open youtube and search Devanand Song"},
    {"role": "assistent", "content": "```python\nimport pywhatkit as kit\nkit.playonyt('Devanand Song')"},
    {"role": "system", "content": "Python includes built-in functions you can use. For instance:"},
    {"role": "system","content": "my currnt path to save file is this folder location /home/suraj2000/Desktop/Jarvis/Outputs"
     }, 
     {"role": "user", "content": "Jarvis generate a cute cat image using Python."},
    {"role": "assistant", "content": """```python
from Online.Image_Generation import Generate_Images,Show_Image
IMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
```"""},
    {"role": "user", "content": "Jarvis show me the next image"},
    {"role": "assistant", "content": """```python
IMGS_TO_SHOW.open(1)
```"""},
{"role": "system",
"content": "don't use input function ad subprocess in python code"},
{"role": "system", "content": "*always use default paths in python code*"}
]
      
def GPT(*args):
    global messages
    assert args!=()

    message=""
    for i in args:
        message+=i


    messages.append({"role": "user", "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.Bing,
        messages=messages,
        stream=True,
    )
    
    ms=""
    for message in response:
        ms+=str(message)
        print(message,end="",flush=True)
    print()
    messages.append({"role": "assistant", "content": ms})
    return ms

        

if __name__ == "__main__":
    GPT()

