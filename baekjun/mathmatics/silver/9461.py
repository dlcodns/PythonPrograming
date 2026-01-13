#파도반 수열

T = int(input())

wave = [0]*100
wave[:10] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]


for i in range(0, T):
    N = int(input())

    if wave[N-1] != 0:
        print(wave[N-1])
        continue

    for i in range(10, N):
        wave[i] = wave[i-2]+wave[i-3]

    print(wave[N-1])

