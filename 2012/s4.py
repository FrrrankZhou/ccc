from copy import deepcopy


class Stack:
    def __init__(self, num):
        self.stack = num

    def push(self, item):
        # item needs to be smaller than top
        if self.stack == 0 or item < self.stack % 10:
            self.stack *= 10
            self.stack += item
            return True
        else:
            return False

    def pop(self):
        if self.stack == 0:
            return -1
        else:
            tmp = self.stack % 10
            self.stack //= 10
            return tmp

    def __str__(self):
        return str(self.stack)


def list_hash_str(arr):
    return ' '.join([str(s) for s in arr])


def bfs(init_state):
    def bfs_helper(nums):
        nonlocal visited, next_layer
        for i in range(1, n):
            cur_nums = deepcopy(nums)
            x = cur_nums[i].pop()
            if x != -1:
                if not cur_nums[i-1].push(x):
                    cur_nums[i].push(x)
                    y = cur_nums[i - 1].pop()
                    cur_nums[i].push(y)
            else:
                y = cur_nums[i - 1].pop()
                if y != -1:
                    cur_nums[i].push(y)
            if list_hash_str(cur_nums) not in visited:
                next_layer.append(cur_nums)
                visited.add(list_hash_str(cur_nums))

    count = 0
    visited = set()
    visited.add(list_hash_str(init_state))
    this_layer = [init_state]

    ans = [Stack(i) for i in range(1, n+1)]

    while list_hash_str(ans) not in visited and this_layer:
        next_layer = []
        for cur_state in this_layer:
            bfs_helper(cur_state)
        this_layer = next_layer
        count += 1
    if list_hash_str(ans) in visited:
        return count
    else:
        return -1


n = int(input())
while n != 0:
    initial_state = [Stack(integer) for integer in map(int, input().split())]
    res = bfs(initial_state)
    if res == -1:
        print('IMPOSSIBLE')
    else:
        print(res)
    n = int(input())
