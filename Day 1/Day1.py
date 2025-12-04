dial = [i for i in range(100)]
count = 0
total_count = 0
with open("input.txt") as f:
    direction = ""
    pointer = 0
    sign = 1
    current_index = 50
    start = current_index
    for line in f:
        direction = line[0]
        pointer = line[1:]
        pointer = int(pointer)
        if pointer == 0:
            continue
        if direction == 'L':
            temp = start - 1
            total_count += temp // 100 - (temp - pointer) // 100
            temp += 1
            end = temp - pointer
        elif direction == 'R':
            end = start + pointer
            total_count += (end // 100 ) - (start // 100)
        current_index = end % 100
        if current_index == 0:
            count += 1
        start = end
print(count)
print(total_count)
print(total_count + count)
