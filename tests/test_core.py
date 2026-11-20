from app.core import milestone_1

def test_milestone_1():
    tokenized = milestone_1()
    assert len(tokenized) >= 5
    assert tokenized[0][0] == "<s>"
    assert tokenized[0][-1] == "</s>"
    assert all(tok == tok.lower() for sent in tokenized for tok in sent)