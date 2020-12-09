from itertools import compress

with open("inputs/day_9_input_encoding_error.txt", "r") as input:
    lines = list(map(int, input.read().split('\n')[:-1]))

input_length = 25

ok_numbers = []
for i in range(input_length, len(lines)):
    next_number = lines[i]
    start = i - input_length
    end = i

    for l1 in range(start, end - 1):
        for l2 in range(l1 + 1, end):
            if lines[l1] + lines[l2] == next_number:
                ok_numbers.append(lines[i])

all_numbers = lines[input_length:]

invalid_number = list(set(all_numbers) - set(ok_numbers))[0]
print(invalid_number)
# 177777905


# part 2
list_to_search = list(compress(
    lines, [l != invalid_number for l in lines]
))

correct_contiguous_sets = []
for i in range(1, len(list_to_search) - 1):
    for j in range(i + 1, len(list_to_search)):
        contiguous_set = list_to_search[i:j]
        if sum(contiguous_set) == invalid_number:
            correct_contiguous_sets.append(contiguous_set)

print(min(correct_contiguous_sets[0]) + max(correct_contiguous_sets[0]))
# 23463012


_encoding_error
