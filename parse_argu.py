import sys
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--mode", dest="server_mode", help="Setting server mode",
                  default="release")
(options, args) = parser.parse_args(sys.argv)

server_yml_name = None

if options.server_mode == "release":
    server_yml_name = "release_config.yml"

elif options.server_mode == "develop":
    server_yml_name = "develop_config.yml"

os.system("pip3 install pyyaml")
command_str = "python3 server.py -f " + server_yml_name
os.system(command_str)



