# Quote generator

The purpose of this program is to generate quotes by giving the user the possibility to consult a quote at random or to choose a category to consult a quote having for theme that one.

## Outbuildings and installation

You must have MySQL and Virtualenv installed on your computer. \
First, create a Python3 virtual environment with the Unix command: \
$ virtualenv env -p python3 \
Then, after cloning the repo, switch to the virtual environment and install the dependencies: \
$. env / bin / activate \
(env) $ pip install -r requirements.txt \
Then initialize the citation database used by the program with the command: \
(env) $ python create_db.py

## Use

Once the preparation is done, you can use the program by running the command: \
(env) $ python main.py
