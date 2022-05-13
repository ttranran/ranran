import sys
import importlib.util
import os
from . import logger


def load_module(module, path):
    files = os.listdir(path)
    for file in files:
        try:
            if file.endswith('.py'):
                filename = file.replace('.py', '')
                name = "ranran.{}.{}".format(module, filename)
                spec = importlib.util.spec_from_file_location(name, path + file)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules[f"ranran.{module}.{filename}"] = load
                logger.info(f"ranran加载-->{filename}-->完成")
        except Exception as e:
            logger.info(f"ranran加载失败-->{file}-->{str(e)}")
            continue
