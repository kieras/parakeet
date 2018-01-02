# -*- coding: utf-8 -*-
from lettuce import step, world
from auth import LoginPage


@step(u'.* the logged user is "([^"]*)"')
def login(step, user_name):
    # If it is already logged do not attempt to login
    if world.cfg['system_page_title'] not in world.browser.selenium.title:
        email = world.cfg['users'][user_name]['email']
        password = world.cfg['users'][user_name]['password']
        LoginPage(world.browser, world.cfg['system_page_title'])\
            .fill_email(email)\
            .click_next()\
            .fill_password(password)\
            .login()\
            .redirect_to_home()
