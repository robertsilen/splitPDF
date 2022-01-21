from PyPDF2 import PdfFileWriter, PdfFileReader
pdf_fil =  'inputfile.pdf'
outputfolder = '/outputfolder/'

inputpdf = PdfFileReader(open(pdf_fil, "rb"),strict=False)

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(outputfolder+"outputfile-%s.pdf" % f'{i+1:02d}', "wb") as outputStream:
        output.write(outputStream)
