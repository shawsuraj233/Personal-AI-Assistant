from huggingface_hub import InferenceClient
import random
from fun.SaveFile import create_file_with_index
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
# Replace YOUR_API_KEY_HERE with the obtained API key from Hugging Face
headers = {"Authorization": "Bearer Your-API-Key"}
messages = [
    {"role": "system", "content": "You the latest JARVIS. AI, designed by Suraj Shaw with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, random, mouse, keyboard, datetime, PyQt5, etc."},
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
# Function to format prompt
def format_prompt(message, custom_instructions=None):
    prompt = ""
    if custom_instructions:
        prompt += f"[INST] {custom_instructions} [/INST]"
    prompt += f"[INST] {message} [/INST]"
    return prompt

# Function to generate response based on user input
def Mistral7B(prompt, temperature=0.9, max_new_tokens=1024, top_p=0.95, repetition_penalty=1.0):
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=random.randint(0, 10**7),
    )
    custom_instructions=str(messages)
    formatted_prompt = format_prompt(prompt, custom_instructions)

    messages.append({"role": "user", "content": prompt})

    client = InferenceClient(API_URL, headers=headers)
    response = client.text_generation(formatted_prompt, **generate_kwargs)

    messages.append({"role": "assistant", "content": response})
    print(response,flush=True)
    return response

x  =  Mistral7B("Can you tell me about this error ***ALSA lib pcm_dsnoop.c:566:(snd_pcm_dsnoop_open) unable to open slave\nALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear\nALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe\nALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side\nALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\nALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\nALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\nALSA lib dlmisc.c:337:(snd_dlobj_cache_get0) Cannot open shared library libasound_module_pcm_a52.so (/home/suraj2000/anaconda3/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /lib/x86_64-linux-gnu/libjxl_threads.so.0.7))\nALSA lib dlmisc.c:337:(snd_dlobj_cache_get0) Cannot open shared library libasound_module_pcm_a52.so (/home/suraj2000/anaconda3/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /lib/x86_64-linux-gnu/libjxl_threads.so.0.7))\nALSA lib confmisc.c:160:(snd_config_get_card) Invalid field card\nALSA lib pcm_usb_stream.c:482:(_snd_pcm_usb_stream_open) Invalid card 'card'\nALSA lib confmisc.c:160:(snd_config_get_card) Invalid field card\nALSA lib pcm_usb_stream.c:482:(_snd_pcm_usb_stream_open) Invalid card 'card'\nALSA lib pcm_dsnoop.c:566:(snd_pcm_dsnoop_open) unable to open slave\nALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear\nALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe\nALSA lib pcm.c:2666:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side\nALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\nALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\nALSA lib pcm_route.c:877:(find_matching_chmap) Found no matching channel map\nALSA lib dlmisc.c:337:(snd_dlobj_cache_get0) Cannot open shared library libasound_module_pcm_a52.so (/home/suraj2000/anaconda3/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /lib/x86_64-linux-gnu/libjxl_threads.so.0.7))\nALSA lib dlmisc.c:337:(snd_dlobj_cache_get0) Cannot open shared library libasound_module_pcm_a52.so (/home/suraj2000/anaconda3/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /lib/x86_64-linux-gnu/libjxl_threads.so.0.7))\nALSA lib confmisc.c:160:(snd_config_get_card) Invalid field card\nALSA lib pcm_usb_stream.c:482:(_snd_pcm_usb_stream_open) Invalid card 'card'\nALSA lib confmisc.c:160:(snd_config_get_card) Invalid field card\nALSA lib pcm_usb_stream.c:482:(_snd_pcm_usb_stream_open) Invalid card 'card'")


create_file_with_index("speech to text",x)