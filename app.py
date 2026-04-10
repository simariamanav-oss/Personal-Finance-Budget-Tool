from flask import Flask, render_template, request, jsonify
import anthropic
import sqlite3
from datetime import datetime

app = Flask(__name__)

client = anthropic.Anthropic(api_key="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")

conn = sqlite3.connect('finhelp.db')
conn.execute('''CREATE TABLE IF NOT EXISTS chats 
             (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, time TEXT)''')
conn.commit()
conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('finhelp.db')
    history = conn.execute('SELECT question, answer, time FROM chats ORDER BY id DESC LIMIT 5').fetchall()
    conn.close()
    return render_template('index.html', history=history)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.get_json().get('question', '')
    
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"You are FinHelp, a friendly AI financial assistant for students. Give practical, concise financial advice. Question: {question}"}
        ]
    )
    
    answer = message.content[0].text
    
    conn = sqlite3.connect('finhelp.db')
    conn.execute('INSERT INTO chats (question, answer, time) VALUES (?, ?, ?)',
                 (question, answer, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()
    conn.close()
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)