import logging

#basic configuration
log = logging.basicConfig(filename = 'mylog',filemode = 'w',level = logging.DEBUG,
                          format= "%(asctime)s-%(message)s-%(levelname)s")
# logging.FileHandler
# logging.Formatter

logger = logging.getLogger() #instance

logger.info("informatiion message")
logger.debug("debug message")
logger.exception("exception message")
logger.critical("critical message")
logger.warning("warning message")
logger.error("error messages")
