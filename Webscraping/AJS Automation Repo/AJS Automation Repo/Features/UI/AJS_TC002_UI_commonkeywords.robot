*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:5000
${BROWSER}    chrome 
${Valid_uname}    Arya
${Valid_email_Id}    arya.thamarakkulam@etteplan.com
${Valid_Job_Role}    test automation engineer
${Valid_Job_Location}    Espoo
${InValid_uname}    
${InValid_Job_Role}    test automation engineer
${InValid_Job_Location}    Espoo
${Invalid_Job_Role_Special_Character}    @@££$$$€€€
${Invalid_Job_Role_Numbers}    1234567
${Invalid_Job_Role_Numbers_Characters}    asdfg123455
${Invalid_Job_Location_Special_Character}    @@££$$$€€€
${Invalid_Job_Location_Numbers}    1222222222
${Invalid_Username_Special_Character}    @@££$$€€€
${Invalid_Username_Numbers}    123333333
${Invalid_Email_ID}    sshivani1091@gmail.com
${EMPTY}

*** Keywords ***

Open the browser localHost url
# we can't invoke the chrome directly we have to give chrome driver path
    Create Webdriver    ${BROWSER}
    Go To    ${url}  
    Maximize Browser Window


Close Browser Session
    Close Browser
