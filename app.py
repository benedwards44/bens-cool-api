from flask import Flask, jsonify
from flask.views import MethodView
from flask_swagger import swagger

app = Flask(__name__)

class AccountAPI(MethodView):

    def get(self):
        """
        Return a dummy endpoint
        ---
        tags:
          - accounts
        definitions:
          - schema:
            id: Group
            properties:
            name:
              type: string
              description: the group's name
        responses:
          200:
            description: Successfully returned accounts
        """
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

app.add_url_rule("/", view_func=AccountAPI.as_view("accounts"))


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Ben\'s Cool API"
    swag['info']['description'] = "Such a cool API"
    #swag['info']['contact']['email'] = "ben@edwards.nz"
    return jsonify(swag)


