import pyttsx3, PyPDF2


reader = PyPDF2.PdfFileReader(open("translate.pdf", "rb"))
speaker = pyttsx3.init()

for page_num in range(reader.numPages):
    text = reader.getPage(0).extractText()  # need to fix getPage()
    clean_text = text.strip().replace(" ", "").replace("\n", " ")
    print(clean_text)

rate = speaker.getProperty("rate")
print(rate)
speaker.setProperty("rate", 120)

voices = speaker.getProperty("voices")
speaker.setProperty("voice", voices[1].id)

speaker.save_to_file(clean_text, "translated.mp3")
speaker.runAndWait()

speaker.stop()
