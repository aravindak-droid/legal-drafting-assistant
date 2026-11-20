from app.cli import main as cli_main
from app.core import CLAUSE_LABELS, milestone_1, milestone_2, milestone_3, milestone_4

def test_milestone_4(capsys):
    cli_main(["draft", "--prompt", "Either party", "--max-words", "8"])
    captured = capsys.readouterr().out
    assert "Drafted Sentence:" in captured
    assert "Predicted Clause:" in captured