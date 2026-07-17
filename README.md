# Auto-Chat: Screenshot-Based Chat Auto-Responder

An experimental automation tool that watches a region of your screen for new chat messages, extracts the text via OCR, generates a reply using a self-hosted LLM (Qwen via Ollama), and types the response back automatically.

## How It Works

1. **Screen Capture** (`ss.py`) — Periodically grabs a defined region of the screen (e.g., a chat window) and saves it as an image.
2. **Change Detection** (`main.py`) — Uses the [`visual-comparison`](https://pypi.org/project/visual-comparison/) library to compare the new screenshot against the previous one. If the similarity score drops below a threshold, a new message is assumed to have arrived.
3. **OCR** (`ocr.py`) — Uses `pytesseract` to extract text from the screenshot.
4. **Remote Inference** (`req.py`) — Sends the extracted text to a remote REST API endpoint that proxies to an Ollama-hosted LLM.
5. **Auto-Reply** (`main.py`) — Uses the `keyboard` library to type the generated reply into the chat and press Enter.
6. **LLM Server** (`ollama.ipynb`) — A Google Colab notebook that sets up the backend: installs Ollama, pulls a model (Qwen), wraps it in a FastAPI server, and exposes it to the internet via a Cloudflare Tunnel.

## Project Structure

```
.
├── main.py          # Main loop: capture -> detect change -> OCR -> get reply -> type reply
├── ss.py             # Screen region capture utility
├── ocr.py            # OCR text extraction via Tesseract
├── req.py            # Sends OCR'd text to the remote LLM API
└── ollama.ipynb       # Colab notebook: sets up Ollama + FastAPI + Cloudflare Tunnel
```

## Requirements

### Client-side (local machine)
- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed locally (update the path in `ocr.py` to match your install location)
- Python packages:
  ```
  pip install pytesseract pillow keyboard requests visual-comparison
  ```

### Server-side (Colab / remote GPU)
- Google Colab (or any machine with a GPU)
- Ollama
- FastAPI + Uvicorn
- Cloudflare Tunnel (for exposing the local API to the internet)

## Setup

1. **Start the backend** (`ollama.ipynb`):
   - Run the notebook in Google Colab.
   - It installs Ollama, pulls the model, wraps it in a FastAPI app (`api.py`), and starts a Cloudflare Tunnel so the API is reachable at a public URL.

2. **Configure the client**:
   - Update the region coordinates in `ss.py` (`capture_region_pil`) to match the chat window area on your screen.
   - Update the endpoint URL in `req.py` to point to your deployed API.
   - Update the Tesseract path in `ocr.py` if needed.

3. **Run the client**:
   ```
   python main.py
   ```
   The script will take a screenshot every 10 seconds, compare it to the previous one, and if a change is detected, extract the text, get a reply from the LLM, and type it out automatically.
   Open the app like whatsapp, and select the "Type a message" box so messages can be entered through the script.

## ⚠️ Important Notes

- **This automates replying to messages on someone's behalf without the other party's knowledge that they're talking to a bot.** Consider the ethical and platform-policy implications before using this on real conversations — many messaging platforms prohibit automated/bot behavior, and people you're chatting with may reasonably expect to be talking to a human.
- The Cloudflare Tunnel token and any API URLs in this repo are examples/placeholders
- This is a personal/experimental project, not production-grade software. Error handling, security, and reliability are minimal.
