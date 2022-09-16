Feature: New Account

  Scenario: Create new account
    Given user clicks on the new account button
    When user fills all fields
    And clicks on the submit button
    Then user sees account id and the same amount
