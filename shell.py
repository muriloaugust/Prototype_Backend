#!/usr/bin/env python

from augusto_prototype_backend import app
from augusto_prototype_backend.app import config  # noqa
from augusto_prototype_backend.db import get_session
from augusto_prototype_backend.db.models import *  # noqa
from augusto_prototype_backend.lib.logger import get_logger
from augusto_prototype_backend.lib.redis import get_redis_connection   # noqa

app.initialize()

logger = get_logger()
session = get_session()
