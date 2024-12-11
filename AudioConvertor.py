from gtts import gTTS
import uuid

def textToSpeech(text, language,slow):
  tts = gTTS(text=text, lang=language, slow=slow)
  audio_file = str(uuid.uuid4())+".mp3"
  tts.save(audio_file)
  return audio_file

