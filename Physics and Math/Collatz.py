import time

def collatz_conjecture(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

start = 1
end = int(input("Enter the number up to which you want to apply the Collatz conjecture: "))

start_time = time.time()

with open('collatz_output.txt', 'w') as file:
    for i in range(start, end+1):
        iterations = collatz_conjecture(i)
        file.write(str(i) + ',' + str(iterations) + '\n')
        print("Number:", i, "Iterations:", iterations)

end_time = time.time()
total_time = end_time - start_time
print("Total time taken: {:.2f} seconds".format(total_time))
