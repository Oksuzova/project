@Catalog
Feature: Catalog


  Scenario: Catalog should open successfully
    When Open <Main> page
    Then Check that <Main> page opened successfully

  Scenario: Category block should present on catalog page
    When Open <Main> page
    Then Check that <Category> block present on <Main> page
