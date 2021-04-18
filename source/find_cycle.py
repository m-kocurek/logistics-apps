def get_loop(bv_positions, ev_position):
    def inner(track):
        if len(track) > 3:
            nodes_tab = get_nodes(track, [ev_position])
            can_be_closed = len(nodes_tab)==1
            if can_be_closed: return track

        k = len(bv_positions)
        not_visited = check_visited(bv_positions, track, k)
        possible_next_nodes = get_nodes(track, not_visited)

        for new_node in possible_next_nodes:
            track.append(new_node)
            new_track = inner(track)
            if new_track: return new_track
    return inner([ev_position])

def check_visited(bv_position, track, k):

    zmienna = False
    lenght = len(track)
    not_visit = [[None, None, None]]
    for i in range(k):
        for j in range(lenght):
            if bv_position[i][0] == track[j][0] and bv_position[i][1] == track[j][1] and bv_position[i][2] == track[j][2]:
                    zmienna = True
                    break

        if zmienna == False:
            if not_visit[0][0] == None:
                not_visit[0][0] = bv_position[i][0]
                not_visit[0][1] = bv_position[i][1]
                not_visit[0][2] = bv_position[i][2]
            else:
                not_visit.append([bv_position[i][0], bv_position[i][1], bv_position[i][2]])

        zmienna = False


    return not_visit




def get_nodes(track, not_visited):

    rows = len(track)

    last_node = [track[rows-1][0], track[rows-1][1], track[rows-1][2]]

    lenght = len(not_visited)

    nodes_in_rows = [[]]
    nodes_in_columns = [[]]

    for i in range(lenght):
        if not_visited[i][1] == last_node[1]:
            nodes_in_rows.append([not_visited[i][0], not_visited[i][1], not_visited[i][2]])
    nodes_in_rows.reverse()
    nodes_in_rows.pop()
    nodes_in_rows.reverse()

    for i in range(lenght):
        if not_visited[i][2] == last_node[2]:
            nodes_in_columns.append([not_visited[i][0], not_visited[i][1], not_visited[i][2]])
    nodes_in_columns.reverse()
    nodes_in_columns.pop()
    nodes_in_columns.reverse()


    if len(track) < 2:
        k = len(nodes_in_columns)
        for i in range(k):
            nodes_in_rows.append([nodes_in_columns[i][0], nodes_in_columns[i][1], nodes_in_columns[i][2]])
        return nodes_in_rows

    else:
        prev_node =  [track[rows-2][0], track[rows-2][1], track[rows-2][2]]
        if prev_node[1] == last_node[1]: return nodes_in_columns
        return nodes_in_rows
