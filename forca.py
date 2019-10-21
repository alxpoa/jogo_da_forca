# Jogo da Forca


# importando biblioteca random
import random

# Board (tabuleiro)
tabuleiro = ['''

>>>>>>>>>>Forca<<<<<<<<<<

 +----+
 |    |
      |
      |
      |
      |
=========''', '''

 +----+
 |    |
 O    |
      |
      |
      |
=========''', '''

 +----+
 |    |
 O    |
 |    |
      |
      |
=========''', '''

 +----+
 |    |
 O    |
/|    |
      |
      |
=========''', '''

 +----+
 |    |
 O    |
/|\   |
      |
      |
=========''', '''

 +----+
 |    |
 O    |
/|\   |
/     |
      |
=========''', '''

 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
=========''']


# Classe
class Forca:

	# Método Construtor
	def __init__(self, palavra):
		self.palavra = palavra
		self.palavras_erradas = []
		self.palavras_certas = []
		
	# Método para adivinhar a letra
	def certa(self, letra):
		if letra in self.palavra and letra not in self.palavras_certas:
			self.palavras_certas.append(letra)
		elif letra not in self.palavra and letra not in self.palavras_erradas:
			self.palavras_erradas.append(letra)
		else:
			return False
		return True
		
	# Método para verificar se o jogo terminou
	def forca_fim(self):
		return self.forca_venceu() or (len(self.palavras_erradas) == 6)
		
	# Método para verificar se o jogador venceu
	def forca_venceu(self):
		if '_' not in self.palavra_oculta():
			return True
		return False
		
	# Método para não mostrar a letra no tabuleiro
	def palavra_oculta(self):
		rtn = ''
		for letra in self.palavra:
			if letra not in self.palavras_certas:
				rtn += '_'
			else:
				rtn += letra
		return rtn
		
	# Método para checar o status do jogo e imprimir o tabuleiro na tela
	def mostra_situacao_jogo(self):
		print (tabuleiro[len(self.palavras_erradas)])
		print ('\nPalavra: ' + self.palavra_oculta())
		print ('\nLetras erradas: ',) 
		for letra in self.palavras_erradas:
			print (letra,) 
		print ()
		print ('Letras corretas: ',)
		for letra in self.palavras_certas:
			print (letra,)
		print ()

# Método para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():
        with open("palavras.txt", "rt") as f:
                banco = f.readlines()
        return banco[random.randint(0,len(banco))].strip()

# Método Main - Execução do Programa
def main():

	# Objeto
	jogo = Forca(palavra_aleatoria())

	# Enquanto o jogo não tiver terminado, mostra a situação, solicita uma letra e faz a leitura do caracter
	while not jogo.forca_fim():
		jogo.mostra_situacao_jogo()
		jogador = input('\nDigite uma letra: ')
		jogo.certa(jogador)

	# Verifica a situação do jogo
	jogo.mostra_situacao_jogo()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if jogo.forca_venceu():
		print ('\nPARABÉNS!!! VOCÊ VENCEU!!!')
	else:
		print ('\nFim de jogo! Infelizmente você perdeu!')
		print ('A palavra que você não acertou era: ' + jogo.palavra)
		
	print ('\nFoi bom jogar com você! Obrigado!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
