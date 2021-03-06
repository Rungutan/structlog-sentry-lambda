"""Structlog Sentry Logger"""
from typing import List

from ._config import (
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
