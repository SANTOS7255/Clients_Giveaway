from random import choices

#list
clientes = []

while True:
    
    #menu
    menu = '-------MENU---------------------------\n'
    
    centralizar = menu.center(25)
    
    print(centralizar)

    menu = str.upper(input('Para ver as informações dos clientes registrados digite "informações"\n\nPara anotar as informações dos clientes digite "Clientes"\n\nPara encerrar o programa digite "Encerrar"\n\nPara realizar o sorteio digite "Sorteio"\n\nDigite aqui: '))
    
    #informações do cliente
    if menu == 'CLIENTES':
        nome = str(input('\nNome do cliente: '))
        telefone = str(input('\nNúmero de telefone do cliente: '))

        #adicionando info dos clientes a lista
        clientes.append(nome)
        clientes.append(telefone)

    #ver informações dos clientes registrados
    if menu == 'INFORMAÇÕES' or 'INFORMAÇOES' or 'INFORMACOES':
        print(clientes)

    #sorteio
    if menu == 'SORTEIO':
        print(choices(clientes, k=2 ))

    #encerrar o programa
    if menu == 'ENCERRAR':
        break

    if menu == '':
        print('Opção inválida')

print('Você encerrou o programa')
    
  