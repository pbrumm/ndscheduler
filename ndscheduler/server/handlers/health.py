"""Serves the single page app web ui."""

import json

from ndscheduler import settings
from ndscheduler import utils
from ndscheduler.version import __version__
from ndscheduler.server.handlers import base
from getpass import getuser
from os import uname
import pkg_resources
import logging

logger = logging.getLogger(__name__)


class Handler(base.BaseHandler):
    """Index page request handler."""

    def get(self):
        self.write("ok");
