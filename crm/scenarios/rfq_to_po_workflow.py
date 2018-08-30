import pytest
from crm.tests import rfq_to_po_tests as tests
from crm.scenarios.login_scenario import TestLogInApp
#import crm.scenarios.work_with_rfq as rfq

# import crm.scenarios.work_with_quotes as quotes

from crm.scenarios.work_with_rfq import TestWorkWithRFQList
from crm.scenarios.work_with_rfq import TestClickAddButton
from crm.scenarios.work_with_rfq import TestCreateRfq
from crm.scenarios.work_with_quotes import TestCreateQuote
from crm.scenarios.work_with_so import TestCreateSO
from crm.scenarios.work_with_po import TestCreatePO

# TestLogInApp()


# @pytest.mark.test
# def test_rfq_work():
#     tests.select_rfq_data()
#
#
# @pytest.mark.test
# def test_create_rfq():
#     TestWorkWithRFQList()
#     TestClickAddButton()
#     TestCreateRfq()
#
#
# @pytest.mark.test
# def test_quote_work():
#     tests.select_quote_data()
#
#
# @pytest.mark.test
# def test_click_add_quote():
#     tests.click_add_quote()
#
#
# @pytest.mark.test
# def test_create_quote():
#     TestCreateQuote()
#
#
# @pytest.mark.test
# def test_so_work():
#     tests.select_so_data()
#
#
# def test_click_add_so():
#     tests.click_add_so()
#
#
# TestCreateSO()
#
#
# @pytest.mark.test
# def test_po_work():
#     tests.select_po_data()
#
#
# def test_click_add_po():
#     tests.click_add_po()
#
#
# TestCreatePO()
