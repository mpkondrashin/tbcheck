
class settings:
    class sms:
        url = 'http://10.1.1.1'
        api_key = '12345-1234-123-123'
        skip_tls_verify = True
"""
from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    settings_files=[
        "default_settings.toml",
        "settings.toml",
        ".secrets.toml"
    ],
    environments=True,
    load_dotenv=False,
    envvar_prefix="TBCHECK",
)

settings.validators.register(
    Validator("SMS.URL", must_exist=True, is_type_of=str),
    Validator("SMS.API_KEY", must_exist=True, is_type_of=str),
    Validator("SMS.SKIP_TLS_VERIFY", must_exist=False, default=False, is_type_of=bool),
)

settings.validators.validate()
"""