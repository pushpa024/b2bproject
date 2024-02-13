import logging

logger = logging.getLogger(__name__)

def print_hello():
	logger.info("cron job called")