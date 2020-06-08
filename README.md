# twitter-off-DSPT5


#Installation

'''sh
git clone git@github.com:ssbyrne89/twitter-off-DSPT5.git

cd twitter-off-DSPT5
'''


#Setup

'''sh
pipenv install
'''

'''sh

'''


Migrate the database:

'''sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
'''

#Usage

'''sh
FLASK_APP=web_app flask run
'''

