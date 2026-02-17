from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template (embedded so you don't need a separate file)
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Interactive Flask App</title>
    <style>
        body { font-family: Arial; background: #f4f4f4; text-align: center; padding-top: 50px; }
        form { background: white; padding: 20px; display: inline-block; border-radius: 10px; }
        input { padding: 10px; margin: 10px; }
        button { padding: 10px 20px; background: #007BFF; color: white; border: none; }
    </style>
</head>
<body>
    <h1>Welcome to My Interactive Flask App 🚀</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Enter your name" required>
        <br>
        <button type="submit">Submit</button>
    </form>

    {% if name %}
        <h2>Hello, {{ name }}! 👋</h2>
        <p>Great! Your Flask app is working interactively.</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template_string(html_page, name=name)

if __name__ == "__main__":
    app.run(debug=True)
