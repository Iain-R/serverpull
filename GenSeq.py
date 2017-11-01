def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)

A = subset_sum([i for i in range(30,65)], 500)
text_file = open("Sequences.txt", "w")
x=0
for i in A:
	x+=0
	text_file.write(str(i))
	
text_file.close()
	# print(i)
