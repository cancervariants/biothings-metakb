import os
from config_hub import *

DATA_SRC_SERVER = "localhost"
DATA_SRC_PORT = 9200
DATA_SRC_DATABASE = "metakb_src"
DATA_SRC_SERVER_USERNAME = None
DATA_SRC_SERVER_PASSWORD = None

DATA_TARGET_SERVER = "localhost"
DATA_TARGET_PORT = 9200
DATA_TARGET_DATABASE = "metakb_merged"
DATA_TARGET_SERVER_USERNAME = None
DATA_TARGET_SERVER_PASSWORD = None

HUB_DB_BACKEND = {
        "module" : "biothings.utils.es",
        "uri" : "localhost:9200",
        }

ES_HOST = "localhost:9200"

DATA_ARCHIVE_ROOT = "/tmp/archive"
DATA_PLUGIN_FOLDER = "/data/biothings_studio/plugins/biothings-metakb"
DATA_UPLOAD_FOLDER = "/data/biothings_studio/dataupload/biothings-metakb"
DIFF_PATH = os.path.join(DATA_ARCHIVE_ROOT, "diff")
RELEASE_PATH = os.path.join(DATA_ARCHIVE_ROOT, "reliease")
LOG_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, "logs")
