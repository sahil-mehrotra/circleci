
import logging
logging.basicConfig(filename='testLogging.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')

class Calculator(object):

    def add(self, number1, number2):
        logging.debug("params add {}, {}".format(number1, number2))
        return number1 + number2

    def subtract(self, param_one, param_two):
        logging.debug("params subtract {}, {}".format(param_one, param_two))
        return param_one - param_two