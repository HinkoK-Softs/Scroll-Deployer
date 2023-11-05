import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.CRITICAL,
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger('Scroll Deploy')
logger.setLevel(logging.INFO)
