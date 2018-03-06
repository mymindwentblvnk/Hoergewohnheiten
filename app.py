import os
from flask import Flask
from flask_restful import Api

from app_models import db
from app_api import Plays, Counts, AudioFeature


POSTGRES_ENVIRON_KEY = 'DATABASE_URL'


app = Flask(__name__)


# ################ #
# 1) Configure app #
# ################ #
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if POSTGRES_ENVIRON_KEY in os.environ:
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        os.environ[settings.POSTGRES_ENVIRON_KEY]
else:
    import secret_settings
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        secret_settings.POSTGRES_CONNECTION_STRING


# ############################## #
# 2) Create db connection in app #
# ############################## #
db.init_app(app)


# ################################## #
# 3) Configure API endpoints for app #
# ################################## #
api = Api(app)
api.add_resource(Plays,
    '/plays/user/<string:user_name>')
api.add_resource(Counts,
    '/counts/per/<string:unit>/user/<string:user_name>',
    '/counts/per/<string:unit>/user/<string:user_name>/from/<string:from_date>',
    '/counts/per/<string:unit>/user/<string:user_name>/from/<string:from_date>/to/<string:to_date>')
api.add_resource(AudioFeature,
    '/audiofeatures/per/<string:unit>/user/<string:user_name>',
    '/audiofeatures/per/<string:unit>/user/<string:user_name>/from/<string:from_date>',
    '/audiofeatures/per/<string:unit>/user/<string:user_name>/from/<string:from_date>/to/<string:to_date>')


if __name__ == '__main__':
    app.run(debug=True)
