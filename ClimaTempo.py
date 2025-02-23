import requests
from datetime import datetime

# Substitua pela sua chave da API
API_KEY = "ae0eabeeed9d4ca084a190313252102"
BASE_URL = "http://api.weatherapi.com/v1/forecast.json?"

# Função para obter a previsão do tempo
def obter_previsao_tempo(cidade, dias):
    url = f"{BASE_URL}key={API_KEY}&q={cidade}&days={dias}&lang=pt"
    resposta = requests.get(url)
    dados = resposta.json()

    if "error" in dados:
        print(f"Erro: {dados['error']['message']}")
        return

    print(f"\nPrevisão para {cidade} ({dias} dias):\n")
    
    # Obtendo a data de cada previsão e as informações
    for i in range(dias):
        dados_dia = dados['forecast']['forecastday'][i]
        
        # Ajusta a data para o formato brasileiro
        data = datetime.strptime(dados_dia['date'], "%Y-%m-%d").strftime("%d/%m/%Y")
        
        temp_max = dados_dia['day']['maxtemp_c']  # Temperatura máxima
        temp_min = dados_dia['day']['mintemp_c']  # Temperatura mínima
        condicao = dados_dia['day']['condition']['text']  # Condições do tempo
        umidade = dados_dia['day']['avghumidity']  # Umidade média
        velocidade_vento = dados_dia['day']['maxwind_kph']  # Velocidade do vento em km/h
        sensacao_termica = dados_dia['day']['avgtemp_c']  # Sensação térmica média
        precipitacao = dados_dia['day']['totalprecip_mm']  # Precipitação (em mm)
        
        print(f"Data: {data}")
        print(f"Temperatura Máxima: {temp_max}°C")
        print(f"Temperatura Mínima: {temp_min}°C")
        print(f"Condição: {condicao}")
        print(f"Umidade: {umidade}%")
        print(f"Velocidade do Vento: {velocidade_vento} km/h")
        print(f"Sensação Térmica: {sensacao_termica}°C")
        print(f"Precipitação: {precipitacao} mm")
        print("-" * 50)

# Função principal para interagir com o usuário
def principal():
    cidade = input("Digite o nome da cidade: \n")
    try:
        dias = int(input("\nDigite o número de dias para a previsão (1, 3, 5 ou 7): \n"))
        if dias not in [1, 3, 5, 7]:
            print("Por favor, insira 1, 3, 5 ou 7 dias.")
        else:
            obter_previsao_tempo(cidade, dias)
    except ValueError:
        print("Por favor, insira um número válido de dias.")

# Executa a função principal
if __name__ == "__main__":
    principal()
