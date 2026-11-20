from app.core import CLAUSE_LABELS, milestone_1, milestone_2, milestone_3

def test_milestone_3():
    classifier = milestone_3(epochs=6)
    label = classifier.predict("Either party may terminate this Agreement upon written notice.")
    assert label in CLAUSE_LABELS