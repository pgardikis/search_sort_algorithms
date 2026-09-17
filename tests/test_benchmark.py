from search_sort import benchmark

SIZES = (10, 50)


def small_run():
    return benchmark.run(sizes=SIZES, searches_per_size=5, seed=1)


def test_run_returns_one_row_per_size():
    rows = small_run()
    assert [size for size, _, _ in rows] == list(SIZES)


def test_run_times_every_algorithm():
    _, sorts, searches = small_run()[0]
    assert set(sorts) == {name for name, _ in benchmark.SORTS}
    assert set(searches) == {name for name, _, _ in benchmark.SEARCHES}


def test_all_times_are_positive():
    for _, sorts, searches in small_run():
        assert all(seconds > 0 for seconds in sorts.values())
        assert all(seconds > 0 for seconds in searches.values())


def test_run_is_repeatable_with_a_seed():
    assert [size for size, _, _ in small_run()] == [size for size, _, _ in small_run()]


def test_format_table_shows_sizes_and_names():
    table = benchmark.format_table(small_run())
    for name, _ in benchmark.SORTS:
        assert name in table
    for name, _, _ in benchmark.SEARCHES:
        assert name in table
    for size in SIZES:
        assert str(size) in table
    assert "milliseconds" in table and "microseconds" in table
