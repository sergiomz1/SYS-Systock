from PyQt5.QtWidgets import (
    QWidget,
    QMessageBox,
)
from PyQt5 import QtWidgets, QtCore
from ..ui import Ui_Facturas
from ..database.database import SessionLocal
from ..controllers.facturas_crud import *
from ..utils.enviar_notifi import enviar_notificacion
from ..utils.restructura_ticket import generate_ticket
from ..view.VentasAView import VentasA_View


class Facturas_View(QWidget, Ui_Facturas):
    def __init__(self, parent=None):
        super(Facturas_View, self).__init__(parent)
        self.setupUi(self)

        self.InputBuscador.setPlaceholderText("Buscar por ID, (Usuario), Fecha, Metodo de pago o Tipo deFactura")
        self.InputBuscador.textChanged.connect(self.buscar_facturas)

        self.TablaFacturas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TablaFacturas.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.TablaFacturas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.BtnEliminarFactura.clicked.connect(self.eliminar_factura)
        self.BtnGenerarTicket.clicked.connect(self.generar_ticket)
        self.BtnFacturaPagada.clicked.connect(self.factura_pagada)
        self.BtnEditarFactura.clicked.connect(self.editar_factura)

    def showEvent(self, event):
        super().showEvent(event)
        self.limpiar_tabla_facturas()
        self.mostrar_facturas()

    def mostrar_facturas(self):
        # Obtener datos de la tabla
        self.db = SessionLocal()
        rows = obtener_facturas(self.db)

        self.actualizar_tabla_facturas(rows)

        # Cerrar la conexión a la base de datos
        self.db.close()

    def limpiar_tabla_facturas(self):
        self.TablaFacturas.setRowCount(0)

    def actualizar_tabla_facturas(self, rows):

        if rows:
            self.TablaFacturas.setRowCount(len(rows))
            self.TablaFacturas.setColumnCount(10)

            for row_idx, row in enumerate(rows):
                id_factura = str(row.ID_Factura)
                fecha = str(row.Fecha_Factura)
                monto_efectivo = str(row.Monto_efectivo)
                monto_transaccion = str(row.Monto_TRANSACCION)
                estado = str(row.Estado)
                id_tipo_factura = str(row.tipofactura)
                id_metodo_pago = str(row.metodopago)
                usuario = str(row.usuario)

                if row.Estado:
                    estado = "Activo"
                else:
                    estado = "Inactivo"

                id_item = QtWidgets.QTableWidgetItem(id_factura)
                id_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TablaFacturas.setItem(row_idx, 0, id_item)

                id_cliente_item = QtWidgets.QTableWidgetItem(usuario)    #usuario
                id_cliente_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TablaFacturas.setItem(row_idx, 1, id_cliente_item)

                id_metodo_pago_item = QtWidgets.QTableWidgetItem(id_metodo_pago)
                id_metodo_pago_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TablaFacturas.setItem(row_idx, 2, id_metodo_pago_item)

                id_tipo_factura_item = QtWidgets.QTableWidgetItem(id_tipo_factura)
                id_tipo_factura_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TablaFacturas.setItem(row_idx, 3, id_tipo_factura_item)

                fecha_item = QtWidgets.QTableWidgetItem(fecha)
                fecha_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TablaFacturas.setItem(row_idx, 4, fecha_item)

                id_categoria_item = QtWidgets.QTableWidgetItem("Actual")  #Fecha Modificación
                id_categoria_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TablaFacturas.setItem(row_idx, 5, id_categoria_item)

                monto_efectivo_item = QtWidgets.QTableWidgetItem(monto_efectivo)
                monto_efectivo_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TablaFacturas.setItem(row_idx, 6, monto_efectivo_item)

                monto_transaccion_item = QtWidgets.QTableWidgetItem(monto_transaccion)
                monto_transaccion_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TablaFacturas.setItem(row_idx, 7, monto_transaccion_item)

                total = row.Monto_efectivo + row.Monto_TRANSACCION

                total_item = QtWidgets.QTableWidgetItem(str(total))
                total_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TablaFacturas.setItem(row_idx, 8, total_item)

                estado_item = QtWidgets.QTableWidgetItem(estado)
                estado_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.TablaFacturas.setItem(row_idx, 9, estado_item)

    def obtener_ids_seleccionados(self):
        """
        Obtiene los IDs de los productos seleccionados en la tabla.
        """
        filas_seleccionadas = self.TablaFacturas.selectionModel().selectedRows()
        ids = []

        for fila in filas_seleccionadas:
            id_producto = self.TablaFacturas.item(
                fila.row(), 0
            ).text()  # Columna 0: ID del producto
            ids.append(int(id_producto))

        return ids

    def eliminar_factura(self):
        """
        Elimina una factura.
        """
        # Obtener el ID de la factura seleccionada
        ids = self.obtener_ids_seleccionados()

        if not ids:
            enviar_notificacion(
                "Advertencia", "No se seleccionaron productos para eliminar."
            )
            return

        respuesta = QtWidgets.QMessageBox.question(
            self,
            "Confirmar Eliminación",
            f"¿Está seguro de que desea eliminar {len(ids)} producto(s)?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        )

        if respuesta == QtWidgets.QMessageBox.Yes:
            try:
                self.db = SessionLocal()


                for id_factura in ids:
                    eliminar_factura(self.db, id_factura)

                self.db.commit()
                enviar_notificacion("Éxito", "Producto(s) eliminado(s) correctamente.")

                # Actualizar la tabla
                self.limpiar_tabla_facturas()
                self.mostrar_facturas()

            except Exception as e:
                enviar_notificacion("Error", f"Error al eliminar productos: {e}")
            finally:
                self.db.close()

    def buscar_facturas(self):
        """
        Busca facturas en la base de datos y actualiza la tabla.
        """
        busqueda = self.InputBuscador.text().strip()
        if not busqueda:
            self.mostrar_facturas()
            return

        self.db = SessionLocal()

        facturas = buscar_facturas(self.db, busqueda)
        self.actualizar_tabla_facturas(facturas)

        self.db.close()

    def generar_ticket(self):
        """
        Genera un ticket de venta para la factura seleccionada.
        """
        ids = self.obtener_ids_seleccionados()

        if not ids:
            enviar_notificacion(
                "Advertencia", "No se seleccionaron facturas para generar ticket."
            )
            return

        db = SessionLocal()

        # Obtener la factura completa
        factura_completa = obtener_factura_completa(db, ids[0])

        if not factura_completa:
            print(f"No se encontró la factura con ID {ids[0]}")
            return
        # Extraer los datos de la factura
        factura = factura_completa["Factura"]
        cliente = factura_completa["Cliente"]  # Acceder al primer elemento de la lista
        detalles = factura_completa["Detalles"]

        # Calcular subtotal y descuento
        subtotal = sum(detalle["Subtotal"] for detalle in detalles)
        delivery_fee = sum(detalle["Descuento"] for detalle in detalles)

        # Extraer información necesaria para el ticket
        client_name = f"{cliente['Nombre']} {cliente['Apellido']}"
        client_id = cliente["ID_Cliente"]
        client_address = cliente["Direccion"]
        client_phone = cliente["Teléfono"]
        items = [
            {
                "quantity": detalle["Cantidad"],
                "name": detalle.get("Producto", "Producto sin nombre"),  # Asegúrate de incluir el nombre del producto en la consulta
                "unit_price": float(detalle["Precio_Unitario"]) if isinstance(detalle["Precio_Unitario"], (int, float)) else 0.0,
            }
            for detalle in detalles
        ]
        
        items2 = []
        for item in items:
            quantity = item["quantity"]
            description = item["name"]
            value = float(item["unit_price"])

            items2.append((quantity, description, value))
            print(f"Debug: quantity={quantity}, description={description}, value={value}")

        # Calcular el total
        total = subtotal + delivery_fee

        # Extraer información adicional de la factura
        payment_method = factura["MetodoPago"]
        invoice_number = factura["ID_Factura"]
        pan = "123456789"  # Número fijo de ejemplo, cámbialo si es necesario

        # Llamar a la función generate_ticket
        generate_ticket(
            client_name=client_name,
            client_id=client_id,
            client_address=client_address,
            client_phone=client_phone,
            items=items2,
            subtotal=subtotal,
            delivery_fee=delivery_fee,
            total=total,
            payment_method=payment_method,
            invoice_number=invoice_number,
            pan=pan,
            filename=None,  # Puedes cambiar esto según tu necesidad
        )
        
        QMessageBox.warning(self, "Ticket", f"Factura generada exitosamente.")

    def factura_pagada(self):
        """
        Marca la factura como pagada.
        """
        ids = self.obtener_ids_seleccionados()

        if not ids:
            enviar_notificacion(
                "Advertencia", "No se seleccionaron productos para marcar como pagada."
            )
            return

        try:
            db = SessionLocal()
            
            for id_factura in ids:
                factura = obtener_factura_por_id(db=db, id_factura=id_factura)
                if factura.Estado == True:
                    QMessageBox.warning(self, "Factura", f"La factura {id_factura} ya está pagada.")
                else:
                    actualizar_factura(db=db, id_factura=id_factura, estado=True)
            db.commit()
            enviar_notificacion("Éxito", "Factura(s) marcada(s) como pagada(s) correctamente.")
            self.limpiar_tabla_facturas()
            self.mostrar_facturas()
        except Exception as e:
            enviar_notificacion("Error", f"Error al marcar factura(s) como pagada(s): {e}")
        finally:
            db.close()
    
    def editar_factura(self):
        """Abrir ventana de ventas con los datos de la factura seleccionada."""
        try:
            seleccion = self.lista_facturas.curselection()
            if not seleccion:
                QMessageBox.showwarning("Advertencia", "Seleccione una factura para editar.")
                return

            # Obtener ID de la factura seleccionada
            factura_id = int(self.lista_facturas.get(seleccion[0]).split()[1])

            # Llamar a la función para obtener todos los datos de la factura
            factura_completa = obtener_factura_completa(self.db, factura_id)

            if not factura_completa:
                QMessageBox.showerror("Error", f"No se encontró la factura con ID {factura_id}.")
                return

            # Abrir la ventana de ventas y pasar los datos de la factura
            VentasA_View(self.root, self.db, factura_completa)
            self.frame.destroy()  # Cierra la ventana actual

        except Exception as e:
            QMessageBox.showerror("Error", str(e))
    