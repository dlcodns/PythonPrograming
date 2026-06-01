h, b, c, s = map(int, input().split())

byte = h*b*c*s/8
MB = byte/1024/1024

print(round(MB, 1), 'MB')