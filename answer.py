import sys
input = sys.stdin.readline

N, M = map(int, input().split())
t = list(map(int, input().split()))

if t[0] == 0:
    for _ in range(M):
        input()
    print(M)
    exit()

truth = set(t[1:])
parties = []

for _ in range(M):
    p = list(map(int, input().split()))
    parties.append(set(p[1:]))

changed = True
while changed:
    changed = False
    for p in parties:
        if p & truth:
            if not p <= truth:
                truth |= p
                changed = True

ans = 0
for p in parties:
    if not p & truth:
        ans += 1

print(ans)