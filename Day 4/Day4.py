count = 0
with open('input.txt') as f:
#     f = ['..@@.@@@@.',
# '@@@.@.@.@@',       
# '@@@@@.@.@@',
# '@.@@@@..@.',
# '@@.@@@@.@@',
# '.@@@@@@@.@',
# '.@.@.@.@@@',
# '@.@@@.@@@@',
# '.@@@@@@@@.',
# '@.@.@@@.@.']
#     f = [list(row) for row in f]
    f = [list(line.strip()) for line in f]
    locations = []
    rows = len(f)
    cols = len(f[0])
    offset = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    possible_move = True
    while possible_move:
        possible_move = False
        for r in range(rows):
            for c in range(cols):
                roll_count = 0
                for dr, dc in offset:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        adj = f[nr][nc]
                        if adj == '@':
                            roll_count += 1
                if roll_count < 4 and f[r][c] != '.':
                    # f[r][c] = '.'
                    locations.append((r, c))
                    count += 1
                    possible_move = True
        for r, c in locations:
            f[r][c] = '.'
        locations = []
        # possible_move = False

print(count)