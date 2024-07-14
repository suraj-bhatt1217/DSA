# T-O(n) | S-O(k)
competitions = [["html", "ruby"], ["python", "swift"], ["ruby", "java"]]
results = [0, 1, 1]


def get_tournament_winner(competitions, results):
    cur_best_team = ""
    scores = {cur_best_team: 0}
    for match_num, match in enumerate(competitions):
        t1, t2 = match

        winner = results[match_num]
        winner_team = None

        if winner == 0:
            update_score(t2, 5, scores)
            winner_team = t2
        else:
            update_score(t1, 5, scores)
            winner_team = t1
        if scores[cur_best_team] < scores[winner_team]:
            cur_best_team = winner_team
    print(scores)
    return cur_best_team


def update_score(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points


print(
    f"-------------Winner of the tournament is {get_tournament_winner(competitions, results).upper()}------------- "
)
