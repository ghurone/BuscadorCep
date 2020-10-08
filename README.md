# Buscar CEP

## Uma biblioteca para encontrar endereços pelo CEP

### Como instalar
---------------------------------------------------
    pip install buscarcep

### Como usar
---------------------------------------------------
    >>> from buscarcep import buscar_cep
    >>> e = buscar_cep('01001-000')
    >>> e
    Endereco(rua='Praça da Sé', bairro='Sé', cidade='São Paulo/SP', cep='01001-000')
    >>> e.all
    ('Praça da Sé', 'Sé', 'São Paulo/SP', '01001-000')
    >>> e[0]
    'Praça da Sé'
    >>> e[1]
    'Sé'
    >>> e[2]
    'São Paulo/SP'
    >>> e[3]
    '01001-000'
    >>> e.rua
    'Praça da Sé'
    >>> e.bairro
    'Sé'
    >>> e.cidade
    'São Paulo/SP'
    >>> e.cep
    '01001-000'
