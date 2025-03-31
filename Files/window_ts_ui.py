# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_ts.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 222)
        icon = QIcon()
        icon.addFile(u"iconey.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.185042 rgba(0, 116, 4, 233), stop:0.359003 rgba(0, 138, 16, 235), stop:1 rgba(0, 184, 41, 233));\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.5, y1:0.9, x2:0.5, y2:0, stop:0 rgba(7, 47, 9, 236), stop:1 rgba(4, 216, 0, 127));\n"
"alternate-background-color: qlineargradient(spread:pad, x1:0.5, y1:0.9, x2:0.5, y2:0, stop:0 rgba(7, 47, 9, 236), stop:1 rgba(4, 216, 0, 127));")
        MainWindow.setIconSize(QSize(25, 25))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(5, 0, 5, 7)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LabelT_Outp = QLabel(self.centralwidget)
        self.LabelT_Outp.setObjectName(u"LabelT_Outp")
        font = QFont()
        font.setFamilies([u"Sitka Small"])
        font.setPointSize(15)
        self.LabelT_Outp.setFont(font)
        self.LabelT_Outp.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.193548 rgba(0, 116, 4, 233), stop:0.476369 rgba(0, 144, 17, 208), stop:1 rgba(0, 184, 41, 0));")
        self.LabelT_Outp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.LabelT_Outp)

        self.ComboBox_Timer = QComboBox(self.centralwidget)
        self.ComboBox_Timer.addItem("")
        self.ComboBox_Timer.addItem("")
        self.ComboBox_Timer.addItem("")
        self.ComboBox_Timer.addItem("")
        self.ComboBox_Timer.setObjectName(u"ComboBox_Timer")
        font1 = QFont()
        font1.setFamilies([u"Sitka Small"])
        font1.setPointSize(11)
        self.ComboBox_Timer.setFont(font1)
        self.ComboBox_Timer.setStyleSheet(u"background-color: rgba(24, 161, 0, 200);")

        self.horizontalLayout_4.addWidget(self.ComboBox_Timer)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_Inp_Timer = QLineEdit(self.centralwidget)
        self.LineEdit_Inp_Timer.setObjectName(u"LineEdit_Inp_Timer")
        font2 = QFont()
        font2.setFamilies([u"Sitka Small"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.LineEdit_Inp_Timer.setFont(font2)
        self.LineEdit_Inp_Timer.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.193548 rgba(0, 116, 4, 233), stop:0.476369 rgba(0, 144, 17, 208), stop:1 rgba(0, 184, 41, 0));\n"
"gridline-color: rgb(0, 0, 0);")
        self.LineEdit_Inp_Timer.setMaxLength(5)
        self.LineEdit_Inp_Timer.setFrame(True)
        self.LineEdit_Inp_Timer.setEchoMode(QLineEdit.Normal)
        self.LineEdit_Inp_Timer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.LineEdit_Inp_Timer)

        self.Button_Start_Timer = QPushButton(self.centralwidget)
        self.Button_Start_Timer.setObjectName(u"Button_Start_Timer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Start_Timer.sizePolicy().hasHeightForWidth())
        self.Button_Start_Timer.setSizePolicy(sizePolicy)
        self.Button_Start_Timer.setBaseSize(QSize(0, 0))
        self.Button_Start_Timer.setFont(font2)
        self.Button_Start_Timer.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.Button_Start_Timer)

        self.Button_Pause_Timer = QPushButton(self.centralwidget)
        self.Button_Pause_Timer.setObjectName(u"Button_Pause_Timer")
        sizePolicy.setHeightForWidth(self.Button_Pause_Timer.sizePolicy().hasHeightForWidth())
        self.Button_Pause_Timer.setSizePolicy(sizePolicy)
        self.Button_Pause_Timer.setBaseSize(QSize(0, 0))
        self.Button_Pause_Timer.setFont(font2)

        self.horizontalLayout_2.addWidget(self.Button_Pause_Timer)

        self.Button_Reset_Timer = QPushButton(self.centralwidget)
        self.Button_Reset_Timer.setObjectName(u"Button_Reset_Timer")
        self.Button_Reset_Timer.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Button_Reset_Timer.sizePolicy().hasHeightForWidth())
        self.Button_Reset_Timer.setSizePolicy(sizePolicy)
        self.Button_Reset_Timer.setBaseSize(QSize(0, 0))
        self.Button_Reset_Timer.setFont(font2)

        self.horizontalLayout_2.addWidget(self.Button_Reset_Timer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Button_Pause_Stopwatch = QPushButton(self.centralwidget)
        self.Button_Pause_Stopwatch.setObjectName(u"Button_Pause_Stopwatch")
        self.Button_Pause_Stopwatch.setFont(font2)

        self.horizontalLayout.addWidget(self.Button_Pause_Stopwatch)

        self.Button_Start_Stopwatch = QPushButton(self.centralwidget)
        self.Button_Start_Stopwatch.setObjectName(u"Button_Start_Stopwatch")
        self.Button_Start_Stopwatch.setFont(font2)

        self.horizontalLayout.addWidget(self.Button_Start_Stopwatch)

        self.Button_Stop_Stopwatch = QPushButton(self.centralwidget)
        self.Button_Stop_Stopwatch.setObjectName(u"Button_Stop_Stopwatch")
        self.Button_Stop_Stopwatch.setFont(font2)

        self.horizontalLayout.addWidget(self.Button_Stop_Stopwatch)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.LabelSW_Outp = QLabel(self.centralwidget)
        self.LabelSW_Outp.setObjectName(u"LabelSW_Outp")
        self.LabelSW_Outp.setFont(font)
        self.LabelSW_Outp.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.193548 rgba(0, 116, 4, 233), stop:0.476369 rgba(0, 144, 17, 208), stop:1 rgba(0, 184, 41, 0));")
        self.LabelSW_Outp.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.LabelSW_Outp, 0, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Output_Label_Timer = QLabel(self.centralwidget)
        self.Output_Label_Timer.setObjectName(u"Output_Label_Timer")
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(26)
        self.Output_Label_Timer.setFont(font3)
        self.Output_Label_Timer.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.193548 rgba(0, 116, 4, 233), stop:0.476369 rgba(0, 144, 17, 208), stop:1 rgba(0, 184, 41, 0));")
        self.Output_Label_Timer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Output_Label_Timer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Timer_Button_20 = QPushButton(self.centralwidget)
        self.Timer_Button_20.setObjectName(u"Timer_Button_20")
        self.Timer_Button_20.setFont(font2)

        self.gridLayout_2.addWidget(self.Timer_Button_20, 1, 1, 1, 1)

        self.Timer_Button_10 = QPushButton(self.centralwidget)
        self.Timer_Button_10.setObjectName(u"Timer_Button_10")
        self.Timer_Button_10.setFont(font2)

        self.gridLayout_2.addWidget(self.Timer_Button_10, 0, 1, 1, 1)

        self.Timer_Button_30 = QPushButton(self.centralwidget)
        self.Timer_Button_30.setObjectName(u"Timer_Button_30")
        self.Timer_Button_30.setFont(font2)
        self.Timer_Button_30.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.Timer_Button_30, 2, 1, 1, 1)

        self.Timer_Button_25 = QPushButton(self.centralwidget)
        self.Timer_Button_25.setObjectName(u"Timer_Button_25")
        self.Timer_Button_25.setFont(font2)

        self.gridLayout_2.addWidget(self.Timer_Button_25, 2, 0, 1, 1)

        self.Timer_Button_15 = QPushButton(self.centralwidget)
        self.Timer_Button_15.setObjectName(u"Timer_Button_15")
        self.Timer_Button_15.setFont(font2)

        self.gridLayout_2.addWidget(self.Timer_Button_15, 1, 0, 1, 1)

        self.Timer_Button_5 = QPushButton(self.centralwidget)
        self.Timer_Button_5.setObjectName(u"Timer_Button_5")
        self.Timer_Button_5.setFont(font2)

        self.gridLayout_2.addWidget(self.Timer_Button_5, 0, 0, 1, 1)

        self.CheckBox_Sound = QCheckBox(self.centralwidget)
        self.CheckBox_Sound.setObjectName(u"CheckBox_Sound")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setStrikeOut(False)
        self.CheckBox_Sound.setFont(font4)
        self.CheckBox_Sound.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.CheckBox_Sound.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.CheckBox_Sound.setLayoutDirection(Qt.RightToLeft)
        self.CheckBox_Sound.setAutoFillBackground(False)
        self.CheckBox_Sound.setStyleSheet(u"background-color: rgba(24, 161, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u"icon_mute_t.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CheckBox_Sound.setIcon(icon1)
        self.CheckBox_Sound.setIconSize(QSize(16, 16))
        self.CheckBox_Sound.setTristate(False)

        self.gridLayout_2.addWidget(self.CheckBox_Sound, 3, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 2, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 1, 2, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Output_Label_Stopwatch = QLabel(self.centralwidget)
        self.Output_Label_Stopwatch.setObjectName(u"Output_Label_Stopwatch")
        font5 = QFont()
        font5.setFamilies([u"Comic Sans MS"])
        font5.setPointSize(26)
        font5.setStrikeOut(False)
        self.Output_Label_Stopwatch.setFont(font5)
        self.Output_Label_Stopwatch.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 97, 6, 223), stop:0.193548 rgba(0, 116, 4, 233), stop:0.476369 rgba(0, 144, 17, 208), stop:1 rgba(0, 184, 41, 0));")
        self.Output_Label_Stopwatch.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Output_Label_Stopwatch)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LineEdit_Time_Stopwath = QLineEdit(self.centralwidget)
        self.LineEdit_Time_Stopwath.setObjectName(u"LineEdit_Time_Stopwath")
        font6 = QFont()
        font6.setPointSize(9)
        self.LineEdit_Time_Stopwath.setFont(font6)
        self.LineEdit_Time_Stopwath.setMaxLength(5)
        self.LineEdit_Time_Stopwath.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.LineEdit_Time_Stopwath)

        self.ComboBox_Stopwatch = QComboBox(self.centralwidget)
        self.ComboBox_Stopwatch.addItem("")
        self.ComboBox_Stopwatch.addItem("")
        self.ComboBox_Stopwatch.addItem("")
        self.ComboBox_Stopwatch.addItem("")
        self.ComboBox_Stopwatch.setObjectName(u"ComboBox_Stopwatch")
        self.ComboBox_Stopwatch.setFont(font1)
        self.ComboBox_Stopwatch.setStyleSheet(u"background-color: rgba(24, 161, 0, 200);")

        self.horizontalLayout_5.addWidget(self.ComboBox_Stopwatch)

        self.CheckBox_Stopwatch = QCheckBox(self.centralwidget)
        self.CheckBox_Stopwatch.setObjectName(u"CheckBox_Stopwatch")
        font7 = QFont()
        font7.setPointSize(10)
        self.CheckBox_Stopwatch.setFont(font7)
        self.CheckBox_Stopwatch.setLayoutDirection(Qt.RightToLeft)
        self.CheckBox_Stopwatch.setStyleSheet(u"background-color: rgba(24, 161, 0, 0);")
        icon2 = QIcon()
        icon2.addFile(u"icon_sw_stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CheckBox_Stopwatch.setIcon(icon2)
        self.CheckBox_Stopwatch.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.CheckBox_Stopwatch)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.StatusBar = QStatusBar(MainWindow)
        self.StatusBar.setObjectName(u"StatusBar")
        font8 = QFont()
        font8.setFamilies([u"Sylfaen"])
        font8.setPointSize(10)
        font8.setKerning(True)
        self.StatusBar.setFont(font8)
        self.StatusBar.setLayoutDirection(Qt.LeftToRight)
        self.StatusBar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.StatusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Timer and Stopwatch", None))
        self.LabelT_Outp.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.ComboBox_Timer.setItemText(0, QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.ComboBox_Timer.setItemText(1, QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.ComboBox_Timer.setItemText(2, QCoreApplication.translate("MainWindow", u"Hours", None))
        self.ComboBox_Timer.setItemText(3, QCoreApplication.translate("MainWindow", u"Days", None))

        self.Button_Start_Timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Button_Pause_Timer.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.Button_Reset_Timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.Button_Pause_Stopwatch.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.Button_Start_Stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Button_Stop_Stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.LabelSW_Outp.setText(QCoreApplication.translate("MainWindow", u"Stopwatch", None))
        self.Output_Label_Timer.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.Timer_Button_20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.Timer_Button_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.Timer_Button_30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.Timer_Button_25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.Timer_Button_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.Timer_Button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.CheckBox_Sound.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.Output_Label_Stopwatch.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.LineEdit_Time_Stopwath.setText("")
        self.ComboBox_Stopwatch.setItemText(0, QCoreApplication.translate("MainWindow", u"Seconds", None))
        self.ComboBox_Stopwatch.setItemText(1, QCoreApplication.translate("MainWindow", u"Minutes", None))
        self.ComboBox_Stopwatch.setItemText(2, QCoreApplication.translate("MainWindow", u"Hours", None))
        self.ComboBox_Stopwatch.setItemText(3, QCoreApplication.translate("MainWindow", u"Days", None))

        self.CheckBox_Stopwatch.setText("")
    # retranslateUi

