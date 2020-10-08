import requests
from bs4 import BeautifulSoup


class Endereco:
    def __init__(self, args = ()):
        self.rua, self.bairro, self.cidade, self.cep = args
        self.all = args
        
    def __repr__(self):
        return f"Endereco(rua='{self.rua}', bairro='{self.bairro}', cidade='{self.cidade}', cep='{self.cep}')"
    
    def __str__(self):
        return self.__repr__()
    
    def __getitem__(self, key):
        return self.all[key]
    
    
def buscar_cep(cep):
    """                         FUNÇÃO PRINCIPAL
        Insira uma string com os números do CEP, e será retornado um objeto
        Endereco, com as informações da rua, bairro, cidade e irônicamente o
        próprio CEP
    """
    if isinstance(cep, str):
        cep = cep.replace('-', '').replace(' ', '')
        if len(cep) != 8:
            raise Exception('CEP Inválido')
    else:
        raise TypeError('Digite o CEP em uma string')
        
    req = request(cep)

    if isinstance(req, requests.models.Response):
        list_values = parser(req)
        
        if list_values != 1:
            texto_clean = text_cleaner(list_values)
                
            return Endereco(tuple(texto_clean))
        else:
            raise Exception('CEP não encontrado')
    
    elif isinstance(req, int):
        raise Exception(f'Error ao checar o CEP. Status Code: {req}')


def request(cep):
    """Função que recebe um cep e faz a requisição no site dos Correios"""
    
    url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
    payload = {'relaxation': cep, 'tipoCEP': 'ALL', 'semelhante': 'N'}
    
    requisicao = requests.post(url, data=payload)
    if requisicao.status_code == 200:
        return requisicao
    else: 
        return requisicao.status_code
    
    
def parser(req):
    """Função que faz o parser do texto em html do request"""
    
    try:
        soup = BeautifulSoup(req.text, "html.parser")
        value_cells = soup.find('table', attrs={'class': 'tmptabela'})
        return list(value_cells.findAll('tr'))
    except:
        return 1

def text_cleaner(l_values):
    """Funcao que arruma o texto, deixando mais visivel"""
    
    texto_clean = [value.get_text().strip() for value in l_values[1].findAll('td')]
    texto_clean[0] = texto_clean[0][:texto_clean[0].find('-') - 1]
    return texto_clean
        
        