# Documentação do Projeto

## 🚀 Projeto de Previsão do Tempo com Python e WeatherAPI 🌦️

## Descrição

Este projeto realiza a consulta da previsão do tempo para uma cidade especificada pelo usuário, utilizando a API do [WeatherAPI](https://www.weatherapi.com/). O programa exibe as previsões de temperatura (máxima e mínima), condições do tempo, umidade, velocidade do vento, entre outros. Além disso, gera um gráfico de temperatura ao longo dos dias utilizando a biblioteca `matplotlib`.

## Funcionalidades

- **Consulta da previsão do tempo**: Obtém dados sobre temperatura máxima, mínima, sensação térmica, umidade, velocidade do vento, etc.
- **Exibição das informações no terminal**: Mostra a previsão do tempo detalhada para os dias solicitados.
- **Previsão por hora**: Exibe a previsão do tempo para cada hora do dia.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `requests`: Para fazer a requisição HTTP à API.
  - `matplotlib`: Para gerar o gráfico de temperatura.

### Instalação das dependências

Execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install requests matplotlib
```

## Como Usar

### Passo 1: Obtenha uma chave da API WeatherAPI

1. Acesse [WeatherAPI](https://www.weatherapi.com/).
2. Crie uma conta e obtenha sua chave de API.

### Passo 2: Atualize o código com sua chave da API

Substitua `"ae0eabeeed9d4ca084a190313252102"` pela sua chave da API no código:

```python
API_KEY = "sua_chave_da_api"
```

### Passo 3: Execute o código

1. **Digite o nome da cidade** para a qual você deseja consultar a previsão do tempo.
2. **Digite o número de dias** para o qual deseja consultar a previsão (1, 3, 5 ou 7 dias).

Exemplo de execução:

```bash
Digite o nome da cidade: 
rio de janeiro

Digite o número de dias para a previsão (1, 3, 5 ou 7): 
3
```

O programa exibirá a previsão do tempo para os dias selecionados e gerará um gráfico de temperaturas.

### Exemplo de Saída no Terminal:

```bash
Previsão para rio de janeiro (3 dias):

Data: 23/02/2025
Temperatura Máxima: 31.6°C
Temperatura Mínima: 23.5°C
Condição: Possibilidade de chuva irregular
Umidade: 70%
Velocidade do Vento: 18.4 km/h
Sensação Térmica: 26.8°C
Precipitação: 1.15 mm
--------------------------------------------------

Previsão por Hora para 23/02/2025:
00:00 - Temperatura: 24.5°C, Condição: Céu limpo
01:00 - Temperatura: 24.3°C, Condição: Céu limpo
02:00 - Temperatura: 24.2°C, Condição: Céu limpo
03:00 - Temperatura: 24.0°C, Condição: Céu limpo
04:00 - Temperatura: 23.8°C, Condição: Céu limpo
05:00 - Temperatura: 23.7°C, Condição: Céu limpo
06:00 - Temperatura: 25.1°C, Condição: Sol
07:00 - Temperatura: 27.1°C, Condição: Sol
08:00 - Temperatura: 29.1°C, Condição: Sol
09:00 - Temperatura: 30.4°C, Condição: Sol
10:00 - Temperatura: 30.8°C, Condição: Sol
11:00 - Temperatura: 31.4°C, Condição: Sol
12:00 - Temperatura: 31.6°C, Condição: Sol
13:00 - Temperatura: 30.1°C, Condição: Parcialmente nublado
14:00 - Temperatura: 31.2°C, Condição: Sol
15:00 - Temperatura: 30.0°C, Condição: Sol
16:00 - Temperatura: 28.7°C, Condição: Possibilidade de chuva irregular
17:00 - Temperatura: 26.7°C, Condição: Possibilidade de chuva irregular
18:00 - Temperatura: 25.1°C, Condição: Possibilidade de chuva irregular
19:00 - Temperatura: 24.3°C, Condição: Possibilidade de chuva irregular
20:00 - Temperatura: 24.1°C, Condição: Céu limpo
21:00 - Temperatura: 23.8°C, Condição: Céu limpo
22:00 - Temperatura: 23.6°C, Condição: Céu limpo
23:00 - Temperatura: 23.5°C, Condição: Céu limpo
--------------------------------------------------
Data: 24/02/2025
Temperatura Máxima: 31.6°C
Temperatura Mínima: 22.3°C
Condição: Possibilidade de chuva irregular
Umidade: 73%
Velocidade do Vento: 16.2 km/h
Sensação Térmica: 26.4°C
Precipitação: 2.36 mm
--------------------------------------------------

Previsão por Hora para 24/02/2025:
00:00 - Temperatura: 23.4°C, Condição: Céu limpo
01:00 - Temperatura: 23.2°C, Condição: Céu limpo
02:00 - Temperatura: 22.9°C, Condição: Céu limpo
03:00 - Temperatura: 22.7°C, Condição: Céu limpo
04:00 - Temperatura: 22.5°C, Condição: Céu limpo
05:00 - Temperatura: 22.3°C, Condição: Céu limpo
06:00 - Temperatura: 23.3°C, Condição: Sol
07:00 - Temperatura: 25.5°C, Condição: Sol
08:00 - Temperatura: 27.7°C, Condição: Sol
09:00 - Temperatura: 29.4°C, Condição: Sol
10:00 - Temperatura: 30.4°C, Condição: Sol
11:00 - Temperatura: 31.3°C, Condição: Sol
12:00 - Temperatura: 31.6°C, Condição: Sol
13:00 - Temperatura: 31.0°C, Condição: Possibilidade de chuva irregular
14:00 - Temperatura: 30.5°C, Condição: Possibilidade de chuva irregular
15:00 - Temperatura: 30.1°C, Condição: Possibilidade de chuva irregular
16:00 - Temperatura: 28.9°C, Condição: Sol
17:00 - Temperatura: 27.3°C, Condição: Possibilidade de chuva irregular
18:00 - Temperatura: 26.3°C, Condição: Possibilidade de chuva irregular
19:00 - Temperatura: 25.5°C, Condição: Céu limpo
20:00 - Temperatura: 24.6°C, Condição: Céu limpo
21:00 - Temperatura: 24.5°C, Condição: Céu limpo
22:00 - Temperatura: 24.5°C, Condição: Céu limpo
23:00 - Temperatura: 24.3°C, Condição: Céu limpo
--------------------------------------------------
Data: 25/02/2025
Temperatura Máxima: 31.5°C
Temperatura Mínima: 23.1°C
Condição: Possibilidade de chuva irregular
Umidade: 70%
Velocidade do Vento: 17.6 km/h
Sensação Térmica: 26.7°C
Precipitação: 0.43 mm
--------------------------------------------------

Previsão por Hora para 25/02/2025:
00:00 - Temperatura: 24.1°C, Condição: Céu limpo
01:00 - Temperatura: 23.9°C, Condição: Céu limpo
02:00 - Temperatura: 23.6°C, Condição: Céu limpo
03:00 - Temperatura: 23.4°C, Condição: Céu limpo
04:00 - Temperatura: 23.2°C, Condição: Céu limpo
05:00 - Temperatura: 23.1°C, Condição: Céu limpo
06:00 - Temperatura: 24.1°C, Condição: Sol
07:00 - Temperatura: 26.3°C, Condição: Sol
08:00 - Temperatura: 28.2°C, Condição: Sol
09:00 - Temperatura: 29.7°C, Condição: Sol
10:00 - Temperatura: 30.6°C, Condição: Sol
11:00 - Temperatura: 31.3°C, Condição: Sol
12:00 - Temperatura: 31.5°C, Condição: Sol
13:00 - Temperatura: 31.1°C, Condição: Sol
14:00 - Temperatura: 30.5°C, Condição: Sol
15:00 - Temperatura: 29.8°C, Condição: Sol
16:00 - Temperatura: 28.7°C, Condição: Possibilidade de chuva irregular
17:00 - Temperatura: 27.4°C, Condição: Possibilidade de chuva irregular
18:00 - Temperatura: 26.3°C, Condição: Possibilidade de chuva irregular
19:00 - Temperatura: 25.5°C, Condição: Possibilidade de chuva irregular
20:00 - Temperatura: 25.3°C, Condição: Céu limpo
21:00 - Temperatura: 25.0°C, Condição: Céu limpo
22:00 - Temperatura: 24.7°C, Condição: Céu limpo
23:00 - Temperatura: 24.4°C, Condição: Céu limpo
--------------------------------------------------
```

### Exemplo de Gráfico Gerado:

- Um gráfico de linha será exibido, mostrando as temperaturas máxima e mínima ao longo dos dias solicitados, com a área entre as linhas preenchida de azul claro.

---

## Estrutura do Código

### 1. **Função `obter_previsao_tempo(cidade, dias)`**:
   - Faz a requisição à API WeatherAPI.
   - Processa a resposta JSON, extrai as informações de previsão diária (temperatura, condição, umidade, etc.).
   - Exibe os dados no terminal e chama a função para gerar o gráfico.

### 2. **Função `plotar_grafico(datas, temp_max, temp_min)`**:
   - Usa a biblioteca `matplotlib` para gerar um gráfico de temperatura com as temperaturas máximas e mínimas ao longo dos dias.
   - O gráfico é exibido em uma nova janela.

### 3. **Função `principal()`**:
   - Função principal que interage com o usuário, solicita a cidade e o número de dias para a previsão, e chama as funções de previsão e gráfico.

---

## Licença

Este projeto é de código aberto e pode ser utilizado e modificado conforme necessário, desde que a chave da API seja gerada pelo usuário e o uso seja compatível com os termos da API da WeatherAPI.

---

Essa documentação cobre os aspectos principais do seu código e como utilizá-lo. Se você precisar adicionar mais informações ou tiver algum outro requisito, me avise!
