# !pip install flask pyngrok
from flask import Flask
from pyngrok import ngrok

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"

if __name__ == '__main__':
    # Uncomment and configure ngrok if needed
    ngrok.set_auth_token("your auth key")
    ngrok_tunnel = ngrok.connect(5000)
    print("Public URL:", ngrok_tunnel.public_url)
    
    app.run(host='0.0.0.0', port=5000)
