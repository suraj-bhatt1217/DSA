# T-O(n) | S-O(k)
from collections import defaultdict

competitions = [["html", "ruby"], ["python", "swift"], ["ruby", "java"]]
results = [0, 1, 1]

scores = defaultdict(int)
for i, match in enumerate(competitions):
    t1, t2 = match
    winner = results[i]

    if winner == 0:
        scores[t2] += 5
    else:
        scores[t1] += 5

scores_list = list(scores.items())
scores_list.sort(key=lambda x: x[1], reverse=True)
print(f"Winner is: {scores_list[0][0]} ")
