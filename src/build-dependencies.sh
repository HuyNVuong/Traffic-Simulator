#!bin/bash
# Install all the dependencies
pip install -r requirements.txt --user || pip3 install -r requirements.txt --user # If user doesn't have pip and only pip3
if python -c 'import pkgutil; exit(not pkgutil.find_loader("tkinter"))'; then
    echo 'tkinter found!'
else
    echo 'Finding a workaround....'
    apt-get python3-tk # For python 2.7 user, hope no one need this :)
fi

