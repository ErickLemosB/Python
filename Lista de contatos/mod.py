listaNome = []
listaSobrenome = []
listaNomeCompleto = []
listaTelefone = []
listaCelular = []
listaEmail = []
listaEndereco = []
listaDetalhes = []
listaOpcoes = [ "Adicionar novo contato." , "Excluir um contato." , "Editar um contato." , "Mostrar todos os contatos." , "Sair."]

class ErroNome(Exception):
    pass

def verificarEmail( email ):
    if (('@' and '.') in email and email.find('@')!= 0 and email.find('.')!=0 ) :
        posArroba = email.find('@')
        if ( email.count('@') == 1 and email[posArroba-1]!='.' and email[posArroba+1]!='.'):
            parteEmail = email.split('@')
            dominio = parteEmail[1]
            if ('.' in dominio):
                return True
    return False #formato pode ser joao.b@gmail.com ou joaob@gmail.com, etc.
def leituraEmail():
    continuar = True
    while (continuar == True):
        email = input ("Email: ")
        if (not verificarEmail(email)):
            print("Erro no input do email, tente novamente.")
        else :
            continuar = False
    return email
def leituraNomeOuSobrenome (num):
    continuar = True
    while (continuar == True):
        if (num == 1):
            nome = input("Nome: ")
        else :
            nome = input ("Sobrenome:")
        if (" " in nome) :
            nomePartes = nome.split()
            try:
                for i in range (len(nomePartes)):
                    if ( not nomePartes[i].isalpha ()) :
                        raise ErroNome("Erro no input do nome, tente novamente.")
            except ErroNome as erro:
                print(erro)
                continue
        else:
            try:
                if ( not nome.isalpha ()) :
                    raise ErroNome("Erro no input do nome, tente novamente.")
            except ErroNome as erro:
                print(erro)
                continue
        continuar = False
    return nome

def leituraTelefoneOuCelular(num):#formato deve ser somente numero ou espaco, exemplo: 1234 1234 ou 12341234
    continuar = True
    while (continuar == True): #condicao para iniciar o loop no minimo uma vez
        if (num == 1):
            numero = input ("Telefone:")
            numero = numero.strip()
        else:
            numero = input ("Celular:")
            numero = numero.strip()
        if (numero == "" or numero.isdigit()):
            return numero
        else:
            print ("Tente novamente, com um input valido.")

def bubbleSort():
    if ( len(listaNome) > 0 ) :
        for i in range (len(listaNome)-1):
            if ( listaNomeCompleto[i] > listaNomeCompleto[i+1]):
                listaNome[i] , listaNome[i+1] = listaNome[i+1] , listaNome[i] 
                listaSobrenome[i] , listaSobrenome[i+1] = listaSobrenome[i+1] , listaSobrenome[i] 
                listaTelefone[i] , listaTelefone[i+1] = listaTelefone[i+1] , listaTelefone[i]
                listaNomeCompleto[i] , listaNomeCompleto[i+1] = listaNomeCompleto[i+1] , listaNomeCompleto[i]
                listaCelular[i] , listaCelular[i+1] = listaCelular[i+1] , listaCelular[i]
                listaEmail[i] , listaEmail[i+1] = listaEmail[i+1] , listaEmail[i]
                listaEndereco[i] , listaEndereco[i+1] = listaEndereco[i+1] , listaEndereco[i]
                listaDetalhes[i] , listaDetalhes[i] = listaDetalhes[i+1] , listaDetalhes[i]

def adicionarContato (listaNome , listaSobrenome , listaNomeCompleto , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes ):
    nome = leituraNomeOuSobrenome(1)#numeros como parametro somente para verificar se e nome ou sobrenome, nome = 1,sobrenome =2
    nome = nome.strip()
    sobrenome = leituraNomeOuSobrenome(2)
    sobrenome = sobrenome.strip()
    nomeCompleto = nome + " " + sobrenome
    telefone = leituraTelefoneOuCelular(1)#numeros como parametro somente para verificar se e celular ou telefone, telefone = 1, celular = 2
    celular = leituraTelefoneOuCelular(2)
    email = leituraEmail()
    endereco = input ("Endereco: ")
    detalhes = input ("Detalhes: ")
    listaNome.append(nome)
    listaSobrenome.append(sobrenome)
    listaNomeCompleto.append(nomeCompleto)
    listaTelefone.append(telefone)
    listaCelular.append(celular)
    listaEmail.append(email)
    listaEndereco.append(endereco)
    listaDetalhes.append(detalhes)


def mostrarContatos( listaNomeCompleto , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes ):
    if (len(listaNomeCompleto)>0):
        for i in range (len(listaNomeCompleto)):
            print("Nome Completo: " + listaNomeCompleto[i])
            print("Telefone: "+listaTelefone [i])
            print("Celular: "+listaCelular[i])
            print("Email: "+listaEmail [i])
            print("Endereco: "+listaEndereco [i])
            print("Detalhes: "+listaDetalhes [i])
            print()
    else:
        print("Lista de Contatos esta vazia.")

def buscaPorNome ( listaNomeCompleto , nomeBusca ):
    for i in range (len(listaNomeCompleto)):
        if (nomeBusca.upper() == listaNomeCompleto[i].upper()):
            return i
    return -1

def buscaPorEmail ( listaEmail , nomeBusca ):
    for i in range (len(listaEmail)):
        if (nomeBusca.upper() == listaEmail[i].upper() ):
            return i
    return -1
def exclusaoDeItensLista ( i , listaNomeCompleto, listaNome , listaSobrenome , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes):
    del listaNomeCompleto[i]
    del listaNome[i]
    del listaSobrenome[i]
    del listaTelefone[i]
    del listaCelular[i]
    del listaEmail[i]
    del listaEndereco[i]
    del listaDetalhes[i]
    bubbleSort()
def excluirContato (listaNomeCompleto, listaNome , listaSobrenome , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes ):
    if (len(listaNome)==0):
        print ("Lista de contatos vazia.")
    else:
        continuar = True
        while (continuar == True):
            opcao = input ("Aperte 1 para procurar por nome ou aperte 2 para procurar por email, ou 3 para cancelar: ")
            if ( opcao == '1'):
                nomeExcluir = input("Informe o nome completo do contato que deseja excluir: ")
                if (buscaPorNome (listaNomeCompleto,nomeExcluir) == -1):
                    print ("Nome nao encontrado na lista de contatos.")
                    continuar = False
                else: 
                    i = buscaPorNome(listaNomeCompleto,nomeExcluir)
                    exclusaoDeItensLista ( i , listaNomeCompleto, listaNome , listaSobrenome , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes)
                    continuar = False
            elif (opcao == '2'):
                nomeExcluir = input("Informe o email completo do contato que deseja excluir: ")
                if (buscaPorEmail (listaEmail,nomeExcluir) == -1):
                    print ("Email nao encontrado na lista de contatos.")
                    continuar = False
                else:
                    i = buscaPorEmail(listaEmail,nomeExcluir)
                    exclusaoDeItensLista ( i , listaNomeCompleto, listaNome , listaSobrenome , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes)
                    continuar = False
            elif (opcao == '3'):
                continuar = False
            else:
                print("Opcao nao encontrada tente novamente.")

def edicaoDeItensLista ( i , listaNomeCompleto, listaNome , listaSobrenome , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes):
    
    listaNome[i] = leituraNomeOuSobrenome(1)
    listaNome[i] = listaNome[i].strip()
    listaSobrenome[i] = leituraNomeOuSobrenome(2)
    listaSobrenome[i] = listaSobrenome[i].strip()
    listaNomeCompleto[i] = listaNome[i] + " " + listaSobrenome[i]
    listaTelefone[i] = leituraTelefoneOuCelular(1)
    listaCelular[i] = leituraTelefoneOuCelular(2)
    listaEmail[i] = leituraEmail()
    listaEndereco[i] = input ("Endereco: ")
    listaDetalhes[i] = input ("Detalhes: ")
    bubbleSort()
def editarContato (listaNomeCompleto, listaNome , listaSobrenome , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes ):
    if (len(listaNome)==0):
        print ("Lista de contatos vazia.")
    else:
        continuar = True
        while (continuar == True):
            opcao = input ("Aperte 1 para procurar por nome ou aperte 2 para procurar por email, ou 3 para cancelar: ")
            if ( opcao == '1'):
                nomeEditar = input("Informe o nome completo do contato que deseja editar: ")
                if (buscaPorNome (listaNomeCompleto,nomeEditar) == -1):
                    print ("Nome nao encontrado na lista de contatos.")
                    continuar = False
                else: 
                    i = buscaPorNome(listaNomeCompleto,nomeEditar)
                    edicaoDeItensLista ( i , listaNomeCompleto, listaNome , listaSobrenome , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes)
                    continuar = False
            elif (opcao == '2'):
                nomeEditar = input("Informe o email completo do contato que deseja editar: ")
                if (buscaPorEmail (listaEmail,nomeEditar) == -1):
                    print ("Email nao encontrado na lista de contatos.")
                    continuar = False
                else:
                    i = buscaPorEmail(listaEmail,nomeEditar)
                    edicaoDeItensLista ( i , listaNomeCompleto, listaNome , listaSobrenome , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes)
                    continuar = False
            elif (opcao == '3'):
                continuar = False
            else:
                print("Opcao nao encontrada tente novamente.")

#listaOpcoes = [ "Adicionar novo contato." , "Excluir um contato." , "Editar um contato." , "Mostrar todos os contatos." , "Sair."]

def menu ():
    opcao = 0
    while (opcao != 5):
        for i, item in enumerate(listaOpcoes):
            print (i+1,item)
        print ()
        str_opcao = input ("Escolha uma opcao: ")
        try:
            opcao = int(str_opcao)
        except ValueError:
            print ("Erro de conversao, tente novamente com um input valido.")
            continue
        if ( opcao < 1 or opcao > 5) :
            print ("Input invalido tente novamente, escolha uma opcao de 1 a 5.")
            continue
        elif (opcao == 1):
            adicionarContato (listaNome , listaSobrenome , listaNomeCompleto , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes )
            bubbleSort()
            print ()
        elif (opcao == 2):
            excluirContato (listaNomeCompleto, listaNome , listaSobrenome , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes )
            print ()
        elif (opcao == 3): 
            editarContato (listaNomeCompleto, listaNome , listaSobrenome , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes )
            print ()
        elif (opcao == 4):
            print()
            print("Contatos:")
            print()
            mostrarContatos( listaNomeCompleto , listaTelefone , listaCelular ,  listaEmail , listaEndereco , listaDetalhes )
        elif (opcao == 5):
          print("Programa finalizado!")
