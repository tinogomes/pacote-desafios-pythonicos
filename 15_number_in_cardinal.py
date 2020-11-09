"""
15. number in cardinal

Dada um número, transcreva seu valor por extenso em reais, por exemplo:

1.34 # => um real, trinta e quatro centavos
5.0 # => cinco reais
100.45 # => cem reais, quarenta e cinco centavos

"""


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

THOUSAND = 1000
NO_SUFFIX = (None,)

DIVISORS = (
    (THOUSAND**4, ("trilhão", "trilhões")),
    (THOUSAND**3, ("bilhão", "bilhões")),
    (THOUSAND**2, ("milhão", "milhões")),
    (THOUSAND, ("mil",)),
    (100, NO_SUFFIX),
    (10, NO_SUFFIX),
    (1, NO_SUFFIX),
)

def number_in_cardinal(number, nindex=0):
    try: return NUMBERS[number][nindex]
    except KeyError: pass

    result = []

    calculated = 0
    for divisor, suffix in DIVISORS:
        value = value_base = number - calculated
        if not value: break

        try: 
            result.append(NUMBERS[value_base][nindex])
            break
        except KeyError:
            value //= divisor
            if value_base < THOUSAND: value *= divisor
            if not value: continue

        _suffix = suffix[0] if value == 1 else suffix[-1]

        result.append(' '.join([__suffix for __suffix in [number_in_cardinal(value, -1), _suffix] if __suffix]))
        if value_base >= THOUSAND: value *= divisor
        calculated += value

    return ' e '.join(result)


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

    message = f'{f.__name__}({in_!r}) retornou {out!r} {info}'
    print(f'{sign} {message}')

if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(number_in_cardinal, 0, "zero")
    test(number_in_cardinal, 1, "um")
    test(number_in_cardinal, 10, "dez")
    test(number_in_cardinal, 11, "onze")
    test(number_in_cardinal, 100, "cem")
    test(number_in_cardinal, 101, "cento e um")
    test(number_in_cardinal, 110, "cento e dez")
    test(number_in_cardinal, 112, "cento e doze")
    test(number_in_cardinal, 123, "cento e vinte e três")
    test(number_in_cardinal, 1000, "um mil")
    test(number_in_cardinal, 1001, "um mil e um")
    test(number_in_cardinal, 1010, "um mil e dez")
    test(number_in_cardinal, 1011, "um mil e onze")
    test(number_in_cardinal, 1234, "um mil e duzentos e trinta e quatro")
    test(number_in_cardinal, 12345, "doze mil e trezentos e quarenta e cinco")
    test(number_in_cardinal, 123456, "cento e vinte e três mil e quatrocentos e cinquenta e seis")
    test(number_in_cardinal, 1234567, "um milhão e duzentos e trinta e quatro mil e quinhentos e sessenta e sete")
    test(number_in_cardinal, 12345678, "doze milhões e trezentos e quarenta e cinco mil e seiscentos e setenta e oito")
    test(number_in_cardinal, 123456789, "cento e vinte e três milhões e quatrocentos e cinquenta e seis mil e setecentos e oitenta e nove")
    test(number_in_cardinal, 1234567890, "um bilhão e duzentos e trinta e quatro milhões e quinhentos e sessenta e sete mil e oitocentos e noventa")
    test(number_in_cardinal, 21345678901, "vinte e um bilhões e trezentos e quarenta e cinco milhões e seiscentos e setenta e oito mil e novecentos e um")
    test(number_in_cardinal, 1000000000000, "um trilhão")
    test(number_in_cardinal, 2000000000000, "dois trilhões")

