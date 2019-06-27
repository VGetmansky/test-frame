import crm.data.report_references as report
import crm.tests.reports_tests as tests
import sys

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine


def parse_pdf(path, pdf):
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
        # text = open("EES Quote test reference.txt")
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
    file_two = "Quote test reference"  # '/home/rc/Downloads/EES I Packing List reference.txt'


def diff(path, type):

    file_one = path + '/result.txt'
    if type == 'quote_ees':
        file_two = "./EES Quote test reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'quote_bann-i':
        file_two = "./BANN-I Quote test reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'quote_bann-d':
        file_two = "./BANN-D Quote test reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'

    elif type == 'so_salesorder_ees':
        file_two = "./EES SO Sales order reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'so_salesorder_bann_i':
        file_two = "./BANN-I SO Sales order reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'so_salesorder_bann_d':
        file_two = "./BANN-D SO Sales order reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'

    elif type == 'so_proforma_ees':
        file_two = "./EES SO Proforma reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'so_proforma_bann_i':
        file_two = "./BANN-I SO Proforma reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'so_proforma_bann_d':
        file_two = "./BANN-D SO Proforma reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'

    elif type == 'po_purchaseorder_ees':
        file_two = "./EES PO Purchase order reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'po_purchaseorder_bann_i':
        file_two = "./BANN-I PO Purchase order reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'po_purchaseorder_bann_d':
        file_two = "./BANN-D PO Purchase order reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'

    elif type == 'i_customsinvoice_ees':
        file_two = "./EES I Customs Invoice reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'i_customsinvoice_bann_i':
        file_two = "./BANN-I I Customs Invoice reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'i_customsinvoice_bann_d':
        file_two = "./BANN-D I Customs Invoice reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'

    elif type == 'i_invoice_ees':
        file_two = "./EES I Invoice reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'i_invoice_bann_i':
        file_two = "./BANN-I I Invoice reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'i_invoice_bann_d':
        file_two = "./BANN-D I Invoice reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'

    elif type == 'i_packinglist_ees':
        file_two = "./EES I Packing List reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'i_packinglist_bann_i':
        file_two = "./BANN-I I Packing List reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'
    elif type == 'i_packinglist_bann_d':
        file_two = "./BANN-D I Packing List reference.txt"  # '/home/rc/Downloads/EES I Packing List reference.txt'

    with open(file_one) as text_one, open(file_two) as text_two:
        one = set(text_one.read().split('\n'))
        two = set(text_two.read().split('\n'))
        if len(one.difference(two)) > 5:
            print(one.difference(two))
            assert len(one.difference(two)) <= 5
        else:
            print("The report is correct")



#
# diff(file_one, file_two)
# parse_pdf('/home/rc/Documents/PDF Report References/INV Packing List reference.pdf', path, pdf)
# if __name__ == '__main__':
#     if len(sys.argv) > 2:
#         print ('\n'.join(diff(sys.argv[1], sys.argv[2]))
