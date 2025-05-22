from typing import List, Tuple, Optional


def merge_intervals(times: List[int]) -> List[Tuple[int, int]]:
    """
    Объединяет пересекающиеся интервалы [start, end, ...] в список кортежей.
    """

    intervals = [(times[i], times[i + 1]) for i in range(0, len(times), 2)]
    intervals.sort()
    merged = []

    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    return merged


def intersect(
        a: Tuple[int, int], b: Tuple[int, int]
) -> Optional[Tuple[int, int]]:
    """Возвращает пересечение двух интервалов или None."""

    start = max(a[0], b[0])
    end = min(a[1], b[1])
    return (start, end) if start < end else None


def appearance(intervals: dict[str, list[int]]) -> int:
    """
    Возвращает общее время, когда ученик и учитель одновременно были на уроке.
    """

    lesson_start, lesson_end = intervals["lesson"]
    lesson = (lesson_start, lesson_end)
    pupil = merge_intervals(intervals["pupil"])
    tutor = merge_intervals(intervals["tutor"])

    total = 0
    for p in pupil:
        for t in tutor:
            common = intersect(p, t)
            if common:
                final = intersect(common, lesson)
                if final:
                    total += final[1] - final[0]
    return total
