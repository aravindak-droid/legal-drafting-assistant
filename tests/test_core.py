def test_milestone_5():
    report = milestone_5()
    assert report["total"] == 8
    assert report["accuracy"] >= 0.75