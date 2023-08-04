*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary
Library    OperatingSystem
*** Variables ***
${base_url}    http://127.0.0.1:5000
${X-RapidAPI-Key}    2c36597583mshb3ec6f540dfd966p181965jsne63a63911509
${CONTENT_TYPE}    application/x-www-form-urlencoded
${role}    Test Automation  
${loc}    Espoo
${csvName1}    /write_csv1
${csvName2}    /write_csv2
${header}
${response}

*** Keywords ***
Input header
    &{header}    Create Dictionary    Content-Type=${CONTENT_TYPE}    User-Agent=RobotFramework    Authorization=${X-RapidAPI-Key}
Input data for csv1    
    [Arguments]    ${role}    ${loc}
    ${data}=    Create Dictionary  role=${role}   loc=${loc}
    [Return]    ${data}
Create Sessions 
    Create Session    mysession    ${base_url}    verify=true

Validate responce
    [Arguments]    ${response}      
    #Validation
    ${response_of_input_data}=    Convert To String    ${response.content}
    Should Contain    ${response_of_input_data}    CSV File Created   
    ${status_code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${status_code}    200  
   
Input data for csv2
    [Arguments]    ${uname}    ${email}
    ${data}=    Create Dictionary  uname=${uname}    email=${email} 
    [Return]    ${data}        
Post response in csv and Validate responce
    [Arguments]    ${data1}    ${data2}    ${CSVname}
    IF    $CSVname == $csvName1
        ${data}=    Input data for csv1    ${data1}    ${data2}  
    ELSE
        ${data}=    Input data for csv2    ${data1}    ${data2}  
    END  
    
    ${response}=    POST On Session    mysession    ${CSV name}    data=${data}    headers=${header}
    Log To Console    ${response.status_code} 200
    Log To Console    Successfully created search_terms.csv file
    Validate responce    ${response}    

Post response in start program and Validate responce
    [Arguments]    ${CSV name}     
    ${response}=    POST On Session    mysession    ${CSV name}    headers=${header}
    Log To Console    ${response.status_code} 200
    Log To Console    Successfully email created     
    #Validation  
    ${status_code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${status_code}    200     