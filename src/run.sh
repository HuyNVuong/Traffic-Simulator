#!bin/bash
# Install all the dependencies
pip install -r requirements.txt --user || pip3 install -r requirements.txt # If user doesn't have pip and only pip3
pip install python3-tk || pip3 install python3-tk || pip install python-tk --user # For python 2.7 user, hope no one need this :)

# Execute the Program and wala!
python Simulation.py || python3 Simulation.py
