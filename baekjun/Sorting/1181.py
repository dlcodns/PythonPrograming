#단어 정렬
#알파벳 소문자로 이루어진 N개의 단어가 들어오면 
# 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

N = int(input())
word = []

for i in range(0, N):
    word.append(input())

#중복 제거
word = list(set(word))

#key=lambda x: (len(x),x)
# => 각 단어를 (길이, 단어)로 리턴
#word.sort(~)
# => 구한 길이에 따라 정렬됨
word.sort(key=lambda x: (len(x),x))

for w in word:
    print(w)