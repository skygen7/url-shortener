from pathlib import Path
import yaml


def load_config(config_file=None):
    default_file = Path(__file__).parent.parent / 'config.yaml'
    with open(default_file, 'r') as f:
        config = yaml.safe_load(f)

    user, password, host, database = config['username'], config['password'], config['host'], config['database']
    config['db_parameters'] = f'postgres://{user}:{password}@{host}/{database}'
    return config
