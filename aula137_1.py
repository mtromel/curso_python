class Computador:
    def __init__(self, modelo):
        self.modelo = modelo
        self._placamae = None
        self._processador = None
        self._memoria = None
        self._armazenamento = None
        self._video = None
        self._sistema = None
        self._gabinete = None
        self._fonte = None
    
    @property
    def placamae(self):
        return self._placamae
    
    @placamae.setter
    def placamae(self, valor):
        self._placamae = valor

    @property
    def processador(self):
        return self._modelo

    @processador.setter
    def processador(self, valor):
        self._modelo = valor
    
    @property
    def memoria(self):
        return self._memoria
    
    @memoria.setter
    def memoria(self, valor):
        self._memoria = valor
    
    @property
    def armazenamento(self):
        return self._armazenamento
    
    @armazenamento.setter
    def armazenamento(self, valor):
        self._armazenamento = valor

    @property
    def video(self):
        return self._video
    
    @video.setter
    def video(self, valor):
        self._video = valor
    
    @property
    def sistema(self):
        return self._sistema
    
    @sistema.setter
    def sistema(self, valor):
        self._sistema = valor
    
    @property
    def gabinete(self):
        return self._gabinete
    
    @gabinete.setter
    def gabinete(self, valor):
        self._gabinete = valor
    
    @property
    def fonte(self):
        return self._fonte
    
    @fonte.setter
    def fonte(self, valor):
        self._fonte = valor

class PlacaMae:
    def __init__(self, valor):
        self.valor = valor

class Processador:
    def __init__(self, valor):
        self.valor = valor

class Memoria:
    def __init__(self, valor):
        self.valor = valor

class Armazenamento:
    def __init__(self, valor):
        self.valor = valor

class Video:
    def __init__(self, valor):
        self.valor = valor

class Sistema:
    def __init__(self, valor):
        self.valor = valor

class Gabinete:
    def __init__(self, valor):
        self.valor = valor

class Fonte:
    def __init__(self, valor):
        self.valor = valor


def imprime_modelo(computador):
    print('Modelo', computador.modelo)
    print(computador.placamae.valor)
    print(computador.processador.valor)
    print(computador.memoria.valor)
    print(computador.armazenamento.valor)
    print(computador.video.valor)
    print(computador.sistema.valor)
    print(computador.fonte.valor)
    print(computador.gabinete.valor)

b300 = Computador('B300')
b500 = Computador('B500')
b700 = Computador('B700')
b900 = Computador('B900')

i3_10 = Processador('Intel Core i3 10º Geração')
i3_11 = Processador('Intel Core i3 11º Geração')
i3_12 = Processador('Intel Core i3 12º Geração')
i3_13 = Processador('Intel Core i3 13º Geração')
i5_11 = Processador('Intel Core i5 11º Geração')
i7_11 = Processador('Intel Core i7 11º Geração')
i9_11 = Processador('Intel Core i9 11º Geração')

mem8gb = Memoria('8GB de Memória RAM')
mem16gb = Memoria('16GB de Memória RAM')
mem32gb = Memoria('32GB de Memória RAM')
mem64gb = Memoria('64GB de Memória RAM')

mbintel510 = PlacaMae('Placa Mãe Intel 510')
mbasus610 = PlacaMae('Placa Mãe Asus 610')
mbmsi710 = PlacaMae('Placa Mãe MSI 710')
mbrogv3 = PlacaMae('Placa Mãe ROG V III')

hd1tb = Armazenamento('HDD 1TB')
ssd256 = Armazenamento('SSD 256GB')
ssd512 = Armazenamento('SSD 512GB')
ssd256m2 = Armazenamento('SSD M2 NVME 256GB')

onboard = Video('Vídeo Intel 510 onboard')
gtx1650 = Video('Placa de Vídeo EVGA GTX 1650 6GB')
gtx3290 = Video('Placa de Vídeo EVGA GDX 3290 12GB')
gtx4390 = Video('Placa de Vídeo EVGA GTX 4390 24GB')

windows11 = Sistema('Windows 11 Professional')
semsistema = Sistema('Sem sistema operacional')
linux = Sistema('Linux Ubuntu 23.04')

gamer = Gabinete('Gabinete Gamex ATX RGB')
business = Gabinete('Gabinete MATX Business')

fonte500r = Fonte('Fonte de 500 Watts reais')
fonte650r = Fonte('Fonte de 650 Watts reais')
fonte750r = Fonte('Fonte de 750 Watts reais')
fonte200 = Fonte('Fonte 200 Watts')

b300.placamae = mbintel510
b300.processador = i3_10
b300.memoria = mem8gb
b300.armazenamento = ssd256
b300.video = onboard
b300.sistema = windows11
b300.gabinete = business
b300.fonte = fonte200

b900.placamae = mbrogv3
b900.processador = i9_11
b900.memoria = mem64gb
b900.armazenamento = ssd256m2
b900.video = gtx4390
b900.sistema = windows11
b900.gabinete = gamer
b900.fonte = fonte750r


imprime_modelo(b300)
print('--------------------------')
imprime_modelo(b900)

