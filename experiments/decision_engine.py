from pathlib import Path

DATA_DIR = Path("data/raw")

def decide(text):
    text = text.lower()
    if any(word in text for word in ["terminate", "penalty", "violation", "lawsuit"]):
        return "HIGH_RISK"
    if any(word in text for word in ["delay", "review", "pending", "audit"]):
        return "MEDIUM_RISK"
    return "LOW_RISK"

def run():
    for file in DATA_DIR.iterdir():
        content = file.read_text()
        decision = decide(content)
        print(f"{file.name} -> {decision}")

if __name__ == "__main__":
    run()
