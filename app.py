from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.webhook_db
collection = db.events

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    formatted_data = format_event(data, event_type)
    if formatted_data:
        collection.insert_one(formatted_data)
    return '', 200

@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find().sort('_id', -1).limit(10))
    for event in events:
        event['_id'] = str(event['_id'])  # Convert ObjectId to string
    return jsonify(events)

def format_event(data, event_type):
    ts = datetime.utcnow().strftime('%d %B %Y - %I:%M %p UTC')

    if event_type == 'push':
        return {
            "msg": f"{data['pusher']['name']} pushed to {data['ref'].split('/')[-1]} on {ts}"
        }

    elif event_type == 'pull_request':
        action = data['action']
        pr = data['pull_request']
        author = pr['user']['login']
        from_branch = pr['head']['ref']
        to_branch = pr['base']['ref']

        if action == 'opened':
            return {
                "msg": f"{author} submitted a pull request from {from_branch} to {to_branch} on {ts}"
            }

        elif action == 'closed' and pr.get('merged'):
            return {
                "msg": f"{author} merged branch {from_branch} to {to_branch} on {ts}"
            }

    return None

if __name__ == '__main__':
    app.run(debug=True)
