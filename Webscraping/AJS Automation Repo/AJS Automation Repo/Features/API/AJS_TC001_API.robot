*** Settings ***
Resource    AJS_TC001_API_keywords.robot
*** Test Cases ***
post request Test for Job Role and Location
    [Documentation]    This point User will enter Job role and job location
    Given Input header      
    When Create Sessions       
    Then Post response in csv and Validate responce    Test Automation    Espoo    /write_csv1   

post request Test for Username and email
    [Documentation]    This point User will enter name and email id
    Given Input header    
    When Create Sessions         
    Then Post response in csv and Validate responce    Shivani    shivani.sharma@etteplan.com    /write_csv2  

post request Test for python script to send email
    [Documentation]    This point User will start program and email will be trigger
    Given Input header    
    When Create Sessions         
    Then Post response in start program and Validate responce    /start_program   