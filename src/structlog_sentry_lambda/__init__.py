import argparse
from argparse import RawTextHelpFormatter
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

"""Structlog Sentry Logger"""
from typing import List

from _config import (
    _init_sentry,
    _load_library_specific_env_vars,
    get_config_dict,
    get_logger,
    get_namespaced_module_name,
    getLogger,
)

__all__: List[str] = [
    "get_config_dict",
    "get_logger",
    "get_namespaced_module_name",
    "getLogger",
]

_load_library_specific_env_vars()
_ = _init_sentry()