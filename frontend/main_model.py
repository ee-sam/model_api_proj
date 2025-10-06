import requests

class MainModel:
    def summarize(self, text: str) -> dict:
        # Access model summarizer API endpoint
        api_url = "http://127.0.0.1:8080/summarize"
        try:
            clean_text = ' '.join(line.strip() for line in text.splitlines() if line.strip())
            payload = {
                "input_text": clean_text,
                "min_length": 80,
                "max_length": 120,
                "length_penalty": 0.5,
                "temperature": 1.0,
                "top_p": 1.0
            }
            response = requests.post(api_url, json=payload, timeout=60)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error":f"API request failed: {e}"}

    def save_output(self, text: str, save_path: str):
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(text)