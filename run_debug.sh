#! /bin/sh
#-------------------------------------------------------------------------------

SERVER_DIR="."
cd ${SERVER_DIR}

if [ ! -d .venv ]; then
    echo "Virtualenv does not exist."
    exit 1
else
    . ${SERVER_DIR}/.venv/bin/activate
fi

export FLASK_CONFIG=development
python ./run.py

deactivate

