# PyWebTest
A Python 3.x tool that can be used for website testing.

## Stack
- Python 3.x
- Selenium

## Setup
- ### Install python 3.x
    - #### For Linux or Mac
    ```
    sudo apt install python3
    ```
    - #### For Windows:
        - Download and install from the official Python website: <a href="https://www.python.org" target="_blank">python.org</a>

- ### Install all the packages:
    ```
    pip3 install -r requirements.txt
    ```
- ### Additional step for Windows:
    - Download <a href="https://chromedriver.chromium.org/home" target="_blank">chromedriver</a>
    - Add an environment variable ``Path`` with the directory of the chromedriver executable.

## Usage
- config.json
    - Update the url to your test website
    - If login is needed, enter accordingly. Otherwise, you may ignore the login part. The idea is that you can access the configuration as an object in the code. 
- To run the code:
    ```
    python3 main_script.py
    ```
