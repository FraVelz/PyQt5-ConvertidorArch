from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
    
    def __style__(self):
        with open('./style.qss', 'r') as f: style = f.read()
        return style

    def setupUi(self, window):
        window.setObjectName('window')
        window.resize(520, 370)
        
        window.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        window.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        window.setStyleSheet(self.__style__())

        self.fr_borde = QtWidgets.QFrame(window)
        self.fr_borde.setGeometry(QtCore.QRect(20, 20, 480, 330))
        self.fr_borde.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_borde.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_borde.setObjectName('fr_borde')

        self.fr_fondo = QtWidgets.QFrame(self.fr_borde)
        self.fr_fondo.setGeometry(QtCore.QRect(5, 5, 470, 320))
        self.fr_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_fondo.setObjectName('fr_fondo')
        
        self.cb_codigo = QtWidgets.QComboBox(self.fr_fondo)
        self.cb_codigo.setGeometry(QtCore.QRect(120, 40, 80, 30))
        self.cb_codigo.setObjectName('cb_codigo')
        self.cb_codigo.addItem('')
        self.cb_codigo.addItem('')
        
        self.cb_convertir = QtWidgets.QComboBox(self.fr_fondo)
        self.cb_convertir.setGeometry(QtCore.QRect(120, 105, 90, 34))
        self.cb_convertir.setObjectName('cb_convertir')
        self.cb_convertir.addItem('')
        self.cb_convertir.addItem('')
        
        self.cb_archMain = QtWidgets.QComboBox(self.fr_fondo)
        self.cb_archMain.setGeometry(QtCore.QRect(120, 170, 90, 34))
        self.cb_archMain.setObjectName('cb_archMain')
        self.cb_archMain.addItem('')
        self.cb_archMain.addItem('')

        self.lbl_codigo = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_codigo.setGeometry(QtCore.QRect(20, 40, 71, 31))
        self.lbl_codigo.setObjectName('lbl_codigo')

        self.lbl_convertir = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_convertir.setGeometry(QtCore.QRect(20, 105, 110, 30))
        self.lbl_convertir.setObjectName('lbl_convertir')

        self.lbl_archMain = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_archMain.setGeometry(QtCore.QRect(20, 170, 110, 30))
        self.lbl_archMain.setObjectName('lbl_archMain')

        self.btn_cerrar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_cerrar.setGeometry(QtCore.QRect(430, 10, 21, 21))
        self.btn_cerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cerrar.setText('')
        self.btn_cerrar.setObjectName('btn_cerrar')

        self.btn_minimizar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_minimizar.setGeometry(QtCore.QRect(390, 10, 21, 20))
        self.btn_minimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimizar.setText('')
        self.btn_minimizar.setObjectName('btn_minimizar')

        self.btn_convertir = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_convertir.setGeometry(QtCore.QRect(50, 240, 121, 31))
        self.btn_convertir.setObjectName('btn_convertir')
        
        self.lbl_archivo = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_archivo.setGeometry(QtCore.QRect(240, 50, 121, 21))
        self.lbl_archivo.setObjectName('lbl_archivo')

        self.btn_abrir_arch = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_abrir_arch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_abrir_arch.setGeometry(QtCore.QRect(360, 50, 80, 25))
        self.btn_abrir_arch.setObjectName('btn_abrir_arch')

        
        self.txte_archivo = QtWidgets.QTextEdit(self.fr_fondo)
        self.txte_archivo.setGeometry(QtCore.QRect(240, 90, 201, 55))
        self.txte_archivo.setTabChangesFocus(False)
        self.txte_archivo.setUndoRedoEnabled(True)
        self.txte_archivo.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txte_archivo.setAcceptRichText(True)
        self.txte_archivo.setObjectName('txte_archivo')
        
        self.txte_guardar_en = QtWidgets.QTextEdit(self.fr_fondo)
        self.txte_guardar_en.setGeometry(QtCore.QRect(240, 220, 201, 55))
        self.txte_guardar_en.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txte_guardar_en.setObjectName('txte_guardar_en')

        self.lbl_guardar_en = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_guardar_en.setGeometry(QtCore.QRect(240, 180, 111, 21))
        self.lbl_guardar_en.setObjectName('lbl_guardar_en')
        
        self.btn_guardar_en = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_guardar_en.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_guardar_en.setGeometry(QtCore.QRect(360, 180, 80, 25))
        self.btn_guardar_en.setObjectName('btn_guardar_en')
        
        self.retranslateUi(window)
        self.btn_cerrar.clicked.connect(window.close) 
        QtCore.QMetaObject.connectSlotsByName(window)
	  
    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate('window', 'Convertidor'))
        
        self.cb_codigo.setItemText(0, _translate('window', 'Pyqt5'))
        self.cb_codigo.setItemText(1, _translate('window', 'PySide2'))
        self.cb_convertir.setItemText(0, _translate('window', '.ui > .py'))
        self.cb_convertir.setItemText(1, _translate('window', '.qrc > .py'))
        self.cb_archMain.setItemText(0, _translate('window', 'True'))
        self.cb_archMain.setItemText(1, _translate('window', 'False'))

        self.lbl_codigo.setText(_translate('window', 'Codigo:'))
        self.lbl_convertir.setText(_translate('window', 'Convertir:'))
        self.lbl_archMain.setText(_translate('window', 'A. Main:'))

        self.lbl_archivo.setText(_translate('window', 'Archivo:'))
        self.lbl_guardar_en.setText(_translate('window', 'Guardar en:'))
        
        self.btn_convertir.setText(_translate('window', 'Convertir'))
        self.btn_abrir_arch.setText(_translate('window', 'Abrir'))
        self.btn_guardar_en.setText(_translate('window', 'Abrir'))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    ui = Ui_window()
    ui.setupUi(window)
    
    window.show()
    sys.exit(app.exec_())
