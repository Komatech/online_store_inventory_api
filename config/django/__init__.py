from django.core.exceptions import ImproperlyConfigured
import os
from config.env import BASE_DIR, env

env.read_env(os.path.join(BASE_DIR, ".env"))

APP_ENV = env.str("APP_ENV")


if APP_ENV == "local":
    from .local import *  # noqa
elif APP_ENV == "prod":
    from .prod import *  # noqa
elif APP_ENV == "test":
    from .test import *  # noqa
else:
    raise ImproperlyConfigured(f"`{APP_ENV}` not in `local`, `prod`, or `test`")
