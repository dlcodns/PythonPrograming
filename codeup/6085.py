w, h, b = map(int, input().split())

byte = w*h*b/8

MB = byte/1024/1024

print('%.2f MB' % MB)