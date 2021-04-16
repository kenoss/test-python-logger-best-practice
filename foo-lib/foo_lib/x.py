import logging as _logging

# noqa idiom
if True:
    logger = _logging.getLogger(__name__)
    logger.addHandler(_logging.NullHandler())


def f():
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
