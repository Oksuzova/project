import pytest
from pytest_bdd import scenario
from steps.catalog_impl import *

@scenario('main.feature', 'Catalog should open successfully')
def test_catalog_opened_successfully():
    pass


@scenario('main.feature', 'Category block should present on catalog page')
def test_catalog_has_category():
    pass
