"""
15. number in cardinal

Dada um número, transcreva seu valor por extenso em reais, por exemplo:

1.34 # => um real, trinta e quatro centavos
5.0 # => cinco reais
100.45 # => cem reais, quarenta e cinco centavos

"""

PLACE_VALUES = (1, 10, 100)

NUMBERS = {
    0: ("zero",), 1: ("um",), 2: ("dois",), 3: ("três",), 4: ("quatro",), 5: ("cinco",),
    6: ("seis",), 7: ("sete",), 8: ("oito",), 9: ("nove",), 10: ("dez",),
    11: ("onze",), 12: ("doze",), 13: ("treze",), 14: ("quatorze",), 15: ("quinze",),
    16: ("dezesseis",), 17: ("dezessete",), 18: ("dezoito",), 19: ("dezenove",),
    20: ("vinte",), 30: ("trinta",), 40: ("quarenta",), 50: ("cinquenta",),
    60: ("sessenta",), 70: ("setenta",), 80: ("oitenta",), 90: ("noventa",),
    100: ("cem","cento",), 200: ("duzentos",), 300: ("trezentos",), 
    400: ("quatrocentos",), 500: ("quinhentos",), 600: ("seiscentos",), 
    700: ("setecentos",), 800: ("oitocentos",), 900: ("novecentos",),
}

OVER_THOUSANDS = {
    10**3: ("mil",),
    10**6: ("milhão", "milhões"),
    10**9: ("bilhão", "bilhões"),
    10**12: ("trilhão", "trilhões"),
}

def number_in_cardinal(number):
    try:
        return NUMBERS[number][0]
    except: pass

    over_values = []
    over_strings = []

    for ot in reversed(OVER_THOUSANDS):
        value = (number - sum(over_values)) // ot * ot

        if value > 0:
            over_values.append(value)
            simple_value = value // ot
            ots = OVER_THOUSANDS[ot]
            over_string = ots[0] if simple_value == 1 else ots[-1]
            over_strings.append(f'{number_in_cardinal(simple_value)} {over_string}')

    placed_values = []
    for pv in reversed(PLACE_VALUES):
        value = (number - sum(over_values) - sum(placed_values)) // pv * pv
        if value > 0:
            placed_values.append(value)
    
    if len(placed_values) == 0 and len(over_strings) > 0:
        return ', '.join(over_strings)

    # eleven until nineteen
    if len(placed_values) > 1 and placed_values[-2] == 10:
        placed_values[-1] += placed_values[-2]
        del placed_values[-2]

    number_as_string = ' e '.join([NUMBERS[n][-1] for n in placed_values])

    return ', '.join(over_strings + [number_as_string])


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    try:
        assert out == expected
        sign = '✅'
        info = ''
    except AssertionError:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')

if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(number_in_cardinal, 0, "zero")
    test(number_in_cardinal, 1, "um")
    test(number_in_cardinal, 10, "dez")
    test(number_in_cardinal, 11, "onze")
    test(number_in_cardinal, 100, "cem")
    test(number_in_cardinal, 123, "cento e vinte e três")
    test(number_in_cardinal, 1234, "um mil, duzentos e trinta e quatro")
    test(number_in_cardinal, 12345, "doze mil, trezentos e quarenta e cinco")
    test(number_in_cardinal, 123456, "cento e vinte e três mil, quatrocentos e cinquenta e seis")
    test(number_in_cardinal, 1234567, "um milhão, duzentos e trinta e quatro mil, quinhentos e sessenta e sete")
    test(number_in_cardinal, 12345678, "doze milhões, trezentos e quarenta e cinco mil, seiscentos e setenta e oito")
    test(number_in_cardinal, 123456789, "cento e vinte e três milhões, quatrocentos e cinquenta e seis mil, setecentos e oitenta e nove")
    test(number_in_cardinal, 1234567890, "um bilhão, duzentos e trinta e quatro milhões, quinhentos e sessenta e sete mil, oitocentos e noventa")
    test(number_in_cardinal, 21345678901, "vinte e um bilhões, trezentos e quarenta e cinco milhões, seiscentos e setenta e oito mil, novecentos e um")
    test(number_in_cardinal, 1000000000000, "um trilhão")
    test(number_in_cardinal, 10000000000000, "dez trilhões")

