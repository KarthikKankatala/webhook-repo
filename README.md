
# 📡 GitHub Webhook Receiver & UI

This project is part of a developer assessment task. It involves building a GitHub webhook receiver using Flask and MongoDB that listens for GitHub repository events like **Push**, **Pull Request**, and **Merge**.

### 🔗 Live Demo (Optional)
If deployed publicly:  
[https://d6adc72dad55.ngrok-free.app/](https://d6adc72dad55.ngrok-free.app/)
---

## 🚀 Project Structure

```
webhook-repo/
├── app.py                 # Flask application
├── .env                   # MongoDB URI
├── requirements.txt       # Dependencies
├── templates/
│   └── index.html         # Frontend UI
└── static/
    └── script.js          # Polls MongoDB every 15s
```

---

## 🎯 Features

- 📬 Receives GitHub webhook events from a linked `action-repo`
- 📦 Stores event data in MongoDB
- 🌐 Displays real-time event logs on a minimal UI
- 🔁 Polls MongoDB every 15 seconds to update the frontend
- ⭐ Bonus: Detects `merge` events using `pull_request.closed` with `merged = true`

---

## 🔧 Technologies Used

- Python
- Flask
- MongoDB Atlas
- HTML + JS
- Ngrok (for local webhook testing)

---

## 🧪 Supported GitHub Events

| Event        | Display Format                                               |
|--------------|--------------------------------------------------------------|
| **Push**         | `"{author} pushed to {branch} on {timestamp}"`              |
| **Pull Request** | `"{author} submitted a pull request from {src} to {dst} on {timestamp}"` |
| **Merge**        | `"{author} merged branch {src} to {dst} on {timestamp}"`     |

---

## ⚙️ Setup Instructions

### 📁 Clone the Repo

```bash
git clone https://github.com/KarthikKankatala/webhook-repo.git
cd webhook-repo
```

### 🧪 Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On Mac/Linux
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 Add `.env` File

Create a `.env` file in the root directory:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/webhook_db?retryWrites=true&w=majority
```

Replace with your MongoDB Atlas connection string.

---

## ▶️ Running the App

```bash
python app.py
```

---

## 🌍 Testing Webhooks with GitHub

1. Use `ngrok` to expose your local server:
   ```bash
   ngrok http 5000
   ```

2. Go to your `action-repo` on GitHub:
   - Settings → Webhooks → Add Webhook
   - Payload URL: `https://<your-ngrok-url>/webhook`
   - Content Type: `application/json`
   - Select Events:
     - ✅ Push
     - ✅ Pull Requests



---

## ✅ Example Usage

```bash
# In action-repo
echo "Test push" > push.txt
git add .
git commit -m "Test push event"
git push origin main
```

Watch the webhook-repo update in real-time 🎯

---

## 🧑‍💻 Author

**Karthik Kankatala**  
[GitHub](https://github.com/KarthikKankatala)

---

## 📝 License

MIT License
