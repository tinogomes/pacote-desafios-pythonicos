number_in_cardinal = __import__('15_number_in_cardinal').number_in_cardinal

"""
16. number in currency

Dada um número, transcreva seu valor por extenso em reais e por exemplo:

1.34 # => um real, trinta e quatro centavos
5.0 # => cinco reais
100.45 # => cem reais e quarenta e cinco centavos
"""
def number_in_currency(number, currency=("real", "reais"), cent=("centavo", "centavos"), cents_sep=",", thousands_sep="."):
    if isinstance(number, float) or isinstance(number, int):
        number = f'{number:.02f}'
    # elif isinstance(number, str):
    #     for old, new in ((thousands_sep, ''), (cents_sep, '.')):
    #         number = number.replace(old, new)
    else:
        raise AssertionError()

    integer, cents = [int(s) for s in number.split(".")]
    integer_string = number_in_cardinal(integer)

    currency = currency[0] if integer == 1 else currency[1]
    joiner = None
    if integer_string[-3:] in ("hão", "ões"):
        joiner = "de"
    integer_currency = ' '.join([s for s in [integer_string, joiner, currency] if s])

    if cents == 0:
        return integer_currency

    if integer == 0:
        integer_currency = None

    decimal_string = number_in_cardinal(cents)
    currency_cents = cent[1] if cents > 1 else cent[0]

    decimal_currency = f'{decimal_string} {currency_cents}'
    
    return ' e '.join([s for s in (integer_currency, decimal_currency) if s])

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
    test(number_in_currency, 0.0, "zero reais")
    test(number_in_currency, 1.0, "um real")
    test(number_in_currency, 5.0, "cinco reais")
    test(number_in_currency, 34.0, "trinta e quatro reais")
    test(number_in_currency, 100.0, "cem reais")
    test(number_in_currency, 105.0, "cento e cinco reais")
    test(number_in_currency, 134.0, "cento e trinta e quatro reais")
    test(number_in_currency, 252.0, "duzentos e cinquenta e dois reais")
    test(number_in_currency, 513.0, "quinhentos e treze reais")
    test(number_in_currency, 1.34, "um real e trinta e quatro centavos")
    test(number_in_currency, 100.45, "cem reais e quarenta e cinco centavos")
    test(number_in_currency, 0.89, "oitenta e nove centavos")
    test(number_in_currency, 0.01, "um centavo")
    test(number_in_currency, 999.99, "novecentos e noventa e nove reais e noventa e nove centavos")
    test(number_in_currency, 1000.0, "um mil reais")
    test(number_in_currency, 1000.01, "um mil reais e um centavo")
    test(number_in_currency, 1000.11, "um mil reais e onze centavos")
    test(number_in_currency, 1234.56, "um mil e duzentos e trinta e quatro reais e cinquenta e seis centavos")
    test(number_in_currency, 12345.67, "doze mil e trezentos e quarenta e cinco reais e sessenta e sete centavos")
    test(number_in_currency, 123456.78, "cento e vinte e três mil e quatrocentos e cinquenta e seis reais e setenta e oito centavos")
    test(number_in_currency, 1000000.0, "um milhão de reais")
    test(number_in_currency, 1234567.89, "um milhão e duzentos e trinta e quatro mil e quinhentos e sessenta e sete reais e oitenta e nove centavos")
    test(number_in_currency, 12345678.9, "doze milhões e trezentos e quarenta e cinco mil e seiscentos e setenta e oito reais e noventa centavos")
    test(number_in_currency, 12000000.01, "doze milhões de reais e um centavo")
    test(number_in_currency, 21000000.0, "vinte e um milhões de reais")
    test(number_in_currency, 123456789.01, "cento e vinte e três milhões e quatrocentos e cinquenta e seis mil e setecentos e oitenta e nove reais e um centavo")
    test(number_in_currency, 1000000000.0, "um bilhão de reais")
    test(number_in_currency, 4000000000.0, "quatro bilhões de reais")
    test(number_in_currency, 9999000000.0, "nove bilhões e novecentos e noventa e nove milhões de reais")
    test(number_in_currency, 1000000000000.0, "um trilhão de reais")
    test(number_in_currency, 5000000000000.0, "cinco trilhões de reais")
    test(number_in_currency, 93, "noventa e três reais")
