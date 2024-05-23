import PyPDF2
import pyttsx3

file = PyPDF2.PdfReader(open('Automate the Boring Stuff with Python.pdf', 'rb'))
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)

clean_txt = ''

for page_num in range(len(file.pages)):
    text = file.pages[page_num].extract_text()
    clean_txt += text.strip().replace('\n', '')

print(clean_txt)

speaker.save_to_file(clean_txt, 'automation.mp3')
speaker.runAndWait()
