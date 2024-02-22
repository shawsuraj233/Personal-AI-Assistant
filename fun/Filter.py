import re
#filter python code for gpt responce
def RunCode(txt):
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, txt, re.DOTALL)

    if matches:
        python_code = matches[0].strip()
        return python_code
    else:
        return None
def Filter(txt):
    pattern = r"```(.*?)```"
    matches = re.findall(pattern, txt, re.DOTALL)

    if matches:
        Output = matches[0].strip()
        return Output
    else:
        return None
