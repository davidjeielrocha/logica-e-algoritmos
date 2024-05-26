import math

class Circulo:
    """
    Representa um círculo no plano cartesiano com informações de posição e raio.
    """

    def __init__(self, x_centro, y_centro, raio):
        """
        Inicializa um novo objeto Circulo.

        Args:
            x_centro (float): Coordenada x do centro do círculo (não negativa).
            y_centro (float): Coordenada y do centro do círculo (não negativa).
            raio (float): Raio do círculo (não negativo).
        """
        if x_centro < 0 or y_centro < 0 or raio < 0:
            raise ValueError("As coordenadas do centro e o raio devem ser não negativos.")

        self.x_centro = x_centro
        self.y_centro = y_centro
        self.raio = raio

    def calcular_area(self):
        """
        Calcula a área do círculo.

        Returns:
            float: Área do círculo.
        """
        return math.pi * self.raio**2

    def calcular_diametro(self):
        """
        Calcula o diâmetro do círculo.

        Returns:
            float: Diâmetro do círculo.
        """
        return 2 * self.raio

    def calcular_comprimento_circunferencia(self):
        """
        Calcula o comprimento da circunferência do círculo.

        Returns:
            float: Comprimento da circunferência do círculo.
        """
        return 2 * math.pi * self.raio

    def mover_circulo(self, novo_x_centro, novo_y_centro):
        """
        Move o círculo para uma nova posição no plano cartesiano.

        Args:
            novo_x_centro (float): Nova coordenada x do centro do círculo (não negativa).
            novo_y_centro (float): Nova coordenada y do centro do círculo (não negativa).
        """
        if novo_x_centro < 0 or novo_y_centro < 0:
            raise ValueError("As novas coordenadas do centro devem ser não negativas.")

        self.x_centro = novo_x_centro
        self.y_centro = novo_y_centro

# Criando um objeto Circulo
meu_circulo = Circulo(2, 3, 5)

# Testando os métodos
print("Área:", meu_circulo.calcular_area())
print("Diâmetro:", meu_circulo.calcular_diametro())
print("Comprimento da circunferência:", meu_circulo.calcular_comprimento_circunferencia())

# Movendo o círculo
meu_circulo.mover_circulo(4, 6)
print("Novas coordenadas do centro:", meu_circulo.x_centro, meu_circulo.y_centro)
