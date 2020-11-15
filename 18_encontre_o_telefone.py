"""
18. Encontre o telefone


Em alguns lugares é comum lembrar um número do telefone associando seus dígitos a letras. Dessa maneira a expressão MY LOVE significa 69 5683. Claro que existem alguns problemas, uma vez que alguns números de telefone não formam uma palavra ou uma frase e os dígitos 1 e 0 não estão associados a nenhuma letra.

Sua tarefa é ler uma expressão e encontrar o número de telefone correspondente baseado na tabela abaixo. Uma expressão é composta por letras maiúsculas (A-Z), hifens (-) e os números 1 e 0.

Letras  ->  Número
ABC    ->  2
DEF    ->  3
GHI    ->  4
JKL    ->  5
MNO    ->  6
PQRS    ->  7
TUV    ->  8
WXYZ   ->  9

Entrada

A entrada consiste de um conjunto de expressões. Cada expressão está sozinha em uma linha e possui C caracteres, onde 1 ≤ C ≤ 30. A entrada é terminada por fim de arquivo (EOF).

Saída

Para cada expressão você deve imprimir o número de telefone correspondente.

Exemplo de entrada:

1-HOME-SWEET-HOME
MY-MISERABLE-JOB

Saída correspondente:

1-4663-79338-4663
69-647372253-562

Curiosidades

A frase "The quick brown fox jumps over the lazy dog" é um pangrama (frase com sentido em que são usadas todas as letras do alfabeto de determinada língua) da língua inglesa.

Fonte: http://br.spoj.pl/problems/ENCOTEL/
"""
MAP = {
    "ABC": 2,
    "DEF": 3,
    "GHI": 4,
    "JKL": 5,
    "MNO": 6,
    "PQRS": 7,
    "TUV": 8,
    "WXYZ": 9,
}

def encontre_o_telefone(text):
    retorno = ''

    for c in text:
        mapeou = False

        for letras, numero in MAP.items():
            if c in letras:
                mapeou = True
                retorno += str(numero)
                break

        if not mapeou: retorno += c

    return retorno

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(encontre_o_telefone, '1-HOME-SWEET-HOME', '1-4663-79338-4663')
    test(encontre_o_telefone, 'MY-MISERABLE-JOB', '69-647372253-562')
    test(encontre_o_telefone, 'MY LOVE', '69 5683')
    test(encontre_o_telefone, 'CELESTINO', '235378466')
