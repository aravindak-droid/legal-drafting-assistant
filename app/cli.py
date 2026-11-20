"""Command-line entry point: `python -m app.cli --help`."""
import argparse
from app.core import milestone_4


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="legal-drafting-assistant",
        description="Paralegals get an assistant to draft simple legal sentences using n-gram prediction and instantly classify them into clause types with a fine-tuned GPT-2 model.",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("hello", help="check that everything is wired up")

    draft_parser = sub.add_parser("draft", help="draft a legal sentence and classify its clause type")
    draft_parser.add_argument("--prompt", default="This agreement", help="starting words for the legal sentence")
    draft_parser.add_argument("--max-words", type=int, default=12, help="maximum words to generate")

    args = parser.parse_args(argv)
    if args.command == "hello":
        print("Legal Drafting Assistant is ready. Open README.md for your milestones.")
    elif args.command == "draft":
        result = milestone_4(prompt=args.prompt, max_words=args.max_words)
        print(f"Drafted Sentence: {result['sentence']}")
        print(f"Predicted Clause: {result['clause_type']}")


if __name__ == "__main__":
    main()