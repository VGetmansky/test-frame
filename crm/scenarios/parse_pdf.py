import crm.data.report_references as report
import crm.tests.reports_tests as tests
import sys

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine


def parse_pdf(path, pdf):
    # fp = open('/home/rc/Documents/PDF Report References/INV Packing List reference.pdf', 'rb')
    fp = open(pdf, 'rb')
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
        # text = open("Quote test reference.txt")
        text_file = open(path + '/result.txt', "w")

        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()
                print(extracted_text)
                # extracted_text >> path + "result.txt"
    text_file.write(extracted_text)

    text_file.close()
    return text_file
    global file_one
    file_one = path + 'result.txt'
    global file_two
    file_two = "Quote test reference"  # '/home/rc/Downloads/INV Packing List reference.txt'


def diff(path):

    file_one = path + '/result.txt'

    file_two = "./Quote test reference.txt"  # '/home/rc/Downloads/INV Packing List reference.txt'
    with open(file_one) as text_one, open(file_two) as text_two:
        one = set(text_one.read().split('\n'))
        two = set(text_two.read().split('\n'))
        if len(one.difference(two)) > 5:  #one != two: #3 for account
        # assert one == two
        # return one.difference(two)
           print(one.difference(two))
        else:
            print("The report is correct")



#
# diff(file_one, file_two)
# parse_pdf('/home/rc/Documents/PDF Report References/INV Packing List reference.pdf', path, pdf)
# if __name__ == '__main__':
#     if len(sys.argv) > 2:
#         print ('\n'.join(diff(sys.argv[1], sys.argv[2]))