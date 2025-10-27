# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""The GraphRAG Config package."""

from graphrag_config.load_config import load_config
from graphrag_config.parsers import ConfigParsingError

__all__ = ["ConfigParsingError", "load_config"]
