
import os
import PyPDF2
import shutil
import json

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):  
            page = reader.pages[page_num]
            text += page.extract_text()
        return text.strip()

def main():
    # Path to the folder containing PDF files
    folder_path = 'path/to/your/pdf/folder'
    
     # Path to the output folder
    output_folder = 'path/to/output/folder'

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        

    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            # Construct full file paths
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(pdf_path)

            output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')
            with open(output_file_path, 'w') as text_file:   
                text_file.write(text)


    #  # Create a new text file with the same name as the PDF
    #         text_file_path = os.path.splitext(pdf_path)[0] + '.txt'
    #         with open(text_file_path, 'w') as text_file:
    #             text_file.write(text)
    
    
####### Saving the pdf file and their json file/output file in the same folder
    # Input and output folders
    
input_folder = r'C:\Users\Admin\AI_ML\ocr\myenv\testing_ocr'
output_folder = r'C:\Users\Admin\AI_ML\ocr\myenv\testing_ocr'

for pdf_file in os.listdir(input_folder):
    if pdf_file.endswith('.pdf'):
        # Create a folder with the same name as the PDF file
        folder_name = os.path.splitext(pdf_file)[0]
        folder_path = os.path.join(output_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Copy the original PDF file to the folder
        shutil.copy(os.path.join(input_folder, pdf_file), folder_path)

        # Convert PDF to images
        pdf_path = os.path.join(input_folder, pdf_file)
        
        
        folder_path = os.path.join(output_folder, os.path.splitext(pdf_file)[0])
        os.makedirs(folder_path, exist_ok=True)
        
        
        data_dict = {}
        json_output_path = os.path.join(folder_path, folder_name + '.json')
        with open(json_output_path, 'w') as f:
            json.dump(data_dict, f)



if __name__ == "__main__":
    main()

