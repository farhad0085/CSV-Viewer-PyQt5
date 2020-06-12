# CSV Viewer - PyQt5
This is a desktop application made for view CSV files more nicely formatted. I used PyQt5 for developing this app. All you need is run the script and then select a CSV file and it will be shown in the app nicely formatted. You can use shortcut (Ctrl+O) also to open a csv file.

### Requirements
Simply run the following command in your virtual environment.
`pip install -r requirements.txt`

## How to build

### Create a spec file with all defaults
`pyi-makespec main.py`
### Or, if you want the final distributable package to be a single file
`pyi-makespec main.py -F`
### To set the icon
`pyi-makespec main.py --icon=icon.png`
### To disable console
`pyi-makespec main.py --noconsole`
### Combined
`pyi-makespec main.py -F --icon=icon.ico --noconsole`