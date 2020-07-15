import PyPDF2

Pdf_file = "Merged.pdf"

Watermark = "wtr.pdf"

input_file = open(Pdf_file, 'rb')
input_pdf = PyPDF2.PdfFileReader(input_file)

Watermark_file = open(Watermark, 'rb')
Watermark_pdf = PyPDF2.PdfFileReader(Watermark_file)

output = PyPDF2.PdfFileWriter()
for i in range(input_pdf.getNumPages()):
    page = input_pdf.getPage(i)
    page.mergePage(Watermark_pdf.getPage(0))
    output.addPage(page)
New_file = open('Watermark.Pdf', 'wb')
output.write(New_file)
