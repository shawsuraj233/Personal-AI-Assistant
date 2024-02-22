
#pip install --upgrade BingImageCreator
from os import system , listdir 
from PIL import Image
C = "Ypu Coockie Of Bing website"
def Generate_Images(prompt:str):
    try:
        # Assuming C is a variable you've defined elsewhere
        system(f'python -m BingImageCreator --prompt "{prompt}" -U "{C}" --output-dir "/home/suraj2000/Desktop/Jarvis/Images"')
        # Change directory to access images
        list_of_images = listdir("/home/suraj2000/Desktop/Jarvis/Images")
        return list_of_images[-4:]
    except Exception as e:
        print("An error occurred:", e)
        return None

class Show_Image:
    def __init__(self, li: list) -> None:
        self.listd = li

    def open(self, no):
        if 0 <= no < 4:
            try:
                img = Image.open(f"/home/suraj2000/Desktop/Jarvis/Images/{self.listd[no]}")
                img.show()
            except Exception as e:
                print("An error occurred while opening the image:", e)
                self.open(no + 1)
        else:
            print("Index out of range")
