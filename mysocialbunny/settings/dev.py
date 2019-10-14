from mysocialbunny.settings.base import *

INSTALLED_APPS += (
	'debug_toolbar',
)

MIDDLEWARE += [
    # Configuración del Debug toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]