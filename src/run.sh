#!bin/bash
# Install all the dependencies
pip install -r requirements.txt --user
pip install python3-tk || pip install python-tk --user # For python 2.7 user, hope no one need this :)

# Execute the Program and wala!
python Simulation.py || python3 Simulation.py
