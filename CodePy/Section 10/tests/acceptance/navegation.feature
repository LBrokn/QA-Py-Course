Feature: Test navigation between pages
  It can have a description
  with lines

  Scenario: Homepage can go to Blog
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am on the blog page

    Scenario: Blog can go to Homepage
    Given I am on the blogpage
    When I click on the "Go to home" link
    Then I am on the homepage