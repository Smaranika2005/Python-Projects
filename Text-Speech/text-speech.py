#from gtts import gTTS
#text = gTTS(input('Enter your text:'))
#file_name=input('Enter desired file name:')
#text.save(f'{file_name}.mp3')
from gtts import gTTS

text="I am Smaranika"
translate=gTTS(text)
save_file_name=input("Enter a File Name=")
speech_save=translate.save(f"{save_file_name}.mp3")