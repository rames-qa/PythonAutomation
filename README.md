\# Python Playwright Pytest Automation Framework



\## Overview



Automation framework developed using Python, Playwright, Pytest and Page Object Model.



\## Tech Stack



\- Python 3.14

\- Playwright

\- Pytest

\- Page Object Model

\- HTML Reports

\- Git/GitHub



\## Framework Structure



PythonAutomation

|

|-- pages

|    |-- login\_page.py

|

|-- tests

|    |-- test\_login.py

|

|-- conftest.py

|

|-- requirements.txt



\## Execution



Install dependencies:



pip install -r requirements.txt



Install browsers:



playwright install



Run tests:



pytest tests -v



Generate HTML Report:



pytest --html=report.html

