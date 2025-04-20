# README - Aplicativo de Previsão do Tempo com Flask

## 📌 Visão Geral

Este projeto é um aplicativo web de previsão do tempo desenvolvido em Python usando o framework Flask. Ele consome dados da [WeatherAPI](https://www.weatherapi.com/) para mostrar previsões meteorológicas detalhadas para qualquer cidade do mundo.

## ✨ Funcionalidades

- 🔍 Consulta de previsão do tempo por cidade
- 📅 Visualização para 1, 3, 5 ou 7 dias
- 📊 Gráfico interativo de temperaturas máximas e mínimas
- ⏱️ Previsão horária detalhada
- 🌦️ Ícones visuais das condições climáticas
- 📱 Design responsivo que funciona em dispositivos móveis

## 🛠️ Tecnologias Utilizadas

- **Backend**:
  - Python 3
  - Flask (Framework web)
  - Requests (Consumo de API)
  - Matplotlib (Geração de gráficos)

- **Frontend**:
  - HTML5, CSS3
  - Bootstrap 5 (Design responsivo)
  - Jinja2 (Templating)

- **API**:
  - WeatherAPI (https://www.weatherapi.com/)

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- pip (Gerenciador de pacotes Python)
- Chave de API da WeatherAPI (gratuita)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/previsao-tempo-flask.git
   cd previsao-tempo-flask
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure sua chave de API:
   - Obtenha uma chave gratuita em [WeatherAPI](https://www.weatherapi.com/)
   - Edite o arquivo `app.py` e substitua:
     ```python
     API_KEY = "sua_chave_aqui"
     ```

### Execução

```bash
python app.py
```

O aplicativo estará disponível em: http://localhost:5000

## 📂 Estrutura do Projeto

```
previsao-tempo-flask/
├── app.py                # Aplicação principal
├── requirements.txt      # Dependências
├── static/               # Arquivos estáticos
│   ├── css/
│   │   └── style.css     # Estilos CSS
│   └── js/               # JavaScript (se necessário)
└── templates/            # Templates HTML
    ├── base.html         # Layout base
    ├── index.html        # Página inicial
    ├── results.html      # Resultados
    └── error.html        # Página de erro
```

## 🌟 Recursos Adicionais

- **Gráficos interativos** de temperatura
- **Previsão horária** com scroll horizontal
- **Responsividade** para mobile
- **Tratamento de erros** amigável

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📧 Contato

