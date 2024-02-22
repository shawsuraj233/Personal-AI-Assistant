import subprocess
from Online.Chatg4f import GPT
from fun.Filter import RunCode

def ExecCode(code:str):

    with open(r"temp.py", "w") as f:
        f.write(code)
    
    subprocess.getoutput("python temp.py 2> error.log")

    with open(r"error.log", "r") as f:
        res = f.read()
        if res != "":
            return False
        else:
            return True
   

  