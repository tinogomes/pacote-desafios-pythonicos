"""
Caixa Eletrônico

Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:

    Entregar o menor número de notas;
    É possível sacar o valor solicitado com as notas disponíveis;
    Saldo do cliente infinito;
    Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
    Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

Exemplos:

    Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
    Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
"""

NOTAS = (100, 50, 20, 10)

def caixa_eletronico(count):
    resultado = {}
    resto = 0

    for divisor in NOTAS:
        notas = (count - resto)
        if not notas: break

        notas //= divisor

        if notas: resultado[divisor] = notas
        resto += notas * divisor

    return resultado


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
    test(caixa_eletronico, 40, { 20: 2 })
    test(caixa_eletronico, 90, { 50: 1, 20: 2 })
    test(caixa_eletronico, 100, { 100: 1 })
    test(caixa_eletronico, 180, { 100: 1, 50: 1, 20: 1, 10: 1 })
    test(caixa_eletronico, 10, {10: 1})
    test(caixa_eletronico, 20, {20: 1})
    test(caixa_eletronico, 50, {50: 1})
