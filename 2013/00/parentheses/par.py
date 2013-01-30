import sys


def doit(s, counter):
    if counter < 0:
        return False
    if not s:
        return counter == 0

    a, b, c, d, e = False, False, False, False, False

    if s.startswith(":("):
        a = doit(s[2:], counter)
    if s.startswith(":)"):
        b = doit(s[2:], counter)
    if s.startswith("("):
        c = doit(s[1:], counter + 1)
    if s.startswith(")"):
        d = doit(s[1:], counter - 1)
    if s[0] not in "()":
        e = doit(s[1:], counter)
    return a or b or c or d or e


with open(sys.argv[1]) as f:
    f.readline()

    for i, line in enumerate(f):
        result = doit(line, 0)
        print "Case #%d: %s" % (i + 1, "YES" if result else "NO")
