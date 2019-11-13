import sys
import random
import time

start_time = time.time()

if (len(sys.argv) != 2):
	print("Only one input is required")
	exit(1)

n = int(sys.argv[1])

if n <= 0:
	print("Input must be positive integer")
	exit(1)

tot_elements = n*n
count = 0

output = [[ -1 for j in range(n)] for i in range(n)]

while True:
	i = random.randint(0, n-1)
	j = random.randint(0, n-1)
	element = random.randint(0, 1000)

	if output[i][j] == -1:
		output[i][j] = element
		count += 1
		if count == tot_elements:
			break

string_output = "\n".join([ " ".join([str(output[i][j]) for j in range(n)]) for i in range(n)])
execution_time = time.time() - start_time
print("Execution Time: {0}\n The output matrix is as below:\n{1}".format(execution_time, string_output))
exit(0)