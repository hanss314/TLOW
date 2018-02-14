def tlow3(input):
    output = []
    iterations = 0
    for x in input:
        temp_list = []
        for i in range(x):
            temp_list.append(x + i*input[iterations-1])
        output.append(temp_list)
        iterations += 1
    return list(output[::-1])