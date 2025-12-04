

@allure.label.epic:WebInterface
Feature: Login on practice.qabrains
  As a user
  I want to be able to login to practice.qabrains
  So that I can access protected areas


  @critical
  @allure.label.owner:JohnDoe
  @allure.link:https://dev.example.com/
  @allure.issue:UI-123
  @allure.tms:TMS-456

  @allure.label.story:Labels
  Scenario: Successful login with valid credentials
    Given the application is opened
    When I login with valid credentials
    Then I should see the dashboard or a logged-in indicator

  Scenario: Unsuccessful login with invalid credentials
    Given the application is opened
    When I login with invalid credentials
    Then I should see an error message
