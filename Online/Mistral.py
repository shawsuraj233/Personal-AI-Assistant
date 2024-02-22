from gradio_client import Client
client = Client("https://osanseviero-miwstral-super-fast.hf.space/")

result = client.predict(
        open("/home/suraj2000/Desktop/Jarvis/setup.txt","r").read(),
        0.6,
        1024,
        0.9,
        1.1,
        api_name="/chat"
    )


def Mistral7B(user_input):
    result = client.predict(
        user_input,
        0.6,
        1024,
        0.9,
        1.1,
        api_name="/chat"
    )
    return result[0:-4]


Mistral7B("***I am giving you an html content analysis this and do something that it can ")