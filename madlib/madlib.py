'''
Gerador de Histórias Desorganizadas

'''
# cabeçalho
print('-' * 50)
print('Gerador de Bibliotecas Desorganizadas (MAD LIB)')
print('-' * 50)
print('Informe seis palavras abaixo:\n')


# estrutura de dados lista
palavras = []


count = 1


# laço while com contador count para seu controle
while count < 7:
        # upper para que toda palavra digitada fique com todas as letras maiúsculas
	palavra = input(f'Palavra{count}: ').upper()
	# adiciona cada palavra digitada à lista palavras
	palavras.append(palavra)
	count += 1


# linha divisória
print('-' * 50)


# texto separado por frases adicionando as palavras em seus respectivos lugares
frase1 = f'\nSeja gentil ao viajar de ônibus movido a {palavras[0]}'
frase2 = f'Pois um pato pode ser a {palavras[1]} de alguém'
frase3 = f'Seja gentil sempre ao {palavras[2]} em {palavras[3]}'
frase4 = f'Onde o tempo está sempre {palavras[4]}.'
frase5 = f'Você pode pensar que isto é uma {palavras[5]},\nPois é.'


# uma lista para incluir todas as frases
texto = [
    frase1,
    frase2,
    frase3,
    frase4,
    frase5
    ]


# usando a estrutura de repetição for para imprimir o texto em tela
for frase in texto:
    print(frase)
