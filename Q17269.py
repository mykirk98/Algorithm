N, M = map(int, input().split())
A, B = map(str, input().split())
A, B = list(A), list(B)

MIN = min(N, M)
lines = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

bucket = []

for i in range(MIN):
    bucket.append(A[i])
    bucket.append(B[i])

if len(A) - MIN > 0:
    for i in range(len(A) - MIN):
        bucket.append(A[i + MIN])

if len(B) - MIN > 0:
    for i in range(len(B) - MIN):
        bucket.append(B[i + MIN])

tmp = []
for b in bucket:
    tmp.append(lines[ord(b) - 65])
bucket = tmp

while len(bucket) > 2:
    tmp = []
    for i in range(len(bucket) - 1):
        tmp.append((bucket[i] + bucket[i+1]) % 10)
    
    bucket = tmp

if bucket[0] == 0:
    bucket.pop(0)

print(*bucket, '%', sep='')