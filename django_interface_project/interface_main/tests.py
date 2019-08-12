from django.test import TestCase

# Create your tests here.

import logging

log = logging.getLogger('interface')  # intserface 是setting里面定义的
log.debug('')
log.info('sss')
log.error('')
log.warn('sss')