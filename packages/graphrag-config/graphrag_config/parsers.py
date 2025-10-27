# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Config parsers of type (str) -> dict[str, Any]."""

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

import toml
import yaml


class ConfigParsingError(ValueError):
    """Configuration Parsing Error."""

    def __init__(self, msg: str) -> None:
        """Initialize the ConfigParsingError."""
        super().__init__(msg)


def parse_json(data: str) -> dict[str, Any]:
    """Parse JSON data."""
    return json.loads(data)


def parse_yaml(data: str) -> dict[str, Any]:
    """Parse YAML data."""
    return yaml.safe_load(data)


def parse_toml(data: str) -> dict[str, Any]:
    """Parse TOML data."""
    return toml.loads(data)


def get_parser_for_file(file_path: str | Path) -> Callable[[str], dict[str, Any]]:
    """Get the parser for the given file path."""
    file_path = Path(file_path).resolve()
    match file_path.suffix.lower():
        case ".json":
            return parse_json
        case ".yaml" | ".yml":
            return parse_yaml
        case ".toml":
            return parse_toml
        case _:
            msg = (
                f"Failed to parse, {file_path}. Unsupported file extension, "
                + f"{file_path.suffix}. Pass in a custom config_parser argument or "
                + "use one of the supported file extensions, .json, .yaml, .yml, .toml."
            )
            raise ConfigParsingError(msg)
