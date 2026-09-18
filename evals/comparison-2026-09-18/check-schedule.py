"""Enumerate editor assignments on the scenario's half-hour grid.

This supplements the continuous-time capacity argument in REPORT.md.
It does not model extra rework, repeated reviews, uploads or transitions.
"""
import json

SLOTS = [20, 21, 22, 23, 26, 27, 28, 29, 30, 31]


def solve(reviews, deadlines):
    answers = []

    def walk(index, done, finish, plan):
        if index == len(SLOTS):
            if done == [4, 4, 1, 1]:
                answers.append(plan)
            return
        time = SLOTS[index]
        for task in range(4):
            limit = 4 if task < 2 else 1
            if done[task] >= limit or (task == 1 and time < 22):
                continue
            if task >= 2:
                item = task - 2
                if (done[item] != 4 or finish[item] > reviews[item]
                        or time < reviews[item] + 1
                        or time + 1 > deadlines[item]):
                    continue
            next_done = done.copy()
            next_done[task] += 1
            next_finish = finish.copy()
            if task < 2 and next_done[task] == 4:
                next_finish[task] = time + 1
            walk(index + 1, next_done, next_finish, plan + [(time, task)])

    walk(0, [0, 0, 0, 0], [99, 99], [])
    return answers


if __name__ == '__main__':
    original = {str(r): len(solve(r, [30, 32])) for r in ([28, 29], [29, 28])}
    adjusted = solve([28, 30], [31, 32])
    assert all(count == 0 for count in original.values())
    assert adjusted
    print(json.dumps({
        'unit': 'half-hour since midnight',
        'original_valid_schedules_by_review_order': original,
        'adjusted_A_review14_B_review15_A_publish1530_B_publish16': len(adjusted),
        'adjusted_example': adjusted[0],
        'scope': 'Enumerates all 30-minute editor slots; edits may pause, no added people or shorter durations. Does not establish conclusions for finer arbitrary durations.',
    }, indent=2))
