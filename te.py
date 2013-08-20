import os
print os.path.realpath(__file__), "haii"
print os.path.join(os.path.dirname(os.path.realpath(__file__)), 'hooy')
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
print os.path.dirname(BASE_DIR), "isthe abs path"
