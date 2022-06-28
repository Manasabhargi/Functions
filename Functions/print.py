import logging
def log(*args):
    logging.info(' '.join(str(arg) for arg in args))

log("execute")