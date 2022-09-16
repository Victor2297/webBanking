Feature: New Cutomer

  Scenario: Create_new_customer
    Given user clicks on the new customer button
    When fills all fields from opened page
    And clicks on the submit button
    Then user sees Registered Successfully message