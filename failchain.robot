*** Settings ***
Library   BuiltIn
Library   Analysis
*** Keywords ***
Third Level
    Fail

Second Level
    Third Level

First Level
    Second Level

Toka
  Log To Console  Toka Before
  Run Keyword And Expect Error    STARTS: AssertionError
  ...   Third Level
  Log To Console  Toka After

Eka
  Toka

*** Test Cases ***
Fail Miserably
    First Level

Do Not Fail
  Eka    
