*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Variables ***


*** Test cases ***

Test News Item exists
    Logged as owner
    Page Should Contain Link  SliderCollection
    Click link  SliderCollection
    Element Should Contain  css=div#slider ul.slides li:nth-child(1) div h2 a  Festival de danse folklorique
    Element Text Should Be  css=div#slider ul.slides li:nth-child(2) div h2 a  Foire aux boudins
    Element Should Contain  css=div#carousel ul.slides li:nth-child(1)  Festival de danse folklorique
    Element Should Contain  css=div#carousel ul.slides li:nth-child(2)  Foire aux boudins

Test Slider and Carousel
    Logged as owner
    Page Should Contain Link  SliderCollection
    Click link  SliderCollection
    Page Should Not Contain Element  css=div#slider ul.slides li:nth-child(2).flex-active-slide
    Click Element  css=div#carousel ul.slides li:nth-child(2)
    Page Should Contain Element  css=div#slider ul.slides li:nth-child(2).flex-active-slide

*** Keywords ***

Logged as owner
    Log in as site owner
