from multiprocessing import cpu_count
from os import environ

bind = '0.0.0.0:' + environ.get('PORT', '8080')

# workers = cpu_count() * 2 + 1
workers = cpu_count()
