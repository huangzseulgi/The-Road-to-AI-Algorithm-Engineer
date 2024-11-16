"""
    用于对UI界面进行展示
"""
from QtTest import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtGui

class Camshow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Camshow, self).__init__(parent)
        self.setupUi(self)
        # 信号与槽
        self.OpenFileBtn.clicked.connect(self.loadImage)   # 打开图片按钮
        self.actionOpen.triggered.connect(self.loadImage)  # 打开文件
        self.actionExit.triggered.connect(self.exit)       # 退出菜单
        self.actionabout.triggered.connect(self.about)     # 关于菜单

    def loadImage(self):
        print("按钮被按下了")
        self.infolabel.setText("打开文件按键被按下")      # 设定infolabel的文本
        self.fname, _ = QFileDialog.getOpenFileNames(self, '选择图片', '.', '图像文件(*.jpg *.png)')
        
        # 检查是否选择了文件
        if self.fname:
            pix = QtGui.QPixmap(self.fname[0]).scaled(self.ImageLable.width(), self.ImageLable.height())
            self.ImageLable.setPixmap(pix)
        else:
            print("没有选择任何文件")
    
    def exit(self):
        # 退出程序
        sys.exit(app.exec_())
    
    def about(self):
        # 需要import QMessageBox
        self.infolabel.setText("帮助按键被按下")  
        QMessageBox.information(self, "软件说明", "该软件由echo制作，仅供学习交流使用，版本号为1.0")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Camshow()
    ui.show()
    sys.exit(app.exec_())
    
