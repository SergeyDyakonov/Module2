numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    print(numbers[i])
for j in numbers:
    if j > 1:
        for i in range(2, j):
            if (j % i) == 0:
                not_primes.append(j)
                break
        else:
            primes.append(j)
    else:
        not_primes.append(j)
print('Primes:', primes)
print('Not Primes:', not_primes)