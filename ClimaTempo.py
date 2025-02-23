import requests
from datetime import datetime
import matplotlib.pyplot as plt

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
    
    # Preparando os dados para o gráfico
    datas = []
    temp_max = []
    temp_min = []
    
    # Obtendo a data de cada previsão e as informações
    for i in range(dias):
        dados_dia = dados['forecast']['forecastday'][i]
        
        # Ajusta a data para o formato brasileiro
        data = datetime.strptime(dados_dia['date'], "%Y-%m-%d").strftime("%d/%m/%Y")
        
        temp_max.append(dados_dia['day']['maxtemp_c'])  # Temperatura máxima
        temp_min.append(dados_dia['day']['mintemp_c'])  # Temperatura mínima
        datas.append(data)
        
        # Exibe os dados diários
        print(f"Data: {data}")
        print(f"Temperatura Máxima: {dados_dia['day']['maxtemp_c']}°C")
        print(f"Temperatura Mínima: {dados_dia['day']['mintemp_c']}°C")
        print(f"Condição: {dados_dia['day']['condition']['text']}")
        print(f"Umidade: {dados_dia['day']['avghumidity']}%")
        print(f"Velocidade do Vento: {dados_dia['day']['maxwind_kph']} km/h")
        print(f"Sensação Térmica: {dados_dia['day']['avgtemp_c']}°C")
        print(f"Precipitação: {dados_dia['day']['totalprecip_mm']} mm")
        print("-" * 50)
        
        # Previsão por hora
        print(f"\nPrevisão por Hora para {data}:")
        for hora in dados_dia['hour']:
            hora_formatada = datetime.strptime(hora['time'], "%Y-%m-%d %H:%M").strftime("%H:%M")
            temp = hora['temp_c']
            condicao = hora['condition']['text']
            print(f"{hora_formatada} - Temperatura: {temp}°C, Condição: {condicao}")
        
        print("-" * 50)
    
    # Criando o gráfico de temperatura
    plotar_grafico(datas, temp_max, temp_min)

# Função para plotar o gráfico de temperaturas
def plotar_grafico(datas, temp_max, temp_min):
    plt.figure(figsize=(10, 5))
    plt.plot(datas, temp_max, label="Temperatura Máxima (°C)", color="red", marker="o")
    plt.plot(datas, temp_min, label="Temperatura Mínima (°C)", color="blue", marker="o")
    plt.fill_between(datas, temp_max, temp_min, color='lightblue', alpha=0.3)
    
    plt.title("Previsão de Temperatura ao Longo dos Dias", fontsize=14)
    plt.xlabel("Datas", fontsize=12)
    plt.ylabel("Temperatura (°C)", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

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

