#Cadastro de Alunos: O programa deve permitir ao usuário cadastrar alunos. Cada aluno terá as seguintes informações: nome, idade e notas em três disciplinas: Matemática, Ciências e História. Os dados de cada aluno devem ser armazenados em um dicionário com as seguintes chaves: ' nome', 'idade', 'notas'. As notas devem ser armazenadas em uma tupla.

#Visualização de Alunos: O programa deve permitir ao usuário visualizar todos os alunos cadastrados, exibindo suas informações de forma organizada. 
#Média de Notas: O programa deve calcular a média das notas de cada aluno e exibi-la. 
#Aluno com Melhor Média: O programa deve identificar e exibir o aluno com a melhor média de notas.

dados = {
  'nome' : None,
  'idade' : None,
  'notas' : (None)
}

lista_dados = []
media_notas = []

while True:
  cadastrar = str(input('Deseja cadastrar algum aluno? (Sim/Nao) ')).lower()
  if cadastrar == 'Nao'.lower():
    break

  elif cadastrar == 'Sim'.lower():
    nome = str(input('Qual o nome do aluno? ')).capitalize()
    idade = int(input('Qual a idade do aluno? '))
    nota_mat = float(input('Qual a nota de matemática do aluno? '))
    nota_cie = float(input('Qual a nota de ciências do aluno? '))
    nota_his = float(input('Qual a nota de história do aluno? '))

    dados['nome'] = nome
    dados['idade'] = idade
    dados['notas'] = nota_mat, nota_cie, nota_his

    lista_dados.append(dados.copy())
    media_notas.append((nota_mat + nota_cie + nota_his) / 3)

  else:
    print('Resposta inválida. Tente novamente.')

print('\nInformações dos alunos cadastrados:\n')

for i, m in zip(lista_dados, media_notas):
  print(f'Nome do aluno: {i['nome']}\nIdade: {i['idade']}\nNota de matemática: {i['notas'][0]}\nNota de ciências {i['notas'][1]}\nNota de história: {i['notas'][2]}')

  print(f'A média de {i['nome']} é: {m:.2f}\n')

indice = media_notas.index(max(media_notas))
print(f'O aluno com maior média é {lista_dados[indice]['nome']} com {media_notas[indice]:.2f} ')