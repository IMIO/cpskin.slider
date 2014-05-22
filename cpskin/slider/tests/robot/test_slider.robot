*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Variables ***


*** Test cases ***

Test slider
    Logged as owner


*** Keywords ***

Logged as owner
    Log in as site owner
