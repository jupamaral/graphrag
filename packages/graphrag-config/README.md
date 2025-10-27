# GraphRAG Config

```python
from pydantic import BaseModel, Field
from graphrag_config import load_config

from pathlib import Path

class Logging(BaseModel):
    """Test nested model."""

    directory: str = Field(default="output/logs")
    filename: str = Field(default="logs.txt")

class Config(BaseModel):
    """Test configuration model."""

    name: str = Field(description="Name field.")
    logging: Logging = Field(description="Nested model field.")

# Basic
# By default, ${} env variables in config file will be parsed and replaced
# can disable by setting parse_env_vars=False
config = load_config(Config, "path/to/config.[yaml|yml|json|toml]")

# with .env file
config = load_config(
    config_initializer=Config,
    config_path="config.yaml",
    dot_env_path=".env"
)

# With overrides - provided values override whats in the config file
# Only overrides what is specified - recursively merges settings.
config = load_config(
    config_initializer=Config,
    config_path="config.yaml",
    overrides={
        "name": "some name"
        "logging": {
            "filename": "my_logs.txt"
        }
    },
)

# Set the working directory to the directory of the config file
config = load_config(
    config_initializer=Config,
    config_path="some/path/to/config.yaml",
    set_cwd=True
)

# now cwd == some/path/to
assert Path.cwd() == "some/path/to"

# And now throughout the codebase resolving relative paths in config
# will resolve relative to the config directory
Path(config.logging.directory) == "some/path/to/output/logging"

```