from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 185)
        ### ІКОНКА !!!!!! ####
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        # MainWindow.setWindowIcon(QtGui.QIcon("icon-1.ico"))
        
        MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.185042 rgba(0, 116, 4, 233), stop:0.359003 rgba(0, 138, 16, 235), stop:1 rgba(0, 184, 41, 233));\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.5, y1:0.9, x2:0.5, y2:0, stop:0 rgba(7, 47, 9, 236), stop:1 rgba(4, 216, 0, 127));\n"
"alternate-background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 0, 5, 7)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Output_Label_Stopwatch = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        font.setStrikeOut(False)
        self.Output_Label_Stopwatch.setFont(font)
        self.Output_Label_Stopwatch.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.193548 rgba(0, 116, 4, 233), stop:0.476369 rgba(0, 144, 17, 208), stop:1 rgba(0, 184, 41, 0));")
        self.Output_Label_Stopwatch.setAlignment(QtCore.Qt.AlignCenter)
        self.Output_Label_Stopwatch.setObjectName("Output_Label_Stopwatch")
        self.gridLayout.addWidget(self.Output_Label_Stopwatch, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_Pause_Stopwatch = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Button_Pause_Stopwatch.setFont(font)
        self.Button_Pause_Stopwatch.setObjectName("Button_Pause_Stopwatch")
        self.horizontalLayout.addWidget(self.Button_Pause_Stopwatch)
        self.Button_Start_Stopwatch = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Button_Start_Stopwatch.setFont(font)
        self.Button_Start_Stopwatch.setObjectName("Button_Start_Stopwatch")
        self.horizontalLayout.addWidget(self.Button_Start_Stopwatch)
        self.Button_Reset_Stopwatch = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Button_Reset_Stopwatch.setFont(font)
        self.Button_Reset_Stopwatch.setObjectName("Button_Reset_Stopwatch")
        self.horizontalLayout.addWidget(self.Button_Reset_Stopwatch)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.LabelSW_Outp = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(15)
        self.LabelSW_Outp.setFont(font)
        self.LabelSW_Outp.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.193548 rgba(0, 116, 4, 233), stop:0.476369 rgba(0, 144, 17, 208), stop:1 rgba(0, 184, 41, 0));")
        self.LabelSW_Outp.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelSW_Outp.setObjectName("LabelSW_Outp")
        self.gridLayout.addWidget(self.LabelSW_Outp, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 1, 2, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LineEdit_Inp_Timer = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.LineEdit_Inp_Timer.setFont(font)
        self.LineEdit_Inp_Timer.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.193548 rgba(0, 116, 4, 233), stop:0.476369 rgba(0, 144, 17, 208), stop:1 rgba(0, 184, 41, 0));\n"
"gridline-color: rgb(0, 0, 0);")
        self.LineEdit_Inp_Timer.setMaxLength(5)
        self.LineEdit_Inp_Timer.setFrame(True)
        self.LineEdit_Inp_Timer.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.LineEdit_Inp_Timer.setAlignment(QtCore.Qt.AlignCenter)
        self.LineEdit_Inp_Timer.setObjectName("LineEdit_Inp_Timer")
        self.horizontalLayout_2.addWidget(self.LineEdit_Inp_Timer)
        self.Button_Start_Timer = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Start_Timer.sizePolicy().hasHeightForWidth())
        self.Button_Start_Timer.setSizePolicy(sizePolicy)
        self.Button_Start_Timer.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Button_Start_Timer.setFont(font)
        self.Button_Start_Timer.setStyleSheet("")
        self.Button_Start_Timer.setObjectName("Button_Start_Timer")
        self.horizontalLayout_2.addWidget(self.Button_Start_Timer)
        self.Button_Pause_Timer = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Pause_Timer.sizePolicy().hasHeightForWidth())
        self.Button_Pause_Timer.setSizePolicy(sizePolicy)
        self.Button_Pause_Timer.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Button_Pause_Timer.setFont(font)
        self.Button_Pause_Timer.setObjectName("Button_Pause_Timer")
        self.horizontalLayout_2.addWidget(self.Button_Pause_Timer)
        self.Button_Stop_Timer = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Stop_Timer.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Stop_Timer.sizePolicy().hasHeightForWidth())
        self.Button_Stop_Timer.setSizePolicy(sizePolicy)
        self.Button_Stop_Timer.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Button_Stop_Timer.setFont(font)
        self.Button_Stop_Timer.setObjectName("Button_Stop_Timer")
        self.horizontalLayout_2.addWidget(self.Button_Stop_Timer)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Output_Label_Timer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        self.Output_Label_Timer.setFont(font)
        self.Output_Label_Timer.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.193548 rgba(0, 116, 4, 233), stop:0.476369 rgba(0, 144, 17, 208), stop:1 rgba(0, 184, 41, 0));")
        self.Output_Label_Timer.setAlignment(QtCore.Qt.AlignCenter)
        self.Output_Label_Timer.setObjectName("Output_Label_Timer")
        self.horizontalLayout_3.addWidget(self.Output_Label_Timer)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Timer_Button_20 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Timer_Button_20.setFont(font)
        self.Timer_Button_20.setObjectName("Timer_Button_20")
        self.gridLayout_2.addWidget(self.Timer_Button_20, 1, 1, 1, 1)
        self.Timer_Button_10 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Timer_Button_10.setFont(font)
        self.Timer_Button_10.setObjectName("Timer_Button_10")
        self.gridLayout_2.addWidget(self.Timer_Button_10, 0, 1, 1, 1)
        self.Timer_Button_25 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Timer_Button_25.setFont(font)
        self.Timer_Button_25.setObjectName("Timer_Button_25")
        self.gridLayout_2.addWidget(self.Timer_Button_25, 2, 0, 1, 1)
        self.Timer_Button_30 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Timer_Button_30.setFont(font)
        self.Timer_Button_30.setStyleSheet("")
        self.Timer_Button_30.setObjectName("Timer_Button_30")
        self.gridLayout_2.addWidget(self.Timer_Button_30, 2, 1, 1, 1)
        self.Timer_Button_5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Timer_Button_5.setFont(font)
        self.Timer_Button_5.setObjectName("Timer_Button_5")
        self.gridLayout_2.addWidget(self.Timer_Button_5, 0, 0, 1, 1)
        self.Timer_Button_15 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Timer_Button_15.setFont(font)
        self.Timer_Button_15.setObjectName("Timer_Button_15")
        self.gridLayout_2.addWidget(self.Timer_Button_15, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LabelT_Outp = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(15)
        self.LabelT_Outp.setFont(font)
        self.LabelT_Outp.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.193548 rgba(0, 116, 4, 233), stop:0.476369 rgba(0, 144, 17, 208), stop:1 rgba(0, 184, 41, 0));")
        self.LabelT_Outp.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelT_Outp.setObjectName("LabelT_Outp")
        self.horizontalLayout_4.addWidget(self.LabelT_Outp)
        self.ComboBox_Timer = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(11)
        self.ComboBox_Timer.setFont(font)
        self.ComboBox_Timer.setObjectName("ComboBox_Timer")
        self.ComboBox_Timer.addItem("")
        self.ComboBox_Timer.addItem("")
        self.ComboBox_Timer.addItem("")
        self.ComboBox_Timer.addItem("")
        self.horizontalLayout_4.addWidget(self.ComboBox_Timer)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.StatusBar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(10)
        font.setKerning(True)
        self.StatusBar.setFont(font)
        self.StatusBar.setObjectName("StatusBar")
        MainWindow.setStatusBar(self.StatusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timer and Stopwatch"))
        self.Output_Label_Stopwatch.setText(_translate("MainWindow", "00:00:00"))
        self.Button_Pause_Stopwatch.setText(_translate("MainWindow", "Pause"))
        self.Button_Start_Stopwatch.setText(_translate("MainWindow", "Start"))
        self.Button_Reset_Stopwatch.setText(_translate("MainWindow", "Reset"))
        self.LabelSW_Outp.setText(_translate("MainWindow", "Stopwatch"))
        self.Button_Start_Timer.setText(_translate("MainWindow", "Start"))
        self.Button_Pause_Timer.setText(_translate("MainWindow", "Pause"))
        self.Button_Stop_Timer.setText(_translate("MainWindow", "Stop"))
        self.Output_Label_Timer.setText(_translate("MainWindow", "00:00"))
        self.Timer_Button_20.setText(_translate("MainWindow", "20"))
        self.Timer_Button_10.setText(_translate("MainWindow", "10"))
        self.Timer_Button_25.setText(_translate("MainWindow", "25"))
        self.Timer_Button_30.setText(_translate("MainWindow", "30"))
        self.Timer_Button_5.setText(_translate("MainWindow", "5"))
        self.Timer_Button_15.setText(_translate("MainWindow", "15"))
        self.LabelT_Outp.setText(_translate("MainWindow", "Timer"))
        self.ComboBox_Timer.setItemText(0, _translate("MainWindow", "Seconds"))
        self.ComboBox_Timer.setItemText(1, _translate("MainWindow", "Minutes"))
        self.ComboBox_Timer.setItemText(2, _translate("MainWindow", "Hours"))
        self.ComboBox_Timer.setItemText(3, _translate("MainWindow", "Days"))
