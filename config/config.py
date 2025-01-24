import yaml
from pathlib import Path


class Config:
    def __init__(self):
        config_path = Path(__file__).parent / "settings.yaml"
        with open(config_path) as f:
            self._config = yaml.safe_load(f)

    @property
    def app_config(self):
        return self._config["app"]

    @property
    def ui_config(self):
        return self._config["ui"]