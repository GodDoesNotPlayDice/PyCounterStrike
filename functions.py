def findMatchs(data):
    match_id= data['MatchId'] # columnas MatchId
    unique_matchs_maps = match_id.drop_duplicates() # Filtra los IDS
    arr = unique_matchs_maps.to_numpy() # Convierte a array
    lista = arr.tolist() # Convierte a lista  
    return lista

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
    return match['Map'].loc[0]

def findMapsByData(data):
    return list(data['Map'].drop_duplicates())

def findRoundByMatch(match):
    return list(match["RoundId"].drop_duplicates())

def findWinnerByMap(match_id, data):    
    match = data[data['MatchId'] == match_id]
    map_ = findMapByMatch(match)
    rounds = findRoundByMatch(match=match)
    print(f"got rounds {len(rounds)}")
    
    T = 0
    CT = 0
    
    print("round for getting")
    for i in rounds:
        matchByRound = match[match["RoundId"] == i]
        matchByRoundByT = matchByRound[matchByRound["Team"] == "Terrorist"] 
        matchByRoundByCT = matchByRound[matchByRound["Team"] == "CounterTerrorist"]
        print("Filttered Match By Round Teams")
        
        winT = matchByRoundByT["RoundWinner"].drop_duplicates()
        winCT = matchByRoundByCT["RoundWinner"].drop_duplicates()
        
        print(winT)
        print(winCT)
        
        # print("Getting bools")
        # if winT == True:
        #     T += 1
        # if winCT == True:
        #     CT += 1
    
    RoundWinners = {
        "Terorist": T,
        "CounterTerrorist": CT
    }
    
    return RoundWinners
    