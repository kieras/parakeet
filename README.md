# Parakeet

A collection of resources, libraries and praticies using the stack: 
- [Selenium](https://www.seleniumhq.org/projects/webdriver/) 
- [Chromewebdriver](https://sites.google.com/a/chromium.org/chromedriver/) 
- [Splinter](https://splinter.readthedocs.io/en/latest/lettuc) 
- [Lettuce](http://lettuce.it/)

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
        <td>True|False</td>
        <td>False</td>
    </tr>
    <tr>
        <td>default_implicitly_wait_seconds</td>
        <td>Setup time in seconds that the tests will wait until some component are ready to be used.</td>
        <td>True|False</td>
        <td>False</td>
    </tr>

</table>

## Why Parakeet?

Github suggested it.
