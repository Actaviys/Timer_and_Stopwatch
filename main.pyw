import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from bookkeeper_timer_stopwatch import TimerTimeWatch
import asyncio




from uiWindow import Ui_MainWindow
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


class StopwatchThread(QThread):
    update_signal = pyqtSignal(int)

    def __init__(self, timer_watch):
        super().__init__()
        self.timer_watch = timer_watch

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.timer_watch.stopwatch(self.update_signal.emit))

    def stop(self):
        self.timer_watch.stop_stopwatch()
        self.quit()

class TimerThread(QThread):
    update_signal = pyqtSignal(int)

    def __init__(self, timer_watch, seconds):
        super().__init__()
        self.timer_watch = timer_watch
        self.seconds = seconds

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.timer_watch.timer(self.seconds, self.update_signal.emit))

    def stop(self):
        self.timer_watch.stop_timer()
        self.quit()


### Використання в UI-класі: ###
timer_watch = TimerTimeWatch()
stopwatch_thread = StopwatchThread(timer_watch)

#####   Секундомір    #####
def start_stopwch():
    ui.Button_Start_Stopwatch.setEnabled(False)
    ui.Button_Pause_Stopwatch.setEnabled(True)
    ui.StatusBar.showMessage("Старт секундоміра")
    global stopwatch_thread
    stopwatch_thread = StopwatchThread(timer_watch)
    stopwatch_thread.update_signal.connect(update_stopwatch_label)
    stopwatch_thread.start()
ui.Button_Start_Stopwatch.clicked.connect(start_stopwch)

def stop_stopwch():
    ui.Button_Start_Stopwatch.setEnabled(True)
    ui.Button_Pause_Stopwatch.setEnabled(False)
    stopwatch_thread.stop()
    update_stopwatch_label(0)
    ui.StatusBar.showMessage("Секундомір скинуто", 5000)
ui.Button_Stop_Stopwatch.clicked.connect(stop_stopwch)

def pause_stopwch():
    ui.Button_Pause_Stopwatch.setEnabled(False)
    ui.Button_Start_Stopwatch.setEnabled(True)
    timer_watch.pause_stopwatch()
    ui.StatusBar.showMessage("Секундомір призупинено")
ui.Button_Pause_Stopwatch.setEnabled(False)
ui.Button_Pause_Stopwatch.clicked.connect(pause_stopwch)
#####   #####







#########   Таймер    #########
timer_thread = None  # Створюється при запуску програми
curent_timer_seconds = 1
timer_seconds_count = 0
flag_status_sp = False
time_buff = 0

def read_signals_tread(val):
    global timer_seconds_count; timer_seconds_count = 1
    global flag_status_sp; flag_status_sp = False
    global time_buff
    
    time_buff = val
    if val <= 0:
        ui.Button_Start_Timer.setEnabled(True) # Вмикання кнопки
        ui.Button_Pause_Timer.setEnabled(False) # Вимикання кнопки
        ui.StatusBar.showMessage("")
        playing_sound_completion() # Функція для звукового сигналу
        
        if timer_thread:
            timer_thread.stop()

def start_tmr(seconds_in):
    global timer_thread
    timer_thread = TimerThread(timer_watch, seconds_in)
    timer_thread.update_signal.connect(update_timer_label)
    timer_thread.update_signal.connect(read_signals_tread)
    timer_thread.start()

def func_start_tmr():
    ui.Button_Start_Timer.setEnabled(False) # Вимикання кнопки
    ui.Button_Pause_Timer.setEnabled(True)
    
    global flag_status_sp
    global timer_seconds_count
    global curent_timer_seconds
    
    if flag_status_sp == True: # Pause #
        start_tmr(timer_seconds_count)
        
    else: # Stop #
        try:
            inp_count_int = int(ui.LineEdit_Inp_Timer.text())
            timer_seconds_count = inp_count_int * curent_timer_seconds    
        except:
            timer_seconds_count = 1 
            ui.StatusBar.showMessage("Введіть число!!", 3000)
        
        # print(curent_timer_seconds)
        start_tmr(timer_seconds_count)
    ui.StatusBar.showMessage("Таймер запущено")
ui.Button_Start_Timer.clicked.connect(func_start_tmr)



def stop_tmr():
    ui.Button_Pause_Timer.setEnabled(False)
    ui.Button_Start_Timer.setEnabled(True) # Вмикання кнопки
    ui.LineEdit_Inp_Timer.setText("")
    
    global flag_status_sp
    global timer_seconds_count; timer_seconds_count = 1
    
    flag_status_sp = False
    
    
    if timer_thread:
        timer_thread.stop()
        update_timer_label(0)
        ui.StatusBar.showMessage("Таймер зупинено", 5000)
ui.Button_Reset_Timer.clicked.connect(stop_tmr)



def pause_tmr():
    ui.Button_Start_Timer.setEnabled(True) # Вмикання кнопки
    ui.Button_Pause_Timer.setEnabled(False)
    
    global flag_status_sp
    global timer_seconds_count
    
    flag_status_sp = True
    timer_seconds_count = time_buff
    
    if timer_thread:
        timer_thread.stop()
        ui.StatusBar.showMessage("Таймер на паузі")
ui.Button_Pause_Timer.setEnabled(False)
ui.Button_Pause_Timer.clicked.connect(pause_tmr)



def combo_box_timer_set_units():
    global timer_seconds_count
    global curent_timer_seconds
    
    cb_text = str(ui.ComboBox_Timer.currentText()).lower()
    if cb_text == "seconds":
        curent_timer_seconds = 1
        # print(f"{cb_text} -> {curent_timer_seconds}")
        
    elif cb_text == "minutes":
        curent_timer_seconds = 60
        # print(f"{cb_text} -> {curent_timer_seconds}")
        
    elif cb_text == "hours":
        curent_timer_seconds = 3600
    #     print(f"{cb_text} -> {curent_timer_seconds}")
    
    elif cb_text == "days":
        curent_timer_seconds = 86400
    #     print(f"{cb_text} -> {curent_timer_seconds}")
    
ui.ComboBox_Timer.activated.connect(combo_box_timer_set_units)
# ui.ComboBox_Timer.currentIndexChanged.connect(combo_box_timer_set_units)
# ui.ComboBox_Timer.highlighted.connect(combo_box_timer_set_units)
#####


#   Кнопки для таймера    #
def count_btn(): ui.LineEdit_Inp_Timer.setText(ui.Timer_Button_5.text())
ui.Timer_Button_5.clicked.connect(count_btn)

def count_btn(): ui.LineEdit_Inp_Timer.setText(ui.Timer_Button_10.text())
ui.Timer_Button_10.clicked.connect(count_btn)

def count_btn(): ui.LineEdit_Inp_Timer.setText(ui.Timer_Button_15.text())
ui.Timer_Button_15.clicked.connect(count_btn)

def count_btn(): ui.LineEdit_Inp_Timer.setText(ui.Timer_Button_20.text())
ui.Timer_Button_20.clicked.connect(count_btn)

def count_btn(): ui.LineEdit_Inp_Timer.setText(ui.Timer_Button_25.text())
ui.Timer_Button_25.clicked.connect(count_btn)

def count_btn(): ui.LineEdit_Inp_Timer.setText(ui.Timer_Button_30.text())
ui.Timer_Button_30.clicked.connect(count_btn)
#####



#####
def update_stopwatch_label(seconds):
    ui.Output_Label_Stopwatch.setText(f"{seconds//3600:02}:{(seconds%3600)//60:02}:{seconds%60:02}")

def update_timer_label(seconds):
    if seconds//86400:
        ui.Output_Label_Timer.setText(f"{seconds//86400:02}d/{(seconds%86400)//3600:02}h\n{(seconds%3600)//60:02}:{seconds%60:02}")
    elif seconds//3600:
        ui.Output_Label_Timer.setText(f"{seconds//3600:02}:{(seconds%3600)//60:02}:{seconds%60:02}")
    else:
        ui.Output_Label_Timer.setText(f"{(seconds%3600)//60:02}:{seconds%60:02}")
#########             #########




flag_sound_chec = 0
##########   Звуковий сигнал     ########## 
def playing_sound_completion():
    global flag_sound_chec
    if flag_sound_chec == 1:
        print("OKKKK")
    else:pass
#####       #####




#####   Виставляю іконку і перемикаю флажок звуку   #####
from PyQt5 import QtGui
iconS = QtGui.QIcon()
file_icon_dir = ""
def func_check_box_sound_controll():
    """"""
    global flag_sound_chec
    stat_check = ui.CheckBox_Sound.checkState()

    if stat_check > 0:
        file_icon_dir = "Files/icon_enable.png"
        flag_sound_chec = 1
    else:
        file_icon_dir = "Files/icon_mute.png"
        flag_sound_chec = 0
    
    iconS.addPixmap(QtGui.QPixmap(file_icon_dir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui.CheckBox_Sound.setIcon(iconS)
    
# ui.CheckBox_Sound.clicked.connect(func_check_box_sound_controll)
ui.CheckBox_Sound.stateChanged.connect(func_check_box_sound_controll)
##########           ##########




def open_window(): # Функція для відкриття вікна
    MainWindow.show()
    app.exec_()

if __name__ == "__main__":
    open_window()

