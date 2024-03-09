# pyuic5 -x register.ui -o  ui_register.py
# pyuic5 -x a.ui -o  ./ala/name.py

from setup import Ui_window, QtWidgets, QtCore
from pathlib import Path
import sys, os

text_info = '''from __setup__ import Ui_Form, QtWidgets
import sys

class MainApp(QtWidgets.QMainWindow): 

    def __init__(self, parent=None, *args): 
        super(MainApp, self).__init__(parent=parent) 

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def funcion(self, *args): pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    window = MainApp() 
    window.show() 
    sys.exit(app.exec_())

#* Author: Francisco Velez
'''

class MainApp(QtWidgets.QMainWindow): 

    def __init__(self, parent=None, *args): 
        super(MainApp, self).__init__(parent=parent) 

        self.ui = Ui_window()
        self.ui.setupUi(self)

        self.ui.btn_abrir_arch.clicked.connect(lambda: self.abrir('archivo'))
        self.ui.btn_guardar_en.clicked.connect(lambda: self.abrir('carpeta'))
        self.ui.btn_convertir.clicked.connect(self.func_convertir)
        
        #? Mover ventana
        self.ui.fr_borde.mouseMoveEvent = self.mover_ventana
	  
    ##? mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        try:
            if self.isMaximized() == False: 
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()
        except: pass        
    
    def abrir(self, opc=''):
        if opc == 'archivo':
            path = QtWidgets.QFileDialog.getOpenFileName(self, 'Escoger archivo')
            name = path[0].split('/')[-1]
            msg = path[0].replace(name, name.replace('.ui', '.py'))

            self.ui.txte_guardar_en.setText(f'"{msg}"')
            self.ui.txte_archivo.setText(f'"{path[0]}"')
            
        if opc == 'carpeta': 
            path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Guardar ruta')
            self.ui.txte_guardar_en.setText(f'"{path}"')

    def func_convertir(self):
        r_archivo = self.ui.txte_archivo.toPlainText()
        r_guardar = self.ui.txte_guardar_en.toPlainText()
        
        c_convertir = self.ui.cb_convertir.currentText().lower()
        c_codigo = self.ui.cb_codigo.currentText().lower()
        
        codig = ''
        
        if r_archivo.replace('"', '').strip() == '' or r_guardar.replace('"', '').strip() == '':
            return 'pass'

        if c_convertir == '.ui > .py': 
            if c_codigo == 'pyqt5': 
                codig += 'pyuic5 -x {} -o {}'.format(r_archivo, r_guardar)
                if self.ui.cb_archMain.currentIndex() == 0: 
                    self.crear_archivo(r_guardar)
            
            if c_codigo == 'pyside2': 
                codig += 'pyside2uic {} > {}'.format(r_archivo, r_guardar)

        if c_convertir == '.qrc > .py':
            if c_codigo == 'pyqt5': 
                codig += 'pyrcc5 -o {} {}'.format(r_guardar, r_archivo)

            if c_codigo == 'pyside2': 
                codig += 'pyside2-rcc {} > {}'.format(r_archivo, r_guardar)
        
        os.system(codig)
    
    def crear_archivo(self, ruta):
        r = Path(ruta)
        ruta = ruta.replace(f'{r.stem}{r.suffix}', '__main__.py')

        with open(ruta.replace('"', ''), 'w') as f:
            f.write(
                f'{text_info}'.replace('__setup__', r.stem)
            ) 
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    window = MainApp() 
    window.show() 
    sys.exit(app.exec_())

#* Author: Francisco Velez
