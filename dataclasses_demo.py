from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int

    # Método propio (no lo genera @dataclass automáticamente)
    def total(self) -> float:
        return self.precio * self.cantidad

    #pruebas
p = Producto("Laptop", 1200.50, 2)
print(p)
print(f"Total: {p.total()}")

