import configparser
import os
import sys
import base64
# Read config.ini from root directory
ROOT_DIR = sys.path[1]
config_path = os.path.join(ROOT_DIR, "config.ini")
print(config_path)
config = configparser.ConfigParser()
config.read(config_path)

# credentials
userRadius = config.get('credentials', 'user')
passwordRadius = base64.b64decode(config.get('credentials', 'password'))



