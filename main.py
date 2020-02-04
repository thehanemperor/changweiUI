from PyQt5.QtCore import QDateTime, Qt, QTimer,pyqtSlot,QSize    
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget,QFormLayout,QMainWindow)
from crawler import Crawlers
import time
import random


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())
        print(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QCheckBox("&Disable widgets")

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()
        self.createProgressBar()

        styleComboBox.activated[str].connect(self.changeStyle)
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        topLayout.addWidget(self.useStylePaletteCheckBox)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        #mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 4,1)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 0,1,2)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Styles")
        self.changeStyle('Fusion')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")
        textLabel = QLabel("搜索词:")
       
        tab2 = QWidget()
        textEdit = QTextEdit()
        textEdit.setPlainText("晚会\n"
                              "米\n" 
                              "直播\n"
                              "亚洲\n"
                              )

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

       

        layout = QVBoxLayout()
        layout.addWidget(textLabel)
        layout.addWidget(tab2)
        
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Group 2")
        textLabel = QLabel("忽略搜索词:")
       
        tab2 = QWidget()
        textEdit = QTextEdit()
        #textEdit.setPlainText()

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

       

        layout = QVBoxLayout()
        layout.addWidget(textLabel)
        layout.addWidget(tab2)
        
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

        # self.topRightGroupBox = QGroupBox("Group 2")

        # defaultPushButton = QPushButton("Default Push Button")
        # defaultPushButton.setDefault(True)

        # togglePushButton = QPushButton("Toggle Push Button")
        # togglePushButton.setCheckable(True)
        # togglePushButton.setChecked(True)

        # flatPushButton = QPushButton("Flat Push Button")
        # flatPushButton.setFlat(True)

        # layout = QVBoxLayout()
        # layout.addWidget(defaultPushButton)
        # layout.addWidget(togglePushButton)
        # layout.addWidget(flatPushButton)
        # layout.addStretch(1)
        # self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Twinkle, twinkle, little star,\n"
                              "How I wonder what you are.\n" 
                              "Up above the world so high,\n"
                              "Like a diamond in the sky.\n"
                              "Twinkle, twinkle, little star,\n" 
                              "How I wonder what you are!\n")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Table")
        self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        usernameEdit = QLineEdit('root')
        passwordEdit = QLineEdit('s3cRe7')
        passwordEdit.setEchoMode(QLineEdit.Password)
        databaseEdit = QLineEdit()
        tableEdit = QLineEdit()
        keywordLengthLess = QLineEdit()
        keywordLengthGreat = QLineEdit()
        refresh = QLineEdit()


        radioButton1 = QRadioButton("搜狗下拉")
        radioButton2 = QRadioButton("神马下拉")
        radioButton3 = QRadioButton("百度下拉")
        radioButton4 = QRadioButton("搜狗相关搜索")
        radioButton5 = QRadioButton("神马相关搜索")
        radioButton6 = QRadioButton("百度相关搜索")
        radioButton1.setChecked(True)

        confirmButton = QPushButton("开始查询",self)
        confirmButton.setToolTip("query button")
        confirmButton.clicked.connect(self.runCrawler)


        # flo = QFormLayout()
        # flo.addRow(QLabel("数据库用户名"),lineEdit,spinBox)

        layout = QGridLayout()
        layout.addWidget(QLabel("数据库用户名:"),1,1)
        layout.addWidget(usernameEdit,1,2)
        layout.addWidget(QLabel("数据库密码:"),1,3)
        layout.addWidget(passwordEdit, 1,4)

        layout.addWidget(QLabel("数据库:"),2,1)
        layout.addWidget(databaseEdit,2,2)
        layout.addWidget(QLabel("数据库表名:"),2,3)
        layout.addWidget(tableEdit, 2,4)

        layout.addWidget(QLabel("关键词不少于:"),3,1)
        layout.addWidget(keywordLengthGreat,3,2)
        layout.addWidget(QLabel("关键词不大于:"),3,3)
        layout.addWidget(keywordLengthLess, 3,4)
        layout.addWidget(QLabel("下拉字数:"),3,5)
        layout.addWidget(refresh, 3,6)

        layout.addWidget(radioButton1,4,1)
        layout.addWidget(radioButton2,4,2)
        layout.addWidget(radioButton3,4,3)
        layout.addWidget(radioButton4,5,1)
        layout.addWidget(radioButton5,5,2)
        layout.addWidget(radioButton6,5,3)
        layout.addWidget(confirmButton,6,1)
        
       

        # layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        # layout.addWidget(slider, 3, 0)
        # layout.addWidget(scrollBar, 4, 0)
        # layout.addWidget(dial, 3, 1, 2, 1)
        # layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)
    
    @pyqtSlot()
    def runCrawler(self):
        print("function executed")


    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)

class Main_window(QMainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.crawler = Crawlers()
        
        self.setWindowTitle("My Awesome App")
        self.resize(800, 600)

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()
        gridlayout = QGridLayout()
        
        gridlayout.addWidget(self.topLeftGroupBox, 1, 0)
        gridlayout.addWidget(self.topRightGroupBox, 1, 1)
        gridlayout.addWidget(self.bottomLeftTabWidget, 4,1)
        gridlayout.addWidget(self.bottomRightGroupBox, 2, 0,1,2)
        
        widget = QWidget()
        widget.setLayout(gridlayout)
        self.setCentralWidget(widget)
        self.show()
    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")
        textLabel = QLabel("搜索词:")
       
        tab2 = QWidget()
        self.searchList = QTextEdit()
        self.searchList.setPlainText("晚会\n"
                              "米\n" 
                              "直播\n"
                              "亚洲\n"
                              )

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(self.searchList)
        tab2.setLayout(tab2hbox)

       

        layout = QVBoxLayout()
        layout.addWidget(textLabel)
        layout.addWidget(tab2)
        
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)   

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Group 2")
        textLabel = QLabel("忽略搜索词:")
       
        tab2 = QWidget()
        textEdit = QTextEdit()
        #textEdit.setPlainText()

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

       

        layout = QVBoxLayout()
        layout.addWidget(textLabel)
        layout.addWidget(tab2)
        
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

        # self.topRightGroupBox = QGroupBox("Group 2")

        # defaultPushButton = QPushButton("Default Push Button")
        # defaultPushButton.setDefault(True)

        # togglePushButton = QPushButton("Toggle Push Button")
        # togglePushButton.setCheckable(True)
        # togglePushButton.setChecked(True)

        # flatPushButton = QPushButton("Flat Push Button")
        # flatPushButton.setFlat(True)

        # layout = QVBoxLayout()
        # layout.addWidget(defaultPushButton)
        # layout.addWidget(togglePushButton)
        # layout.addWidget(flatPushButton)
        # layout.addStretch(1)
        # self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Twinkle, twinkle, little star,\n"
                              "How I wonder what you are.\n" 
                              "Up above the world so high,\n"
                              "Like a diamond in the sky.\n"
                              "Twinkle, twinkle, little star,\n" 
                              "How I wonder what you are!\n")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Table")
        self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        usernameEdit = QLineEdit('root')
        passwordEdit = QLineEdit('s3cRe7')
        passwordEdit.setEchoMode(QLineEdit.Password)
        databaseEdit = QLineEdit()
        tableEdit = QLineEdit()
        keywordLengthLess = QLineEdit()
        keywordLengthGreat = QLineEdit()
        refresh = QLineEdit()


        radioButton1 = QRadioButton("搜狗下拉")
        radioButton2 = QRadioButton("神马下拉")
        radioButton3 = QRadioButton("百度下拉")
        radioButton4 = QRadioButton("搜狗相关搜索")
        radioButton5 = QRadioButton("神马相关搜索")
        radioButton6 = QRadioButton("百度相关搜索")
        radioButton1.setChecked(True)

        confirmButton = QPushButton("开始查询",self)
        confirmButton.setToolTip("query button")
        confirmButton.clicked.connect(self.runCrawler)


        # flo = QFormLayout()
        # flo.addRow(QLabel("数据库用户名"),lineEdit,spinBox)

        layout = QGridLayout()
        layout.addWidget(QLabel("数据库用户名:"),1,1)
        layout.addWidget(usernameEdit,1,2)
        layout.addWidget(QLabel("数据库密码:"),1,3)
        layout.addWidget(passwordEdit, 1,4)

        layout.addWidget(QLabel("数据库:"),2,1)
        layout.addWidget(databaseEdit,2,2)
        layout.addWidget(QLabel("数据库表名:"),2,3)
        layout.addWidget(tableEdit, 2,4)

        layout.addWidget(QLabel("关键词不少于:"),3,1)
        layout.addWidget(keywordLengthGreat,3,2)
        layout.addWidget(QLabel("关键词不大于:"),3,3)
        layout.addWidget(keywordLengthLess, 3,4)
        layout.addWidget(QLabel("下拉字数:"),3,5)
        layout.addWidget(refresh, 3,6)

        layout.addWidget(radioButton1,4,1)
        layout.addWidget(radioButton2,4,2)
        layout.addWidget(radioButton3,4,3)
        layout.addWidget(radioButton4,5,1)
        layout.addWidget(radioButton5,5,2)
        layout.addWidget(radioButton6,5,3)
        layout.addWidget(confirmButton,6,1)
        
       

        # layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        # layout.addWidget(slider, 3, 0)
        # layout.addWidget(scrollBar, 4, 0)
        # layout.addWidget(dial, 3, 1, 2, 1)
        # layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)
    
    @pyqtSlot()
    def runCrawler(self):
        self.window2()
        results =[]
        searchList = self.searchList.toPlainText().split('\n')
        print(searchList)
        for key in searchList:
            if key:
                x=self.crawler.baidu(key)
                results.append(x)
                print(x)
                time.sleep(random.randint(1,3))
        print('result',results)
        self.w.textbox.setPlainText('\n'.join(str(item)  for i in results for item in i))
        
        # keyList = self.crawler.baidu("病毒")
        # print('\n'.join(keyList))

        #self.w.textbox.setPlainText(keyList[0])
        

    def window2(self):                                             
        self.w = Window2()
        self.w.show()
        self.w.resize(500, 400)
        
        

class Window2(QMainWindow):                           
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window2")
        self.textbox =  QTextEdit()
        self.setCentralWidget(self.textbox)
       


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    # gallery = WidgetGallery()
    # gallery.show()
    mainWin = Main_window()
    mainWin.show()
    sys.exit(app.exec_()) 