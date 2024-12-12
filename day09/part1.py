""" Day 9 - part 1 """


def get_file_free_map(disk_map: str) -> tuple[int, list[int], list[int]]:
    file_map = [int(c) for c in disk_map[::2]]
    free_map = [int(c) for c in disk_map[1::2]]
    return len(file_map), file_map, free_map


def compress_disk(disk_map: str) -> list[int]:
    ids, file_map, free_map = get_file_free_map(disk_map)

    if ids == 0:
        return []

    new_disk: list[int] = []
    rindex = ids - 1
    for index in range(ids):
        new_disk.extend([index] * file_map[index])

        if index >= len(free_map):
            break
        if index >= rindex:
            break

        free_space = free_map[index]
        while free_space > 0:
            file_size = min(file_map[rindex], free_space)
            new_disk.extend([rindex] * file_size)

            free_space -= file_size
            file_map[rindex] -= file_size

            if file_map[rindex] == 0:
                rindex -= 1

    return new_disk


def compute_hash(disk_map: list[int]) -> int:
    return sum(i * m for i, m in enumerate(disk_map))


def solve(problem: list[str]) -> int:
    disk_map = problem[0]
    new_disk_map = compress_disk(disk_map)
    return compute_hash(new_disk_map)


if __name__ == "__main__":
    from aoc.utils import read_from_string

    example = """
2333133121414131402
"""
    problem = read_from_string(example)
    print(f"Example solution {solve(problem)}")
