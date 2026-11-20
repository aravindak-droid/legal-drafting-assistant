import torch
from transformers import GPT2ForSequenceClassification, GPT2Tokenizer

CLAUSE_LABELS = [
    "Governing Law",
    "Confidentiality",
    "Limitation of Liability",
    "Termination",
    "Indemnification",
    "Notices",
    "Entire Agreement",
    "Payment Terms",
]

LABELED_CLAUSES = [
    ("This Agreement shall be governed by and construed in accordance with the laws of the State.", 0),
    ("All disputes arising under this contract shall be resolved under the governing law of California.", 0),
    ("The Receiving Party shall hold and maintain the Confidential Information in strictest confidence.", 1),
    ("Neither party shall disclose proprietary or confidential information to any third party.", 1),
    ("Neither party shall be liable for any indirect, incidental, special, or consequential damages.", 2),
    ("In no event shall the total liability of either party exceed the fees paid hereunder.", 2),
    ("Either party may terminate this Agreement upon thirty days prior written notice to the other party.", 3),
    ("This contract may be terminated immediately upon material breach by either party.", 3),
    ("The Vendor agrees to indemnify, defend, and hold harmless the Client from any and all claims.", 4),
    ("Each party shall indemnify the other against third-party claims arising from negligence.", 4),
    ("All notices required under this Agreement shall be in writing and delivered to the address specified.", 5),
    ("Any formal notice under this contract shall be sent via certified mail or overnight courier.", 5),
    ("This Agreement constitutes the entire understanding between the parties and supersedes all prior agreements.", 6),
    ("This contract represents the complete and entire agreement between the parties.", 6),
    ("Payment of all undisputed invoices shall be due within thirty days from the receipt of invoice.", 7),
    ("The Client shall pay all invoiced amounts within thirty days of the billing date.", 7),
]


class LegalClauseClassifier:
    def __init__(self, model_name: str = "gpt2"):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = GPT2ForSequenceClassification.from_pretrained(
            model_name, num_labels=len(CLAUSE_LABELS)
        )
        self.model.config.pad_token_id = self.tokenizer.eos_token_id

    def fine_tune(self, epochs: int = 8, lr: float = 5e-4) -> None:
        texts = [text for text, _ in LABELED_CLAUSES]
        labels = torch.tensor([label for _, label in LABELED_CLAUSES], dtype=torch.long)
        encodings = self.tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        optimizer = torch.optim.AdamW(self.model.parameters(), lr=lr)
        self.model.train()
        for _ in range(epochs):
            optimizer.zero_grad()
            outputs = self.model(**encodings, labels=labels)
            outputs.loss.backward()
            optimizer.step()
        self.model.eval()

    def predict(self, sentence: str) -> str:
        self.model.eval()
        inputs = self.tokenizer(sentence, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        pred_id = int(torch.argmax(logits, dim=-1).item())
        return CLAUSE_LABELS[pred_id]


def milestone_3(epochs: int = 8) -> LegalClauseClassifier:
    """Load GPT-2 and fine-tune it on labeled legal contract clauses."""
    classifier = LegalClauseClassifier(model_name="gpt2")
    classifier.fine_tune(epochs=epochs)
    return classifier

def milestone_4(prompt: str = "This agreement", max_words: int = 12, classifier: LegalClauseClassifier | None = None) -> dict[str, str]:
    """Generate a legal sentence via n-gram prediction and classify its clause type with GPT-2."""
    _, generated_sentence = milestone_2(prompt=prompt, n=2, max_words=max_words)
    clf = classifier if classifier is not None else milestone_3(epochs=6)
    clause_type = clf.predict(generated_sentence)
    return {"sentence": generated_sentence, "clause_type": clause_type}
def milestone_5(classifier: LegalClauseClassifier | None = None) -> dict[str, object]:
    """Evaluate GPT-2 clause classification accuracy on example legal clauses."""
    clf = classifier if classifier is not None else milestone_3(epochs=10)
    eval_samples = [
        ("This Agreement shall be governed by the laws of the State.", "Governing Law"),
        ("The Receiving Party shall keep all Confidential Information secret.", "Confidentiality"),
        ("Neither party shall be liable for consequential damages.", "Limitation of Liability"),
        ("Either party may terminate this Agreement upon thirty days notice.", "Termination"),
        ("The Vendor agrees to indemnify and hold harmless the Client.", "Indemnification"),
        ("All notices under this Agreement shall be in writing.", "Notices"),
        ("This Agreement constitutes the entire understanding between the parties.", "Entire Agreement"),
        ("Payment of undisputed invoices shall be due within thirty days.", "Payment Terms"),
    ]
    correct = 0
    results = []
    for text, expected in eval_samples:
        predicted = clf.predict(text)
        is_correct = predicted == expected
        if is_correct:
            correct += 1
        results.append({"text": text, "expected": expected, "predicted": predicted, "correct": is_correct})
    accuracy = correct / len(eval_samples)
    return {"accuracy": accuracy, "correct": correct, "total": len(eval_samples), "results": results}