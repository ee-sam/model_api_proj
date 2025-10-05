class MainModel:
    def summarize(self, text: str) -> str:
        # [TODO] Access model summarizer API here
        return f"[Summary of]: {text[:50]}..."

    def save_output(self, text: str):
        with open("summary.txt", "w", encoding="utf-8") as f:
            f.write(text)