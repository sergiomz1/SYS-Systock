# Form implementation generated from reading ui file 'd:\SYSTOCK\SYSTOCK\DESARROLLO\python\programacion_ladynails\Project_LadyNails\app\ui\Facturas.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1282, 982)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Contenedor = QtWidgets.QWidget(parent=Form)
        self.Contenedor.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: black; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white; /* Color del texto */\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: center; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    margin-top:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer; /* Cursor de mano al pasar sobre el botón */\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: white; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  rgb(50, 50, 50); /* Color del texto */\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: left; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f2f2f2; /* Gris claro al pasar el mouse */\n"
"    cursor: pointer;\n"
"}\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Fondo blanco */\n"
"    border: none; /* Sin bordes visibles */\n"
"    padding: 4px; /* Espaciado interno entre el texto y los bordes */\n"
"    margin-right: 5px; /* Espaciado externo solo a la derecha */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    color: black; /* Texto negro */\n"
"    text-align: left; /* Texto alineado a la izquierda */\n"
"    font-size: 18px; /* Tamaño del texto */\n"
"}\n"
"\n"
"/* Cuando el QLineEdit está enfocado (se está escribiendo) */\n"
"QLineEdit:focus {\n"
"    background-color: rgb(230, 230, 250); /* Color de fondo cuando el campo está activo */\n"
"    border: 1px solid rgb(0, 0, 0); /* Borde negro al estar activo */\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 20px; /* Tamaño de fuente */\n"
"    color:  black; /* Color del texto */\n"
"    margin-right: 10px; /* Espaciado a la derecha */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    text-align: left; /* Alineación del texto a la izquierda */\n"
"}\n"
"QTableWidget {\n"
"    border: none;\n"
"    background-color: #ffffff; /* Fondo blanco para la tabla */\n"
"    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave alrededor de la tabla */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"    transition: background-color 0.3s ease; /* Suavizado de transición de color de fondo */\n"
"    pointer-events: none; /* Desactiva la interacción con las celdas (como editar) */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #aad4ff; /* Color azul claro para celdas seleccionadas */\n"
"    color: black; /* Texto negro para celdas seleccionadas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none; \n"
"    background-color: #f2f2f2; \n"
"    font-weight: normal; /* No negritas */\n"
"    text-align: center; /* Centrado del texto en los encabezados */\n"
"    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra suave para los encabezados */\n"
"}\n"
"\n"
"QHeaderView::section:focus {\n"
"    background-color: #f2f2f2; /* Sin color de fondo cuando está en foco */\n"
"    border: none; /* Sin borde cuando está en foco */\n"
"}\n"
"\n"
"QTableWidget::item:focus {\n"
"    border: none; /* Sin borde cuando las celdas tienen el foco */\n"
"    background-color: #f2f2f2; /* Mantener el fondo sin color azul */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"}\n"
"\n"
"QTableWidget::verticalHeader {\n"
"    background-color: #f2f2f2;\n"
"    border: none;\n"
"    font-weight: normal; /* No negritas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"\n"
"/* Personalización de la barra de desplazamiento */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    width: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-height: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #f2f2f2; /* Fondo para los botones de la barra */\n"
"    height: 0px; /* Sin altura para los botones */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    height: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-width: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #f2f2f2; /* Fondo para los botones de la barra */\n"
"    width: 0px; /* Sin ancho para los botones */\n"
"}\n"
"\n"
"\n"
"")
        self.Contenedor.setObjectName("Contenedor")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Contenedor)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Contenido = QtWidgets.QStackedWidget(parent=self.Contenedor)
        self.Contenido.setStyleSheet("margin-left:10px;\n"
"border-radius:15px;\n"
"background-color: #f2f2f2; \n"
"")
        self.Contenido.setObjectName("Contenido")
        self.ContenidoPage1 = QtWidgets.QWidget()
        self.ContenidoPage1.setObjectName("ContenidoPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ContenidoPage1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(parent=self.ContenidoPage1)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(1200, 50))
        self.frame_2.setStyleSheet("")
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LabelProductos = QtWidgets.QLabel(parent=self.frame_2)
        self.LabelProductos.setStyleSheet("#LabelProductos {\n"
"    font-weight: bold; /* Negrita */\n"
"    font-size: 34px; /* Tamaño de fuente */\n"
"}\n"
"")
        self.LabelProductos.setObjectName("LabelProductos")
        self.gridLayout_3.addWidget(self.LabelProductos, 0, 0, 1, 1)
        self.InputBuscador = QtWidgets.QLineEdit(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputBuscador.sizePolicy().hasHeightForWidth())
        self.InputBuscador.setSizePolicy(sizePolicy)
        self.InputBuscador.setMinimumSize(QtCore.QSize(1100, 0))
        self.InputBuscador.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    border-bottom: 0.5px solid gray;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: none;\n"
"    border-bottom: 1.5px solid black; /* Cambia el color y grosor según desees */\n"
"}\n"
"")
        self.InputBuscador.setText("")
        self.InputBuscador.setObjectName("InputBuscador")
        self.gridLayout_3.addWidget(self.InputBuscador, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QtCore.QSize(50, 35))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("d:\\SYSTOCK\\SYSTOCK\\DESARROLLO\\python\\programacion_ladynails\\Project_LadyNails\\app\\ui\\../../assets/iconos/buscar.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.TablaFacturas = QtWidgets.QTableWidget(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TablaFacturas.sizePolicy().hasHeightForWidth())
        self.TablaFacturas.setSizePolicy(sizePolicy)
        self.TablaFacturas.setMinimumSize(QtCore.QSize(1150, 600))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TablaFacturas.setFont(font)
        self.TablaFacturas.setStyleSheet("\n"
"QTableWidget {\n"
"    border: none;\n"
"    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave alrededor de la tabla */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"    font-size: 18px; /* Tamaño de letra */\n"
"    transition: background-color 0.3s ease; /* Suavizado de transición de color de fondo */\n"
"    pointer-events: none; /* Desactiva la interacción con las celdas (como editar) */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #aad4ff; /* Color azul claro para celdas seleccionadas */\n"
"    color: black; /* Texto negro para celdas seleccionadas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none; \n"
"    background-color: #f2f2f2; \n"
"    font-size: 18px; /* Tamaño de letra */\n"
"    font-weight: normal; /* No negritas */\n"
"    text-align: center; /* Centrado del texto en los encabezados */\n"
"    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra suave para los encabezados */\n"
"}\n"
"\n"
"QHeaderView::section:focus {\n"
"    background-color: #f2f2f2; /* Sin color de fondo cuando está en foco */\n"
"    border: none; /* Sin borde cuando está en foco */\n"
"}\n"
"\n"
"QTableWidget::item:focus {\n"
"    border: none; /* Sin borde cuando las celdas tienen el foco */\n"
"    background-color: #f2f2f2; /* Mantener el fondo sin color azul */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"}\n"
"\n"
"QTableWidget::verticalHeader {\n"
"    background-color: #f2f2f2;\n"
"    font-size: 23px;\n"
"    border: none;\n"
"    font-weight: normal; /* No negritas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"/* Personalización de la barra de desplazamiento */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    width: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"    margin: 0px 2px 0px 0px; /* Un pequeño margen para el desplazamiento */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-height: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #f2f2f2; /* Fondo para los botones de la barra */\n"
"    height: 0px; /* Sin altura para los botones */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    height: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"    margin: 0px 0px 2px 0px; /* Un pequeño margen para el desplazamiento */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-width: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"")
        self.TablaFacturas.setObjectName("TablaFacturas")
        self.TablaFacturas.setColumnCount(10)
        self.TablaFacturas.setRowCount(26)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaFacturas.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        self.TablaFacturas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaFacturas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaFacturas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaFacturas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaFacturas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaFacturas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaFacturas.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaFacturas.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaFacturas.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaFacturas.setHorizontalHeaderItem(9, item)
        self.verticalLayout_3.addWidget(self.TablaFacturas, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.BtnFacturaPagada = QtWidgets.QToolButton(parent=self.widget_2)
        self.BtnFacturaPagada.setMinimumSize(QtCore.QSize(200, 40))
        self.BtnFacturaPagada.setMaximumSize(QtCore.QSize(200, 50))
        self.BtnFacturaPagada.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BtnFacturaPagada.setStyleSheet("QToolButton {\n"
"    background-color: black; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white;\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: left; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 22px; /* Tamaño de fuente */\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer;\n"
"}")
        self.BtnFacturaPagada.setObjectName("BtnFacturaPagada")
        self.gridLayout.addWidget(self.BtnFacturaPagada, 0, 0, 1, 1)
        self.BtnEditarFactura = QtWidgets.QToolButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnEditarFactura.sizePolicy().hasHeightForWidth())
        self.BtnEditarFactura.setSizePolicy(sizePolicy)
        self.BtnEditarFactura.setMinimumSize(QtCore.QSize(200, 50))
        self.BtnEditarFactura.setMaximumSize(QtCore.QSize(200, 50))
        self.BtnEditarFactura.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BtnEditarFactura.setStyleSheet("QToolButton {\n"
"    background-color: black; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white;\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: left; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 22px; /* Tamaño de fuente */\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer;\n"
"}")
        self.BtnEditarFactura.setObjectName("BtnEditarFactura")
        self.gridLayout.addWidget(self.BtnEditarFactura, 0, 3, 1, 1)
        self.BtnEliminarFactura = QtWidgets.QToolButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnEliminarFactura.sizePolicy().hasHeightForWidth())
        self.BtnEliminarFactura.setSizePolicy(sizePolicy)
        self.BtnEliminarFactura.setMinimumSize(QtCore.QSize(250, 50))
        self.BtnEliminarFactura.setMaximumSize(QtCore.QSize(250, 50))
        self.BtnEliminarFactura.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BtnEliminarFactura.setStyleSheet("QToolButton {\n"
"    background-color: red; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white;\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: left; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 22px; /* Tamaño de fuente */\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\SYSTOCK\\SYSTOCK\\DESARROLLO\\python\\programacion_ladynails\\Project_LadyNails\\app\\ui\\../../assets/iconos/eliminar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BtnEliminarFactura.setIcon(icon)
        self.BtnEliminarFactura.setIconSize(QtCore.QSize(30, 30))
        self.BtnEliminarFactura.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.BtnEliminarFactura.setObjectName("BtnEliminarFactura")
        self.gridLayout.addWidget(self.BtnEliminarFactura, 0, 4, 1, 1)
        self.BtnGenerarTicket = QtWidgets.QToolButton(parent=self.widget_2)
        self.BtnGenerarTicket.setMinimumSize(QtCore.QSize(250, 50))
        self.BtnGenerarTicket.setMaximumSize(QtCore.QSize(250, 50))
        self.BtnGenerarTicket.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BtnGenerarTicket.setStyleSheet("QToolButton {\n"
"    background-color: black; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white;\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: left; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 22px; /* Tamaño de fuente */\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\SYSTOCK\\SYSTOCK\\DESARROLLO\\python\\programacion_ladynails\\Project_LadyNails\\app\\ui\\../../assets/iconos/pdf.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BtnGenerarTicket.setIcon(icon1)
        self.BtnGenerarTicket.setIconSize(QtCore.QSize(30, 30))
        self.BtnGenerarTicket.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.BtnGenerarTicket.setObjectName("BtnGenerarTicket")
        self.gridLayout.addWidget(self.BtnGenerarTicket, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_2, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_2.addWidget(self.widget)
        self.Contenido.addWidget(self.ContenidoPage1)
        self.horizontalLayout_2.addWidget(self.Contenido)
        self.gridLayout_2.addWidget(self.Contenedor, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LabelProductos.setText(_translate("Form", "Facturas"))
        item = self.TablaFacturas.verticalHeaderItem(0)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(1)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(2)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(3)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(4)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(5)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(6)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(7)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(8)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(9)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(10)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(11)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(12)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaFacturas.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(19)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(20)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(21)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(22)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(23)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(24)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.verticalHeaderItem(25)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaFacturas.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Id"))
        item = self.TablaFacturas.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Usuario"))
        item = self.TablaFacturas.horizontalHeaderItem(2)
        item.setText(_translate("Form", "MedPago"))
        item = self.TablaFacturas.horizontalHeaderItem(3)
        item.setText(_translate("Form", "TipoFac"))
        item = self.TablaFacturas.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Fecha"))
        item = self.TablaFacturas.horizontalHeaderItem(5)
        item.setText(_translate("Form", "F.Modif"))
        item = self.TablaFacturas.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Efectivo"))
        item = self.TablaFacturas.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Transferencia"))
        item = self.TablaFacturas.horizontalHeaderItem(8)
        item.setText(_translate("Form", "M.Total"))
        item = self.TablaFacturas.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Estado"))
        self.BtnFacturaPagada.setText(_translate("Form", "Factura Pagada"))
        self.BtnEditarFactura.setText(_translate("Form", "Editar Factura"))
        self.BtnEliminarFactura.setText(_translate("Form", "   Eliminar Factura"))
        self.BtnGenerarTicket.setText(_translate("Form", "   Generar Ticket"))