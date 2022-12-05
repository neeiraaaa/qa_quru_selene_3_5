from selene.support.shared import browser
from selene import have
from selene import command
import os

def test_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Irina')
    browser.element('#lastName').type('Rogova')
    browser.element('#userEmail').type('neeiraaaa@gmail.com')
    browser.element('#userNumber').type('+79253999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="9"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1997"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--025 react-datepicker__day--weekend"]').click()
    browser.element('#subjectsInput').set_value('eng').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
