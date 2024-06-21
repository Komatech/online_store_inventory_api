import os
from config.env import BASE_DIR, env
from datetime import timedelta

env.read_env(os.path.join(BASE_DIR, ".env"))

REST_KNOX = {
  "SECURE_HASH_ALGORITHM": "cryptography.hazmat.primitives.hashes.SHA512",
  "AUTH_TOKEN_CHARACTER_LENGTH": env.int("KNOX_CHAR_LENGTH", default=64),
  "TOKEN_TTL": timedelta(minutes=env.int("TOKEN_EXPIRY", default=30)),
  "USER_SERIALIZER": "knox.serializers.UserSerializer",
  "TOKEN_LIMIT_PER_USER": env.int("MAX_LOGIN", default=3),
  "AUTO_REFRESH": env.bool("TOKEN_REFRESH",default=False)
}