from flask import Flask
from flask_cors import CORS
from BLL.loadBLL import MainBLL
from bson import ObjectId
import json

from routers.subsRouter import subs
bll = MainBLL()


app = Flask(__name__)
CORS(app)



# loads Data if it doesnt exist

bll.insert_members_to_db()
bll.insert_movies_to_db()


app.register_blueprint(subs, url_prefix='/subs')
if __name__ == "__main__":
    app.run(debug=True)