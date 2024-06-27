from flask import Flask
from dotenv import load_dotenv
from blueprints.posts.posts_bp import posts_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(posts_bp, url_prefix="/posts")

if __name__ == "__main__":
    app.run()