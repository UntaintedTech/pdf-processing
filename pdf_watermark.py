import PyPDF2

def pdf_watermarker():
    # pdf to be watermarked
    pdf = PyPDF2.PdfReader(open('enter_pdf_filename.pdf', 'rb'))
    # watermark to be stamped
    watermark = PyPDF2.PdfReader(open('enter_pdf_filename.pdf', 'rb'))
    writer = PyPDF2.PdfWriter()

    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        page.merge_page(watermark.pages[0])
        writer.add_page(page)

    # enter filename of output pdf here
    with open('enter_pdf_filename', 'wb') as file:
        writer.write(file)

pdf_watermarker()