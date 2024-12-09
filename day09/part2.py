""" Day 9 - part 2 """


def get_file_free_map(disk_map: str) -> tuple[int, list[int, int], list[int, int]]:
    file_map = [int(c) for c in disk_map[::2]]
    free_map = [int(c) for c in disk_map[1::2]]
    return file_map, free_map


def compress_disk(disk_map: str) -> list[int]:
    file_map, free_map = get_file_free_map(disk_map)
    ids = len(file_map)
    file_sizes = list(file_map)

    if ids == 0:
        return []

    free_buckets: list[list[int]] = []

    for index, free_space in enumerate(free_map):
        bucket: list[int] = []

        rindex = ids - 1
        while free_space > 0 and rindex > index:
            file_size = file_map[rindex]
            if free_space >= file_size:
                bucket.extend([rindex] * file_size)
                free_space -= file_size
                file_map[rindex] -= file_size
            rindex -= 1

        bucket.extend([None] * free_space)
        free_buckets.append(bucket)

    new_disk: list[int | None] = []
    for index in range(ids):
        new_disk.extend([index if file_map[index] else None] * file_sizes[index])

        if index >= len(free_map):
            break
        new_disk.extend(free_buckets[index])

    return new_disk


def compute_hash(disk_map: list[int]) -> int:
    return sum(i * m for i, m in enumerate(disk_map) if m is not None)


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
