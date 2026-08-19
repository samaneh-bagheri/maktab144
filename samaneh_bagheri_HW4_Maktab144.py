def solve(get_next_number):
    seen = set()

    count = 0
    best_number = None
    best_ones = -1

    while count < 50:
        x = get_next_number()
        if x in seen:
            continue
        seen.add(x)
        s = str(x)
        if len(s) % 2 == 0:
           continue
        if sum(int(d) for d in s) != 5:
            continue

        ones = s.count('1')
        if ones > best_ones:
            best_ones = ones
            best_number = x
        count += 1

    return best_number