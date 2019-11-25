alunos = {}

def inserir(cpf, nome) :
  alunos[cpf] = (nome, {})

def estaRegistrado(cpf) :
  if cpf in alunos :
    return alunos[cpf]
  return ()

def remover(cpf) :
  if cpf in alunos :
    del alunos[cpf]

def cadastrarDisciplina(cpf, codigo, nomeDisciplina,semestre) :
  aluno = estaRegistrado(cpf)
  if aluno != () :
    disciplinasCursadas = aluno[1]
    disciplinasCursadas[codigo] = (nomeDisciplina, semestre)
    
def jaCursou(cpf, codigo) :
  cursou = False
  aluno = estaRegistrado(cpf)
  if aluno != () and codigo in aluno[1] : 
    cursou = True
  return cursou

def removeUltimo(str) :
  if len(str) > 0 and str[len(str) - 1] == '\n':
    return str[0:len(str)-1]
  else :
    return str

def lerBD(arquivo):
  f = open(arquivo, 'r')
  conteudo = f.readlines()
  bdAlunos = {}
  temp = []
  for x in conteudo :
    temp.append(removeUltimo(x))

  conteudo = temp
    
  i = 0
  while i < len(conteudo) :
    if (i + 2  < len(conteudo)) :
      cpf = conteudo[i]
      nome = conteudo[i+1]
      bdAlunos[cpf] = (nome, {})
      qtdDisciplinas = int(conteudo[i+2])
      i = i + 3
      ultimaPosicao = (i + (qtdDisciplinas * 3)) - 1
      while i <= ultimaPosicao:
        codigoDisciplina = conteudo[i]
        nomeDisciplina = conteudo[i+1]
        semestreDisciplina = conteudo[i+2]
        bdAlunos[cpf][1][codigoDisciplina] = (nomeDisciplina, semestreDisciplina)
        i = i + 3

  f.close()     
  return bdAlunos
def opcoes(opc):
    if opc == 1:
        cpf=input("Informe o CPF:")
        nome=input("Informe o nome do aluno: ")
#            codigo=input("Informe o código da disciplina: ")
        inserir(cpf,nome)
    print(alunos)

print("1 - Cadastrar Aluno: ")
print("2 - Cadastrar Disciplina: ")
print("3 - Alterar Aluno: ")
print("4 - Alterar Disciplina: ")
print("5 - Sair ")
opc=int(input("Escolha sua opção: "))
opcoes(opc)