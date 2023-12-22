from re import findall
from queue import Queue


def is_connected(a: str, goal: str) -> bool:
    visited = {name: False for name in webpages.keys()}
    q = Queue()
    q.put(a)
    while not q.empty():
        parent = q.get()
        for child in webpages[parent]:
            if child == goal:
                return True
            elif visited[child]:
                continue
            visited[parent] = True
            q.put(child)
    return False


n = int(input())
webpages: dict[str:list] = {}
pattern = r'<A HREF=".*?">'
for i in range(n):
    cur_page = input()
    x = input()
    webpages[cur_page] = []
    while x != '</HTML>':
        lst = findall(pattern, x)
        res = [s[9:-2]for s in lst]
        for x in res:
            webpages[cur_page].append(x)
            print(f'Link from {cur_page} to {x}')
        x = input()
x = input()
while x != 'The End':
    y = input()
    if is_connected(x, y):
        print(f'Can surf from {x} to {y}.')
    else:
        print(f"Can't surf from {x} to {y}.")
    x = input()
