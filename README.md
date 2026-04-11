# FinHelp- An AI Financial Assistant for Students

## What is this?
FinHelp is a web app I built that uses AI to help students with their finances. You can ask it anything money-related like how to budget, how student loans work, or how to save money and it gives you a real, helpful answer instantly. Think of it like having a financial advisor in your pocket, except it's free and doesn't judge you for spending $8 on a coffee or spending over $100 at a bar one night :)

## Why I built this
One big thing. RELATABILITY. Honestly, managing money as a student is hard. That too an international student. Nobody really teaches you how to budget, what to do with your student loans, or how credit cards work. I wanted to build something that actually helps students figure this stuff out without having to sit through a boring finance lecture or pay for a consultation, even if this is generic.

## How it works
It's pretty simple. You type a question into the chat box, hit send, and the AI (Anthropic's Claude) gives you a response. Your questions and answers get saved to a database (Recent Questions) so you can scroll back and see what you asked before.

## Tools used:
- Flask- runs the backend and handles requests
- Claude AI- reads your question and generates a response
- SQLite- saves your chat history to a database
- HTML/CSS/JS- makes everything look nice in the browser

 ## Data Model
The application stores one main type of information, chat records:
- Student question
- AI-generated answer
- Timestamp of the conversation

This allows the app to behave like a small personal finance log that doesnt forget everything when you close it.

## How to run it yourself
1. Clone this repo:
git clone https://github.com/simariamanav-oss/Personal-Finance-Budget-Tool.git

2. Install what you need:
pip install flask anthropic

3. Open `app.py` and swap in your own Anthropic API key:
client = anthropic.Anthropic(api_key="api key here")

4. Run it:
python app.py

5. Go to `http://127.0.0.1:5000` in your browser and start asking questions!

## What you can ask it (for e.g.)
- How do I make a budget as a student?
- How do student loans work in Canada?
- What's the 50/30/20 rule?
- Should I get a credit card?
- How do I start saving money?

## File structure
app.py  #backend logic
finhelp.db  #database that stores chat history
requirements.txt  #dependencies
 
templates:
index.html  # the actual webpage

## Limitations and Future Work:
- This prototype doesn't include user login, spending tracking, or integration with real banking data. 
- The AI responses are also only as good as the question asked, it works best with specific questions rather than vague ones.

## Future improvements could include:
- A budget tracker where students log actual expenses.
- Personalized financial plans based on income and spending.
- Multilingual support for international students.
- Integration with Canadian student loan portals or any atoher country if it goes global.
