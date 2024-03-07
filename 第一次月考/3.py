inputs = []
outputs = []
n = int(input())

for i in range(n):
    inputs.append(int(input()))

max_index = max(inputs)
for i in range(max_index):
    if i in [0, 1]:
        outputs.append(1)
    else:
        outputs.append(outputs[-1] + outputs[-2])
for i in inputs:
    print(outputs[i - 1])