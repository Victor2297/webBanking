Feature: Login
  Background:
    Given user goes on the login page

  Scenario: Login_with_valid_data
    Given user fills username "mngr435545" field
    And user fills password "ugadAse" field
    When user clicks on the login button
    Then user sees the username "mngr435545" on the hello page

  Scenario Outline: Login_with_invalid_data
    Given user fills username <username> field
    And user fills password <password> field
    When user clicks on the login button
    Then user sees the alert pop up
    Examples:
      | username | password |
      |mngr435545|test      |
      |test      |ugadAse   |
      |test      |test      |