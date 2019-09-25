import os
import distutils.util

LOG_GROUP_NAME = os.getenv("LOG_GROUP_NAME")
LOG_STREAM_NAME_PREFIX = os.getenv("LOG_STREAM_NAME_PREFIX")
KEEP = os.getenv("KEEP", default="")
AFTER = os.getenv("AFTER", default="")
DRY_RUN = bool(distutils.util.strtobool(os.getenv("DRY_RUN", "False")))
DEBUG = bool(distutils.util.strtobool(os.getenv("DEBUG", "True")))
