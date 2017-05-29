"""Sllurp logging tools
"""

import logging
logger = logging.getLogger(__name__)


def init_logging(debug=False, logfile=None):
    logLevel = (debug and logging.DEBUG or logging.INFO)
    logFormat = '%(asctime)s %(name)s: %(levelname)s: %(message)s'
    formatter = logging.Formatter(logFormat)
    stderr = logging.StreamHandler()
    stderr.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(logLevel)
    root.handlers = [stderr]

    if logfile:
        fHandler = logging.FileHandler(logfile)
        fHandler.setFormatter(formatter)
        root.addHandler(fHandler)

    logger.log(logLevel, 'log level: %s', logging.getLevelName(logLevel))