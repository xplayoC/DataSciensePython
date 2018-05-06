#In this scripts i will probe the loop senteces in python

print("\n\nHere we are probing the while loop\n")

i = 0
while i < 10:
	print("i has the value of:", i,  ".")
	i = i + 1


print("\n\nHere we are probing the for loop\n")

for i in range(10, 0, -1):
	print("i has the value of:", i,  ".")


print("\n\nWe will print all the even numbers from 0 to 100")

i = 0
while i < 100:
	if not(i % 2):
		print(i)
	i += 1

print("\nThe program has finished.")

	
