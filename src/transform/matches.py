import src.extract.matches as matches_json
import pandas as pd
from sqlalchemy import create_engine

def get_json():
    dados = matches_json.get_api().json()
    return dados

def transform():
    print('adicionando valores')
    data_json = get_json()['matches']
    matches = []
    contador = 0
    for data in data_json:
        if data['matchday'] < 10:
            df = {
                'id': contador,
                'rodada': data['matchday'],
                'time_mandante': data['homeTeam']['shortName'],
                'gols_mandante': data['score']['fullTime']['home'],
                'gols_visitante': data['score']['fullTime']['away'],
                'time_visitante': data['awayTeam']['shortName'],
                'status': data['status'],
                'resultado': data['score']['winner']
            }
        contador = contador + 1

        matches.append(df)

    return matches

def pre_processamento():
    data = pd.DataFrame(transform())
    data['status'] = data['status'].replace({
        'FINISHED': 'Finalizado',
        'SCHEDULED': 'Agendado'
    })

    data['resultado'] = data['resultado'].replace({
        'DRAW': 'Empate',
        'HOME_TEAM': 'Mandante',
        'AWAY_TEAM': 'Visitante'
    })

    engine = create_engine('postgresql://postgres:rick2003@localhost:5432/pipeline')
    data.to_sql('matches_SQL', con=engine, if_exists='replace', index=False)

    return data


def main():
    pre_processamento()