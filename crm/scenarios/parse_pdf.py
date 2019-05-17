import crm.data.report_references as report

import sys

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

fp = open('/home/rc/Documents/PDF Report References/INV Packing List reference.pdf', 'rb')

parser = PDFParser(fp)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize('')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
laparams.char_margin = 1.0
laparams.word_margin = 1.0
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
extracted_text = ''

for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()
    text = open("Quote test reference.txt")
    text_file = open('/home/rc/Downloads/INV Packing List reference.txt', "w")

    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            extracted_text += lt_obj.get_text()
            print(extracted_text)
            # extracted_text >> '/home/rc/Downloads/Quote.txt'
text_file.write(extracted_text)

text_file.close()
file_one = 'Quote test reference.txt'
file_two = '/home/rc/Downloads/INV Packing List reference.txt'


def diff(file_one, file_two):
    with open(file_one) as text_one, open(file_two) as text_two:
        one = set(text_one.read().split('\n'))
        two = set(text_two.read().split('\n'))
    if len(one.difference(two)) > 3:  #one != two:
    # assert one == two
    # return one.difference(two)
       print(one.difference(two))
    else:
        print("Report is correct")
        return



diff(file_one, file_two)
# if __name__ == '__main__':
#     if len(sys.argv) > 2:
#         print ('\n'.join(diff(sys.argv[1], sys.argv[2]))
