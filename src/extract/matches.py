import requests
import os
import json
from datetime import date
from dotenv import load_dotenv


# função para pegar a resposta da API
def get_api():
    # carrega os arquivos do .env
    load_dotenv()
    # API + O código de autentificação
    url = os.getenv('jogos_URL')
    headers = {'X-Auth-Token': '9a3a5e83af0648c79f7525d4f0aec957'}
    # Pega a resposta da API
    response = requests.get(url, headers=headers)
    return response


# Transforma a resposta em Json
def extract_matches():
    response = get_api()
    # Verifica se a conexão foi bem sucedida
    if response.status_code == 200:
        # Retorna a resposta como Json
        return response.json()
    return None


# Salva os dados originais
def save_data(data_type, data):
    if not data:
        print("Dados inválidos, não salvando.")
        return

    # Cria a pasta para armazenar o arquivo Json, cado ele não exista ainda
    dir_path = os.path.join("data", "raw")
    os.makedirs(dir_path, exist_ok=True)

    # Criando a o nome do arquivo e gerando o caminho
    filename = f"{data_type}_{date.today()}.json"
    filepath = os.path.join(dir_path, filename)

    # Salvando o arquivo
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em: {filepath}")
        return True
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
        return False

# Rodando o codigo completo
def main():
    data = get_api().json()
    matches_data = data['matches']
    save_data('matches', matches_data)

