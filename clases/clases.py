										
# Escribir una clase en python llamada círculo que contenga un radio, con un método que
# devuelva el área y otro que devuelva el perímetro del círculo.
# Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
# usuario e impidiendo la instanciación.
# Si printeamos el objeto creado debe mostrarse una representación amigable.
# El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
# mostrar un error y no permitir modificación.
# Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
# multiplicado por n. No permitir la multiplicación por números <= 0

class Circulo:
    radio = int (input("Ingrese el radio del circulo: "))
    
    def area(self):
        """Método para definir el área del circulo"""
        return ("el área del circulo es: ", 3.14 * self.radio ** 2)
        """retorna:
        >>> c = Circulo(5)
        >>> c.area()
        78.5
        """
    
    def perimetro(self):
        """método para definir el perímetro del circulo"""
        return ("El perímetro del círculo es: ", 2 * 3.14 * self.radio)
        """retorna:
        >>> c = Circulo(5)
        >>> c.perimetro()
        31.400000000000002
        """
    def __mult__(self, n):
        """método para permitir la multiplicación del circulo por n"""
        n = int (input("Ingrese el número por el que desea multiplicar el radio: "))
        if n <= 0:
            raise Exception("No se puede multiplicar por un numero negativo o cero")
        else:
            return self.radio * n
        """retorna:
        >>> c = Circulo(5)
        >>> c * 2
        10
        """

newCirculo = Circulo();
if newCirculo.radio <= 0:
    """Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
    usuario e impidiendo la instanciación."""
    raise Exception("Para crear un circulo, el radio debe ser mayor a 0");
else:
    print(newCirculo.area());
    print(newCirculo.perimetro());
    print(newCirculo.__mult__(8));

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True);