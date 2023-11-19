*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Start Registration

*** Test Cases ***
Register With Valid Username And Password
    Set Username  palle
    Set Password  kalle456
    Set PasswordConfirmation  kalle456
    Submit Registration
    Register Should Succeed
    Go To Main Page
    Main Page Should Be Open
    Click Button  Logout
    Login Page Should Be Open
    Reset Application

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle456
    Set PasswordConfirmation  kalle456
    Submit Registration
    Register Should Fail With Message  too short username, min 3 characters
    Reset Application

Register With Valid Username And Invalid Password
    Set Username  kallenpoika
    Set Password  kalle
    Set PasswordConfirmation  kalle
    Submit Registration
    Register Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kallenisa
    Set Password  kalle456
    Set PasswordConfirmation  kalle123
    Submit Registration
    Register Should Fail With Message  Password doesn't match with Password confirmation

Login After Successful Registration
    Set Username  palle
    Set Password  kalle456
    Set PasswordConfirmation  kalle456
    Submit Registration
    Register Should Succeed
    Go To Main Page
    Main Page Should Be Open
    Click Button  Logout
    Login Page Should Be Open
    Set Username  palle
    Set Password  kalle456
    Submit Credentials
    Login Should Succeed
    Reset Application

Login After Failed Registration
    Set Username  kallenpoika
    Set Password  kalle
    Set PasswordConfirmation  kalle
    Submit Registration
    Register Should Fail With Message  Password cannot contain only letters
    Go To Login Page
    Login Page Should Be Open
    Set Username  kallenpoika
    Set Password  kalle
    Submit Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Submit Registration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Start Registration
    Go To Register Page
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
    