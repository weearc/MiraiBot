import os
import importlib
from pathlib import Path
from mirai import Mirai
from mirai.logger import Session as SessionLogger


def load_plugins(app: Mirai, *debug: str):
    plugin_dir = Path(__file__).parent
    module_prefix = plugin_dir.name

    if debug:
        [load_plugin(app, f'{module_prefix}.{p}') for p in debug]
        return
    for plugin in plugin_dir.iterdir():
        if plugin.is_dir() \
                and not plugin.name.startswith('_') \
                and plugin.joinpath('__init__.py').exists():
            load_plugin(app, f'{module_prefix}.{plugin.name}')


def load_plugin(app: Mirai, module_path: str):
    try:
        module = importlib.import_module(module_path)
        # 无需调用app.include_others()，否则会导致重复注册事件，原理不明
        # app.include_others(module.sub_app)
        SessionLogger.info(f'Succeeded to import "{module_path}"')
    except Exception as e:
        SessionLogger.error(f'Failed to import "{module_path}", error: {e}')
        SessionLogger.exception(e)


def load_env(path):
    with open(path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            if not line.startswith("#") and len(line.split("=", 1)) == 2:
                key, value = line.strip().split("=", 1)
                value = value[1:-1] if value[0] == value[-1] == '"' else value
                os.environ.setdefault(key, value)
