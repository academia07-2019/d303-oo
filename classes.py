
class CuboMagico():


    def __init__(self, cores, lados):
        self.colors = cores
        self.sides = lados


    def get_cores(self):
        return self.colors


    def print_cores_por_linha(self):
        for i in self.colors:
            print(i)

    
    def get_lados(self):
        return self.sides


    def set_cores(self, pigmentos):
        self.colors = pigmentos

    
    def set_lados(self, lados):
        self.sides = lados


cubomagico = CuboMagico(['vermelho', 'azul'], 6)


class Animal():
    vida = True

    def __init__(self, pelo, especie, olhos, patas, nome):
        self.nome = nome
        self.pelo = pelo
        self.especie = especie
        self.olhos = olhos
        self.patas = patas
    

    def quero_todas_informacoes(self):
        print("Esse animal é um {}, tem {} olhos e tem {} patas.".format(
            self.especie, self.olhos, self.patas))
    

    def quero_qtd_olhos(self):
        print("Esse animal tem {} olhos".format(self.olhos))


class Cachorro(Animal):


    def __init__(self, pelo, especie, olhos, patas, nome, raca):
        super()
        self.olhos = olhos
        self.raca = raca
        self.patas = patas

    
    def get_vida(self):
        print(self.vida)


    def quero_todas_informacoes(self):
        print("Esse animal é um {}, tem {} olhos, tem {} patas.".format(
        self.raca, self.olhos, self.patas))

    
    def tem_pelo(self):
        print(self.pelo)


#cleiton = Cachorro(True, 'vira lata', 1, 3, 'Cleiton', 'vira lata')
#cleiton.quero_todas_informacoes()
#cleiton.tem_pelo()
#cleiton.quero_todas_informacoes()
#cleiton.get_vida()

#porco = Animal(True, "Suíno", 2, 4)
#print(porco.nome)
#galinha = Animal(False, "Aves", 2, 2)

#galinha.quero_todas_informacoes()
#porco.quero_todas_informacoes()
#porco.quero_qtd_olhos()

