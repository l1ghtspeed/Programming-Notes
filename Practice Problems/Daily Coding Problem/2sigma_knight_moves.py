def get_probability(x, y, k, memo={}):
    if (x, y, k) in memo:
        return memo[(x, y, k)]

    if k == 0:
        return on_board(x, y)
    if not on_board(x, y):
        return 0

    jumps = get_moves(x, y)
    probs = [get_probability(x, y, k - 1, memo) for x, y in jumps]

    memo[(x, y, k)] = 0.125 * sum(probs)

    return memo[(x, y, k)]
