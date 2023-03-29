from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader

def seurce_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    # Beolvassuk a pdf fájlt.
    for page in range(pdf.numPages):
        # A pdf minden oldalához adj hozzá egy új fájlt.
        parser.addPage(pdf.numPages)
    # Titkosítja a pdf-et, amely lehetővé teszi a jelszavas védelmi funkciót
    parser.encrypt(password)
    #Megnyitja a pdf fájlt
    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
    print(f"encrypted_{file} Created...")

if __name__ == "main":
    file = "test.pdf"
    password = "Gorni1899"
    seurce_pdf(file, password)

