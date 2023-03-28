import pyttsx3, PyPDF2


reader = PyPDF2.PdfFileReader(open("translate.pdf", "rb"))
speaker = pyttsx3.init()

for page_num in range(reader.numPages):
    text = reader.getPage(page_num).extractText()
    clean_text = text.strip().replace("\n", " ")
    print(clean_text)

speaker.save_to_file(clean_text, "translated.mp3")
speaker.runAndWait()

speaker.stop()
