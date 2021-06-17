# PVCase technical part

## Selenium test

Selenium test was written with Python using selenium binding.
### Pre-requisite
1. Download and install Python latest version

Execute command to isntall relevant binding for test
1. pip install selenium
2. pip install xlrd
3. pip install urllib3

### Execution

## API test
### Pre-requisite
API test was created using Postman tool which has an integration with newman CLI tool
To run Newman, ensure that you have Node.js >= v10.

Installation
The easiest way to install Newman is using NPM. If you have Node.js installed, it is most likely that you have NPM installed as well.

$ npm install -g newman

### Execution
There are several ways to execute test:
1. From API_Postman folder execute command "newman run PVCase.postman_collection.json -d, --iteration-data data.json"
2. Run test.bat

Output on command prompt will give a report
