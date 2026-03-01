def get_nth_line(file, n):
    """
    Return the nth line from a file
    """
    with open(file) as lines:
        for i, line in enumerate(lines, 1):
            if i == n:
                return line.rstrip('\n')
    raise ValueError('%s only has %i lines' % (file, i)
