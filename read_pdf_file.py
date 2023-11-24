
import PyPDF2
import os
file_path =  "C://Users//Hdsadmin//Documents//CRA 1931 of 2009  Eng.pdf"
def read_pdf_file(file_path):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        # Iterate through each page in the PDF and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()          
    return print(text)



# p = read_pdf_file(file_path)

def prepare_data(folder_path):
    pdf_texts = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # file must be pdf
        if filename.lower().endswith(".pdf"):
            try:
                with open(file_path, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    text = ""
                    # Iterate through each page in the PDF and extract text
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        text += page.extract_text()
                    pdf_texts.append(text)
            except Exception as e:
                print(str(e))
    return pdf_texts
folder_path = "C://Users//Hdsadmin//Documents//02 may, Part 1//Civil Appeal 619 of 2023"
p = prepare_data(folder_path)
print(p[0])