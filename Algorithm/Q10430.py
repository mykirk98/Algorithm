A, B, C = input().split()
A, B, C = int(A), int(B), int(C)

print((A + B) % C, ((A % C) + (B % C)) % C, (A * B) % C, ((A % C) * (B % C)) % C, sep='\n')
