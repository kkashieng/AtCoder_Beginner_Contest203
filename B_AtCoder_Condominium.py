N, K = list(map(int, input().split()))

result = 0

for floor_i in range(1,N+1):
    for room_i in range(1,K+1):
        result += floor_i * 100
        result += room_i

print(result)