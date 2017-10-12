print('1')


def a_wrapper(funct):
    def inner_funct():
        print('pre')
        funct()
        print('post')

    print('test')
    return inner_funct


print('2')


@a_wrapper
def hello_world():
    print('hello')


print('3')


def hello_world_b(funct, name):
    print(f'hello name {name}')
    funct()


hello_world_b(hello_world, 'Justin')
hello_world_b(hello_world, 'Justin')
hello_world_b(lambda: 'here', 'Justin')
