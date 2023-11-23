from functools import lru_cache


def solution(total_days, max_absent_days):

    total_ways = get_valid_ways(total_days, 0, max_absent_days)
    miss_grad = get_valid_ways(total_days - 1, 1, max_absent_days)

    return f"{miss_grad}/{total_ways}"


@lru_cache(None)
def get_valid_ways(total_days, cur_absent_days, max_absent_days):

    if max_absent_days == cur_absent_days:
        return 0
    if total_days == 0:
        return 1

    return get_valid_ways(total_days - 1, 0, max_absent_days) + get_valid_ways(total_days - 1, cur_absent_days + 1, max_absent_days)


if __name__ == "__main__":
    max_absent_days = 4
    total_days = 5
    print(solution(total_days, max_absent_days))

    total_days = 10
    print(solution(total_days, max_absent_days))