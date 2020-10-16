from pathlib import Path
import yaml


def load_config(config_file=None):
    default_file = Path(__file__).parent / 'config.yaml'
    with open(default_file, 'r') as f:
        config = yaml.safe_load(f)
    return config['db_parameters']
