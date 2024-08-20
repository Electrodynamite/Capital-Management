from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import sys
import os
import keyboard
import time
import mysql.connector as db_module


class Options:
    def listen_key(self, pressed_key: str, functions: list, args=None):
        while True:
            time.sleep(0.15)
            if keyboard.read_key() == pressed_key or keyboard.read_key() in pressed_key:
                if args:
                    for function, arg in zip(functions, args):
                        function(arg)
                else:
                    for function in functions:
                        function()

    def call_database(self, db_host: str, db_username: str, db_password: str, db_name: str, commands: list=None):
        try:
            temp_db = db_module.connect(
                host=db_host,
                username=db_username,
                password=db_password
            )
            temp_cursor = temp_db.cursor()
            temp_cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
            temp_db.close()
            mydb = db_module.connect(
                host=db_host,
                username=db_username,
                password=db_password,
                database=db_name
            )
            mycursor = mydb.cursor()
            if commands:
                for command in commands:
                    mycursor.execute(command)
        except:
            sys.exit()
        finally:
            mydb.close()


class uiPage(object):
    def setupUi(self, main_window):
        self.option = Options()
        main_window.setObjectName("mainWindow")
        main_window.resize(1340, 800)
        main_window.setMinimumSize(QtCore.QSize(1340, 750))
        main_window.setMaximumSize(QtCore.QSize(1340, 800))
        main_window.setSizeIncrement(QtCore.QSize(0, 0))
        main_window.setBaseSize(QtCore.QSize(1350, 778))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setItalic(True)
        main_window.setFont(font)
        main_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        if hasattr(sys, '_MEIPASS'):
            icon_path1 = os.path.join(sys._MEIPASS, "Icon.ico")
        else:
            icon_path1 = os.path.join(os.path.dirname(__file__), "Icon.ico")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(icon_path1), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon1)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(0, 0, 1345, 805))
        self.tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab.setElideMode(QtCore.Qt.ElideNone)
        self.tab.setTabBarAutoHide(False)
        self.tab.setObjectName("tab")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.frame = QtWidgets.QFrame(self.main_tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1331, 751))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setItalic(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.profit_input_text_box = QtWidgets.QLineEdit(self.frame)
        self.profit_input_text_box.setGeometry(QtCore.QRect(10, 10, 310, 50))
        self.profit_input_text_box.setInputMask("")
        self.profit_input_text_box.setText("")
        self.profit_input_text_box.setMaxLength(16)
        self.profit_input_text_box.setFrame(True)
        self.profit_input_text_box.setObjectName("profitInput")
        self.description_text_box = QtWidgets.QLineEdit(self.frame)
        self.description_text_box.setGeometry(QtCore.QRect(10, 130, 310, 50))
        self.description_text_box.setInputMask("")
        self.description_text_box.setText("")
        self.description_text_box.setMaxLength(70)
        self.description_text_box.setObjectName("description")
        self.submit_button = QtWidgets.QPushButton(self.frame)
        self.submit_button.setGeometry(QtCore.QRect(60, 190, 210, 60))
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        if hasattr(sys, '_MEIPASS'):
            icon_path2 = os.path.join(sys._MEIPASS, "Submit.ico")
        else:
            icon_path2 = os.path.join(os.path.dirname(__file__), "Icons", "Submit.ico")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(icon_path2), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit_button.setIcon(icon2)
        self.submit_button.setObjectName("submitBtn")
        self.delete_text_box = QtWidgets.QLineEdit(self.frame)
        self.delete_text_box.setEnabled(False)
        self.delete_text_box.setGeometry(QtCore.QRect(10, 280, 311, 50))
        self.delete_text_box.setInputMask("")
        self.delete_text_box.setText("")
        self.delete_text_box.setMaxLength(10)
        self.delete_text_box.setObjectName("deleteTxtbox")
        self.delete_button = QtWidgets.QPushButton(self.frame)
        self.delete_button.setEnabled(False)
        self.delete_button.setGeometry(QtCore.QRect(60, 340, 210, 60))
        self.delete_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_button.setAutoFillBackground(False)
        if hasattr(sys, '_MEIPASS'):
            icon_path3 = os.path.join(sys._MEIPASS, "Trash bin.ico")
        else:
            icon_path3 = os.path.join(os.path.dirname(__file__), "Icons", "Trash bin.ico")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(icon_path3), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon3)
        self.delete_button.setFlat(False)
        self.delete_button.setObjectName("deleteBtn")
        self.details_text_browser = QtWidgets.QTextBrowser(self.frame)
        self.details_text_browser.setGeometry(QtCore.QRect(340, 10, 980, 400))
        self.details_text_browser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.details_text_browser.setTabChangesFocus(False)
        self.details_text_browser.setDocumentTitle("")
        self.details_text_browser.setObjectName("details")
        self.recent_operations_text_browser = QtWidgets.QTextBrowser(self.frame)
        self.recent_operations_text_browser.setGeometry(QtCore.QRect(10, 420, 1311, 321))
        self.recent_operations_text_browser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.recent_operations_text_browser.setObjectName("recentOperations")
        self.currency_unit_text_box = QtWidgets.QLineEdit(self.frame)
        self.currency_unit_text_box.setGeometry(QtCore.QRect(10, 70, 310, 50))
        self.currency_unit_text_box.setInputMask("")
        self.currency_unit_text_box.setText("")
        self.currency_unit_text_box.setMaxLength(24)
        self.currency_unit_text_box.setObjectName("currencyuUnitTxtBtn")
        self.tab.addTab(self.main_tab, "")
        self.all_operations_tab = QtWidgets.QWidget()
        self.all_operations_tab.setObjectName("all_operations")
        self.all_operations_text_browser = QtWidgets.QTextBrowser(self.all_operations_tab)
        self.all_operations_text_browser.setGeometry(QtCore.QRect(10, 10, 1311, 730))
        self.all_operations_text_browser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.all_operations_text_browser.setObjectName("allOperations")
        self.tab.addTab(self.all_operations_tab, "")
        main_window.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(main_window)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.setTabOrder(self.tab, self.profit_input_text_box)
        main_window.setTabOrder(self.profit_input_text_box, self.currency_unit_text_box)
        main_window.setTabOrder(self.currency_unit_text_box, self.description_text_box)
        main_window.setTabOrder(self.description_text_box, self.submit_button)
        main_window.setTabOrder(self.submit_button, self.details_text_browser)
        main_window.setTabOrder(self.details_text_browser, self.delete_text_box)
        main_window.setTabOrder(self.delete_text_box, self.delete_button)
        main_window.setTabOrder(self.delete_button, self.recent_operations_text_browser)
        main_window.setTabOrder(self.recent_operations_text_browser, self.all_operations_text_browser)

        self.profit_input_text_box.setFocus()
        self.setup_threads()
        self.option.call_database('localhost', 'root', '', 'capital_management')
    
    def focus_next_widget(self):
        if self.profit_input_text_box.hasFocus():
            self.currency_unit_text_box.setFocus()
        elif self.currency_unit_text_box.hasFocus():
            self.description_text_box.setFocus()
        elif self.description_text_box.hasFocus():
            self.delete_text_box.setFocus()

    def focus_previous_widget(self):
        if self.description_text_box.hasFocus():
            self.currency_unit_text_box.setFocus()
        elif self.currency_unit_text_box.hasFocus():
            self.profit_input_text_box.setFocus()
        elif self.delete_text_box.hasFocus():
            self.description_text_box.setFocus()

    def setup_threads(self):
        thread_function1 = [self.focus_next_widget]
        thread_function2 = [self.focus_next_widget]
        thread_function3 = [self.focus_previous_widget]
        keys_thread1 = Thread(name='down', target=self.option.listen_key, args=('down', thread_function1))
        keys_thread2 = Thread(name='enter', target=self.option.listen_key, args=('enter', thread_function2))
        keys_thread3 = Thread(name='up', target=self.option.listen_key, args=('up', thread_function3))
        keys_thread1.daemon = keys_thread2.daemon = keys_thread3.daemon = True
        keys_thread1.start()
        keys_thread2.start()
        keys_thread3.start()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Capital Management"))
        self.profit_input_text_box.setPlaceholderText(_translate("mainWindow", "Profit*"))
        self.description_text_box.setPlaceholderText(_translate("mainWindow", "Description*"))
        self.submit_button.setText(_translate("mainWindow", "Submit"))
        self.submit_button.setShortcut(_translate("mainWindow", "Ctrl+Return"))
        self.delete_text_box.setPlaceholderText(_translate("mainWindow", "Operation ID"))
        self.delete_button.setText(_translate("mainWindow", "Delete operation"))
        self.delete_button.setShortcut(_translate("mainWindow", "Ctrl+F10"))
        self.details_text_browser.setPlaceholderText(_translate("mainWindow", "Operation details"))
        self.recent_operations_text_browser.setPlaceholderText(_translate("mainWindow", "Recent operations"))
        self.currency_unit_text_box.setPlaceholderText(_translate("mainWindow", "Currency unit*"))
        self.tab.setTabText(self.tab.indexOf(self.main_tab), _translate("mainWindow", "Main tab"))
        self.all_operations_text_browser.setPlaceholderText(_translate("mainWindow", "All operations"))
        self.tab.setTabText(self.tab.indexOf(self.all_operations_tab), _translate("mainWindow", "All operations"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = uiPage()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
