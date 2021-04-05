# Crawler do Zé
É um script que crawleia os anuncios de diferentes marcas de cerveja do Zé delivery e retorna para o usuário qual é o produto mais custo beneficio de acordo com o preço do litro da embalagem. O crawler é configurado para crawlear os anuncios de acordo com o endereço passado pelo usuário na execução do script.


## Tecnologia utilizada
A aplicação foi construída usando python 3 e a biblioteca Selenium.


## Iniciar aplicação 
### Instalar as pendencias

pip install -r requirements.txt 

### Para iniciar o script é necessário rodar o seguinte comando no terminal:

DEBUG=false BRAND=Marca_cerveja STREET=Nome_Rua NUMBER=Numero_endereco NEIGHBORHOOD=Bairro  python app.py


### Os parametros da execução são:

| Nome | Descrição |
| --- | --- |
| BRAND |  Marca da cerveja |
| STREET | Nome da rua |
| NUMBER |  Número do endereco |
| NEIGHBORHOOD | Bairro do endereco |
| DEBUG | Ligar logs ou não |

<br>

## Parametro BRAND : 
<br>

### Passando uma marca valida:
Caso o usuário queira ver qual a melhor escolha e a melhor ordem de embalagem de uma marca específica, ele pode passar BRAND com os seguintes valores:

| BRAND |
| --- | 
| BRAHMA | 
| BUDWEISER |
| ANTARTICA |
| ORIGINAL | 
| STELLA |
| BECKS |
| CORONA | 
| BOHEMIA |
| COLORADO |
| ALL |

<br>

### Exemplo de um retorno de anuncio:
[{
'brand': 'BRAHMA', 
'product_name': 'Brahma Chopp 269ml', 
'price': 1.87, 
'price_per_liter': 6.95
}]

| Nome | Descrição |
| --- | --- |
| brand |  Marca da cerveja |
| product_name | Nome do produto |
| price |  Preço do produto |
| price_per_liter | Preço do litro do produto |

<br>



### Exemplo da reposta da marca BRAHMA:

{"logger":"root","timestamp": "2021-04-05T18:04:08Z" , "level": "INFO", "message": "The best choice(s) is/are:"}

[{'brand': 'BRAHMA', 'product_name': 'Brahma Chopp 269ml', 'price': 1.87, 'price_per_liter': 6.95}]


{"logger":"root","timestamp": "2021-04-05T18:04:08Z" , "level": "INFO", "message": "The complete list of prices in order of BRAHMA is:"}

1ª {'brand': 'BRAHMA', 'product_name': 'Brahma Chopp 269ml', 'price': 1.87, 'volume': 269, 'price_per_liter': 6.95}\
2ª {'brand': 'BRAHMA', 'product_name': 'Brahma Chopp 1L | Apenas o Líquido - Unidade', 'price': 7.09, 'volume': 1, 'price_per_liter': 7.09}\
3ª {'brand': 'BRAHMA', 'product_name': 'Brahma Chopp 350ml', 'price': 2.69, 'volume': 350, 'price_per_liter': 7.69}\
4ª {'brand': 'BRAHMA', 'product_name': 'Brahma Malzbier 350ml', 'price': 2.69, 'volume': 350, 'price_per_liter': 7.69}\
5ª {'brand': 'BRAHMA', 'product_name': 'Brahma Chopp 473ml', 'price': 3.69, 'volume': 473, 'price_per_liter': 7.8}

<br>

### Não passar BRAND ou passar BRAND=ALL
O usuário pode escolher ou não passar uma marca de cerveja, caso não passe, o crawler irá definir BRAND=ALL e irá crawlear todas as marcas e listar ordenando do litro mais barato para o mais caro dentre todas as marcas.

<br>

### Exemplo da resposta ao passar BRAND=ALL:
1ª {'brand': 'ANTARTICA', 'product_name': 'Antarctica Subzero 473ml', 'price': 2.69, 'price_per_liter': 5.69}\
2ª {'brand': 'SKOL', 'product_name': 'Skol 473ml', 'price': 2.99, 'price_per_liter': 6.32}\
3ª {'brand': 'SKOL', 'product_name': 'Skol Puro Malte 473ml', 'price': 2.99, 'price_per_liter': 6.32}\
4ª {'brand': 'BRAHMA', 'product_name': 'Brahma Chopp 269ml', 'price': 1.87, 'price_per_liter': 6.95}\
5ª {'brand': 'BOHEMIA', 'product_name': 'Bohemia 990ml | Apenas o Líquido', 'price': 7.39, 'price_per_liter': 7.46}\
6ª {'brand': 'BUDWEISER', 'product_name': 'Budweiser 473ml', 'price': 4.29, 'price_per_liter': 9.07}\
7ª {'brand': 'ORIGINAL', 'product_name': 'Original 350ml', 'price': 3.19, 'price_per_liter': 9.11}\
8ª {'brand': 'STELLA', 'product_name': 'Stella Artois 350ml', 'price': 3.79, 'price_per_liter': 10.83}\
9ª {'brand': 'BECKS', 'product_name': 'Becks 350ml', 'price': 4.49, 'price_per_liter': 12.83}\
10ª {'brand': 'COLORADO', 'product_name': 'Colorado Ribeirão Lager 350ml', 'price': 4.99, 'price_per_liter': 14.26}\
11ª {'brand': 'CORONA', 'product_name': 'Corona Extra 330ml', 'price': 5.49, 'price_per_liter': 16.64}\


