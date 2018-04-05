# Parakeet

UI tests automation utilities library.
 
The aim is to easy the development of tests for applications that follow a 
known set of technologies:

- Angular JS
- Angular JS Material
- Google OAuth2
- Chrome Browser

This library depends, and sometime implements useful abstractions, on the following libraries: 

- [Lettuce](http://lettuce.it/)
- [Splinter](https://splinter.readthedocs.io/)
- [Selenium](https://www.seleniumhq.org/projects/webdriver/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

We designed it overcome some challenges of developing BDD tests considering the technologies below:

![Parakeet stack](parakeet-stack.png?raw=true "Parakeet Stack")

## Installation

You can install Parakeet using the package manager PIP.

```
pip install parakeet -U
```

## Configuration

Parakeet reads a **config.yaml** file that can be used to parameterize it's behaviours.

It need to be saved on the home directory of the operation system running the tests.

<table>
    <tr style="background: grey;font-weight: bold;">
        <td>Parameter</td>
        <td>Description</td>
        <td>Values</td>
        <td>Default</td>
    </tr>
    <tr>
        <td>browser</td>
        <td>This parameter define which browser will be used to run the tests. Today we only support the Chrome Browser</td>
        <td>chrome</td>
        <td>chrome</td>
    </tr>
    <tr>
        <td>headless</td>
        <td>Define if the tests will open the browser or perform the tests with graphical mode off. It is very useful in developer mode, when the developer need to debug or understand some issues. Case True, doesn't open the browser.</td>
        <td>True<br>False</td>
        <td>False</td>
    </tr>
    <tr>
        <td>default_implicitly_wait_seconds</td>
        <td>Setup time in seconds that the tests will wait until some component are ready to be used.</td>
        <td>Integer Number</td>
        <td>30</td>
    </tr>
    <tr>
        <td>default_poll_frequency_seconds</td>
        <td>Interval time during the default_implicitly_wait_seconds, that the application will wait until check if the component are ready to be used.</td>
        <td>Integer Number</td>
        <td>2</td>
    </tr> 
    <tr>
        <td>log_level</td>
        <td>You can define the level of the application logs.</td>
        <td>INFO<br>WARN<br>DEBUG<br>TRACE<br>ERROR</td>
        <td>INFO</td>
    </tr>         
    <tr>
        <td>log_name</td>
        <td>You can setup the name of the logs that you want to see. For example if you want to see everyone you don't need to setup this field. But you can setup this parameter to just see the Parakeet logs or just the loggers that you application are logging.</td>
        <td>Ex.: google.tests.e2e</td>
        <td>Empty</td>
    </tr>
    <tr>
        <td>retry</td>
        <td>Some resources on the application use the retry feature. This item give to the user the ability to setup how many times the test will try to click on some button for example.</td>
        <td>Integer Number</td>
        <td>1</td>
    </tr> 
    <tr>
        <td>login_provider</td>
        <td>The parakeet provide to you an abrastraction mechanism in order to login in the Google account (if your application have something like it). Thinking of it, we created a parameter where the user can setup the version of this mechanism.</td>
        <td>google_oauth</td>
        <td>google_oauth<br/>google_oauth_gapi2</td>
    </tr>
    <tr>
        <td>window_size:<br/>&nbsp;&nbsp;&nbsp;&nbsp;width: 9999<br/>&nbsp;&nbsp;&nbsp;&nbsp;height: 9999</td>
        <td>Setup the size of the screen where the tests will be performed.</td>
        <td>Integer Number</td>
        <td>Empty</td>
    </tr>                   
    <tr>
        <td>users:<br/>&nbsp;&nbsp;&nbsp;&nbsp;file: 'users.yaml'</td>
        <td>The parakeet provide a way to setup which users you will use on your tests. So this file can be setup here</td>
        <td>File Path</td>
        <td>Empty</td>
    </tr> 
    <tr>
        <td>home_url</td>
        <td>The home url used to access the application that will be tested.</td>
        <td>http://localhost</td>
        <td>Empty</td>
    </tr>
        <tr>
        <td>system_page_title</td>
        <td>The system page title, this is used in order to check if the user are logged on the application. That's the way we check if the test already passed the login phase.</td>
        <td>Text defined on the tag title on the application</td>
        <td>Empty</td>
    </tr>  
</table>

### Configuration example

(TODO - create/maintain example files and reference it here)

## Users configuration

Parakeet reads a **users.yaml** file that can be used to store users credentials 
that will be used in the tests..

It need to be saved on the home directory of the operation system running the tests.

### Users configuration example

(TODO - create/maintain example files and reference it here)

## Lettuce terrain

In order to bootstrap and start using this library in your Lettuce tests, you
should initialize it in the "terrain" file.

### Lettuce terrain example

(TODO - create/maintain example files and reference it here)

## Why Parakeet?

Github suggested it.
