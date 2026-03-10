# 트리 구조 정의 (이미지 기반)
tree = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': ['J'],
    'F': [],
    'G': ['K', 'L'],
    'H': ['M'],
    'I': [],
    'J': ['N'],
    'K': [],
    'L': ['O', 'P', 'Q'],
    'M': [],
    'N': ['R'],
    'O': [],
    'P': [],
    'Q': ['S', 'T'],
    'R': [],
    'S': [],
    'T': []
}

# TARGET 설정
TARGET = 'T'  # 찾고자 하는 노드 (원하는 노드로 변경 가능)

# expand 함수: 주어진 노드의 자식 노드들을 반환
def expand(node):
    return tree.get(node, [])

def DFS(start_node):
    # 1) stack 에 첫 번째 노드 넣으면서 시작
    stack = [start_node, ]
    visited = []  # 방문한 노드 추적 (선택사항)
    
    while True:
        # 2) stack이 비어있는지 확인
        if len(stack) == 0:
            print('All node searched.')
            return None
        
        # 3) stack에서 맨 위의 노드를 pop
        node = stack.pop()
        
        # 방문한 노드 기록
        visited.append(node)
        print(f'Visiting: {node}')
        
        # 4) 만약 node가 찾고자 하는 target이라면 서치 중단!
        if node == TARGET:
            print('The target found.')
            print(f'Search path: {" -> ".join(visited)}')
            return node
        
        # 5) node의 자식을 expand 해서 children에 저장
        children = expand(node)
        
        # 6) children을 stack에 쌓기
        # DFS는 깊이 우선이므로 역순으로 넣어서 왼쪽부터 탐색
        stack.extend(reversed(children))
        
        # 7) 이렇게 target을 찾거나, 전부 탐색해서 stack이 빌 때까지 while문 반복

# 실행
if __name__ == "__main__":
    print(f"Starting DFS from node 'A', searching for '{TARGET}'")
    print("=" * 50)
    result = DFS('A')
    print("=" * 50)
    if result:
        print(f"Result: Found '{result}'")
    else:
        print(f"Result: '{TARGET}' not found in the tree")