#코드를 수정해서 IP별 트래픽 합계를 구해서 출력해보세요
"""
try:
    file = open("./log.txt")
    loglist = []

    for line in file:
        loglist.append(line)
    
    #각 문자열을 공백으로 분할하면 0번쨰가 ip, 9번째가 트래픽
    #각 IP별 접속 횟수
    result = {}
    result1 = {}
    for log in loglist:
        result[log.split(" ")[0]] = result.get(log.split(" ")[0], 1) + 1
        result1[log.split(" ")[9]] = result.get(log.split(" ")[0], 1) + 1


    #데이터 출력
    for data in result:
        print(data, ":", result[data])

except Exception as e:
    print("파일 처리 중 예외 발생", e)
finally:
    file.close()
"""


#코드를 수정해서 IP별 트래픽 합계를 구해서 출력해보세요

try:
    file = open("./log.txt")
    loglist = []

    for line in file:
        loglist.append(line)
    
    #각 문자열을 공백으로 분할하면 0번쨰가 ip, 9번째가 트래픽
    #각 IP별 접속 횟수
    result = {}
    for log in loglist:
        try:
            result[log.split(" ")[0]] = result.get(log.split(" ")[0], 1) + int(log.split(" ")[9])
        except:
            result[log.split(" ")[0]] = result.get(log.split(" ")[0], 1) + 0

    #데이터 출력
    for data in result:
        print(data, ":", result[data])

except Exception as e:
    print("파일 처리 중 예외 발생", e)
finally:
    file.close()