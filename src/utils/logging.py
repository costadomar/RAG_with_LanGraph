import logging


def get_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    ch = logging.StreamHandler()
    ch.setLevel(level)

    def fmt_filter(record):
        record.levelname = "%s:" % record.levelname
        return True

    logger.addFilter(fmt_filter)

    formatter = logging.Formatter(
        "%(levelname)-9s %(asctime)s %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger
