def marble_game(list):
    player_point_list = []
    point_list = []
    max_scored_players = []
    max_point = 0
    max_player = []
    for player in list:
        point = 0
        for marble in player:
            if marble == "yellow":
                point += 3
            elif marble == "blue":
                point += 4
            elif marble == "green":
                point += 8
            elif marble == "red":
                point += 0
            else:
                point += 2
        player_point_list.append((player, point))
        point_list.append(point)
        if max_point < point:
            max_point = point
    temp = max(point_list)
    for player in player_point_list:
        if player[1] == temp:
            max_scored_players.append(player)
    if len(max_scored_players) == 1:
        max_player = [max_scored_players[0][0], max_scored_players[0][1]]
    return max_player