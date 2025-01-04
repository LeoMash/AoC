import re
from collections import defaultdict
from functools import cache

f = '14.in'
D = open(f).read().strip()

# Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
R = re.compile("(.*) can fly (.*) km/s for (.*) seconds, but then must rest for (.*) seconds.")

G = defaultdict(tuple)
for line in D.splitlines():
    m = R.match(line)
    assert m is not None
    a = m.group(1)
    speed = int(m.group(2))
    time_fly = int(m.group(3))
    time_rest = int(m.group(4))
    G[a] = (speed, time_fly, time_rest)

G = dict(G)
print(G)

TIME = 2503
ans1 = 0
max_k = None
for k, v in G.items():
    speed, time_fly, time_rest = v
    cycle_len = time_fly + time_rest
    total_cycles = TIME // cycle_len
    fly_leftover = min(TIME % cycle_len, time_fly)
    dist = (total_cycles * time_fly + fly_leftover) * speed
    if dist > ans1:
        ans1 = dist
        max_k = k
print(ans1, max_k)

dist = {}
for k in G.keys():
    speed, time_fly, time_rest = G[k]
    cycle_len = time_fly + time_rest
    cur_dist = [0]
    for t in range(0, TIME):
        if (t % cycle_len) < time_fly:
            cur_dist.append(cur_dist[-1] + speed)
        else:
            cur_dist.append(cur_dist[-1])
    dist[k] = cur_dist
print(dist)

score = {k: 0 for k in G.keys()}
for t in range(1, TIME + 1):
    max_dist_k = list(G.keys())[0]
    max_dist = dist[max_dist_k][t]
    for k in G.keys():
        if max_dist < dist[k][t]:
            max_dist = dist[k][t]
            max_dist_k = k
    score[max_dist_k] += 1
print(score)