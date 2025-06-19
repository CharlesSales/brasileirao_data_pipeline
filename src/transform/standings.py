import src.extract.standings as standings_json
import pandas as pd
from sqlalchemy import create_engine

def get_json():
    dados = standings_json.get_api().json()
    return dados


def transform():
    print('adicionando valores')
    data_json = get_json()['standings']

    players = []
    for data_total in data_json:
        for data in data_total['table']:
            df = {
                'id': data['position'],
                'posição': data['position'],
                'time': data['team']['shortName'],
                'partidas': data['playedGames'],
                'vitorias': data['won'],
                'empates': data['draw'],
                'derrotas': data['lost'],
                'pontos' : data['points'],
                'Gols feitos' : data['goalsFor'],
                'Gols sofridos' : data['goalsAgainst'],
                'SG' : data['goalDifference']
            }
            players.append(df)
    print(players)
    return players


def pre_processamento():
    data = pd.DataFrame(transform())
    engine = create_engine('postgresql://postgres:rick2003@localhost:5432/pipeline')
    data.to_sql('standings_SQL', con=engine, if_exists='replace', index=False)

    return data

def main():
    pre_processamento()