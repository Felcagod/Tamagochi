import personagens 
from personagens import * 
from os import * 
from time import sleep
from configuracoes_de_estetica import limpar_tela
from configuracoes_de_estetica import linhas

#criando o tamagochi;
class Tamagochi():
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 10
        self.felicidade = 5
        self.idade = 0
        self.necessidade_banheiro = 0
        self.energia = 10
        self.sujeira = 0 

    #funcao para mudar de nome;
    def MudarNome(self, nome):
        self.nome = nome 

    #Alimentando o personagem;
    def alimentar(self, comida):
        if comida == "carne":
            self.fome -= 3
        elif comida == "fruta":
            self.fome -= 2
        elif comida == "doce":
            self.fome -= 1
        self.felicidade += 1
        self.saude += 1

    #brincando com o personagem;
    def brincar(self):
        self.fome += 1 
        self.energia -= 1
        self.felicidade +=3
        self.necessidade_banheiro += 1

    #Cuidar do personagem;
    def cuidar(self):
        self.saude += 2
        if self.saude > 10:
            self.saude = 10 
        self.necessidade_banheiro += 1

    #Personagem dormir;
    def dormir(self):
        self.fome+=2 
        self.energia+=5
        if self.energia > 10:
            self.energia = 10
        self.necessidade_banheiro+=1

    #Personagem vai ao banheiro;
    def banheiro(self):
        self.necessidade_banheiro = 0 
        self.sujeira += 1
    
    #Limpando a sujeira
    def LimparSujeira(self):
        self.sujeira-=1

    #Deixando o persoangem mai velho
    #mude o numero daa variavel "self.idade += 0.5" para o tempo passar mais rapido
    def envelhecer(self):
        self.idade += 0.5
        self.fome += 1
        self.saude -= 1
        self.felicidade -= 1
        self.necessidade_banheiro += 1

tamagochi = Tamagochi("Pikachu")

#escolhendo o personagem
def escolha():
    global cont 
    cont=0
    limpar_tela()
    print("---ESCOLHA UM PERSONAGEM---")
    print("1. Pikachu")
    print("2. Monstrinho")
    print("3. Porquinho")
    print("4. AmongUs")
    try:
        character_option = int(input(": "))
        
        if character_option == 1:
            cont+=1
            
        elif character_option == 2:
            cont+=2
            
        elif character_option == 3:
            cont+=3
            
        elif character_option == 4:
            cont+=4
        else:
            print("Opcao invalida. Tente novamente")
            linhas()

    except:
        limpar_tela()
        print('Erro Inesperado. Tente novamente!')
        sleep(2)
        limpar_tela()

#escolhendo o nome do personagem 
def Escolher_nome():
    limpar_tela()
    print("---Nome do Personagem--- ")
    troca = input("Nome: ")
    troca.capitalize()
    tamagochi.MudarNome(troca)
try:
    escolha()
    Escolher_nome()
except:
    print("Error.")

#looping do jogo 
while True:
    try:

        limpar_tela()
        if cont == 1:
            pikachu()
        elif cont == 2:
            monstrinho()
        elif cont == 3:
            porco()
        elif cont == 4:
            amongus()
        linhas()
        print(f"Nome: {tamagochi.nome}")
        print(f"Fome: {tamagochi.fome}")
        print(f"Saude: {tamagochi.saude}")
        print(f"Felicidade: {tamagochi.felicidade}")
        print(f"Idade: {tamagochi.idade} anos")
        print(f"Necessidade de ir ao banheiro: {tamagochi.necessidade_banheiro}")
        print(f"Energia: {tamagochi.energia}")
        print(f"Sujeira: {tamagochi.sujeira}")
        linhas()
        print("O que você quer fazer?")
        print("1. Alimentar")
        print("2. Brincar")
        print("3. Cuidar")
        print("4. Dormir")
        print("5. Banheiro")
        print("6. Limpar Sujeira")
        print("7. Sair")
        opcao = input("Opcao escolhida: ")
        limpar_tela()

        if opcao == "1":#Alimentando o {personagem}
            comida = input("O que você quer alimentar? (carne, fruta, doce): ".lower())
            tamagochi.alimentar(comida)

        elif opcao == "2":#brincando com o {personagem}
            tamagochi.brincar() 
    
        elif opcao == "3":#Cuidando do {Personagem}
            tamagochi.cuidar()

        elif opcao == "4":#{Personagem} Dormindo
            tamagochi.dormir()

        elif opcao == "5":#Personagem vai ao banheiro
            tamagochi.banheiro() 

        elif opcao == "6":#Limpando a sujeira 
            tamagochi.LimparSujeira()
            

        elif opcao == "7":#Saindo do Jogo
            limpar_tela()
            print("----OBRIGADO POR JOGAR!----")
            sleep(2)
            break 
        else:
            print("Opcao invalida. Tente novamente!")

        tamagochi.envelhecer()

        if tamagochi.fome >= 10:
            print("Seu tamagochi Morreu de fome ")
            break 
        elif tamagochi.saude <= 0:
            print("Seu Tamagochi morreum, a saude dele estava baixa")
            break 

    except:
        print("Error.")

















    