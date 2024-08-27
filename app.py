from flask import Flask, render_template, request
import google.generativeai as palm
import os
import openai

# Configure the API keys
palm_api_key = "YOUR_PALM_API_KEY"
palm.configure(api_key=palm_api_key)

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/ai_agent", methods=["GET", "POST"])
def ai_agent():
    return render_template("ai_agent.html")

@app.route("/ai_agent_reply", methods=["POST"])
def ai_agent_reply():
    q = request.form.get("q")
    try:
        # OpenAI GPT-3.5 API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": q}],
        )
        r = response.choices[0].message['content']
    except Exception as e:
        r = f"Error: {str(e)}"
    
    return render_template("ai_agent_reply.html", r=r)

@app.route("/singapore_joke", methods=["POST"])
def singapore_joke():
    # A common joke in Singapore
    joke = "The only thing faster than Singapore's MRT during peak hours is the way we 'chope' seats with a tissue packet."
    return render_template("joke.html", joke=joke)

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
