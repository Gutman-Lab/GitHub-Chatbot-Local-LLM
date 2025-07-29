import json
from datetime import datetime

HISTORY_FILE = "chat_history.jsonl"

def save_chat(question, answer, model="unknown"):
    record = {
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "question": question,
        "answer": answer
    }
    with open(HISTORY_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")
