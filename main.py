import pyttsx3
import PyPDF2

book = open("oop.pdf", 'rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()

# Print all available voices
voices = speaker.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

# Voice IDs pulled from engine.getProperty('voices')
# These will be system specific
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
fr_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"

# Use female English voice
speaker.setProperty('voice', en_voice_id)

#Read all pdf
for num in range(7,pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

# Uncomment this if no runAndWait above
# speaker.runAndWait()
