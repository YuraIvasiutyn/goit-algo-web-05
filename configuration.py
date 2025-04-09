import configparser
from os.path import abspath, dirname, join

conf_file_name = 'conf'

path_of_conf = join(abspath(dirname(__file__)), '', conf_file_name)

config = configparser.RawConfigParser()

config.read(path_of_conf, encoding='utf-8')

api_url = config.get('api', 'url')
