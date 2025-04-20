from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import matplotlib.pyplot as plt
import io
import base64
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv() 
# Configuração da API
API_KEY = "ae0eabeeed9d4ca084a190313252102"
BASE_URL = "http://api.weatherapi.com/v1/forecast.json?"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cidade = request.form.get('cidade')
        dias = request.form.get('dias', '1')
        
        if not cidade:
            return render_template('error.html', message="Por favor, digite o nome de uma cidade.")
        
        try:
            dias = int(dias)
            if dias not in [1, 3, 5, 7]:
                return render_template('error.html', message="Por favor, selecione 1, 3, 5 ou 7 dias.")
        except ValueError:
            return render_template('error.html', message="Número de dias inválido.")
        
        try:
            url = f"{BASE_URL}key={API_KEY}&q={cidade}&days={dias}&lang=pt"
            resposta = requests.get(url)
            dados = resposta.json()
            
            if "error" in dados:
                return render_template('error.html', message=dados['error']['message'])
            
            # Processar dados para o template
            processed_data = process_weather_data(dados, cidade, dias)
            return render_template('results.html', **processed_data)
            
        except Exception as e:
            return render_template('error.html', message=f"Ocorreu um erro: {str(e)}")
    
    return render_template('index.html')

def process_weather_data(dados, cidade, dias):
    # Preparar dados diários
    daily_data = []
    datas = []
    temp_max = []
    temp_min = []
    
    for i in range(dias):
        dados_dia = dados['forecast']['forecastday'][i]
        data = datetime.strptime(dados_dia['date'], "%Y-%m-%d").strftime("%d/%m/%Y")
        
        datas.append(data)
        temp_max.append(dados_dia['day']['maxtemp_c'])
        temp_min.append(dados_dia['day']['mintemp_c'])
        
        daily_data.append({
            'date': data,
            'maxtemp': dados_dia['day']['maxtemp_c'],
            'mintemp': dados_dia['day']['mintemp_c'],
            'condition': dados_dia['day']['condition']['text'],
            'humidity': dados_dia['day']['avghumidity'],
            'wind': dados_dia['day']['maxwind_kph'],
            'feelslike': dados_dia['day']['avgtemp_c'],
            'precip': dados_dia['day']['totalprecip_mm'],
            'icon': dados_dia['day']['condition']['icon'],
            'hourly': [{
                'time': datetime.strptime(hora['time'], "%Y-%m-%d %H:%M").strftime("%H:%M"),
                'temp': hora['temp_c'],
                'condition': hora['condition']['text'],
                'icon': hora['condition']['icon'],
                'chance_of_rain': hora['chance_of_rain']
            } for hora in dados_dia['hour']]
        })
    
    # Gerar gráfico
    graph_url = create_temperature_graph(datas, temp_max, temp_min, cidade)
    
    return {
        'cidade': cidade,
        'dias': dias,
        'daily_data': daily_data,
        'graph_url': graph_url
    }

def create_temperature_graph(datas, temp_max, temp_min, cidade):
    plt.figure(figsize=(10, 5))
    plt.plot(datas, temp_max, label="Temperatura Máxima (°C)", color="red", marker="o")
    plt.plot(datas, temp_min, label="Temperatura Mínima (°C)", color="blue", marker="o")
    plt.fill_between(datas, temp_max, temp_min, color='lightblue', alpha=0.3)
    
    plt.title(f"Previsão de Temperatura para {cidade}", fontsize=14)
    plt.xlabel("Datas", fontsize=12)
    plt.ylabel("Temperatura (°C)", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Converter gráfico para imagem base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return f"data:image/png;base64,{graph_url}"

if __name__ == '__main__':
    app.run(debug=True)
    