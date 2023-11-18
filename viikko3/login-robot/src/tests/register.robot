*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input Register Command
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Register Command
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered
    Input Register Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Register Command
    Input Credentials  ka  kalle123
    Output Should Contain  too short username, min 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Register Command
    Input Credentials  kauniskalle123  kalle123
    Output Should Contain  username can contain only small letters

Register With Valid Username And Too Short Password
    Input Register Command
    Input Credentials  kalle  kalu123
    Output Should Contain  too short password, min 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Register Command
    Input Credentials  kalle  kalukalle
    Output Should Contain  password cannot contain only Letters

    


