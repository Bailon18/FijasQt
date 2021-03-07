'''
compilacion de metodos y eventos de QT v3 by ALEX7320

ultimos actualizados:
    Clipboard
    Talbas
    CajaText

    Calendario (acceso a sus objetos)

'''
from PySide2.QtWidgets import (QApplication,QMainWindow,QTableWidgetItem,QHeaderView,QWidget,
                                QToolButton,QSpinBox)# importaciones_usadas

from PySide2.QtCore import (QDate,QDateTime,QTime,Qt,QTranslator,QLocale,QLibraryInfo)# importaciones_usadas

from VISTA.ui_elementos import Ui_Elementos# diseños

# quitar advertencias de ejecucion
from os import environ
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

class Ui_Controlador(QMainWindow):

    def __init__(self):
        super(Ui_Controlador, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS OTROS-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # Quitar "?" de la ventana widget tener en cuenta la importacion: QtCore.Qt.WindowContextHelpButtonHint
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)

        # cambiar estilo css de un widget 
        "widget.setStyleSheet('border: 1px solid red')"

        # insertar texto en el clipboard (esto es para pegar el texto con el mouse)
        self.myClipboard = QApplication.clipboard()
    
        self.raiz.botSiete.clicked.connect(lambda : self.myClipboard.setText('texto para copiar'))#agregar
        self.raiz.botOcho.clicked.connect(lambda : self.myClipboard.clear())#vaciar

        # minimizar, maximizar, cerrar (puedes borrar el que no quieres que este activado)
        'self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)'

        # transparencia de frame y quitar barra superior
        'self.setWindowFlag(Qt.FramelessWindowHint)'
        'self.setAttribute(Qt.WA_TranslucentBackground)'


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS COMBOBOX-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # insertar valore(s) combobox
        self.raiz.comboUno.insertItems(0, ['datos','gta iii','python 3','java'])
        self.raiz.comboUno.addItem('texto aqui')

        # establecer item por index
        self.raiz.comboUno.setCurrentIndex(0)

        # obtener texto y index
        self.raiz.comboUno.currentTextChanged.connect(lambda : print(self.raiz.comboUno.currentText()))
        self.raiz.comboUno.currentTextChanged.connect(lambda : print(self.raiz.comboUno.currentIndex()))

        # eliminar item por index (usando boton)
        self.raiz.botUno.clicked.connect(
            lambda : self.raiz.comboUno.removeItem(0)
            )
        
        # eliminar todos los valores del combobox
        """
        self.raiz.botUno.clicked.connect(
            lambda : self.raiz.comboUno.clear()
            )
        """

        # contar cuantos elementos tiene el combobox
        print(self.raiz.comboUno.count())


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS BUTTON-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # cambiar texto de boton
        self.raiz.botOcho.setText('Boton 8')

        # capturar evento clic
        self.raiz.botOcho.clicked.connect(lambda : print('Presionando boton 8'))

        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS LABEL-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


        # cambiar texto label (mediante clic o evento) 
        'es el label del TabUno'
        self.raiz.botSiete.clicked.connect(lambda : 
            self.raiz.labelPrueba.setText('TEXTO CAMBIADO')
        )



        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS CALENDAR-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # extraer variable str
        variableCalen=self.raiz.calendarUno.selectedDate().toString("dd/MM/yyyy")
        
        # establecer fecha
        self.raiz.calendarUno.setSelectedDate(QDate.fromString("08/11/2020", "dd/MM/yyyy" ))

        # establecer fecha minima
        'self.raiz.calendarUno.setMinimumDate(QDate.fromString("08/11/2020", "dd/MM/yyyy" ))'

        # establecr fecha maxima//

        # metodo 1 (manera personalizada)
        'self.raiz.calendarUno.setMaximumDate(QDate.fromString("20/12/2020", "dd/MM/yyyy" ))'

        # metodo 2 (fecha actual)
        'self.raiz.calendarUno.setMaximumDate(QDate.currentDate())'


        # establecer un rango de fecha
        'self.raiz.calendarUno.setDateRange(QDate.fromString("05/11/2020", "dd/MM/yyyy" ), QDate.fromString("15/12/2020", "dd/MM/yyyy" ))' #min-max
                
        # extraer fecha por evento
        self.raiz.calendarUno.clicked.connect(lambda date: print(date.toString("dd/MM/yyyy")))


        # establece pagina basado en (AÑO,MES)
        'self.raiz.calendarUno.setCurrentPage(year, month)'

        # mostrar mes y año del calendario 
        print(f'año calendario: {self.raiz.calendarUno.yearShown()}',
            f'mes calendario {self.raiz.calendarUno.monthShown()}')

        # objetos del calendario /////
        'para acceder a los objetos del calendario, primero debemos extraerlos'
        
        # boton mes previo
        self.btnCalPrev = self.raiz.calendarUno.findChild(QToolButton, "qt_calendar_prevmonth")
        self.btnCalPrev.clicked.connect(lambda: print('cal btn mesPrev'))

        # boton mes siguiente
        self.btnCalNext = self.raiz.calendarUno.findChild(QToolButton, "qt_calendar_nextmonth")
        self.btnCalNext.clicked.connect(lambda: print('cal btn mesNext'))

        # boton seleccion mes
        'esto tambien se aplica a los botones que tengan menu'
        self.btnCalMes = self.raiz.calendarUno.findChild(QToolButton, "qt_calendar_monthbutton")
        self.btnCalMes.triggered.connect(lambda action :print('cal btn mes',action.text()))

        # spinbox seleccion año
        self.spinCalYear = self.raiz.calendarUno.findChild(QSpinBox, "qt_calendar_yearedit")
        self.spinCalYear.valueChanged.connect(lambda : print('cal spin año'))


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS DATE_EDIT-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        '/*fecha*/*/*/*/*/*/*/'
        # extraer variable str
        variable=self.raiz.dateUno.date().toString("dd/MM/yyyy")

        # establecer fecha minima
        'self.raiz.dateUno.setMinimumDate(QDate.fromString("08/11/2020", "dd/MM/yyyy" ))'

        # establecr fecha maxima
        'self.raiz.dateUno.setMaximumDate(QDate.fromString("20/12/2020", "dd/MM/yyyy" ))'

        # establecer rango de fecha
        'self.raiz.dateUno.setDateRange(QDate.fromString("05/12/2020", "dd/MM/yyyy" ), QDate.fromString("15/12/2020", "dd/MM/yyyy" ))' #min-max
                
        # establecer fecha
        self.raiz.dateUno.setDate(QDate.fromString( "06/12/2020", "dd/MM/yyyy" ))

        # mandar fecha por evento
        self.raiz.dateUno.dateChanged.connect(lambda : print(self.raiz.dateUno.date().toString("dd/MM/yyyy")))


        '/*fecha y hora*/*/*/*/*/*/*/'
        # extraer variable str
        variableFech=self.raiz.dateDos.date().toString("dd/MM/yyyy")#fecha
        variableTime=self.raiz.dateDos.time().toString("hh:mm AP")#hora

        # establecer fecha minima
        'self.raiz.dateDos.setMinimumDate(QDate.fromString("08/11/2020", "dd/MM/yyyy" ))'

        # establecr fecha maxima
        'self.raiz.dateDos.setMaximumDate(QDate.fromString("20/12/2020", "dd/MM/yyyy" ))'

        # establecer rango de fecha
        'self.raiz.dateDos.setDateRange(QDate.fromString("05/12/2020", "dd/MM/yyyy" ), QDate.fromString("15/12/2020", "dd/MM/yyyy" ))' #min-max

        # establecer fecha y hora (para QDateTimeEdit) importado de QtCore
        self.raiz.dateDos.setDate(QDate.fromString( "08/12/2020", "dd/MM/yyyy" ))#fecha
        self.raiz.dateDos.setTime(QTime.fromString( "10:31 AM", "hh:mm AP" ))#hora

        # caturar eventos por evento
        self.raiz.dateDos.dateChanged.connect(lambda : print(self.raiz.dateDos.date().toString("dd/MM/yyyy")))#fecha
        self.raiz.dateDos.timeChanged.connect(lambda : print(self.raiz.dateDos.time().toString("hh:mm AP")))#hora

        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS TIME_EDIT-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # extraer variable str
        variableTime=self.raiz.dateUno.time().toString("hh:mm AP")

        # establecer hora importado de QtCore
        self.raiz.horaUno.setTime(QTime.fromString( "12:32 PM", "hh:mm AP" ))

        # mandar hora por evento
        self.raiz.horaUno.timeChanged.connect(lambda : print(self.raiz.horaUno.time().toString("hh:mm AP")))


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS LINE_EDIT-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # establecer texto (pone solamente el texto)
        self.raiz.lineUno.setText('texto aqui')

        # enviar texto por parametro
        self.raiz.lineUno.textChanged.connect(lambda : print(self.raiz.lineUno.text()))

        # extraer texto de cadena
        textoSalida = self.raiz.lineUno.text()

        # agregar texto (agrega a la caja el texto)
        self.raiz.botExtra.clicked.connect(lambda : self.raiz.lineUno.insert(' Nuevo mundo'))

        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS SPINBOX-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # capturar valor
        valorSpin = self.raiz.spinUno.value()

        # establecer valor
        self.raiz.spinUno.setValue(15)

        # evento de spinbox
        self.raiz.spinUno.valueChanged.connect(lambda : print(self.raiz.spinUno.value()))

        'esos cambios tambien se aplican tambien para spinDecimal'

        # establecer valor minimo
        "self.raiz.spinUno.setMinimum(12)"

        # establecer valor maximo
        "self.raiz.spinUno.setMaximum(999)"


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS TEXT_EDIT-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        '''
        recomendamos que de su diseño de la caja texto tenga desmarcada la casilla "acceptRichText"
        esto para evitar que los diferentes formatos de texto entren en la caja

        NOTA: en este modelo se le configuro de dicha manera.
        '''

        # establecer texto (pone solamente el texto)
        self.raiz.textUno.setText('almacenamiento de 240gb')

        # extraer texto
        todoTexto = self.raiz.textUno.toPlainText()

        # texto evento
        self.raiz.textUno.textChanged.connect(lambda : print(self.raiz.textUno.toPlainText()))


        # borrar texto (con boton)
        self.raiz.botDos.clicked.connect(
            lambda : self.raiz.textUno.setText('')
            )

        # agregar texto (agrega a la caja el texto)

        'append > agrega el texto despues de un salto de linea'
        'insertPlainText > agrega el texto en la posicion donde se encuentre el cursor'
        self.raiz.botExtra.clicked.connect(lambda : self.raiz.textUno.insertPlainText(' Nuevo mundo'))


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS SLIDER-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # establecer valor
        self.raiz.verticalSlider.setValue(17)

        # extraer valor
        valorVertica = self.raiz.verticalSlider.value() 

        # conectar evento
        self.raiz.verticalSlider.valueChanged.connect(lambda : print(self.raiz.verticalSlider.value()))

        'esto se aplica para horizontal/vertical'


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS DIAL-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # establecer valor
        self.raiz.dialUno.setValue(17)

        # extraer valor
        valorVertica = self.raiz.dialUno.value() 

        # conectar evento
        self.raiz.dialUno.valueChanged.connect(lambda : print(self.raiz.dialUno.value()))



        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS RADIOBUTTON-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        
        # cambiar de texto
        self.raiz.radioA1.setText('a1_new')

        # capturar evento puede ser 'clicked' o 'toggled'
        'nota: *funciones en en final del codigo*'
        self.raiz.radioA1.clicked.connect(lambda :self.eventoRadio())
        self.raiz.radioA2.clicked.connect(lambda :self.eventoRadio())
        self.raiz.radioA3.clicked.connect(lambda :self.eventoRadio())

        # establecer una seleccion (de paso llamamos a la funcion)
        self.raiz.radioA3.setChecked(True);self.eventoRadio()

        # sentencia para saver si el boton esta marcado:
        'if(self.raiz.radioA1.isChecked()==True):'

        # extraer texto de radio button
        self.raiz.radioP1.clicked.connect(lambda : print(self.raiz.radioP1.text()))
        self.raiz.radioP2.clicked.connect(lambda : print(self.raiz.radioP2.text()))
        self.raiz.radioP3.clicked.connect(lambda : print(self.raiz.radioP3.text()))


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS CHECKBUTTON-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # cambiar de texto
        self.raiz.checkY1.setText('y1_new')

        # capturar evento puede ser 'clicked' o 'toggled'        
        'nota: *funciones en en final del codigo*'
        self.raiz.checkY1.clicked.connect(lambda :self.eventoCheck())
        self.raiz.checkY2.clicked.connect(lambda :self.eventoCheck())
        self.raiz.checkY3.clicked.connect(lambda :self.eventoCheck())

        # establecer una seleccion (de paso llamamos a la funcion)
        self.raiz.checkY3.setChecked(True);self.eventoCheck()

        # sentencia para saver si el boton esta marcado:
        'if(self.raiz.radioA1.isChecked()==True):'

        # extraer texto de check button 
        self.raiz.checkT1.clicked.connect(lambda : print(self.raiz.checkT1.text()))
        self.raiz.checkT2.clicked.connect(lambda : print(self.raiz.checkT2.text()))
        self.raiz.checkT3.clicked.connect(lambda : print(self.raiz.checkT3.text()))



        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS LCDNUMER-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # insertar valores (int,str,float)
        self.raiz.lcdUno.display('TEXTO')
        self.raiz.lcdUno.display(73.20)

        # obtener valor numerico (en caso de que sea cadena, retorn 0.0)
        self.raiz.botTres.clicked.connect(lambda : print(self.raiz.lcdUno.value()))


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS LISTA-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # eliminar valores de la lista
        self.raiz.listaUno.clear()

        # agregar elementos
        self.raiz.botCuatro.clicked.connect(
            lambda: self.raiz.listaUno.addItem('*newer-texto')
        )
        
        # extraer index
        self.raiz.listaUno.clicked.connect(lambda : print(self.raiz.listaUno.currentRow()))

        # extraer texto
        self.raiz.listaUno.clicked.connect(lambda : print(self.raiz.listaUno.currentItem().text()))

        # orden automatico de items
        'self.raiz.listaUno.setSortingEnabled(True)'

        # esto se puede aplicar en un boton, para ordenarlo ↓ ↑
        'self.raiz.listaUno.sortItems(order=Qt.SortOrder.DescendingOrder)'
        'AscendingOrder o DescendingOrder'

        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS STACKED (CAJA ELEMENTOS)-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # cambiar entre pestañas (por index)
        self.raiz.botNueve.clicked.connect(lambda : self.raiz.stackedWidget.setCurrentIndex(0))
        self.raiz.botDiez.clicked.connect(lambda : self.raiz.stackedWidget.setCurrentIndex(1))


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS TABS(FOLDER)-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # capturar ubicacion del tab (index)
        variTab=self.raiz.tabWidget.currentIndex()

        # cambiar ubicacion de la pesataña
        self.raiz.tabWidget.setCurrentIndex(1)

        #capturar evento de cambio de pestaña
        self.raiz.tabWidget.currentChanged.connect(lambda: 
                    print(f'Tab actual {self.raiz.tabWidget.currentIndex()}'))

        # agregar nuevo tab
        self.raiz.tabWidget.addTab(QWidget(),"Tab 5")

        # cambiar texto del tab (por index)
        self.raiz.tabWidget.setTabText(2,"tabTresNEW")
        

        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS TOOLBOX(PAGINAS)-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # capturar ubicacion del tab (index)
        variTool=self.raiz.toolBox.currentIndex()

        # cambiar ubicacion de la pesataña
        self.raiz.toolBox.setCurrentIndex(1)

        self.raiz.toolBox.currentChanged.connect(lambda: 
                    print(f'Pagina actual {self.raiz.toolBox.currentIndex()}'))

        # cambiar texto de una pagina (por index)
        self.raiz.toolBox.setItemText(1,"pageDosNEW")


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS PROGRESS-BAR-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # obtener valor
        variablePb=self.raiz.progressUno.value()

        # reestablecer valores
        self.raiz.progressUno.reset()

        # establecer un rango
        self.raiz.progressUno.setRange(0,20) #min-max

        # establecer un valor (que este dentro del rango)
        self.raiz.progressUno.setValue(10)

        #cambiar de orientacion
        'self.raiz.progressUno.setOrientation(Qt.Horizontal)' #Qt.Horizontal / Qt.Vertical


        #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-METODOS TABLA-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


        # insertar elementos de una tabla (actualizar tabla)
        self.dataBase=[
                ['a12','nokia','nokia@gmail.com','nokia.org'],
                ['a15','huawei','huawei@gmail.com','huawei.org'],
                ['a16','asus','asus@gmail.com','asus.org'],
                ['a20','blackberry','blackberry@gmail.com','blackberry.org'],
                ['a24','oppo','oppo@gmail.com','oppo.org'],
                    ]

        'nota: *funciones en en final del codigo*'
        self.raiz.botOnce.clicked.connect(lambda : self.llenarTablaUno(self.dataBase))

        # insertar columna y fila en la ultima posicion
        'self.raiz.tablaUno.insertRow(self.raiz.tablaUno.rowCount())'
        'self.raiz.tablaUno.insertColumn(self.raiz.tablaUno.columnCount())'

        # recorrer columnas


        # crear columna y filas por rango
        'self.raiz.tablaUno.setRowCount(10)'
        'self.raiz.tablaUno.setColumnCount(10)'

        # insertar columna y fila por index
        'self.raiz.tablaUno.insertRow(2)#se basa en index'
        'self.raiz.tablaUno.insertColumn(2)#se basa en index'

        # extraer fila,columna,item, lista_fila (evento)-------------- arreglar
        self.raiz.tablaUno.cellClicked.connect(
            lambda fila,columna: 
                print(
                    f'\n*fila:\t{fila}', 
                    f'\n*colum:\t{columna}',
                    f'\n*item:\t{self.raiz.tablaUno.item(fila, columna).text()}',
                    f'\n*lista:\t{[self.raiz.tablaUno.item(fila, columna).text() for columna in range(self.raiz.tablaUno.columnCount())]}',
                    f'\n*1er item:\t{self.raiz.tablaUno.item(fila, 0).text()}',

                
                )
            )

        # eliminar fila de tabla
        '''
        para esto deberas agregar un controlador para evitar que 
        los elementos se sigan eliminado con el boton.

        En este caso no se le agrego, esto solo es para mostrar la funcionalidad. 
        '''
        self.raiz.botCatorce.clicked.connect(lambda : 
                self.raiz.tablaUno.removeRow(
                    self.raiz.tablaUno.currentRow()#NOTA: con este mismo index podremos eliminarlo de la matriz
                )
            )

        # obtener lista de fila (por boton)
        'nota: *funciones en en final del codigo*'
        self.raiz.botTrece.clicked.connect(lambda : self.listaRowTablaUno(self.raiz.tablaUno.currentRow()))#FN_EXt

        # extraer solo row, fila (currentRow o currentColumn)
        self.raiz.tablaUno.clicked.connect(lambda: print('solo fila /',self.raiz.tablaUno.currentRow()))
        
        # extraer solo columna
        self.raiz.tablaUno.clicked.connect(lambda: print('solo column /',self.raiz.tablaUno.currentColumn()))

        # borrado de elementos
        self.raiz.botDoce.clicked.connect(lambda : self.raiz.tablaUno.setRowCount(0))

        # total de filas y columnas
        cantidadFilas = self.raiz.tablaUno.rowCount()
        cantidadColumnas = self.raiz.tablaUno.columnCount()


        
        # establecer tamaño de columnas por index
        self.raiz.tablaUno.setColumnWidth(1,50)

        # establecer columnas fija, elastica, interactiva (para todos)
        'Fixed Stretch Interactive'
        self.raiz.tablaUno.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # establecer columna fija (por index)
        'se puso 0 por que fue el que anteriormente se configuro a tamaño 50'
        self.raiz.tablaUno.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)

        # establecer filas fija, elastica, interactiva (para todos)      
        'Fixed Stretch Interactive'
        self.raiz.tablaUno.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        
        


        # nota_de_tablas
        '''
        si queremos conservar las filas para realizar:
            ↓
                    user    admin   senior  jefe
          nombre    d1      d2      d3      d4
        apellido    a1      a2      a3      a4        
             dni    q1      q2      q3      q4

        tengamos en cuenta que en los metodos aplicados no se tomo en cuenta
        pero los procesos y eventos son los mismo, solamentea aplicar logica
        y queda
        '''

    #/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/-FUNCIONES IMPLEMENTADAS-/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


    # /*/*/*/-EVENTO_RADIO_BUTTON-/*/*/*/
    def eventoRadio(self):
        '''se puede pasar parametro, pero esta es una manera'''
        if(self.raiz.radioA1.isChecked()):#==True):
            print('radioA1')
        elif(self.raiz.radioA2.isChecked()):#==True):
            print('radioA2')
        else:
            print('radioA3')


    # /*/*/*/-EVENTO_CHECK_BUTTON-/*/*/*/
    def eventoCheck(self):
        '''se puede pasar parametro, pero esta es una manera'''
        listaSeleccion=[]
        if(self.raiz.checkY1.isChecked()):
            listaSeleccion.append('checkY1')
        if(self.raiz.checkY2.isChecked()):
            listaSeleccion.append('checkY2')
        if(self.raiz.checkY3.isChecked()):
            listaSeleccion.append('checkY3')    
        print(listaSeleccion) 


    # /*/*/*/-EVENTO_LLENAR_TABLA-/*/*/*/
    def llenarTablaUno(self,datos):
        # borrar todas las filas
        self.raiz.tablaUno.setRowCount(0)

        # llenado de datos
        self.raiz.tablaUno.setRowCount(len(datos))
        for fila,listaItem in enumerate(datos):
            for columna,item in enumerate(listaItem):
                self.raiz.tablaUno.setItem(fila, columna, QTableWidgetItem(str(item)))



        # establecer tamaño de columnas por index
        # self.raiz.tablaUno.setRowWidth(0,150)

        # alinear items
        for fila in range(self.raiz.tablaUno.rowCount()):
            for columna in range(self.raiz.tablaUno.columnCount()):
                self.raiz.tablaUno.item(fila,columna).setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)

    # /*/*/*/-EVENTO_SACAR_LISTA_ROW_TABLA-/*/*/*/
    def listaRowTablaUno(self,fila):
        
        '''si no se selecciono nada, la fila sera -1'''
        if(fila>=0):

            lista=[]
            for columna in range(self.raiz.tablaUno.columnCount()):
                lista.append(
                self.raiz.tablaUno.item(fila, columna).text()

                )

            print(lista)





if __name__ == "__main__":

    import sys

    suppress_qt_warnings()#quitar advertencias

    app = QApplication(sys.argv)
    # app.setStyle('Fusion')#opcional
    
    #---traductor-cajaTexto-(copy,paste,cut)------
    'importaciones de QtCore'
    'QTranslator,QLocale,QLibraryInfo'
    traductor = QTranslator(app)
    lugar = QLocale.system().name()
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    traductor.load("qtbase_%s" % lugar, path)
    app.installTranslator(traductor)
    #---traductor-cajaTexto-(copy,paste,cut)---fin

    mi_aplicacion = Ui_Controlador()
    mi_aplicacion.show()
    sys.exit(app.exec_())

