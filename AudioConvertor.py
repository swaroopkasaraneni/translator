import os
import uuid
from gtts import gTTS

def textToSpeech(text, language="en", slow=False):
    # Ensure the media directory exists
    media_folder = "media"
    if not os.path.exists(media_folder):
        os.makedirs(media_folder)

    audio_file = os.path.join(media_folder, f"{uuid.uuid4()}.mp3")
    
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save(audio_file)
  
    return audio_file
