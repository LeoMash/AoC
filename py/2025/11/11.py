from collections import deque

f = '11.in'
# f = '11_test.in'
# f = '11_test2.in'
F = open(f).read().strip().splitlines()

G = {}
for line in F:
    u, v = line.split(':')
    u = u.strip()
    G[u] = v.strip().split()

print(G)


def bfs(u):
    visited = set()
    visited.add(u)
    queue = deque([u])
    num_paths = 0
    while queue:
        u = queue.popleft()
        if u == 'out':
            num_paths += 1
        else:
            for v in G[u]:
                if v not in visited:
                    queue.append(v)
    return num_paths


ans1 = bfs('you')
print(ans1)


# def bfs2(u):
#     visited = set()
#     visited.add((u, False, False))
#     queue = deque([(u, False, False)])
#     num_paths = 0
#     while queue:
#         u, dac_vis, fft_vis = queue.popleft()
#         if u == 'out':
#             num_paths += 1 if dac_vis and fft_vis else 0
#         else:
#             for v in G[u]:
#                 v_dac_vis = dac_vis or v == 'dac'
#                 v_fft_vis = fft_vis or v == 'fft'
#                 if (v, v_dac_vis, v_fft_vis) not in visited:
#                     queue.append((v, v_dac_vis, v_fft_vis))
#     return num_paths


def dfs(u):
    MEMO = {}
    def _dfs(u, vis_state):
        if (u, vis_state) in MEMO:
            return MEMO[(u, vis_state)]

        dac, fft = vis_state
        paths = 0
        if u == 'out':
            if dac and fft:
                paths = 1
        else:
            for v in G[u]:
                new_vis_state = (dac or v == 'dac', fft or v == 'fft')
                paths += _dfs(v, new_vis_state)

        MEMO[(u, vis_state)] = paths
        return paths
    return _dfs(u, (False, False))

# ans2 = bfs2('svr')
ans2 = dfs('svr')
print(ans2)
