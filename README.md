# Parakeet

A collection of resources, libraries and praticies using the stack: 

- [Selenium](https://www.seleniumhq.org/projects/webdriver/) 
- [Chromewebdriver](https://sites.google.com/a/chromium.org/chromedriver/) 
- [Splinter](https://splinter.readthedocs.io/en/latest/lettuc) 
- [Lettuce](http://lettuce.it/)

Focused on the applications that use Google Stack (GCP, Gmail OAUTH2 and others).

## Instalation

You can install the parakeet using the the package manager PIP.

```
pip install parakeet -U
```

> **Note**: To use parakeet is necessary install previously all of tools metnioned above.

## Config

The parakeet works with a parameterized files **config.yaml** and **users.yaml**. These files are responsible for some tests behaviors. They need to be saved on the home directory of the operation system.

<table>
    <tr style="background: grey;font-weight: bold;">
        <td>Parameter</td>
        <td>Description</td>
        <td>Values</td>
        <td>Default</td>
    </tr>
    <tr>
        <td>browser</td>
        <td>This parameter define how browser will be used to test. Today the parakeet support just Chrome browser</td>
        <td>chrome</td>
        <td>chrome</td>
    </tr>
    <tr>
        <td>headless</td>
        <td>Define if the tests will open the browser or perform the tests with graphical mode off. It is very usefull in developer mode, when the developer need to debug or understand some issues. Case True, doesn't open the browser.</td>
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
        <td>You can setup the name of the logs that you want to see. For example if you want to see everyone you don't need to setup this field. But you can setup this one just to see the parakeet or just the loggers that you application are logging.</td>
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
        <td>The parakeet provide to you an abrastraction mechanism in order to login in the google account (if your application have something like it). Thinking on it, we created a parameter where the user can setup the version of this mechanism.</td>
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
        <td>The system page title, this is used in order to check if the user are logged on the application. Just in cases that tests envolving Google login.</td>
        <td>Text defined on the tag title on the application</td>
        <td>Empty</td>
    </tr>  
</table>

# Methods and Functions

- TBD

## Why Parakeet?

Github suggested it.
