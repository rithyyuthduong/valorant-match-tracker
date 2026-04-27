from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Valorant Tracker - Coming soon.'