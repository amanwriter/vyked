from .utils.common_utils import json_file_to_dict, valid_timeout


class CONFIG:
    config = json_file_to_dict('./config.json')
    HTTP_TIMEOUT = config['HTTP_TIMEOUT'] if isinstance(config, dict) and 'HTTP_TIMEOUT' in config and valid_timeout(config['HTTP_TIMEOUT']) else 60
    TCP_TIMEOUT = config['TCP_TIMEOUT'] if isinstance(config, dict) and 'TCP_TIMEOUT' in config and valid_timeout(config['TCP_TIMEOUT']) else 60
    HTTP_KEEP_ALIVE_TIMEOUT = config['HTTP_KEEP_ALIVE_TIMEOUT'] if isinstance(config, dict) and 'HTTP_KEEP_ALIVE_TIMEOUT' in config and valid_timeout(config['HTTP_KEEP_ALIVE_TIMEOUT']) else 15
    INTERNAL_HTTP_PREFIX = '/__onemg-internal__'
