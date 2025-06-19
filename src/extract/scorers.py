import requests
import os
import json
from datetime import date
from dotenv import load_dotenv

def get_api():
    load_dotenv()
    url = os.getenv('estatisticas_URL')
    headers = {'X-Auth-Token': '9a3a5e83af0648c79f7525d4f0aec957'}
    response = requests.get(url, headers=headers)
    return response


def extract_matches():
    response = get_api()
    if response.status_code == 200:
        return response.json()
    return None


def save_data(data_type, data):
    if not data:
        print("Dados inválidos, não salvando.")
        return

    dir_path = os.path.join("data", "raw")
    os.makedirs(dir_path, exist_ok=True)

    filename = f"{data_type}_{date.today()}.json"
    filepath = os.path.join(dir_path, filename)

    try:
        with open(filepath, "w", encoding="utf-8",) as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em: {filepath}")
        return True
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
        return False

def main():
    data = get_api().json()
    scorers_data = data['scorers']
    save_data('scorers', scorers_data)

