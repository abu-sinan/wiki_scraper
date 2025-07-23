![Wikipedia Scraper](https://github.com/abu-sinan/wiki_scraper/blob/main/assets%2Fthumbnail.png)
# 📚 Unlimited Wikipedia Scraper with Telegram Integration

A powerful, asynchronous Wikipedia scraper for collecting unlimited topics with real-time Telegram updates. Supports both PC and Android (Termux).

---

## 🌟 Features

- ✅ Scrape **unlimited Wikipedia topics**
- 📱 Works on **PC (Windows/Linux/macOS)** and **Android (Termux)**
- ⚡ Concurrent scraping for faster results
- 📤 Sends each result to Telegram instantly
- ♻️ Automatic retry on failures
- 📁 Uses `topics.txt` file for topic list
- 🔐 Stores sensitive info securely in `.env`
- 💾 Logs progress and errors on the console

---

## ▶️ Usage

### 1. Clone the repository

```bash
git clone https://github.com/abu-sinan/wiki_scraper.git
cd wiki_scraper
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

On Termux:

```bash
pkg update && pkg install python -y
pip install -r requirements.txt
```

---

### 3. Configure environment
Create a `.env` file in the project folder:

```.env
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

---

### 4. Run the scraper

```bash
python wiki.py
```

---

## ⚙️ Configuration
### config.json

Configure scraping options:

```json
{
  "topics_file": "topics.txt",
  "concurrency": 20,
  "max_retries": 3,
  "telegram_enabled": true
}
```


### topics.txt

List all Wikipedia topics you want to scrape, one per line:

```txt
Artificial intelligence
Python (programming language)
OpenAI
Machine learning
Deep learning
Neural network
ChatGPT
```

---

## 📤 Telegram Output Example


> ✅ Topic: Deep learning  
📄 Summary: Deep learning is part of a broader family of machine learning methods based on artificial neural networks...  
🔗 https://en.wikipedia.org/wiki/Deep_learning


---

## 📁 Project Structure

```
wiki_scraper/
├── wiki.py
├── config.json
├── topics.txt
├── .gitignore
│   └── .env
├── requirements.txt
└── README.md
```

---

## 💡 Notes

- To disable Telegram messages, set `"telegram_enabled": false` in `config.json`.

- You can pause and resume scraping anytime by managing your `topics.txt`.

- Supports scraping thousands of topics efficiently.

---

## 🧪 Tested On

- Android (Termux)

- Windows 10/11

- Linux (Ubuntu, Debian)

- macOS

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🤝 Contributions

Feel free to open issues or submit pull requests!

---

## ✨ Author

Developed by **Abu Sinan**