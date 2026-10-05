# Aula 11

# Variáveis de Ambiente

"""
    Variáveis de ambiente ficam no escopo do sistema operacional
"""

# variável comum em código

nome = 'João'
print(nome)

# variável de ambiente

import os
nome = os.environ.get('nome')
print(nome)


