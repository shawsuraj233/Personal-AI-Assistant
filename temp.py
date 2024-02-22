import tkinter as tk
import pyttsx3

# initialize TTS engine
engine = pyttsx3.init()

# create GUI window
window = tk.Tk()
window.title("Speech-to-Text Converter")

# create menu bar
menu_bar = tk.Menu(window)
menu_bar.add_command(label="English-India", command=lambda: convert_text("en-in"))
menu_bar.add_command(label="Hindi-India", command=lambda: convert_text("hi-in"))
menu_bar.add_command(label="Bengali-India", command=lambda: convert_text("bn-in"))
window.config(menu=menu_bar)

# create output label
output_label = tk.Label(window, text="Output:")
output_label.pack(pady=10)

# create output text box
output_text_box = tk.Text(window, height=10, width=30)
output_text_box.pack()

# define function to convert text
def convert_text(language):
    # set language code
    engine.say(language)
    
    # convert text to speech and save to file
    engine.runAndWait()
    with open("output.txt", "w") as f:
        f.write(output_text_box.get())

# start TTS engine
engine.say("Hello, world!")
engine.runAndWait()

# main event loop
window.mainloop()