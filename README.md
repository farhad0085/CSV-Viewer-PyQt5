# CSV Viewer - PyQt5
This is a desktop application made for view CSV files more nicely formatted. I used PyQt5 for developing this app. All you need is run the script and then select a CSV file and it will be shown in the app nicely formatted. You can use shortcut (Ctrl+O) also to open a csv file.

## Requirements
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
`pyi-makespec main.py -F --icon=icon.png --noconsole`

### Build the package

Once the `.spec` file is up to your standards, use pyinstaller and pass it the `.spec` file as the first argument. It will use the information specified in the file to create the final distributable package.

`pyinstaller main.spec`