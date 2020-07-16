#! /bin/sh
#-------------------------------------------------------------------------------

SERVER_DIR="."
cd ${SERVER_DIR}

if [ ! -d .venv ]; then
    echo "create virtual env."
    virtualenv -p `which python3` ${SERVER_DIR}/.venv/
    . ${SERVER_DIR}/.venv/bin/activate
    pip install --upgrade pip
    
else
    . ${SERVER_DIR}/.venv/bin/activate
    # pip install -r requirements.txt
    # pip freeze

    export FLASK_CONFIG=development
    export FLASK_APP=run.py

    # flask db init
    # flask db migrate
    # flask db upgrade
    # flask shell <<EOF
#from app.models import Employee; from app import db; admin = Employee(email="admin0@admin.com", username="admin0", password="102938", is_admin=True); db.session.add(admin); db.session.commit()
#EOF
fi

deactivate
