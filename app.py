from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return [
        {
            'name': 'Ben Enterprises',
            'phone': '021 111 222 333',
            'website': 'https://www.google.com',
            'contacts': [
                {
                    'firstName': 'Ben',
                    'lastName': 'Edwards',
                    'email': 'ben@edwards.nz'
                },
                {
                    'firstName': 'Bob',
                    'lastName': 'Jones',
                    'email': 'bob@jones.com'
                },
            ]
        },
        {
            'name': 'Evil Conglomerate',
            'phone': '09 123 456',
            'website': 'https://www.google.com',
            'contacts': [
                {
                    'firstName': 'Evil',
                    'lastName': 'Kenevil',
                    'email': 'evil@kenevil.com'
                },
            ]
        }
    ]