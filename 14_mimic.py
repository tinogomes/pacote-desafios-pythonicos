"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys
from collections import defaultdict

def extrair_palavras(filename):
    with open(filename) as arquivo:
        return arquivo.read().split()

def mimic_dict(filename):
    """
    Retorna o dicionario imitador mapeando cada palavra para a lista de palavras subsequentes.
    """

    dicionario = defaultdict(lambda : [])

    ultima_palavra = ''

    for palavra in extrair_palavras(filename):
        dicionario[ultima_palavra].append(palavra)
        ultima_palavra = palavra

    dicionario[ultima_palavra] = ['']

    return dicionario


def print_mimic(mimic_dict, word):
    """
    Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras.
    """

    sentence = []
    last_word = word

    while len(sentence) < 200:
        last_word = random.choice(mimic_dict[last_word])

        sentence.append(last_word)

        if last_word.endswith('.'): break

    print(' '.join(sentence))


# Chama mimic_dict() e print_mimic()
def main():
    if not 1 < len(sys.argv) < 4:
        print('Utilização: ./14_mimic.py file-to-read [start_word]')
        sys.exit(1)

    start_word = ''
    if len(sys.argv) == 3:
        start_word = sys.argv[2]

    print_mimic(mimic_dict(sys.argv[1]), start_word)


if __name__ == '__main__':
    main()
