from flask import Flask, render_template, request, redirect, url_for, session
import openai
import os
import random

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Define a list of Singaporean jokes
jokes = [
    "The only thing faster than Singapore's MRT during peak hours is the way we 'chope' seats with a tissue packet.",
    "Why did the chicken cross the road in Singapore? To get to the hawker centre on the other side!",
    "Singapore's food is so good, even our MRT has its own 'food court'!",
    "How does a Singaporean get from one end of the island to the other? MRT and a little bit of patience!",
    "Why don't Singaporeans get lost? Because every corner has a 'kopi' shop!"
]

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/ai_agent", methods=["GET", "POST"])
def ai_agent():
    return render_template("ai_agent.html")

@app.route("/ai_agent_reply", methods=["POST"])
def ai_agent_reply():
    q = request.form.get("q")
    api_key = session.get('openai_api_key')
    
    if api_key:
        openai.api_key = api_key
    else:
        return redirect(url_for('index'))
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Updated model
            messages=[{"role": "user", "content": q}],
        )
        r = response.choices[0].message['content'].strip()
    except Exception as e:
        r = f"Error: {str(e)}"
    
    return render_template("ai_agent_reply.html", r=r)

@app.route("/singapore_joke", methods=["POST"])
def singapore_joke():
    # Choose a random joke from the list
    joke = random.choice(jokes)
    return render_template("joke.html", joke=joke)

@app.route("/set_api_key", methods=["POST"])
def set_api_key():
    api_key = request.form.get("api_key")
    if api_key:
        session['openai_api_key'] = api_key
        return redirect(url_for('index'))
    return "API Key not provided", 400

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
