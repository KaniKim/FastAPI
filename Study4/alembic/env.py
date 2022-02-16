from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

import models
import os, sys
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)

config = context.config
config.set_main_option("sqlalchemy.url", os.environ["DB_URL"])

fileConfig(config.config_file_name)

target_metadata = models.Base.metadata
