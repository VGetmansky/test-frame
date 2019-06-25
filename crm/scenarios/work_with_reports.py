import pytest
from crm.tests import reports_tests as tests
from crm.scenarios.login_scenario import TestLogInApp
from crm.scenarios import parse_pdf as parse
from crm.tests import quotest_tests, so_tests, po_tests, invoice_tests
import common_functions as additional

TestLogInApp()


@pytest.allure.testcase('Work With RFQ')
@pytest.mark.test
class TestWorkWithRFQList:
    # def test_open_quotes_tab(self, driver):
    #     with pytest.allure.step('Select quote'):
    #         tests.select_quote(driver)

    # def test_open_quotes_details(self, driver, url):
    #     with pytest.allure.step('Open quotes details'):
    #         tests.open_quote_details(driver, url)
    #
    # # ----- Quote BAI  -----
    #
    # def test_open_quote_to_set_ees(self, driver, url):
    #     with pytest.allure.step('Open quote'):
    #        quotest_tests.click_edit_quote(driver, url)
    #
    # def test_fill_in_billing_address(self, driver):
    #     with pytest.allure.step('Fill billing address'):
    #         quotest_tests.fill_in_billing_address(driver)
    #
    # def test_fill_in_shipping_address(self, driver):
    #     with pytest.allure.step('Fill shipping address'):
    #         quotest_tests.fill_in_shipping_address(driver)
    #
    # def test_fill_in_billing_po_box(self, driver):
    #     with pytest.allure.step('Fill billing box'):
    #         quotest_tests.fill_in_billing_po_box(driver)
    #
    # def test_fill_in_billing_city(self, driver):
    #     with pytest.allure.step('Fill billing city'):
    #         quotest_tests.fill_in_billing_city(driver)
    #
    # def test_fill_in_billing_state(self, driver):
    #     with pytest.allure.step('Fill billing state'):
    #         quotest_tests.fill_in_billing_state(driver)
    #
    # def test_fill_in_billing_post_code(self, driver):
    #     with pytest.allure.step('Fill billing post code'):
    #         quotest_tests.fill_in_billing_post_code(driver)
    #
    # def test_fill_in_billing_post_country(self, driver):
    #     with pytest.allure.step('Fill billing country'):
    #         quotest_tests.fill_in_billing_country(driver)
    #
    # def test_fill_in_shipping_po_box(self, driver):
    #     with pytest.allure.step('Fill shipping box'):
    #         quotest_tests.fill_in_shipping_po_box(driver)
    #
    # def test_fill_in_shipping_city(self, driver):
    #     with pytest.allure.step('Fill shipping city'):
    #         quotest_tests.fill_in_shipping_city(driver)
    #
    # def test_fill_in_shipping_state(self, driver):
    #     with pytest.allure.step('Fill shipping state'):
    #         quotest_tests.fill_in_shipping_state(driver)
    #
    # def test_fill_in_shipping_post_code(self, driver):
    #     with pytest.allure.step('Fill shipping post code'):
    #         quotest_tests.fill_in_shipping_post_code(driver)
    #
    # def test_fill_in_shipping_post_country(self, driver):
    #     with pytest.allure.step('Fill shipping country'):
    #         quotest_tests.fill_in_shipping_country(driver)
    #
    # def test_set_territory_as_ees(self, driver):
    #     with pytest.allure.step('change territory'):
    #         quotest_tests.select_territory(driver, 'ees')
    #
    # def test_save_ees_territory(self, driver):
    #     with pytest.allure.step('Save ees territory quote'):
    #         quotest_tests.save_quote(driver)
    #
    # def test_expand_pdfmaker_tab(self, driver):
    #     with pytest.allure.step('Expand PDF maker'):
    #         tests.expand_pdfmaker(driver)
    #
    # def test_click_export(self, driver):
    #     with pytest.allure.step('export file'):
    #         tests.export_document(driver)
    #
    # def test_parse_document(self, driver):
    #     with pytest.allure.step('Parse PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_ees')
    #
    # # ----- Quote BANN-I  -----
    #
    # def test_open_bann_i_quote(self, driver, url):
    #     with pytest.allure.step('Open quote'):
    #        quotest_tests.click_edit_quote(driver, url)
    #
    # def test_edit_bann_i_territory(self, driver):
    #     with pytest.allure.step('change territory'):
    #         quotest_tests.select_territory(driver, 'bann-i')
    #
    # def test_save_bann_i_territory(self, driver):
    #     with pytest.allure.step('Save bann-i territory quote'):
    #         quotest_tests.save_quote(driver)
    #
    # def test_click_bann_i_export(self, driver):
    #     with pytest.allure.step('export file'):
    #         tests.export_document(driver)
    #
    # def test_parse_bann_i_document(self, driver):
    #     with pytest.allure.step('Parse PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_bann_i_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_bann-i')
    #
    # # ----- Quote BANN-D  -----
    #
    # def test_open_bann_d_quote(self, driver, url):
    #     with pytest.allure.step('Open quote'):
    #         quotest_tests.click_edit_quote(driver, url)
    #
    # def test_edit_bann_d_territory(self, driver):
    #     with pytest.allure.step('change territory'):
    #         quotest_tests.select_territory(driver, 'bann-d')
    #
    # def test_save_bann_d_territory(self, driver):
    #     with pytest.allure.step('Save bann-d territory quote'):
    #         quotest_tests.save_quote(driver)
    #
    # def test_click_bann_d_export(self, driver):
    #     with pytest.allure.step('export file'):
    #         tests.export_document(driver)
    #
    # def test_parse_bann_d_document(self, driver):
    #     with pytest.allure.step('Parse PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_bann_d_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_bann-d')
    #
    # def test_open_so_tab(self, driver):
    #     with pytest.allure.step('Select SO'):
    #         tests.select_so(driver)
    #
    # # ----- SO BAI SalesOrder -----
    #
    # def test_open_so_details(self, driver, url):
    #     with pytest.allure.step('Open so details'):
    #         tests.open_so_details(driver, url)
    #
    # def test_open_so_to_set_ees(self, driver, url):
    #     with pytest.allure.step('Open quote'):
    #         so_tests.click_edit_so(driver, url)
    #
    # def test_set_so_territory_as_ees(self, driver):
    #     with pytest.allure.step('change so territory'):
    #         so_tests.select_territory(driver, 'ees')
    #
    # def test_save_so_ees_territory(self, driver):
    #     with pytest.allure.step('Save SO ees territory quote'):
    #         so_tests.save_so(driver)
    #
    # def test_expand_so_pdfmaker_tab(self, driver):
    #     with pytest.allure.step('Expand SO PDF maker'):
    #         tests.expand_pdfmaker(driver)
    #
    # def test_select_so_ees_salesorder(self, driver):
    #     with pytest.allure.step('Select SO ees salesorder'):
    #         tests.select_report_type(driver, "so_bai_salesorder", 'ees')
    #
    # def test_click_so_ees_export(self, driver):
    #     with pytest.allure.step('export ees SO file'):
    #         tests.export_document(driver)
    #
    # def test_parse_so_ees_document(self, driver):
    #     with pytest.allure.step('Parse PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_so_ees_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_ees')
    #
    # # ----- SO BAI Proforma -----
    #
    # def test_select_so_ees_proforma(self, driver):
    #     with pytest.allure.step('Select SO ees proforma'):
    #         tests.select_report_type(driver, "so_bai_proforma", "ees")
    #
    # def test_click_so_ees_proforma_export(self, driver):
    #     with pytest.allure.step('export ees SO proforma file'):
    #         tests.export_document(driver)
    #
    # def test_parse_so_ees_proforma_document(self, driver):
    #     with pytest.allure.step('Parse ees proforma PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_so_ees_proforma_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_ees')
    #
    # # ----- SO BANN-I SalesOrder -----
    #
    # def test_select_so_bann_i_salesorder(self, driver):
    #     with pytest.allure.step('Select SO bann-i salesorder'):
    #         tests.select_report_type(driver, "so_bann_salesorder", "bann-i")
    #
    # def test_open_so_to_set_bann_i(self, driver, url):
    #     with pytest.allure.step('Open quote'):
    #         so_tests.click_edit_so(driver, url)
    #
    # def test_set_so_territory_as_bann_i(self, driver):
    #     with pytest.allure.step('change so territory'):
    #         so_tests.select_territory(driver, 'bann-i')
    #
    # def test_save_so_bann_i_territory(self, driver):
    #     with pytest.allure.step('Save SO ees territory quote'):
    #         so_tests.save_so(driver)
    #
    # def test_expand_so_bann_i_pdfmaker_tab(self, driver):
    #     with pytest.allure.step('Expand SO PDF maker'):
    #         tests.expand_pdfmaker(driver)
    #
    # def test_click_so_bann_i_export(self, driver):
    #     with pytest.allure.step('export ees SO file'):
    #         tests.export_document(driver)
    #
    # def test_parse_so_bann_i_document(self, driver):
    #     with pytest.allure.step('Parse PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_so_bann_i_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_ees')
    #
    # # ----- SO BANN-I Proforma -----
    #
    # def test_select_so_bann_i_proforma(self, driver):
    #     with pytest.allure.step('Select SO ees proforma'):
    #         tests.select_report_type(driver, "so_bann_proforma", "bann-i")
    #
    # def test_click_so_bann_i_proforma_export(self, driver):
    #     with pytest.allure.step('export ees SO proforma file'):
    #         tests.export_document(driver)
    #
    # def test_parse_so_bann_i_proforma_document(self, driver):
    #     with pytest.allure.step('Parse ees proforma PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_so_bann_i_proforma_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_ees')
    #
    # # ----- SO BANN-D SalesOrder -----
    #
    # def test_select_so_bann_d_salesorder(self, driver):
    #     with pytest.allure.step('Select SO bann-d salesorder'):
    #         tests.select_report_type(driver, "so_bann_salesorder", "bann-d")
    #
    # def test_open_so_to_set_bann_d(self, driver, url):
    #     with pytest.allure.step('Open quote'):
    #         so_tests.click_edit_so(driver, url)
    #
    # def test_set_so_territory_as_bann_d(self, driver):
    #     with pytest.allure.step('change so territory'):
    #         so_tests.select_territory(driver, 'bann-d')
    #
    # def test_save_so_bann_d_territory(self, driver):
    #     with pytest.allure.step('Save SO BANN-D territory quote'):
    #         so_tests.save_so(driver)
    #
    # def test_expand_so_bann_d_pdfmaker_tab(self, driver):
    #     with pytest.allure.step('Expand SO PDF maker'):
    #         tests.expand_pdfmaker(driver)
    #
    # def test_click_so_bann_d_export(self, driver):
    #     with pytest.allure.step('export BANN-D SO file'):
    #         tests.export_document(driver)
    #
    # def test_parse_so_bann_d_document(self, driver):
    #     with pytest.allure.step('Parse PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_so_bann_d_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_ees')
    #
    # # ----- SO BANN-D Proforma -----
    #
    # def test_select_so_bann_d_proforma(self, driver):
    #     with pytest.allure.step('Select SO ees proforma'):
    #         tests.select_report_type(driver, "so_bann_proforma", "bann-d")
    #
    # def test_click_so_bann_d_proforma_export(self, driver):
    #     with pytest.allure.step('export ees SO proforma file'):
    #         tests.export_document(driver)
    #
    # def test_parse_so_bann_d_proforma_document(self, driver):
    #     with pytest.allure.step('Parse ees proforma PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_so_bann_d_proforma_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_ees')
    #
    # # ----- PO BAI PurchaseOrder -----
    #
    # def test_open_po_tab(self, driver):
    #     with pytest.allure.step('Select PO'):
    #         tests.select_po(driver)
    #
    # def test_open_po_details(self, driver, url):
    #     with pytest.allure.step('Open PO details'):
    #         tests.open_po_details(driver, url)
    #
    # def test_open_po_to_set_ees(self, driver, url):
    #     with pytest.allure.step('Open quote'):
    #         po_tests.click_edit_po(driver, url)
    #
    # def test_set_po_territory_as_ees(self, driver):
    #     with pytest.allure.step('change so territory'):
    #         po_tests.select_territory(driver, 'ees')
    #
    # #
    #
    # def test_save_ees_po_territory(self, driver):
    #     with pytest.allure.step('Save ees territory PO'):
    #         po_tests.save_po(driver)
    #
    # def test_expand_po_ees_pdfmaker_tab(self, driver):
    #     with pytest.allure.step('Expand PDF maker'):
    #         tests.expand_pdfmaker(driver)
    #
    # def test_clickpo_ees_export(self, driver):
    #     with pytest.allure.step('export file'):
    #         tests.export_document(driver)
    #
    # def test_parse_po_ees_document(self, driver):
    #     with pytest.allure.step('Parse PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_po_ees_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_ees')
    #
    # def test_open_po_to_set_ees(self, driver, url):
    #     with pytest.allure.step('Open quote'):
    #         po_tests.click_edit_po(driver, url)
    #
    # def test_set_po_territory_as_ees(self, driver):
    #     with pytest.allure.step('change so territory'):
    #         po_tests.select_territory(driver, 'ees')
    #
    # # bann-i
    #
    # def test_open_po_to_set_bann_i(self, driver, url):
    #     with pytest.allure.step('Open PO'):
    #         po_tests.click_edit_po(driver, url)
    #
    # def test_set_po_territory_as_bann_i(self, driver):
    #     with pytest.allure.step('change PO territory'):
    #         po_tests.select_territory(driver, 'bann-i')
    #
    # def test_save_bann_i_po_territory(self, driver):
    #     with pytest.allure.step('Save ees territory PO'):
    #         po_tests.save_po(driver)
    #
    # def test_expand_bann_i_po_pdfmaker_tab(self, driver):
    #     with pytest.allure.step('Expand PDF maker'):
    #         tests.expand_pdfmaker(driver)
    #
    # def test_click_bann_i_po_ees_export(self, driver):
    #     with pytest.allure.step('export file'):
    #         tests.export_document(driver)
    #
    # def test_parse_po_bann_i_document(self, driver):
    #     with pytest.allure.step('Parse PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_po_bann_i_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_ees')
    #
    # # bann-d
    #
    # def test_open_po_to_set_bann_d(self, driver, url):
    #     with pytest.allure.step('Open quote'):
    #         po_tests.click_edit_po(driver, url)
    #
    # def test_set_po_territory_as_bann_d(self, driver):
    #     with pytest.allure.step('change so territory'):
    #         po_tests.select_territory(driver, 'bann-d')
    #
    # def test_save_bann_d_po_territory(self, driver):
    #     with pytest.allure.step('Save ees territory PO'):
    #         po_tests.save_po(driver)
    #
    # def test_expand_bann_d_po_pdfmaker_tab(self, driver):
    #     with pytest.allure.step('Expand PDF maker'):
    #         tests.expand_pdfmaker(driver)
    #
    # def test_click_bann_d_po_ees_export(self, driver):
    #     with pytest.allure.step('export file'):
    #         tests.export_document(driver)
    #
    # def test_parse_po_bann_d_document(self, driver):
    #     with pytest.allure.step('Parse PDF'):
    #         parse.parse_pdf(tests.path, tests.pdf)
    #
    # def test_compare_po_bann_d_documents(self):
    #     with pytest.allure.step('compare documents'):
    #         parse.diff(tests.path, 'quote_ees')

    # Invoice

    def test_open_invoice_tab(self, driver):
        with pytest.allure.step('Select Invoices'):
            tests.select_invoice(driver)

    def test_open_invoice_ees_details(self, driver, url):
        with pytest.allure.step('Open invoice details'):
            tests.open_invoice_details(driver, url)

    def test_open_invoice_to_set_ees(self, driver, url):
        with pytest.allure.step('Open invoice'):
            invoice_tests.click_edit_invoice(driver, url)

    def test_set_invoice_territory_as_ees(self, driver):
        with pytest.allure.step('change Invoice territory'):
            invoice_tests.select_territory(driver, 'ees')

    def test_save_ees_invoice_territory(self, driver):
        with pytest.allure.step('Save ees territory invoice'):
            invoice_tests.click_save_button(driver)

    def test_expand_invoice_ees_pdfmaker_tab(self, driver):
        with pytest.allure.step('Expand PDF maker'):
            tests.expand_pdfmaker(driver)

    # -----     BAI Customs Invoice     -----

    def test_select_invoice_ees_customs_invoice(self, driver):
        with pytest.allure.step('Select EES Invoice Customs Invoice'):
            tests.select_report_type(driver, "i_bai_customs_invoice", "ees", "Invoice")

    def test_click_customs_invoice_ees_export(self, driver):
        with pytest.allure.step('export file'):
            tests.export_document(driver)

    def test_parse_customs_invoice_ees_document(self, driver):
        with pytest.allure.step('Parse PDF'):
            parse.parse_pdf(tests.path, tests.pdf)

    def test_compare_customs_invoice_ees_documents(self):
        with pytest.allure.step('compare documents'):
            parse.diff(tests.path, 'quote_ees')

    # -----     BAI Invoice     -----

    def test_select_invoice_ees_invoice(self, driver):
        with pytest.allure.step('Select EES Invoice Customs Invoice'):
            tests.select_report_type(driver, "i_bai_invoice", "ees", "Invoice")

    def test_click_invoice_ees_export(self, driver):
        with pytest.allure.step('export file'):
            tests.export_document(driver)

    def test_parse_invoice_ees_document(self, driver):
        with pytest.allure.step('Parse PDF'):
            parse.parse_pdf(tests.path, tests.pdf)

    def test_compare_invoice_ees_documents(self):
        with pytest.allure.step('compare documents'):
            parse.diff(tests.path, 'quote_ees')

    # -----     BAI Packing List     -----

    def test_select_invoice_ees_packing_list(self, driver):
        with pytest.allure.step('Select EES Invoice Customs Invoice'):
            tests.select_report_type(driver, "i_bai_packing_list", "ees", "Invoice")

    def test_click_packing_list_ees_export(self, driver):
        with pytest.allure.step('export file'):
            tests.export_document(driver)

    def test_parse_packing_list_ees_document(self, driver):
        with pytest.allure.step('Parse PDF'):
            parse.parse_pdf(tests.path, tests.pdf)

    def test_compare_packing_list_ees_documents(self):
        with pytest.allure.step('compare documents'):
            parse.diff(tests.path, 'quote_ees')

    # -----     BANN-I     -----

    def test_open_invoice_to_set_bann_i(self, driver, url):
        with pytest.allure.step('Open invoice'):
            invoice_tests.click_edit_invoice(driver, url)

    def test_set_invoice_territory_as_bann_i(self, driver):
        with pytest.allure.step('change Invoice territory'):
            invoice_tests.select_territory(driver, 'bann-i')

    def test_save_bann_i_invoice_territory(self, driver):
        with pytest.allure.step('Save bann-i territory invoice'):
            invoice_tests.click_save_button(driver)

    # -----     BANN-I Customs Invoice     -----

    def test_select_invoice_bann_i_customs_invoice(self, driver):
        with pytest.allure.step('Select BANN-I Invoice Customs Invoice'):
            tests.select_report_type(driver, "i_bann_customs_invoice", "bann-i", "Invoice")

    def test_click_customs_invoice_bann_i_export(self, driver):
        with pytest.allure.step('export file'):
            tests.export_document(driver)

    def test_parse_customs_invoice_bann_i_document(self, driver):
        with pytest.allure.step('Parse PDF'):
            parse.parse_pdf(tests.path, tests.pdf)

    def test_compare_customs_invoice_bann_i_documents(self):
        with pytest.allure.step('compare documents'):
            parse.diff(tests.path, 'quote_ees')

    # -----     BANN-I Invoice     -----

    def test_select_invoice_bann_i_invoice(self, driver):
        with pytest.allure.step('Select BANN-I Invoice Customs Invoice'):
            tests.select_report_type(driver, "i_bann_invoice", "bann-i", "Invoice")

    def test_click_invoice_bann_i_export(self, driver):
        with pytest.allure.step('export file'):
            tests.export_document(driver)

    def test_parse_invoice_bann_i_document(self, driver):
        with pytest.allure.step('Parse PDF'):
            parse.parse_pdf(tests.path, tests.pdf)

    def test_compare_invoice_bann_i_documents(self):
        with pytest.allure.step('compare documents'):
            parse.diff(tests.path, 'quote_ees')

    # -----     BANN-I Packing List     -----

    def test_select_invoice_bann_i_packing_list(self, driver):
        with pytest.allure.step('Select BANN-I Invoice Customs Invoice'):
            tests.select_report_type(driver, "i_bann_packing_list", "bann-i", "Invoice")

    def test_click_packing_list_bann_i_export(self, driver):
        with pytest.allure.step('export file'):
            tests.export_document(driver)

    def test_parse_packing_list_bann_i_document(self, driver):
        with pytest.allure.step('Parse PDF'):
            parse.parse_pdf(tests.path, tests.pdf)

    def test_compare_packing_list_bann_i_documents(self):
        with pytest.allure.step('compare documents'):
            parse.diff(tests.path, 'quote_ees')

    # -----     BANN-D     -----

    def test_open_invoice_to_set_bann_d(self, driver, url):
        with pytest.allure.step('Open invoice'):
            invoice_tests.click_edit_invoice(driver, url)

    def test_set_invoice_territory_as_bann_d(self, driver):
        with pytest.allure.step('change Invoice territory'):
            invoice_tests.select_territory(driver, 'bann-d')

    def test_save_bann_d_invoice_territory(self, driver):
        with pytest.allure.step('Save bann-d territory invoice'):
            invoice_tests.click_save_button(driver)

    # -----     BANN-D Customs Invoice     -----

    def test_select_invoice_bann_d_customs_invoice(self, driver):
        with pytest.allure.step('Select BANN-D Invoice Customs Invoice'):
            tests.select_report_type(driver, "i_bann_customs_invoice", "bann-d", "Invoice")

    def test_click_customs_invoice_bann_d_export(self, driver):
        with pytest.allure.step('export file'):
            tests.export_document(driver)

    def test_parse_customs_invoice_bann_d_document(self, driver):
        with pytest.allure.step('Parse PDF'):
            parse.parse_pdf(tests.path, tests.pdf)

    def test_compare_customs_invoice_bann_d_documents(self):
        with pytest.allure.step('compare documents'):
            parse.diff(tests.path, 'quote_ees')

        # -----     BANN-D Invoice     -----

    def test_select_invoice_bann_d_invoice(self, driver):
        with pytest.allure.step('Select BANN-D Invoice Customs Invoice'):
            tests.select_report_type(driver, "i_bann_invoice", "bann-d", "Invoice")

    def test_click_invoice_bann_d_export(self, driver):
        with pytest.allure.step('export file'):
            tests.export_document(driver)

    def test_parse_invoice_bann_d_document(self, driver):
        with pytest.allure.step('Parse PDF'):
            parse.parse_pdf(tests.path, tests.pdf)

    def test_compare_invoice_bann_d_documents(self):
        with pytest.allure.step('compare documents'):
            parse.diff(tests.path, 'quote_ees')

        # -----     BAI Packing List     -----

    def test_select_invoice_bann_d_packing_list(self, driver):
        with pytest.allure.step('Select BANN-D Invoice Customs Invoice'):
            tests.select_report_type(driver, "i_bann_packing_list", "bann-d", "Invoice")

    def test_click_packing_list_bann_d_export(self, driver):
        with pytest.allure.step('export file'):
            tests.export_document(driver)

    def test_parse_packing_list_bann_d_document(self, driver):
        with pytest.allure.step('Parse PDF'):
            parse.parse_pdf(tests.path, tests.pdf)

    def test_compare_packing_list_bann_d_documents(self):
        with pytest.allure.step('compare documents'):
            parse.diff(tests.path, 'quote_ees')