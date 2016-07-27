# bin/robot-server cpskin.slider.testing.CPSKIN_SLIDER_ROBOT_TESTING
# bin/robot cpskin/slider/tests/robot/test_slider.robot
*** Settings ***

Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Run keywords  Open test browser
Test Teardown  Close all browsers


*** Variables ***


*** Test cases ***

Test News Item exists
    Enable autologin as  Site Administrator
    Page Should Contain Link  SliderCollection
    Click link  SliderCollection
    Element Should Contain  css=div#slider ul.slides li.flex-active-slide div h2 a  Foire aux boudins
    Click Element  css=div#carousel ul.slides li:nth-child(2)
    Element Text Should Be  css=div#slider ul.slides li.flex-active-slide div h2 a  Festival de danse folklorique

Test Slider and Carousel
    Enable autologin as  Site Administrator
    Page Should Contain Link  SliderCollection
    Click link  SliderCollection
    Page Should Not Contain Element  css=div#slider ul.slides li:nth-child(3).flex-active-slide
    Click Element  css=div#carousel ul.slides li:nth-child(2)
    Page Should Contain Element  css=div#slider ul.slides li:nth-child(3).flex-active-slide

Test Url Carousel
    Enable autologin as  Site Administrator
    Page Should Contain Link  SliderCollection
    Click link  SliderCollection
    Click link  Festival de danse folklorique
    Location Should Be  http://localhost:55001/plone/2-festival-de-danse-folklorique

Test Event in Slider
    Enable autologin as  Site Administrator
    Page Should Contain Link  SliderCollection
    Click link  SliderCollection
    Click Element  css=div#carousel ul.slides li:nth-child(3)
    Click link  Evénement important
    Location Should Be  http://localhost:55001/plone/3-evenement-important


*** Keywords ***

Logged as owner
    Log in as site owner
