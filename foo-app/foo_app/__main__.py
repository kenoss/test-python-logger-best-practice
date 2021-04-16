import logging as _logging

# noqa idiom
if True:
    logger = _logging.getLogger(__name__)
    _logging.basicConfig(level=_logging.DEBUG)


import foo_lib


def main():
    foo_lib.x.f()
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")


if __name__ == "__main__":
    main()
