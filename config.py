import logging

BOT_EXTRA_PLUGIN_DIR = './dependent_plugins'
BACKEND = 'Text'
BOT_DATA_DIR = './data'
BOT_ADMINS = ('@foo',)
BOT_LOG_FILE = BOT_DATA_DIR + '/err.log'
BOT_LOG_LEVEL = logging.INFO
BOT_PREFIX_OPTIONAL_ON_CHAT = True
BOT_PREFIX = ''
CORE_PLUGINS = ('Help', )
