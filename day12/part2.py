""" Day 12 - part 2 """

from collections import defaultdict

from aoc.structures import Matrix, UnionFind


def relabel(image: Matrix[int]) -> Matrix[int]:
    new_image = Matrix([[0] * image.cols for _ in range(image.rows)], 0)
    new_label = 0
    equivalent: UnionFind[int] = UnionFind()
    for (r, c), label in image:
        # Neighbors match
        if image[r - 1, c] == label and image[r, c - 1] == label:
            l1 = new_image[r - 1, c]
            l2 = new_image[r, c - 1]

            # Set a label
            new_image[r, c] = min(l1, l2)

            # Mark l1 and l2 as equivalent
            if l1 != l2:
                equivalent.union(l1, l2)

        elif image[r - 1, c] == label:
            new_image[r, c] = new_image[r - 1, c]

        elif image[r, c - 1] == label:
            new_image[r, c] = new_image[r, c - 1]

        else:
            new_label += 1
            new_image[r, c] = new_label

    for rc, label in new_image:
        if label in equivalent:
            new_image[rc] = equivalent.find(label)

    return new_image


def solve(problem: list[str]) -> int:
    labels = [[ord(p) for p in line] for line in problem]
    garden = Matrix(labels, 0)
    garden = relabel(garden)

    areas: dict[int, int] = defaultdict(int)
    for (r, c), plant in garden:
        areas[plant] += 1

    h_sides: dict[int, int] = defaultdict(int)
    v_sides: dict[int, int] = defaultdict(int)
    for r in range(garden.rows):
        for c in range(garden.cols):
            plant = garden[r, c]
            ll = garden[r, c - 1] == plant

            if garden[r - 1, c] != plant:
                if not ll or garden[r - 1, c - 1] == plant:
                    h_sides[plant] += 1

            if garden[r + 1, c] != plant:
                if not ll or garden[r + 1, c - 1] == plant:
                    h_sides[plant] += 1

    for c in range(garden.cols):
        for r in range(garden.rows):
            plant = garden[r, c]
            tt = garden[r - 1, c] == plant

            if garden[r, c - 1] != plant:
                if not tt or garden[r - 1, c - 1] == plant:
                    v_sides[plant] += 1

            if garden[r, c + 1] != plant:
                if not tt or garden[r - 1, c + 1] == plant:
                    v_sides[plant] += 1

    tot = 0
    for plot, area in areas.items():
        tot += area * (h_sides[plot] + v_sides[plot])
    return tot


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
