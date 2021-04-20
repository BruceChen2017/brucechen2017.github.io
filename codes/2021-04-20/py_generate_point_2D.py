from random import seed, randint, normalvariate as normal
from collections import namedtuple
from typing import Iterator, List, Tuple, Union
from math import sqrt

Point = namedtuple("Point", ["x", "y"])


def sqrt_dist(p1: Point, p2: Point) -> float:
    ds = (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
    return sqrt(ds)


def brute_force(points: List[Point]) -> float:
    n = len(points)
    min_dist = float("inf")
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = sqrt_dist(points[i], points[j])
            min_dist = min(d, min_dist)
    return min_dist


def generete_2D_points(
    groups: int = 100,
    min_num_in_group: int = 10,
    max_num_in_group: int = 50,
    precision: int = 9,
    random_state: int = 123,
) -> None:
    f = open("2d_points.txt", mode="w", encoding="utf-8")
    f.write("{} {}\n".format(groups, precision))
    seed(random_state)
    for group in range(groups):
        num_points = randint(min_num_in_group, max_num_in_group)
        points = []
        for _ in range(num_points):
            x = round(normal(0, 10), 2)
            y = round(normal(0, 20), 2)
            points.append(Point(x, y))
        min_dist = round(brute_force(points), precision)

        f.write("{} {}\n".format(num_points, min_dist))
        for point in points:
            x, y = point.x, point.y
            f.write(f"{x} {y}\n")
    f.close()


def read_data(fn: str) -> Iterator[Tuple[Union[int, List[Point]], Union[int, float]]]:
    f = open(fn, "r", encoding="utf-8")
    groups, precision = [int(s) for s in f.readline().strip().split()]
    yield groups, precision
    for group in range(groups):
        num_points, min_dist = f.readline().strip().split()
        num_points = int(num_points)
        min_dist = float(min_dist)
        # print(
        #     "Processing {}th data, which has {} pair of points with min distance {}".format(
        #         group + 1, num_points, min_dist
        #     )
        # )
        points = []
        for _ in range(num_points):
            x, y = [float(s) for s in f.readline().strip().split()]
            points.append(Point(x, y))
        yield points, min_dist
    f.close()


if __name__ == "__main__":
    generete_2D_points(1000, 100, 200)
