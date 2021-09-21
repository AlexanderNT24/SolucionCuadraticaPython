import win32com.client

class TextoaVoz:
    def __init__(self,palabras): 
        voz=win32com.client.Dispatch("SAPI.SpVoice")
        voz.Speak(palabras)
        