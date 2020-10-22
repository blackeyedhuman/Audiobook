import pyttsx3
import PyPDF2

#play the pdf
def audioBook(page_number):
    speaker = pyttsx3.init()
    #book_ext = find_ext(".", "pdf") 
    #print(book_ext)
    book = open("/home/venkatesh/Documents/GitHub/audiobook/PythonForInfromatics.pdf", 'rb') #pdf.pdf
    pdfReader = PyPDF2.PdfFileReader(book)
    lastPage = pdfReader.getNumPages()
    while(1):
        if lastPage <= page_number:
            break
        cache_pg = page_number
        page = pdfReader.getPage(page_number)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
        page_number = page_number + 1
    
    writeCache(page_number)
