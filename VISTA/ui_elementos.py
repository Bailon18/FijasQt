# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementosbKUXIm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import source

class Ui_Elementos(object):
    def setupUi(self, Elementos):
        if not Elementos.objectName():
            Elementos.setObjectName(u"Elementos")
        Elementos.resize(936, 711)
        Elementos.setStyleSheet(u"QFrame#frameOne{\n"
"	background:qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 106, 48, 255), stop:1 rgba(85, 215, 0, 255));\n"
"}\n"
"\n"
"\n"
"QFrame#frameTwo{\n"
"	background:rgba(0, 0, 0, 140);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(Elementos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frameOne = QFrame(self.centralwidget)
        self.frameOne.setObjectName(u"frameOne")
        self.gridLayout_2 = QGridLayout(self.frameOne)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.frameTwo = QFrame(self.frameOne)
        self.frameTwo.setObjectName(u"frameTwo")
        self.gridLayout_15 = QGridLayout(self.frameTwo)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame = QFrame(self.frameTwo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.botOcho = QPushButton(self.frame)
        self.botOcho.setObjectName(u"botOcho")

        self.gridLayout_5.addWidget(self.botOcho, 1, 3, 1, 1)

        self.botTres = QPushButton(self.frame)
        self.botTres.setObjectName(u"botTres")

        self.gridLayout_5.addWidget(self.botTres, 0, 2, 1, 1)

        self.botCinco = QPushButton(self.frame)
        self.botCinco.setObjectName(u"botCinco")

        self.gridLayout_5.addWidget(self.botCinco, 1, 0, 1, 1)

        self.botDos = QPushButton(self.frame)
        self.botDos.setObjectName(u"botDos")

        self.gridLayout_5.addWidget(self.botDos, 0, 1, 1, 1)

        self.botSeis = QPushButton(self.frame)
        self.botSeis.setObjectName(u"botSeis")

        self.gridLayout_5.addWidget(self.botSeis, 1, 1, 1, 1)

        self.botSiete = QPushButton(self.frame)
        self.botSiete.setObjectName(u"botSiete")

        self.gridLayout_5.addWidget(self.botSiete, 1, 2, 1, 1)

        self.botCuatro = QPushButton(self.frame)
        self.botCuatro.setObjectName(u"botCuatro")

        self.gridLayout_5.addWidget(self.botCuatro, 0, 3, 1, 1)

        self.botUno = QPushButton(self.frame)
        self.botUno.setObjectName(u"botUno")

        self.gridLayout_5.addWidget(self.botUno, 0, 0, 1, 1)

        self.botExtra = QPushButton(self.frame)
        self.botExtra.setObjectName(u"botExtra")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botExtra.sizePolicy().hasHeightForWidth())
        self.botExtra.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.botExtra, 0, 4, 2, 1)


        self.gridLayout_15.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frameTwo)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.frame_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabUno = QWidget()
        self.tabUno.setObjectName(u"tabUno")
        self.gridLayout_10 = QGridLayout(self.tabUno)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_6 = QFrame(self.tabUno)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.gridLayout_9 = QGridLayout(self.frame_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.spinUno = QSpinBox(self.frame_6)
        self.spinUno.setObjectName(u"spinUno")

        self.gridLayout_9.addWidget(self.spinUno, 3, 0, 1, 1)

        self.labelPrueba = QLabel(self.frame_6)
        self.labelPrueba.setObjectName(u"labelPrueba")
        self.labelPrueba.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_9.addWidget(self.labelPrueba, 0, 0, 1, 2)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(150, 25))

        self.gridLayout_9.addWidget(self.label_14, 1, 0, 1, 1)

        self.spinDos = QDoubleSpinBox(self.frame_6)
        self.spinDos.setObjectName(u"spinDos")

        self.gridLayout_9.addWidget(self.spinDos, 5, 0, 1, 1)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 25))

        self.gridLayout_9.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(150, 25))

        self.gridLayout_9.addWidget(self.label_9, 1, 1, 1, 1)

        self.dialUno = QDial(self.frame_6)
        self.dialUno.setObjectName(u"dialUno")

        self.gridLayout_9.addWidget(self.dialUno, 3, 1, 3, 1)


        self.gridLayout_10.addWidget(self.frame_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabUno, "")
        self.tabDos = QWidget()
        self.tabDos.setObjectName(u"tabDos")
        self.gridLayout_13 = QGridLayout(self.tabDos)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.listaUno = QListWidget(self.tabDos)
        self.listaUno.setObjectName(u"listaUno")

        self.gridLayout_13.addWidget(self.listaUno, 2, 0, 1, 2)

        self.label_8 = QLabel(self.tabDos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_13.addWidget(self.label_8, 0, 0, 1, 1)

        self.lcdUno = QLCDNumber(self.tabDos)
        self.lcdUno.setObjectName(u"lcdUno")
        self.lcdUno.setMinimumSize(QSize(0, 50))

        self.gridLayout_13.addWidget(self.lcdUno, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tabDos, "")
        self.tabTres = QWidget()
        self.tabTres.setObjectName(u"tabTres")
        self.gridLayout_16 = QGridLayout(self.tabTres)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_11 = QFrame(self.tabTres)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Plain)
        self.gridLayout_17 = QGridLayout(self.frame_11)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.calendarUno = QCalendarWidget(self.frame_11)
        self.calendarUno.setObjectName(u"calendarUno")
        self.calendarUno.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        self.gridLayout_17.addWidget(self.calendarUno, 0, 0, 1, 1)

        self.progressUno = QProgressBar(self.frame_11)
        self.progressUno.setObjectName(u"progressUno")
        self.progressUno.setValue(24)

        self.gridLayout_17.addWidget(self.progressUno, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_11, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabTres, "")
        self.tabCuatro = QWidget()
        self.tabCuatro.setObjectName(u"tabCuatro")
        self.verticalLayout_8 = QVBoxLayout(self.tabCuatro)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.tabCuatro)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.tabWidget.addTab(self.tabCuatro, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.toolBox = QToolBox(self.frame_4)
        self.toolBox.setObjectName(u"toolBox")
        self.pageUno = QWidget()
        self.pageUno.setObjectName(u"pageUno")
        self.pageUno.setGeometry(QRect(0, 0, 362, 264))
        self.gridLayout_8 = QGridLayout(self.pageUno)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_9 = QFrame(self.pageUno)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.frame_7)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.radioP1 = QRadioButton(self.groupBox_2)
        self.radioP1.setObjectName(u"radioP1")

        self.verticalLayout_6.addWidget(self.radioP1)

        self.radioP2 = QRadioButton(self.groupBox_2)
        self.radioP2.setObjectName(u"radioP2")

        self.verticalLayout_6.addWidget(self.radioP2)

        self.radioP3 = QRadioButton(self.groupBox_2)
        self.radioP3.setObjectName(u"radioP3")

        self.verticalLayout_6.addWidget(self.radioP3)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.frame_7)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.radioA1 = QRadioButton(self.groupBox)
        self.radioA1.setObjectName(u"radioA1")

        self.verticalLayout_7.addWidget(self.radioA1)

        self.radioA2 = QRadioButton(self.groupBox)
        self.radioA2.setObjectName(u"radioA2")

        self.verticalLayout_7.addWidget(self.radioA2)

        self.radioA3 = QRadioButton(self.groupBox)
        self.radioA3.setObjectName(u"radioA3")

        self.verticalLayout_7.addWidget(self.radioA3)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.horizontalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_4 = QGroupBox(self.frame_8)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkT1 = QCheckBox(self.groupBox_4)
        self.checkT1.setObjectName(u"checkT1")

        self.verticalLayout_5.addWidget(self.checkT1)

        self.checkT2 = QCheckBox(self.groupBox_4)
        self.checkT2.setObjectName(u"checkT2")

        self.verticalLayout_5.addWidget(self.checkT2)

        self.checkT3 = QCheckBox(self.groupBox_4)
        self.checkT3.setObjectName(u"checkT3")

        self.verticalLayout_5.addWidget(self.checkT3)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.frame_8)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkY1 = QCheckBox(self.groupBox_3)
        self.checkY1.setObjectName(u"checkY1")

        self.verticalLayout_4.addWidget(self.checkY1)

        self.checkY2 = QCheckBox(self.groupBox_3)
        self.checkY2.setObjectName(u"checkY2")

        self.verticalLayout_4.addWidget(self.checkY2)

        self.checkY3 = QCheckBox(self.groupBox_3)
        self.checkY3.setObjectName(u"checkY3")

        self.verticalLayout_4.addWidget(self.checkY3)


        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.horizontalLayout.addWidget(self.frame_8)


        self.gridLayout_8.addWidget(self.frame_9, 0, 0, 1, 1)

        self.toolBox.addItem(self.pageUno, u"pageUno")
        self.pageDos = QWidget()
        self.pageDos.setObjectName(u"pageDos")
        self.pageDos.setGeometry(QRect(0, 0, 362, 281))
        self.gridLayout_14 = QGridLayout(self.pageDos)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_11 = QLabel(self.pageDos)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_14.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_17 = QLabel(self.pageDos)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(320, 220))
        self.label_17.setPixmap(QPixmap(u":/imagen/cover.jpg"))
        self.label_17.setScaledContents(True)

        self.gridLayout_14.addWidget(self.label_17, 6, 0, 1, 1)

        self.horaUno = QTimeEdit(self.pageDos)
        self.horaUno.setObjectName(u"horaUno")

        self.gridLayout_14.addWidget(self.horaUno, 4, 0, 1, 1)

        self.toolBox.addItem(self.pageDos, u"pageDos")

        self.verticalLayout.addWidget(self.toolBox)


        self.gridLayout_15.addWidget(self.frame_4, 0, 1, 4, 1)

        self.frame_2 = QFrame(self.frameTwo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboUno = QComboBox(self.frame_2)
        self.comboUno.setObjectName(u"comboUno")
        self.comboUno.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.comboUno, 2, 0, 1, 1)

        self.comboDos = QComboBox(self.frame_2)
        self.comboDos.setObjectName(u"comboDos")

        self.gridLayout_4.addWidget(self.comboDos, 2, 1, 1, 1)

        self.dateUno = QDateEdit(self.frame_2)
        self.dateUno.setObjectName(u"dateUno")
        self.dateUno.setAlignment(Qt.AlignCenter)
        self.dateUno.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.dateUno, 2, 2, 1, 1)

        self.dateDos = QDateTimeEdit(self.frame_2)
        self.dateDos.setObjectName(u"dateDos")
        self.dateDos.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.dateDos, 2, 3, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 0, 3, 1, 1)


        self.gridLayout_15.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_10 = QFrame(self.frameTwo)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.gridLayout_11 = QGridLayout(self.frame_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.botTrece = QPushButton(self.frame_10)
        self.botTrece.setObjectName(u"botTrece")

        self.gridLayout_11.addWidget(self.botTrece, 1, 4, 1, 1)

        self.botDoce = QPushButton(self.frame_10)
        self.botDoce.setObjectName(u"botDoce")

        self.gridLayout_11.addWidget(self.botDoce, 1, 3, 1, 1)

        self.botOnce = QPushButton(self.frame_10)
        self.botOnce.setObjectName(u"botOnce")

        self.gridLayout_11.addWidget(self.botOnce, 1, 2, 1, 1)

        self.botNueve = QPushButton(self.frame_10)
        self.botNueve.setObjectName(u"botNueve")

        self.gridLayout_11.addWidget(self.botNueve, 1, 0, 1, 1)

        self.botDiez = QPushButton(self.frame_10)
        self.botDiez.setObjectName(u"botDiez")

        self.gridLayout_11.addWidget(self.botDiez, 1, 1, 1, 1)

        self.botCatorce = QPushButton(self.frame_10)
        self.botCatorce.setObjectName(u"botCatorce")

        self.gridLayout_11.addWidget(self.botCatorce, 1, 5, 1, 1)

        self.stackedWidget = QStackedWidget(self.frame_10)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_6 = QGridLayout(self.page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tablaUno = QTableWidget(self.page)
        if (self.tablaUno.columnCount() < 4):
            self.tablaUno.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaUno.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaUno.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaUno.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaUno.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tablaUno.setObjectName(u"tablaUno")
        self.tablaUno.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaUno.setAlternatingRowColors(True)
        self.tablaUno.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablaUno.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablaUno.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tablaUno.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout_6.addWidget(self.tablaUno, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_12 = QGridLayout(self.page_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(350, 240))
        self.label_15.setPixmap(QPixmap(u":/imagen/cover.jpg"))
        self.label_15.setScaledContents(True)

        self.gridLayout_12.addWidget(self.label_15, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_11.addWidget(self.stackedWidget, 0, 0, 1, 6)


        self.gridLayout_15.addWidget(self.frame_10, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.frameTwo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineUno = QLineEdit(self.frame_3)
        self.lineUno.setObjectName(u"lineUno")
        self.lineUno.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.lineUno, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 3, 1, 1, 1)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.textUno = QTextEdit(self.frame_3)
        self.textUno.setObjectName(u"textUno")
        self.textUno.setAcceptRichText(False)

        self.gridLayout_3.addWidget(self.textUno, 5, 1, 1, 1)

        self.lineDos = QLineEdit(self.frame_3)
        self.lineDos.setObjectName(u"lineDos")

        self.gridLayout_3.addWidget(self.lineDos, 1, 1, 1, 1)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSlider = QSlider(self.frame_5)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.horizontalSlider, 3, 0, 1, 1)

        self.verticalSlider = QSlider(self.frame_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_7.addWidget(self.verticalSlider, 3, 1, 1, 1)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 0, 0, 1, 2)


        self.gridLayout_3.addWidget(self.frame_5, 3, 0, 3, 1)


        self.gridLayout_15.addWidget(self.frame_3, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameTwo, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frameOne, 0, 0, 1, 1)

        Elementos.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_8.setBuddy(self.label_8)
        self.label_17.setBuddy(self.label_8)
        self.label_15.setBuddy(self.label_8)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Elementos)

        self.tabWidget.setCurrentIndex(2)
        self.toolBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Elementos)
    # setupUi

    def retranslateUi(self, Elementos):
        Elementos.setWindowTitle(QCoreApplication.translate("Elementos", u"Metodos y Eventos v3 - ALEX7320", None))
        self.botOcho.setText(QCoreApplication.translate("Elementos", u"ocho", None))
        self.botTres.setText(QCoreApplication.translate("Elementos", u"tres", None))
        self.botCinco.setText(QCoreApplication.translate("Elementos", u"cinco", None))
        self.botDos.setText(QCoreApplication.translate("Elementos", u"dos", None))
        self.botSeis.setText(QCoreApplication.translate("Elementos", u"seis", None))
        self.botSiete.setText(QCoreApplication.translate("Elementos", u"siete", None))
        self.botCuatro.setText(QCoreApplication.translate("Elementos", u"cuatro", None))
        self.botUno.setText(QCoreApplication.translate("Elementos", u"uno", None))
        self.botExtra.setText(QCoreApplication.translate("Elementos", u"extra", None))
        self.labelPrueba.setText(QCoreApplication.translate("Elementos", u"LABEL USO LIBRE", None))
        self.label_14.setText(QCoreApplication.translate("Elementos", u"spin Uno", None))
        self.label_3.setText(QCoreApplication.translate("Elementos", u"spin dos", None))
        self.label_9.setText(QCoreApplication.translate("Elementos", u"dial uno", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUno), QCoreApplication.translate("Elementos", u"tabUno1", None))
        self.label_8.setText(QCoreApplication.translate("Elementos", u"lcd y lista", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDos), QCoreApplication.translate("Elementos", u"tabDos2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTres), QCoreApplication.translate("Elementos", u"tabTres3", None))
        self.label.setText(QCoreApplication.translate("Elementos", u"texto de prueba", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCuatro), QCoreApplication.translate("Elementos", u"tabCuatro4", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Elementos", u"Radio grupo P", None))
        self.radioP1.setText(QCoreApplication.translate("Elementos", u"p1", None))
        self.radioP2.setText(QCoreApplication.translate("Elementos", u"p2", None))
        self.radioP3.setText(QCoreApplication.translate("Elementos", u"p3", None))
        self.groupBox.setTitle(QCoreApplication.translate("Elementos", u"Radio grupo A", None))
        self.radioA1.setText(QCoreApplication.translate("Elementos", u"a1", None))
        self.radioA2.setText(QCoreApplication.translate("Elementos", u"a2", None))
        self.radioA3.setText(QCoreApplication.translate("Elementos", u"a3", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Elementos", u"Check grupo P", None))
        self.checkT1.setText(QCoreApplication.translate("Elementos", u"t1", None))
        self.checkT2.setText(QCoreApplication.translate("Elementos", u"t2", None))
        self.checkT3.setText(QCoreApplication.translate("Elementos", u"t3", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Elementos", u"Check grupo Y", None))
        self.checkY1.setText(QCoreApplication.translate("Elementos", u"y1", None))
        self.checkY2.setText(QCoreApplication.translate("Elementos", u"y2", None))
        self.checkY3.setText(QCoreApplication.translate("Elementos", u"y3", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageUno), QCoreApplication.translate("Elementos", u"pageUno", None))
        self.label_11.setText(QCoreApplication.translate("Elementos", u"time uno", None))
        self.label_17.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageDos), QCoreApplication.translate("Elementos", u"pageDos", None))
        self.label_7.setText(QCoreApplication.translate("Elementos", u"date uno", None))
        self.label_5.setText(QCoreApplication.translate("Elementos", u"combo dos", None))
        self.label_6.setText(QCoreApplication.translate("Elementos", u"combo uno", None))
        self.label_10.setText(QCoreApplication.translate("Elementos", u"date dos", None))
        self.botTrece.setText(QCoreApplication.translate("Elementos", u"trece", None))
        self.botDoce.setText(QCoreApplication.translate("Elementos", u"doce", None))
        self.botOnce.setText(QCoreApplication.translate("Elementos", u"once", None))
        self.botNueve.setText(QCoreApplication.translate("Elementos", u"nueve", None))
        self.botDiez.setText(QCoreApplication.translate("Elementos", u"diez", None))
        self.botCatorce.setText(QCoreApplication.translate("Elementos", u"catorce", None))
        ___qtablewidgetitem = self.tablaUno.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Elementos", u"cod", None));
        ___qtablewidgetitem1 = self.tablaUno.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Elementos", u"nombre", None));
        ___qtablewidgetitem2 = self.tablaUno.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Elementos", u"mail", None));
        ___qtablewidgetitem3 = self.tablaUno.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Elementos", u"web", None));
        self.label_15.setText("")
        self.label_2.setText(QCoreApplication.translate("Elementos", u"text uno", None))
        self.label_12.setText(QCoreApplication.translate("Elementos", u"line dos", None))
        self.label_4.setText(QCoreApplication.translate("Elementos", u"line uno", None))
        self.label_13.setText(QCoreApplication.translate("Elementos", u"Slider h, v", None))
    # retranslateUi

