Feature: Guru Page
  Scenario: Verify hello message and url
    Given click guru logo
    Then see hello message "Guru99 is totally new kind of learning experience." and the url "https://www.guru99.com/"

  Scenario: Verify search from guru page
    Given click on guru logo
    When fill search field "Test"
    And click search button
    Then results window contains the "Test" text used in search