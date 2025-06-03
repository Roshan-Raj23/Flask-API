from flask import Flask , jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<h1>This page is useless</h1>"

@app.route('/<url>' , methods=['GET'])
def findURL(url):
    # url = "https://www.youtube.com/watch?v=WquGhpG5o1Y"
    url = "https://www.youtube.com/watch?v=" + url

    ydl_opts = { 'quiet': True,'skip_download': True , 'proxy': 'http://159.65.245.255' }

    ydl = yt_dlp.YoutubeDL(ydl_opts)
    info = ydl.extract_info(url, download=False)

    progressive_formats = [
        f for f in info['formats']
        if f.get('acodec') != 'none' and f.get('vcodec') != 'none'
    ]

    best_progressive = max(progressive_formats, key=lambda x: x.get('height', 0))


    return jsonify(message=best_progressive['url'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
