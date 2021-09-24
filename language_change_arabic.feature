Feature: Switch language
  As a user
  I should be able to change language I prefer

  Scenario: Change language to Arabic

    Given I am on the pl version of the Symptomate
    When I change language using dropdown menu on ar
    Then I am on the ar version of the Symptomate
