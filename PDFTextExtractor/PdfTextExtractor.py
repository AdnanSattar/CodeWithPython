import PyPDF2

def extract_text_from_pdf(pdf_path, output_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            extracted_text = ""
            
            for page in reader.pages:
                extracted_text += page.extract_text()
            
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)
        
        print(f"Text successfully extracted and saved to {output_path}")
    except FileNotFoundError:
        print("Error: PDF file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the PDF Text Extractor! 📄🔍")
    pdf_path = input("Enter the path to your PDF file: ").strip()
    output_path = input("Enter the path to save the extracted text: ").strip()
    
    extract_text_from_pdf(pdf_path, output_path)