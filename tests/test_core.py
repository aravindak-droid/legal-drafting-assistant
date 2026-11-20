import pytest
from app.core import milestone_1, milestone_2


def test_milestone_1():
    tokenized = milestone_1()
    assert len(tokenized) >= 5
    assert tokenized[0][0] == "<s>"
    assert tokenized[0][-1] == "</s>"
    assert all(tok == tok.lower() for sent in tokenized for tok in sent)


def test_milestone_2():
    predictor, generated = milestone_2(prompt="This agreement", n=2, max_words=10)
    assert isinstance(generated, str)
    assert generated.lower().startswith("this agreement")
    assert len(generated.split()) > 2


@pytest.mark.skip(reason="remove this line when you start milestone 3")
def test_milestone_3():
    raise NotImplementedError("write the test for milestone 3")


@pytest.mark.skip(reason="remove this line when you start milestone 4")
def test_milestone_4():
    raise NotImplementedError("write the test for milestone 4")


@pytest.mark.skip(reason="remove this line when you start milestone 5")
def test_milestone_5():
    raise NotImplementedError("write the test for milestone 5")