from src.transform.scorers import pre_processamento
import os
from datetime import date

def save_data_processed(data_type, data):
    if data is None or data.empty:
        print("Dados inválidos, não salvando.")
        return

    # Cria a pasta para armazenar o arquivo Json, cado ele não exista ainda
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = os.path.join(BASE_DIR, "data", "processed")

    os.makedirs(dir_path, exist_ok=True)

    # Criando a o nome do arquivo e gerando o caminho
    filename = f"{data_type}_{date.today()}.csv"
    filepath = os.path.join(dir_path, filename)

    # Salvando o arquivo
    try:
        with open(filepath, "w", encoding="utf-8", newline='') as f:
            data.to_csv(f, index=False)
        #print(f"Dados salvos com sucesso em: {filepath}")
        return True
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e} scorers")
        return False


def main():
    scorers_data = pre_processamento()
    save_data_processed('scorers_processed', scorers_data)

