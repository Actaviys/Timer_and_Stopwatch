## Таймер з Секундоміром
\
Для створення .exe: \
pyinstaller --onefile --noconsole --icon=Files\iconey.ico main.py

Альтернативне компілювання в .exe: \
1 - pyinstaller --onefile --noconsole --icon=icon_chess_clock_1949946.ico main.py \
2 - python -m PyInstaller --onefile --noconsole --name "Timer and Stopwatch" --icon=icon_chess_clock_1949946.ico main.py \
3 - python -m PyInstaller --onefile --noconsole --name "Timer and Stopwatch" --uac-admin --icon=icon_chess_clock_1949946.ico main.py 