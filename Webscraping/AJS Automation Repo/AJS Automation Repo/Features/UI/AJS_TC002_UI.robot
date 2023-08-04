*** Settings ***
Resource    AJS_TC002_UI_keywords.robot
Resource    AJS_TC002_UI_commonkeywords.robot

Documentation    To validate the login form
Library    SeleniumLibrary
Test Setup    Open the browser localHost url
Test Teardown    Close Browser Session   #it is executed at the end of Test cases ex. Close the browser

*** Test Cases ***
AJS user enter valid input
    [Documentation]    When AJS user enter valid job rol, valid job location, valid username and valid email id
    [Tags]    Happy path
    Given User enter job role and job location    ${Valid_Job_Role}    ${Valid_Job_Location}
    And Validate job role and job location
    And User enter valid username and email    ${Valid_uname}    ${Valid_email_Id}
    When User send jobs to valid email 
    Then Validate final screen

Validate Close Button
    [Documentation]    Validating  AJS user able to click on close button in pop up
    [Tags]    Happy path
    Given Click Close Button
    Then wait untill main page appears

AJS user enter Validate Job role Text Field with mandatory checks
    [Documentation]    When AJS user enter empty field job rol, valid job location
    [Tags]    Unhappy path and mandatory check
    Given User enter job role and job location    ${EMPTY}    ${Valid_Job_Location}
    When Wait untill it checks and display Error message for invalid job role
    Then Verify error message is correct for invalid job role


Validate Username Text Field with mandatory checks
    [Documentation]    When AJS user enter empty username and valid email id
    [Tags]    Unhappy path and mandatory check
    Given User enter username and email    ${EMPTY}    ${valid_Email_ID}       
    When wait untill it checks and display Error message for Username
    Then verify error message is correct for Username

Validate Email Address Text Field with mandatory checks
    [Documentation]    When AJS user enter valid username and empty email id
    [Tags]    Unhappy path and mandatory check
    Given User enter username and email   ${Valid_uname}    ${EMPTY}       
    When wait untill it checks and display Error message for EmailID
    Then verify error message is correct for EmailID

Validate Job Role Text Field with Special Characters
    [Documentation]    When AJS user enter Special Characters field job rol, valid job location
    [Tags]    Unhappy path and error validation
   Given User enter job role and job location    ${Invalid_Job_Role_Special_Character}     ${Valid_Job_Location}
   Then Validate Error message for invalid Job Role

Validate Job Role Text Field with numbers
    [Documentation]    When AJS user enter numbers field job rol, valid job location
    [Tags]    Unhappy path and error validation
   Given User enter job role and job location    ${Invalid_Job_Role_Numbers}    ${Valid_Job_Location}
   Then Validate Error message for invalid Job Role

Validate Job Role Text Field with numbers and Characters
    [Documentation]    When AJS user enter numbers and Characters in field job rol, valid job location
    [Tags]    Unhappy path and error validation
   Given User enter job role and job location    ${Invalid_Job_Role_Numbers_Characters}    ${Valid_Job_Location}
   Then Validate Error message for invalid Job Role

Validate Job Location Text Field with numbers
    [Documentation]    When AJS user enter valid field job rol and numbers job location
    [Tags]    Unhappy path and error validation
    Given User enter job role and job location    ${Valid_Job_Role}    ${Invalid_Job_Location_Numbers}
    Then Validate Error message for invalid job location 

Validate Job Location Text Field with Special Characters
    [Documentation]    When AJS user enter valid field job rol and Special Characters job location
    [Tags]    Unhappy path and error validation
    Given User enter job role and job location    ${Valid_Job_Role}    ${Invalid_Job_Location_Special_Character}
    Then Validate Error message for invalid job location 

Validate Job Location Text Field with numbers and Characters
    [Documentation]    When AJS user enter valid field job rol and numbers and Characters job location
    [Tags]    Unhappy path and error validation
    Given User enter job role and job location    ${Valid_Job_Role}    ${Invalid_Job_Role_Numbers_Characters} 
    Then Validate Error message for invalid job location 

Validate user name Text Field with Special Characters
    [Documentation]    When AJS user enter Special Characters username and valid email id
    [Tags]    Unhappy path and error validation
    Given User enter username and email    ${Invalid_Username_Special_Character}    ${valid_Email_ID}       
    Then wait untill it checks and display tooltip for Username

Validate email id Text Field with invalid email id
    [Documentation]    When AJS user enter valid username and invalid email id
    [Tags]    Unhappy path and error validation
    Given User enter username and email    ${Valid_uname}    ${Invalid_Email_ID}        
    When wait untill it checks and display Error message for invalid EmailID
    Then verify error message is correct for invalidEmailID

    