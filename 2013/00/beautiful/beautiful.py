import sys

VALID = "abcdefghijklmnopqrstuvwxyz"

with open(sys.argv[1]) as f:
    f.readline()

    for i, line in enumerate(f):
        freq = {}
        for char in line:
            char = char.lower()
            if char in VALID:
                if not char in freq:
                    freq[char] = 0
                freq[char] += 1

        l = [(v, k) for k, v in freq.items()]
        l.sort(reverse=True)

        mapping = {l[i][1]: 26 - i for i in range(len(l))}

        s = 0
        for char in line:
            char = char.lower()
            s += mapping.get(char, 0)
        print "Case #%d: %s" % (i + 1, s)
