alunos = []

# Supomos que inicialmente o aluno nao tem disciplinas cursadas.
def inserir(cpf, nome) :
  alunos.append((cpf, nome, []))

def estaRegistrado(cpf) :
  l = [aluno for aluno in alunos if cpf in aluno]
  if len(l) > 0 :
    return l[0]
  return ()
  
  for (cpf, nome, disciplinas) in alunos :
      if cpfBuscado == cpf :
        return (cpf, nome, disciplinas) # True
  return ()    # False


def removerAlt(cpf) :
  aluno = estaRegistrado (cpf)
  if aluno != () :
    alunos.remove(aluno)
    
#(cpf, nome, disciplinas)
def cadastrarDisciplina(cpf, codigo, nomeDisciplina,semestre) :
  aluno = estaRegistrado(cpf)
  if aluno != () :
    aluno[2].append((codigo, nomeDisciplina, semestre))
    
def jaCursou(cpf, codigo) :
  resultado = False
  aluno = estaRegistrado(cpf)
  if aluno != () :
    for x in aluno[2] :
      if x[0] == codigo :
        resultado = True
  return resultado


def remover(cpf) :
  i = 0
  while i < len(alunos) :
    if alunos[i][0] == cpf :
      del alunos[i]
    i = i + 1
def opcoes():
  print("1 - Cadastrar Aluno: ")
  print("2 - Cadastrar Disciplina: ")
  print("3 - Alterar Aluno: ")
  print("4 - Alterar Disciplina: ")
  print("5 - Sair ")
  opc=int(input("Escolha sua opção: "))
  if opc == 1:
    cpf=input("Informe o CPF:")
    nome=input("Informe o nome do aluno: ")
#            codigo=input("Informe o código da disciplina: ")
    inserir(cpf,nome)
  arq1=open("ListaAlunos.txt", 'r', encoding='utf8')
  lista=arq1.readlines()
  lista.append(alunos)
  arq1.close()
  arq1=open("ListaAlunos.txt","w",encoding="utf8")
  for i in lista:
    arq1.write(str(i))
  arq1.close()


opcoes()