from openai import OpenAI
from gtts import gTTS
import os
from playsound3 import playsound
import speech_recognition as sr
import asyncio

palabras = "recuerda que te llamas dedbot , solo quiero los mensajes limpios sin nada mas"


async def transcribe_audio_from_microphone():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio) # Using Google's Web Speech API
            print(f"You said: {text}")
            await Ia(text + palabras)
            return 0
        except sr.UnknownValueError:
            print("Could not understand audio")
            return 0
        except sr.RequestError as e:
            print(f"Could not request results from service; {e}")
            return 0



async def Ia(palabras):
    client = OpenAI()

    response = client.responses.create(
      model="gpt-4.1",
      input=palabras
    )
    print(response.output_text)

    language = 'es'

    tts = gTTS(text=response.output_text, lang=language, slow=False) # slow=True for slower speech

    filename = "output.mp3"
    tts.save(filename)


    playsound(filename)
    return 0

async def main():
     while True:
      await transcribe_audio_from_microphone()

asyncio.run(main())