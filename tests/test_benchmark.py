import random

from search_sort import benchmark

SIZES = (10, 50)
SEARCHES = 5


def small_run():
    return benchmark.run(sizes=SIZES, searches_per_size=SEARCHES, seed=1, repeat=1)


def test_run_returns_one_result_per_size():
    assert [result.size for result in small_run()] == list(SIZES)


def test_run_times_every_algorithm():
    result = small_run()[0]
    assert set(result.sorts) == {name for name, _ in benchmark.SORTS}
    assert set(result.searches) == {name for name, _, _ in benchmark.SEARCHES}


def test_all_times_are_positive():
    for result in small_run():
        assert all(seconds > 0 for seconds in result.sorts.values())
        assert all(seconds > 0 for seconds in result.searches.values())


def test_the_same_seed_generates_the_same_numbers():
    first = benchmark.random_numbers(100, 1000, random.Random(7))
    second = benchmark.random_numbers(100, 1000, random.Random(7))
    different = benchmark.random_numbers(100, 1000, random.Random(8))
    assert first == second and first != different


def test_random_numbers_stay_in_range():
    numbers = benchmark.random_numbers(200, 50, random.Random(1))
    assert len(numbers) == 200
    assert all(0 <= number <= 50 for number in numbers)


def test_fastest_runs_the_function_once_per_repeat():
    calls = []
    taken = benchmark.fastest(4, calls.append, "x")
    assert calls == ["x"] * 4
    assert taken >= 0


def test_fastest_keeps_the_shortest_time(monkeypatch):
    clock = iter([0, 3, 3, 4, 4, 9])  # three runs taking 3, 1 and 5 seconds
    monkeypatch.setattr(benchmark, "perf_counter", lambda: next(clock))
    assert benchmark.fastest(3, lambda: None) == 1


def test_format_table_shows_sizes_and_names():
    table = benchmark.format_table(small_run())
    for name, _ in benchmark.SORTS:
        assert name in table
    for name, _, _ in benchmark.SEARCHES:
        assert name in table
    for size in SIZES:
        assert str(size) in table
    assert "milliseconds" in table and "microseconds" in table


def test_format_table_reports_the_search_count_actually_used():
    assert f"average of {SEARCHES} searches" in benchmark.format_table(small_run())
    many = benchmark.run(sizes=(10,), searches_per_size=12, seed=1, repeat=1)
    assert "average of 12 searches" in benchmark.format_table(many)
