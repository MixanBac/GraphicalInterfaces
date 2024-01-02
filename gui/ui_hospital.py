import pyodbc
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import helper

class Ui_MainWindow(object):
    global server, database, username, password, cnxn, cursor
    server = '' 
    database = 'gui_base' 
    username = '' 
    password = '' 
    cnxn = pyodbc.connect("DRIVER={CData ODBC Driver for PostgreSQL}; DATABASE=hospital; UID=postgres; PWD=postgres; SERVER=localhost; PORT=5432;")
    cursor = cnxn.cursor()
      
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1910, 1040)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1910, 1040))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum) # type: ignore 
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum) # type: ignore 
        self.gridLayout_3.addItem(spacerItem1, 1, 4, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed) # type: ignore 
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed) # type: ignore 
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.execut_query)
        self.gridLayout_3.addWidget(self.pushButton, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum) # type: ignore 
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget_2, 2, 0, 1, 6)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_connection = QtWidgets.QAction(MainWindow)
        self.actionOpen_connection.setObjectName("actionOpen_connection")
        self.actionOpen_connection.triggered.connect(self.open_connect)
        self.actionClose_connection = QtWidgets.QAction(MainWindow)
        self.actionClose_connection.setObjectName("actionClose_connection")
        self.actionClose_connection.triggered.connect(self.close_connect)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.triggered.connect(self.help_click)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.about_click)
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit_2.triggered.connect(self.exit_click)
        self.menuMenu.addAction(self.actionOpen_connection)
        self.menuMenu.addAction(self.actionClose_connection)
        self.menuMenu.addAction(self.actionExit_2)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exit_click(self):
        self.close_connect()
        quit()

    def about_click(self):
        msg_text = 'Лабораторная работа №3 Неженского М.С.'
        helper.ld_data.show_message(msg_text, QMessageBox.Information) # type: ignore

    def open_connect(self): 
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        cnxn = pyodbc.connect("DRIVER={CData ODBC Driver for PostgreSQL}; DATABASE=hospital; UID=postgres; PWD=postgres; SERVER=localhost; PORT=5432;")
        cursor = cnxn.cursor()
        helper.ld_data.ld_labels(cursor, self.tableWidget)              
        helper.ld_data.ld_data_main_window(cursor, self.tableWidget)
        self.comboBox.addItems(helper.ld_data.load_name_tables(cursor))
    
    def close_connect(self): 
        cnxn = pyodbc.connect("DRIVER={CData ODBC Driver for PostgreSQL}; DATABASE=hospital; UID=postgres; PWD=postgres; SERVER=localhost; PORT=5432;")
        cnxn.close() # type: ignore
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.clear()
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.comboBox.clear()

    def help_click(self):
        msg_text = 'Лабораторная работа №3 Неженского М.С.'
        helper.ld_data.show_message(msg_text, QMessageBox.Information) # type: ignore

    def execut_query(self):
        if(self.comboBox.currentText()!=""):
            self.tableWidget_2.clear()
            self.tableWidget_2.setColumnCount(1)
            self.tableWidget_2.setRowCount(0)
            cnxn = pyodbc.connect("DRIVER={CData ODBC Driver for PostgreSQL}; DATABASE=hospital; UID=postgres; PWD=postgres; SERVER=localhost; PORT=5432;")
            cursor = cnxn.cursor()
            helper.ld_data.ld_data_add_window(cursor, self.tableWidget_2, self.comboBox.currentText())
        else:
            msg_text = 'Нет связи с Базой данных'
            helper.ld_data.show_message(msg_text, QMessageBox.Warning) # type: ignore

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Просмотр базы данных"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "SELECT * FROM patient LIMIT 100"))
        self.pushButton.setText(_translate("MainWindow", "Выполнить запрос"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "SELECT column_name FROM patient LIMIT 100"))
        self.menuMenu.setTitle(_translate("MainWindow", "Меню подключения"))
        self.menuAbout.setTitle(_translate("MainWindow", "Еще"))
        self.actionOpen_connection.setText(_translate("MainWindow", "Открыть соединение"))
        self.actionClose_connection.setText(_translate("MainWindow", "Закрыть соединение"))
        self.actionHelp.setText(_translate("MainWindow", "Помощь"))
        self.actionAbout.setText(_translate("MainWindow", "О программе"))
        self.actionExit_2.setText(_translate("MainWindow", "Выход"))
