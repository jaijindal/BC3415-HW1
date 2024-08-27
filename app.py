from flask import Flask, render_template, request
import openai
import os

# Configure the API keys
palm_api_key = os.getenv("PALM_API_KEY")
# palm.configure(api_key=palm_api_key)  # Uncomment if you are using the PALM API

openai.api_key = os.getenv("OPENAI_API_KEY")

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
        response = openai.Completion.create(
            model="text-davinci-003",  # Adjust model as necessary
            prompt=q,
            max_tokens=150  # Adjust max_tokens as necessary
        )
        r = response.choices[0].text.strip()
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
