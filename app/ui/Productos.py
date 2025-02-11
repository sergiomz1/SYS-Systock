# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Productos.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Productos(object):
    def setupUi(self, Productos):
        Productos.setObjectName("Productos")
        Productos.resize(1402, 1095)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Productos.sizePolicy().hasHeightForWidth())
        Productos.setSizePolicy(sizePolicy)
        Productos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Productos)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Contenedor = QtWidgets.QWidget(Productos)
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
        self.Contenido = QtWidgets.QStackedWidget(self.Contenedor)
        self.Contenido.setStyleSheet("margin-left:10px;\n"
"border-radius:15px;\n"
"background-color: #f2f2f2; \n"
"")
        self.Contenido.setObjectName("Contenido")
        self.ContenidoPage1 = QtWidgets.QWidget()
        self.ContenidoPage1.setObjectName("ContenidoPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ContenidoPage1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.ContenidoPage1)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BtnIngresarProducto = QtWidgets.QPushButton(self.widget_3)
        self.BtnIngresarProducto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnIngresarProducto.setStyleSheet("\n"
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
"}")
        self.BtnIngresarProducto.setObjectName("BtnIngresarProducto")
        self.gridLayout_2.addWidget(self.BtnIngresarProducto, 8, 3, 1, 1)
        self.InputPrecioMayor = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputPrecioMayor.sizePolicy().hasHeightForWidth())
        self.InputPrecioMayor.setSizePolicy(sizePolicy)
        self.InputPrecioMayor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputPrecioMayor.setObjectName("InputPrecioMayor")
        self.gridLayout_2.addWidget(self.InputPrecioMayor, 5, 5, 1, 1)
        self.BtnEliminar = QtWidgets.QPushButton(self.widget_3)
        self.BtnEliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnEliminar.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: red; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white; /* Color del texto */\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: center; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    margin-top:20px;\n"
"    cursor: pointer; /* Cursor de mano al pasar sobre el botón */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer; /* Cursor de mano al pasar sobre el botón */\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/iconos/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnEliminar.setIcon(icon)
        self.BtnEliminar.setIconSize(QtCore.QSize(30, 30))
        self.BtnEliminar.setObjectName("BtnEliminar")
        self.gridLayout_2.addWidget(self.BtnEliminar, 8, 5, 1, 1)
        self.InputCantidadMin = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputCantidadMin.sizePolicy().hasHeightForWidth())
        self.InputCantidadMin.setSizePolicy(sizePolicy)
        self.InputCantidadMin.setMinimumSize(QtCore.QSize(250, 50))
        self.InputCantidadMin.setMaximumSize(QtCore.QSize(250, 50))
        self.InputCantidadMin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputCantidadMin.setObjectName("InputCantidadMin")
        self.gridLayout_2.addWidget(self.InputCantidadMin, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 1, 1, 1)
        self.InputCantidadMax = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputCantidadMax.sizePolicy().hasHeightForWidth())
        self.InputCantidadMax.setSizePolicy(sizePolicy)
        self.InputCantidadMax.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputCantidadMax.setObjectName("InputCantidadMax")
        self.gridLayout_2.addWidget(self.InputCantidadMax, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.InputMarca = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputMarca.sizePolicy().hasHeightForWidth())
        self.InputMarca.setSizePolicy(sizePolicy)
        self.InputMarca.setMinimumSize(QtCore.QSize(250, 50))
        self.InputMarca.setMaximumSize(QtCore.QSize(250, 50))
        self.InputMarca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputMarca.setObjectName("InputMarca")
        self.gridLayout_2.addWidget(self.InputMarca, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.InputPrecioCompra = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputPrecioCompra.sizePolicy().hasHeightForWidth())
        self.InputPrecioCompra.setSizePolicy(sizePolicy)
        self.InputPrecioCompra.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputPrecioCompra.setObjectName("InputPrecioCompra")
        self.gridLayout_2.addWidget(self.InputPrecioCompra, 5, 2, 1, 1)
        self.InputCodigo = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputCodigo.sizePolicy().hasHeightForWidth())
        self.InputCodigo.setSizePolicy(sizePolicy)
        self.InputCodigo.setMinimumSize(QtCore.QSize(250, 50))
        self.InputCodigo.setMaximumSize(QtCore.QSize(250, 50))
        self.InputCodigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputCodigo.setObjectName("InputCodigo")
        self.gridLayout_2.addWidget(self.InputCodigo, 3, 0, 1, 1)
        self.InputCantidad = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputCantidad.sizePolicy().hasHeightForWidth())
        self.InputCantidad.setSizePolicy(sizePolicy)
        self.InputCantidad.setMinimumSize(QtCore.QSize(250, 50))
        self.InputCantidad.setMaximumSize(QtCore.QSize(250, 50))
        self.InputCantidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputCantidad.setObjectName("InputCantidad")
        self.gridLayout_2.addWidget(self.InputCantidad, 3, 5, 1, 1)
        self.InputCategoria = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputCategoria.sizePolicy().hasHeightForWidth())
        self.InputCategoria.setSizePolicy(sizePolicy)
        self.InputCategoria.setMinimumSize(QtCore.QSize(250, 50))
        self.InputCategoria.setMaximumSize(QtCore.QSize(250, 50))
        self.InputCategoria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputCategoria.setObjectName("InputCategoria")
        self.gridLayout_2.addWidget(self.InputCategoria, 3, 3, 1, 1)
        self.LabelVentasA = QtWidgets.QLabel(self.widget_3)
        self.LabelVentasA.setStyleSheet("#LabelVentasA {\n"
"    font-weight: bold; /* Negrita */\n"
"    font-size: 34px; /* Tamaño de fuente */\n"
"}\n"
"")
        self.LabelVentasA.setObjectName("LabelVentasA")
        self.gridLayout_2.addWidget(self.LabelVentasA, 0, 0, 1, 1)
        self.InputPrecioUnitario = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputPrecioUnitario.sizePolicy().hasHeightForWidth())
        self.InputPrecioUnitario.setSizePolicy(sizePolicy)
        self.InputPrecioUnitario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputPrecioUnitario.setObjectName("InputPrecioUnitario")
        self.gridLayout_2.addWidget(self.InputPrecioUnitario, 5, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)
        self.InputNombre = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputNombre.sizePolicy().hasHeightForWidth())
        self.InputNombre.setSizePolicy(sizePolicy)
        self.InputNombre.setMinimumSize(QtCore.QSize(250, 50))
        self.InputNombre.setMaximumSize(QtCore.QSize(250, 50))
        self.InputNombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputNombre.setObjectName("InputNombre")
        self.gridLayout_2.addWidget(self.InputNombre, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(self.ContenidoPage1)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(1200, 50))
        self.frame_2.setStyleSheet("")
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.InputBuscador = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
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
        self.horizontalLayout_3.addWidget(self.InputBuscador)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setMaximumSize(QtCore.QSize(50, 50))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("assets/iconos/buscar.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.verticalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.TablaProductos = QtWidgets.QTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TablaProductos.sizePolicy().hasHeightForWidth())
        self.TablaProductos.setSizePolicy(sizePolicy)
        self.TablaProductos.setMinimumSize(QtCore.QSize(1320, 450))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TablaProductos.setFont(font)
        self.TablaProductos.setStyleSheet("\n"
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
        self.TablaProductos.setObjectName("TablaProductos")
        self.TablaProductos.setColumnCount(13)
        self.TablaProductos.setRowCount(24)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaProductos.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        self.TablaProductos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaProductos.setHorizontalHeaderItem(12, item)
        self.verticalLayout_3.addWidget(self.TablaProductos, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(500, 50))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12, 0, QtCore.Qt.AlignRight)
        self.LabelTotalCp = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelTotalCp.sizePolicy().hasHeightForWidth())
        self.LabelTotalCp.setSizePolicy(sizePolicy)
        self.LabelTotalCp.setMinimumSize(QtCore.QSize(300, 30))
        self.LabelTotalCp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LabelTotalCp.setObjectName("LabelTotalCp")
        self.horizontalLayout_6.addWidget(self.LabelTotalCp, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget)
        self.Contenido.addWidget(self.ContenidoPage1)
        self.horizontalLayout_2.addWidget(self.Contenido)
        self.horizontalLayout.addWidget(self.Contenedor)

        self.retranslateUi(Productos)
        QtCore.QMetaObject.connectSlotsByName(Productos)

    def retranslateUi(self, Productos):
        _translate = QtCore.QCoreApplication.translate
        Productos.setWindowTitle(_translate("Productos", "Form"))
        self.BtnIngresarProducto.setText(_translate("Productos", "Ingresar Producto"))
        self.BtnEliminar.setText(_translate("Productos", "   Eliminar"))
        self.label_2.setText(_translate("Productos", "Cantidad Max."))
        self.label_10.setText(_translate("Productos", "Precio al por Mayor"))
        self.label.setText(_translate("Productos", "Cantidad"))
        self.label_9.setText(_translate("Productos", "Precio Unitario"))
        self.label_7.setText(_translate("Productos", "Categoria"))
        self.label_8.setText(_translate("Productos", "Cantidad Min."))
        self.label_5.setText(_translate("Productos", "Nombre"))
        self.label_4.setText(_translate("Productos", "Precio Compra"))
        self.label_3.setText(_translate("Productos", "Codigo"))
        self.LabelVentasA.setText(_translate("Productos", "Productos"))
        self.label_6.setText(_translate("Productos", "Marca"))
        item = self.TablaProductos.verticalHeaderItem(0)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(1)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(2)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(3)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(4)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(5)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(6)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(7)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(8)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(9)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(10)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(11)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(12)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(13)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(14)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(15)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(16)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(17)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(18)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(19)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(20)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(21)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(22)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.verticalHeaderItem(23)
        item.setText(_translate("Productos", "Nueva fila"))
        item = self.TablaProductos.horizontalHeaderItem(0)
        item.setText(_translate("Productos", "Código"))
        item = self.TablaProductos.horizontalHeaderItem(1)
        item.setText(_translate("Productos", "Nombre"))
        item = self.TablaProductos.horizontalHeaderItem(2)
        item.setText(_translate("Productos", "Marca"))
        item = self.TablaProductos.horizontalHeaderItem(3)
        item.setText(_translate("Productos", "Categoria"))
        item = self.TablaProductos.horizontalHeaderItem(4)
        item.setText(_translate("Productos", "Cantidad"))
        item = self.TablaProductos.horizontalHeaderItem(5)
        item.setText(_translate("Productos", "CMin"))
        item = self.TablaProductos.horizontalHeaderItem(6)
        item.setText(_translate("Productos", "CMax"))
        item = self.TablaProductos.horizontalHeaderItem(7)
        item.setText(_translate("Productos", "CP"))
        item = self.TablaProductos.horizontalHeaderItem(8)
        item.setText(_translate("Productos", "PU"))
        item = self.TablaProductos.horizontalHeaderItem(9)
        item.setText(_translate("Productos", "PAM"))
        item = self.TablaProductos.horizontalHeaderItem(10)
        item.setText(_translate("Productos", "GU"))
        item = self.TablaProductos.horizontalHeaderItem(11)
        item.setText(_translate("Productos", "GAM"))
        item = self.TablaProductos.horizontalHeaderItem(12)
        item.setText(_translate("Productos", "State"))
        self.label_12.setText(_translate("Productos", "Total CP:"))
        self.LabelTotalCp.setText(_translate("Productos", "$"))
