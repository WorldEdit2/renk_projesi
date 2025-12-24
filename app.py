from flask import Flask, render_template
import random

app = Flask(__name__)

def generate_hex_color():
    """Rastgele bir HEX renk kodu üretir."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@app.route('/')
def home():
    # Her istekte (refresh) yeni renkler üretilir.
    # Sunucu bu renkleri hafızasında tutmaz (Stateless).
    context = {
        'color1': generate_hex_color(),
        'color2': generate_hex_color(),
        'color3': generate_hex_color(),
        'angle': random.randint(0, 360)
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
