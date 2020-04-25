import sys
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--mode", dest="server_mode", help="Setting server mode",
                  default="release")
(options, args) = parser.parse_args(sys.argv)

server_yml_name = None

if options.mode == "release":
    server_yml_name = "release_config.yml"
if options.mode == "develop":
    server_yml_name = "develop_config.yml"

command_str = "python server.py -f " + server_yml_name
os.system(command_str)
