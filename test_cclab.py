from hello import some_func


def test_always_true():
    assert True


def test_some_func():
    assert some_func() == "this is the choice of steins;gate"
