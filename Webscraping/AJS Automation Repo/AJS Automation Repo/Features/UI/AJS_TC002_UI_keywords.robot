*** Settings ***
Library    SeleniumLibrary
Resource    AJS_TC002_UI_commonkeywords.robot

*** Variables ***
${URL}    http://127.0.0.1:5000
${BROWSER}    Chrome
${Valid_uname}    Arya
${Valid_email_Id}    arya.thamarakkulam@etteplan.com
${Valid_Job_Role}    test automation engineer
${Valid_Job_Location}    Espoo

${Error_Message_EmailID_Vaidity_Check}    xpath://p[text()='Please enter an email address']
${Error_Message}    xpath://p[text()='Please enter the Job role.']
${Error_Message_Username_Vaidity_Check}    xpath://p[text()='Please enter the Username'] 
${Error_Message_invalidEmailID_Vaidity_Check}    xpath://p[text()="Please enter an email address ending with '@etteplan.com'"]   



*** Keywords ***

User enter job role and job location
    [Arguments]    ${role}    ${loc}    
    [Documentation]    User need to enter job role and job location
    Fill the AJS form with keywords    ${role}    ${loc}
    Click Submit button
Validate job role and job location
    Confirmation page Should open up
    Click the "home" button
Validate Error message for invalid job role
    Wait untill it checks and display tooltip for invalid job role
    #Verify error message is correct for invalid job role

Validate Error message for invalid job location
    Wait untill it checks and display Error message for invalid job location 
    #Verify error message is correct for invalid job location    

User enter valid username and email

    [Arguments]    ${username}    ${email}        
    [Documentation]    User need to enter job role and job location
    Switch Window    NEW
    Set Focus To Element    xpath://button[@id="user"]
    Click Button    xpath://button[@id="user"]
    Sleep    5s 
    Input Text    xpath://input[@id="uname"]   ${username}    
    Input Text    xpath://input[@id="email"]   ${email} 
    Sleep    5s
    Click Button    xpath://button[@id="save"]
    Sleep    2s
User send jobs to valid email     
    Page Should Contain    CSV File Created 'contacts.csv' has been created successfully
    Click Button    xpath:/html/body/div/div[1]/button
    Switch Window    NEW
    Sleep    3s
    Execute Javascript    window.scrollTo(0, window.scrollY+50)
    Sleep    3s
    Click Button    xpath://button[text()='Send Jobs to Email']
    Wait Until Page Contains    Email sent to ${Valid_uname} successfully

User enter username and email
    [Arguments]    ${username}    ${email}        
    [Documentation]    User need to enter job role and job location
    Click the "Next" button
    Input keywords to Username and email fields    ${username}    ${email}
    Click the "Submit" button
User send jobs to email
    New confirmation page should open up
    Click the "home" button to get to the main page
    Click "Send Jobs to Email" button
Validate final screen
    Page Should Contain    successfully
 
Open the browser with AJS URL
    [Arguments]    ${URL}    ${BROWSER}
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
  
  
Fill the AJS form with keywords
    [arguments]    ${Valid_Job_Role}     ${Vaid_Location}
    Input Text    xpath://label[text()='Job Role*']/following::input   ${Valid_Job_Role}     
    Input Text    xpath://*[@id="loc"]     ${Vaid_Location}   
    Sleep    3s


Click Submit button
    Execute Javascript    window.scrollTo(0, window.scrollY+100)
    Click Button  id:job    
    Sleep    3s

Confirmation page Should open up
    Title Should Be    CSV File Created
    #Wait Until Element Is Visible    xpath:/html[1]/body[1]/div[1]/div[2]/h3[1]
    Sleep    3s

Click the "home" button    
    Click Button    xpath:/html/body/div/div[1]/button
    Sleep    5s
    
Click the "Next" button    
    #Switch Window    NEW
    Set Focus To Element    xpath://button[@id="user"]
    Click Button    xpath://button[@id="user"]
    Sleep    5s

Input keywords to Username and email fields
    [Arguments]    ${username}    ${email}  
    Input Text    xpath://input[@id="uname"]   ${username}    
    Input Text    xpath://input[@id="email"]   ${email} 
 
    Sleep    5s

Click the "Submit" button
    Click Button    xpath://button[@id="save"]
    Sleep    2s

New confirmation page should open up
    Page Should Contain    CSV File Created 'contacts.csv' has been created successfully

Click the "home" button to get to the main page
    Click Button    xpath:/html/body/div/div[1]/button
    #Switch Window    NEW
    Sleep    3s


 Click "Send Jobs to Email" button   
    Execute Javascript    window.scrollTo(0, window.scrollY+50)
    Click Button    xpath://button[text()='Send Jobs to Email']]
    Wait Until Page Contains    Email sent to ${Valid_uname} successfully    

Wait untill it checks and display Error message for invalid job role
    Wait Until Element Is Visible    xpath://p[text()='Please enter the Job role.']
    Page Should Contain Element    xpath://p[text()='Please enter the Job role.']
Verify error message is correct for invalid job role
    #result is local variable
     ${Result}=    Get Text    xpath://p[text()='Please enter the Job role.']
     Should Be Equal As Strings    Please enter the Job role.    ${Result}  



wait untill it checks and display Error message for Username
    Wait Until Element Is Visible    xpath://p[text()='Please enter the Username']
    Page Should Contain Element    xpath://p[text()='Please enter the Username']
      

verify error message is correct for Username
#result is local variable
     ${result}=     Get Text    xpath://p[text()='Please enter the Username']
     Should Be Equal    ${result}    Please enter the Username

wait untill it checks and display Error message for EmailID
    Wait Until Element Is Visible    ${Error_Message_EmailID_Vaidity_Check}
    Page Should Contain Element    ${Error_Message_EmailID_Vaidity_Check}
verify error message is correct for EmailID
     ${result}=     Get Text    ${Error_Message_EmailID_Vaidity_Check}
     Should Be Equal    ${result}    Please enter an email address 

Click Close Button
    Click Button    (//button[@class='btn btn-primary'])[2]
    Sleep    2s
    Click Button    //button[@class='btn btn-secondary']

wait untill main page appears
    Switch Window    MAIN
    Wait Until Page Contains    AJS - Automated Job Search  

      
Wait untill it checks and display Error message for invalid job location 
    Click Element    xpath://*[@id="job"]
    Sleep    3 seconds
    #${error_message}=    Get Text    css=#loc
    ${validation_message}=    Execute JavaScript    return document.querySelector('#loc').validationMessage
    Sleep    3 seconds
    Should Be Equal As Strings    ${validation_message}    Please enter valid Job Location
#Verify error message is correct for invalid job location 


Wait untill it checks and display tooltip for invalid job role
    Click Element    xpath://*[@id="job"]
    Sleep    3 seconds
    #${error_message}=    Get Text    css=#loc
    ${validation_message}=    Execute JavaScript    return document.querySelector('#role').validationMessage
    Sleep    3 seconds
    Should Be Equal As Strings    ${validation_message}    Please enter valid Keyword

wait untill it checks and display tooltip for Username
    Click Element    xpath://*[@id="save"]
    Sleep    3 seconds
    #${error_message}=    Get Text    css=#loc
    ${validation_message}=    Execute JavaScript    return document.querySelector('#uname').validationMessage
    Sleep    3 seconds
    Should Be Equal As Strings    ${validation_message}    Please enter valid Username


wait untill it checks and display Error message for invalid EmailID
    Wait Until Element Is Visible    ${Error_Message_invalidEmailID_Vaidity_Check}
    Page Should Contain Element    ${Error_Message_invalidEmailID_Vaidity_Check}
verify error message is correct for invalidEmailID
     ${result}=     Get Text    ${Error_Message_invalidEmailID_Vaidity_Check}
     Should Be Equal    ${result}    Please enter an email address ending with '@etteplan.com'

    
       

