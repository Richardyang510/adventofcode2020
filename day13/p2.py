input_file = open("input.txt", "r")

depart_time = int(input_file.readline().strip())
buses = input_file.readline().strip().split(',')

crt_list = []
N = 1
for i in range(len(buses)):
    if buses[i] != 'x':
        crt_list.append((i, int(buses[i])))
        N *= int(buses[i])

print(N)

t = 0
for b, n in crt_list:
    N_i = int(N / n)
    x_i = pow(N_i, n - 2, n)  # modular inverse
    b_i = n - b
    print(n, b_i, N_i, x_i, b_i * N_i * x_i)
    t += b_i * N_i * x_i

print(t % N)
