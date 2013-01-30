import sys
from collections import deque, Counter


with open(sys.argv[1]) as f:
    t = int(f.readline())

    for case in xrange(t):
        n, k = [int(x) for x in f.readline().split()]
        a, b, c, r = [int(x) for x in f.readline().split()]

        m = deque([a])
        for i in xrange(1, k):
            m.append((b * m[i - 1] + c) % r)

        m_set = Counter(m)
        j = 0
        for i in xrange(k + 1):
            while True:
                if j in m_set:
                    j += 1
                else:
                    break
            m.append(j)
            m_set[j] += 1

            if i != k:
                to_remove = m.popleft()
                m_set[to_remove] -= 1
                if m_set[to_remove] == 0:
                    del m_set[to_remove]

            j = min([to_remove, j])

        res = m[(n - k) % (k + 1) - 1]

        print "Case #%d: %s" % (case + 1, res)
