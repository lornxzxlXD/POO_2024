

class Figura:
    def calcular_area(self):
        return 0

class Rectangulo(Figura):
    def _init_(self, largo, ancho):
        self._largo = largo
        self._ancho = ancho

    def getLargo(self):
        return self._largo

    def setLargo(self, largo):
        self._largo = largo

    def getAncho(self):
        return self._ancho

    def setAncho(self, ancho):
        self._ancho = ancho

    def calcular_area(self):
        return self._largo * self._ancho

    def getInfo(self):
        print(f"Rectángulo de largo {self._largo} y ancho {self._ancho}, área: {self.calcular_area()}")

class Circulo(Figura):
    def _init_(self, radio):
        self._radio = radio
def getRadio(self):
        return self._radio

        def setRadio(self, radio):
            self._radio = radio

        def calcular_area(self):
            return 3.1416 * self._radio ** 2

        def getInfo(self):
            print(f"Círculo de radio {self._radio}, área: {self.calcular_area()}")

class Triangulo(Figura):
    def _init_(self, altura, base):
        self._altura = altura
        self._base = base

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        self._altura = altura

    def get_base(self):
        return self._base
def set_base(self, base):
        self._base = base

        def calcular_area(self):
            return (self._altura * self._base) / 2

        def getInfo(self):
            print(f"Triángulo de altura {self._altura} y base {self._base}, área: {self.calcular_area()}")


