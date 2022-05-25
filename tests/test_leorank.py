from lexorank.lexorank import lexorank


def test_empty_prev_empty_next() -> None:
    rank, ok = lexorank("")
    assert rank == "U"
    assert ok is True


def test_empty_prev() -> None:
    rank, ok = lexorank("", "2")
    assert rank == "1"
    assert ok is True


def test_empty_next() -> None:
    rank, ok = lexorank("x")
    assert rank == "y"
    assert ok is True


def test_success_new_digit() -> None:
    rank, ok = lexorank("aaaa", "aaab")
    assert rank == "aaaaU"
    assert ok is True


def test_success_mid_value() -> None:
    rank, ok = lexorank("aaaa", "aaac")
    assert rank == "aaab"
    assert ok is True


def test_success_new_digit_mid_value() -> None:
    rank, ok = lexorank("az", "b")
    assert rank == "azU"
    assert ok is True


def test_fail_same_prev_next() -> None:
    rank, ok = lexorank("aaaa", "aaaa")
    assert rank == "aaaa"
    assert ok is False


def test_fail_asjacent() -> None:
    rank, ok = lexorank("a", "a0")
    assert rank == "a"
    assert ok is False
