nome = 'Renato'
cores = {'limpa':'\033[m',
         'azul': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;40m'}
print('Olá! Muiuto prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))