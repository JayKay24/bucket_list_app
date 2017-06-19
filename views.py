from app import app

@app.route('/')
def homepage():
    return 'home.html'