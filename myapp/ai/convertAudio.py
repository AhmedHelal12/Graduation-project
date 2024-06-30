from gtts import gTTS
import os
from django.core.files.base import ContentFile

def audioFun(text):
    # Initialize the gTTS object with the text and language
    tts = gTTS(text=text, lang='en')
    
    # Save the speech audio into a temporary file
    audio_file_path = "audio1.mp3"
    tts.save(audio_file_path)
    
    # Read the file content
    with open(audio_file_path, 'rb') as f:
        audio_content = f.read()
    
    # Clean up the temporary file
    os.remove(audio_file_path)
    
    return ContentFile(audio_content)
