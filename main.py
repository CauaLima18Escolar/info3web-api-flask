from app import createApp

app = createApp()

@app.route("/")
def index():
    return "Versão 0.0.1"

