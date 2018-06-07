# -*- coding: utf-8 -*-
import requests
import os
import timeout_decorator
from timeout_decorator import TimeoutError

from common.logger import logger
from scanner.poc_scan.poc_script import PocScript


class xx(PocScript):
    poc_name = os.path.splitext(os.path.basename(__file__))[0]
    poc_type = 'web'
    poc_cms = 'hanweb'

    def __init__(self, target):
        super(xx, self).__init__(target)

    @timeout_decorator.timeout(180)
    def verify(self):
        try:
            if not self.target.url:
                return self.output(False)

        except TimeoutError as e:
            logger.error("****** script:  {} verify function timeout ******".format(self.poc_name))
            return self.output(False)
        except Exception as e:
            print
            e.message
        return self.output(False)
