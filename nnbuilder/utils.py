
def findPt(x1, y1, x2, y2, c1, c2, t):
    tSqu = t ** 2
    xt = (x1 - 2 * c1 + x2) * tSqu + 2 * (c1 - x1) * t + x1
    yt = (y1 - 2 * c2 + y2) * tSqu + 2 * (c2 - y1) * t + y1
    return xt, yt


def findDerPt(x1, y1, x2, y2, c1, c2, t):
    xt = 2 * (x1 - 2 * c1 + x2) * t + 2 * (c1 - x1)
    yt = 2 * (y1 - 2 * c2 + y2) * t + 2 * (c2 - y1)
    return xt, yt