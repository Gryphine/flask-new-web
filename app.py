from flask import Flask
app = Flask(__name__)

@app.route('/')
def new_web():
    return 'Come for new era! 오라! 오라! by 글이피네 작가'
