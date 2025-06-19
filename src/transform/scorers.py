import src.extract.scorers as scorers_json
import pandas as pd
from sqlalchemy import create_engine


def get_json():
    dados = scorers_json.get_api().json()

    return dados

def transform():
    print('adicionando valores')

    data_json = get_json()['scorers']
    players = []
    contador = 0
    for data in data_json:
        contador = contador + 1
        df = {
            'id': contador,
            'jogador': data['player']['lastName'],
            'time': data['team']['shortName'],
            'partidas_jogadas': data['playedMatches'],
            'gols': data['goals'],
            'assistencias': data['assists']
        }
        players.append(df)

    return players


def pre_processamento():
    data = pd.DataFrame(transform())
    engine = create_engine('postgresql://postgres:rick2003@localhost:5432/pipeline')
    data.to_sql('scorers_SQL', con=engine, if_exists='replace', index=False)
    return data

def main():
    pre_processamento()