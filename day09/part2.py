""" Day 9 - part 2 """

import heapq
from dataclasses import dataclass


@dataclass
class File:
    ID: int
    size: int
    begin: int

    def __hash__(self) -> int:
        return self.ID * (self.size * self.begin + sum(range(self.size)))

    @property
    def end(self) -> int:
        return self.begin + self.size


def compute_hash(file_map: list[File]) -> int:
    return sum(hash(file) for file in file_map)


def get_file_space_maps(disk_map: str) -> tuple[list[File], dict[int, list[int]]]:
    file_map: list[File] = []
    free_space_map: dict[int, list[int]] = {}
    off = 0
    for i, d in enumerate(disk_map):
        size = int(d)
        ID = i // 2
        if i % 2 == 0:  # is file
            file_map.append(File(ID, size, off))
            off += size
        else:  # is free space
            free_space_map.setdefault(size, []).append(off)
            off += size

    for heap in free_space_map.values():
        heapq.heapify(heap)

    return file_map, free_space_map


def compress_files(
    file_map: list[File], free_space_map: dict[int, list[int]]
) -> list[File]:
    # files are ordered by ID
    for file in file_map[::-1]:
        if file.size == 0:
            continue

        # find smallest free location that can accomodate file
        min_heap_index = None
        for free_space, heap in free_space_map.items():
            if not heap:
                continue
            if file.size > free_space or file.begin <= heap[0]:
                continue

            if min_heap_index is None:
                min_heap_index = free_space

            if heap[0] < free_space_map[min_heap_index][0]:
                min_heap_index = free_space

        if min_heap_index is None:
            continue

        free_space = min_heap_index
        heap = free_space_map[min_heap_index]

        # move the file
        free_space_location = heapq.heappop(heap)
        file.begin = free_space_location

        # add any space left back to the map
        space_left = free_space - file.size
        heapq.heappush(free_space_map.setdefault(space_left, []), file.end)

    return file_map


def solve(problem: list[str]) -> int:
    disk_map = problem[0]
    file_map, free_space_map = get_file_space_maps(disk_map)
    new_file_map = compress_files(file_map, free_space_map)
    return compute_hash(new_file_map)


if __name__ == "__main__":
    from aoc.utils import read_from_file, read_from_string

    example = """
2333133121414131402
"""
    problem = read_from_string(example)
    problem = read_from_file("day09/bonus")
    print(f"Example solution {solve(problem)}")
