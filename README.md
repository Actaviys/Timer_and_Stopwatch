## Таймер з Секундоміром ##


Компілюлювання .ui в .py:
 - pip install PyQt5 pyqt5-tools

 - pyuic5 -x window_ts.ui -o uiWindow.py

\
\
Компілювання в .exe: 
 - python -m PyInstaller --onefile --noconsole --name "Timer and Stopwatch" --icon=iconey.ico main.py 

 - python -m PyInstaller --onefile --noconsole --name "Timer and Stopwatch" --uac-admin --icon=iconey.ico main.py 
