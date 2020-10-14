import pyttsx3
import PyPDF2

book = open("file.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
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

# Voice IDs from the system
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
fr_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"

# Use female English voice
speaker.setProperty('voice', en_voice_id)

text = ""
# Read all pdf
for num in range(1, pages):
    page = pdfReader.getPage(1)
    text += page.extractText()
    # speaker.say(text)

speaker.save_to_file(text, 'file.mp3')
speaker.runAndWait()
