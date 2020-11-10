def separador(funcao):
    def wrapper(*args, **kwargs):
        print('-' * 80)
        funcao(*args, **kwargs)
    
    return wrapper

def log(prefix='app'):
    def _log(funcao):
        def wrapper(*args, **kwargs):
            print(f'[{prefix}]: Executando função')
            try:
                result = funcao(*args, **kwargs)
                print(f'[{prefix}]: Sucesso na execução da função')
                return result
            except BaseException as e:
                print(f'[{prefix}]: ERRO na execução da função')
                raise e
        return wrapper
    return _log

@separador
@log(prefix='soma')
def soma_numeros(*args):
    return sum(args)

print('Resultado da função é:', soma_numeros(1, 2))
print('Resultado da função é:', soma_numeros(1,2,3))
print('Resultado da função é:', soma_numeros(1,2,3))
print('Resultado da função é:', soma_numeros(1,2,3))
print('Resultado da função é:', soma_numeros(1,2,3))
print('Resultado da função é:', soma_numeros(1,2,3))
print('Resultado da função é:', soma_numeros(1,2,3))
