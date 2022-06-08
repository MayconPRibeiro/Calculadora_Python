import this
import Operacoes #Acessando a classe Operacoes
this.opcao = -1 #Declaração de variavel global
this.num1 = 0
this.num2 = 0

def mostrarMenu():
    print('Escolha uma das opções abaixo: \n' +
          '1. Soma\n' +
          '2. Subtração\n' +
          '3. Multiplicação\n' +
          '4. Divisão\n' +
          '0. Sair \n\n')

    this.opcao = int(input()) #Entrada de dados

def coletarNum1():
    print('Informe o primeiro número: ')
    this.num1 = float(input()) #Float converte em número com vírgula

def coletarNum2():
    print('Informe o segundo número: ')
    this.num2 = float(input())

def executar():
    while(this.opcao != 0):

        mostrarMenu() #Chamando método que mostra as opções ao usuário

        if this.opcao == 1:
            coletarNum1()
            coletarNum2()
            print('A soma entre {} e {} = {}' .format(this.num1, this.num2, Operacoes.soma(this.num1, this.num2)))

        elif this.opcao == 2:
            coletarNum1()
            coletarNum2()
            print('A subtração entre {} e {} = {}' .format(this.num1, this.num2, Operacoes.subtrair(this.num1, this.num2)))

        elif this.opcao == 3:
            coletarNum1()
            coletarNum2()
            print('A multiplicação entre {} e {} = {}' .format(this.num1, this.num2, Operacoes.multiplicar(this.num1, this.num2)))

        elif this.opcao == 4:
            coletarNum1()
            coletarNum2()
            if this.num2 <= 0:
                print(Operacoes.dividir(this.num1, this.num2))

            else:
                print('A divisão entre {} e {} = {}' .format(this.num1, this.num2, Operacoes.dividir(this.num1, this.num2)))

        else:
            print('Obrigado!')
            this.opcao=0