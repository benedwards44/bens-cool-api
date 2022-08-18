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
        summary: Return a list of accounts
        description: Return a list of accounts
        definitions:
          - schema:
            id: Account
            properties:
              name:
                type: string
                description: The Account Name
              phone:
                type: string
                description: The Account Phone Number
              website:
                type: string
                description: The Account Website
              
        responses:
          200:
            description: Successfully returned accounts
            content:
              application/json:
                schema:
                  type: array
                  items:
                    - schema:
                        id: Account
                        properties:
                        name:
                            type: string
                            description: The Account Name
                        phone:
                            type: string
                            description: The Account Phone Number
                        website:
                            type: string
                            description: The Account Website
        """
        return [
            {
                'name': 'Ben Enterprises',
                'phone': '021 111 222 333',
                'website': 'https://www.google.com'
            },
            {
                'name': 'Evil Conglomerate',
                'phone': '09 123 456',
                'website': 'https://www.google.com'
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


