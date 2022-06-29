from Almacen.models import Producto


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, prod: Producto):
        id = str(prod.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": prod.id,
                "nombre": prod.nombre,
                "acumulado": prod.precio_venta,
                "cantidad": 1
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += prod.precio_venta
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, prod: Producto):
        id = str(prod.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, prod: Producto):
        id = str(prod.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= prod.precio_venta
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(prod)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True  


        