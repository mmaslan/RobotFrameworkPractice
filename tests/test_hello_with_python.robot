*** Settings ***
Library    ../resources/MyKeywords.py

*** Test Cases ***
Test Python Keyword
    ${greeting}=    Say Hello    Marek
    Log    ${greeting}