import logging

logging.basicConfig(filename='mylog.log',level=logging.ERROR)#.ERROR do from bot to top
logging.error('Error')
logging.critical('critical')
logging.warning('warning')
logging.info('info')
logging.debug('debug')