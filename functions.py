def findMatchsIds(data):
    match_id= data['MatchId'] # columnas MatchId
    unique_matchs_maps = match_id.drop_duplicates() # Filtra los IDS
    arr = unique_matchs_maps.to_numpy() # Convierte a array
    lista = arr.tolist() # Convierte a lista  
    return lista

def findTimeAliveByTeamByMatch(match):
    team_CT = match[match['Team'] == "CounterTerrorist"]
    team_T = match[match['Team'] == "Terrorist"]
    
    timeAliveCT = list(team_CT['TimeAlive'].str.replace('.','').astype(float))
    timeAliveT = list(team_T['TimeAlive'].str.replace('.','').astype(float))
        
    return [timeAliveT, timeAliveCT]
    
def findTravelledDistanceByTeamByMatch(match):
    team_CT = match[match['Team'] == "CounterTerrorist"]
    team_T = match[match['Team'] == "Terrorist"]
    
    
    TravelledDistanceCT = list(team_CT['TravelledDistance'].str.replace(',','.').str.replace('.','').astype(float))
    TravelledDistanceT = list(team_T['TravelledDistance'].str.replace(',','.').str.replace('.','').astype(float))
        
    return [TravelledDistanceT, TravelledDistanceCT]


def findMatchByMap(data, map):
    matchs = data[data['Map'] == map]
    return matchs


def findMatch(match_id, data):
    match = data[data['MatchId'] == match_id]
    return match

def findMatchs(data):
    matchs_ids = findMatchsIds(data)
    matchs = []
    for i in matchs_ids:
        match = data[data['MatchId'] == i]
        matchs.append(match)
    return matchs
        
     
def findMatchsByMap(data, map_):
    matchs_map = data[data['Map'] == map_]
    matchs_id = list(matchs_map['MatchId'].drop_duplicates())
    matchs = [findMatch(i, data) for i in matchs_id]
    return matchs


def findRoundKillsByTeamByMatch(match):
    team_CT = match[match['Team'] == "CounterTerrorist"]
    team_T = match[match['Team'] == "Terrorist"]
    
    roundKillsT = [i for i in list(team_T['RoundKills']) if i > 0]
    roundKillsCT = [i for i in list(team_CT['RoundKills']) if i > 0]
    
    return [roundKillsT, roundKillsCT ]

def findHalfsByMatch(data, match_id):
    match = data[data['MatchId'] == match_id]
    half_one = match[match['RoundId'] <= 15]
    half_two = match[match['RoundId'] > 15]
    return [half_one, half_two] 


def findRoundKillsByHalf(half):
    half_one, half_two = half
    total_kills_half_one = half_one['RoundKills'].sum()
    total_kills_half_two = half_two['RoundKills'].sum()
    
    return [total_kills_half_one, total_kills_half_two]


def count_round_winner(team_df, team_name):
    return team_df[team_df['Team'] == team_name]['RoundWinner'].astype(str).eq('True').sum()

def findWinnersByHalf(half):
    halfOne = {}
    halfTwo = {}
    for half_df, half_name in zip(half, ["HalfOne", "HalfTwo"]):
        for team_name in ["Terrorist", "CounterTerrorist"]:
            win_count = count_round_winner(half_df, team_name)
            if half_name == "HalfOne":
                halfOne[team_name] = win_count
            else:
                halfTwo[team_name] = win_count
    
    return [halfOne, halfTwo]

def findMapByMatch(match):
    return match['Map'].iloc[0]


def findMapsByData(data):
    return list(data['Map'].drop_duplicates())

def findRoundByMatch(match):
    return list(match["RoundId"].drop_duplicates())

def ValidBool(string):
    return True if string == "True" else False



def findWinnerOfMapByMatch(match):    
    map_ = findMapByMatch(match)
    rounds = findRoundByMatch(match=match)
    T, CT = 0,0
    for i in rounds:
        matchByRound = match[match["RoundId"] == i]
        matchByRoundByT, matchByRoundByCT = matchByRound[matchByRound["Team"] == "Terrorist"], matchByRound[matchByRound["Team"] == "CounterTerrorist"]
        winT, winCT = matchByRoundByT["RoundWinner"].dropna().value_counts().index[0], matchByRoundByCT["RoundWinner"].dropna().value_counts().index[0]
        winT, winCT = ValidBool(winT), ValidBool(winCT)
        
        T += 1 if winT else 0
        CT += 1 if winCT else 0
    
    RoundWinners = {
        "Map": map_,
        "Terrorist": T,
        "CounterTerrorist": CT
    }
    
    return RoundWinners

    
    
    