import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    # enter filename of output pdf here
    merger.write('enter_pdf_filename.pdf')

pdf_merger(inputs)