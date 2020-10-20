from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from admin_particulas import Admin_particulas

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.particulas = Admin_particulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Agregar_Inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Agregar_Final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar)

       
    @Slot()
    def click_agregar_inicio(self):
        Id = self.ui.ID_spinBox.value()
        Origen_X = self.ui.Origen_X_spinBox.value()
        Origen_Y = self.ui.Origen_Y_spinBox.value()
        Destino_X = self.ui.Destino_X_spinBox.value()
        Destino_Y = self.ui.Destino_Y_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()

        particula = Particula(Id, Origen_X, Origen_Y, Destino_X, Destino_Y, Velocidad, Red, Green, Blue)
        self.particulas.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
        Id = self.ui.ID_spinBox.value()
        Origen_X = self.ui.Origen_X_spinBox.value()
        Origen_Y = self.ui.Origen_Y_spinBox.value()
        Destino_X = self.ui.Destino_X_spinBox.value()
        Destino_Y = self.ui.Destino_Y_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()

        particula = Particula(Id, Origen_X, Origen_Y, Destino_X, Destino_Y, Velocidad, Red, Green, Blue)
        self.particulas.agregar_final(particula)

    @Slot()
    def click_mostrar(self):
        self.ui.Salida.clear()
        self.ui.Salida.insertPlainText(str(self.particulas))