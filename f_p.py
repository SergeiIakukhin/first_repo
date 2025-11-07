"Module do something"

user = 'Sergei Iakukhin'

def say_hello(name:str = 'Anton Pupkin') -> None:
    "Function do hello"
    return f'Привет, {name}!'

# print(say_hello(user))

if __name__ == '__main__':
    assert say_hello(user) == 'Привет, Sergei Iakukhin!'
    assert say_hello() == 'Привет, Anton Pupkin!'
    assert say_hello('Konstantin Iakukhin') == 'Привет, Konstantin Iakukhin!'
    print('Test passed')
