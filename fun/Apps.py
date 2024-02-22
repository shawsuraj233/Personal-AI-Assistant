import os
from fun.Speak import speak
Apps = [["vlc","/usr/bin/vlc"],["firefox","/snap/bin/firefox"],\
        ["code","/snap/bin/code"],["telegram","/snap/bin/telegram-desktop"],\
        ["file","/usr/bin/file"],["wps","/usr/bin/wps"],\
            ["libre office","/usr/bin/libreoffice"],["chrome","/opt/google/chrome/chrome"]]

def OpenCloseApp(query):                
    for app in Apps:
        if app[0] in query:
            if 'open' in query:
                try:
                    os.system(f'"{app[1]}" &')
                    speak(f"Opening {app[0]}")
                    
                except Exception as e:
                    speak(f"Error opening : {e}")
            else:
                pid = os.popen(f'pgrep {app[0]}').read()
                if pid:
                    try:
                        os.system(f'kill {pid}')
                        speak(f'Closing "{app[0]}"')
                    except Exception as e:
                        speak(f"Error closing: {e}")
                else:
                    speak(f'Process "{app[0]}" not found')
