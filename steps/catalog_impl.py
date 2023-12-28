from pytest_bdd import given, when, then
from pytest_bdd.parsers import cfparse
from playwright.sync_api import *


@when(cfparse('Open <{page_type}> page'))
def catalog_open_page(page: Page, page_type: str):
    pass


@then(cfparse('Check that <{page_type}> page opened successfully'))
def catalog_check_page_content(page: Page, page_type: str):
    pass


@then(cfparse('Check that <{block}> block present on <{page_type}> page'))
def catalog_check_page_block(page: Page, block: str, page_type: str):
    pass
