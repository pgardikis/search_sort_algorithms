import pytest

from search_sort import cli


def test_random_list_has_requested_size_and_range():
    numbers = cli.random_list(1000)
    assert len(numbers) == 1000
    assert all(0 <= n <= cli.MAX_VALUE for n in numbers)


def test_random_list_can_be_empty():
    assert cli.random_list(0) == []


def test_preview_shows_short_lists_in_full():
    assert cli.preview([1, 2, 3]) == "[1, 2, 3]"


def test_preview_shortens_long_lists():
    text = cli.preview(list(range(100)))
    assert text.startswith("[0, 1, 2")
    assert text.endswith("98, 99] (100 numbers)")


def answers(monkeypatch, *replies):
    replies = iter(replies)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(replies))


def test_read_size_uses_default_on_enter(monkeypatch):
    answers(monkeypatch, "")
    assert cli.read_size() == cli.DEFAULT_SIZE


@pytest.mark.parametrize("bad", ["abc", "-1", str(cli.MAX_SIZE + 1)])
def test_read_size_rejects_invalid_sizes(monkeypatch, bad):
    answers(monkeypatch, bad, "25")
    assert cli.read_size() == 25


def test_read_size_accepts_the_maximum(monkeypatch):
    answers(monkeypatch, str(cli.MAX_SIZE))
    assert cli.read_size() == cli.MAX_SIZE


def test_read_number_asks_again_on_invalid_input(monkeypatch):
    answers(monkeypatch, "abc", "1.5", "42")
    assert cli.read_number() == 42


def test_report_found(capsys):
    cli.report(7)
    assert capsys.readouterr().out.strip() == "Number found at index 7"


def test_report_not_found(capsys):
    cli.report(-1)
    assert capsys.readouterr().out.strip() == "Number not found!"


def test_menu_sorts_and_searches_then_exits(monkeypatch, capsys):
    monkeypatch.setattr(cli, "random_list", lambda size, max_value=cli.MAX_VALUE: [3, 1, 2])
    answers(monkeypatch, "5", "1", "2", "3", "2", "4", "2", "5", "2", "9", "0")
    cli.menu()
    out = capsys.readouterr().out
    assert out.count("The sorted list is [1, 2, 3]") == 2  # merge sort and quick sort
    assert out.count("Number found at index 2") == 1  # linear search, list unsorted
    assert out.count("Number found at index 1") == 2  # binary and interpolation, list sorted
    assert "Try again, choice 9 doesn't exist!" in out


def test_menu_sorts_once_for_repeated_searches(monkeypatch, capsys):
    calls = []
    real_merge_sort = cli.merge_sort
    monkeypatch.setattr(cli, "merge_sort", lambda items: calls.append(1) or real_merge_sort(items))
    monkeypatch.setattr(cli, "random_list", lambda size, max_value=cli.MAX_VALUE: [3, 1, 2])
    answers(monkeypatch, "5", "4", "1", "5", "1", "0")
    cli.menu()
    assert len(calls) == 1  # the sorted copy is reused by the second search
