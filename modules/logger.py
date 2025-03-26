from loguru import logger
def customize_logger():
    logger.remove()
    logger.add(lambda msg: print(msg, end=""), format="\t<level>{level: <8}</level> | "
                "<level>{message}</level>", colorize=True)