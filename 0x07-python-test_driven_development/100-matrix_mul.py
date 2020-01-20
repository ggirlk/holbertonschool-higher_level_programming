#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not (m_a or m_a[0]):
        raise TypeError("m_a can't be empty")
    if not (m_b or m_b[0]):
        raise TypeError("m_b can't be empty")
    l = []
    for i in range(0, len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of lists")
        if not isinstance(m_b[i], list):
            raise TypeError("m_b must be a list of lists")
        if (len(m_a[i]) != len(m_a[0])):
            raise TypeError("each row of m_a must be of the same size")
        if (len(m_b[i]) != len(m_b[0])):
            raise TypeError("each row of m_b must be of the same size")
        t = []
        for j in range(0, len(m_b[0])):
            r = 0
            for k in range(0, len(m_b)):
                if not (isinstance(m_a[i][k], int) or isinstance(m_a[i][k], float)):
                    raise TypeError("m_a should contain only integers or floats")
                if not (isinstance(m_b[k][j], int) or isinstance(m_a[k][j], float)):
                    raise TypeError("m_a should contain only integers or floats")
                try:
                    r += m_a[i][k] * m_b[k][j]
                except:
                    raise ValueError("m_a and m_b can't be multiplied")
            t.append(r)
        l.append(t)
        t = []
    return (l)
