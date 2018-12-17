# -*- coding: utf-8 -*-
from lettuce import step, world
from auth import LoginPage
from parakeet.lettuce_logger import LOG


@step(u'.* the logged user is "([^"]*)"')
def login(step, user_name):
    """
    If it is already logged do not attempt to login
    :param step:
    :param user_name:
    :return:
    """
    if world.cfg['system_page_title'] not in world.browser.selenium.title:
        LOG.debug(world.cfg.get('login_provider','missing login provider'))
        if world.cfg['login_provider'] == 'google_oauth':
            google_oauth(user_name)
        elif world.cfg['login_provider'] == 'google_oauth_gapi2':
            google_oauth_gapi2(user_name)
            LoginPage(world.browser, world.cfg['system_page_title']).redirect_to_home()


def google_oauth(user_name):
    """
    Default login with old GAPI Google Oauth version
    :param user_name:
    :return:
    """
    email = world.users[user_name]['email']
    password = world.users[user_name]['password']
    LoginPage(world.browser, world.cfg['system_page_title'])\
        .fill_email(email)\
        .click_next()\
        .fill_password(password)\
        .login()


def google_oauth_gapi2(user_name):
    """
    Login with personalized GAPI2 oauth version
    :return:
    """
    LoginPage(world.browser, world.cfg['system_page_title'])\
        .set_window()\
        .click_sign_in()\
        .switch_windows_after()

    google_oauth(user_name)
    LoginPage(world.browser, world.cfg['system_page_title'])\
        .switch_windows_before()
