"""
    [1] https://www.geeksforgeeks.org/closest-pair-of-points-onlogn-implementation/
    [2] https://www.youtube.com/watch?v=0W_m46Q4qMc
    [3] https://stackoverflow.com/a/61981008/7390103
"""

from typing import List
from py_generate_point_2D import Point, sqrt_dist, brute_force, read_data


def strip_closest(strip: List[Point], d: float) -> float:
    r = len(strip)
    min_value = d
    for i in range(r):
        j = i + 1
        while j < r and (strip[j].y - strip[i].y) < min_value:
            ds = sqrt_dist(strip[j], strip[i])
            min_value = min(min_value, ds)
            j += 1
    return min_value


def closest_half(points_xs: List[Point]) -> float:
    n = len(points_xs)
    if n <= 3:
        return brute_force(points_xs)
    mid = n // 2
    mid_point = points_xs[mid]

    xs_left = points_xs[:mid]
    xs_right = points_xs[mid:]

    # sort ys
    # ys_left = sorted(xs_left, key=lambda p: p.y)
    # ys_right = sorted(xs_right, key=lambda p: p.y)

    # use presorted ys
    # ys_left = [p for p in points_ys if p.x < mid_point.x]
    # ys_right = [p for p in points_ys if p.x >= mid_point.x]

    dL = closest_half(xs_left)
    dR = closest_half(xs_right)

    d = min(dL, dR)  # upper bound of min distance
    # get strip
    strip = []
    points_ys = sorted(points_xs, key=lambda p: p.y)
    for p in points_ys:
        if abs(p.x - mid_point.x) < d:
            strip.append(p)

    # find min distance in strip
    if strip:
        ds = strip_closest(strip, d)
        return ds
    else:
        return d


def get_closest(points: List[Point]) -> float:
    points.sort(key=lambda point: point.x)
    # xs = points
    # ys = sorted(xs, key=lambda point: point.y)
    return closest_half(points)


if __name__ == "__main__":
    import time

    fn = "./2d_points.txt"
    t1 = time.time()
    cnt = 0
    data_loader = read_data(fn)
    _, precision = next(data_loader)
    for points_list, min_dist in data_loader:
        cnt += 1
        min_dist_2 = round(get_closest(points_list), precision)
        try:
            assert min_dist == min_dist_2
        except AssertionError as err:
            print(
                "{}th group: true distance vs test distance: {} vs {}".format(
                    cnt, min_dist, min_dist_2
                )
            )
            raise err
    print(f"processed {cnt} groups")
    print("running time is {:.2f}".format(time.time() - t1))
