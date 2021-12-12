# structlog-sentry-lambda

## Description
This repository is a fork of https://github.com/TeoZosa/structlog-sentry-logger
and all credits for this solution should go to
@TeoZosa !!!

Use this **ONLY** if you are planning to integrate this
into AWS Lambda or AWS Fargate.

For any other use-case, check the original repository.

## Notes

Sentry SDK Initialization is **NOT** done within this library.

If you're going to use this library, you need to ensure that the
Sentry SDK is properly initialized **before** importing
the library.

Example for a standard AWS Lambda function:

filename = `libraries/sentry.py`
```python
import os
import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    integrations= [AwsLambdaIntegration(timeout_warning=True)],
    environment=os.environ.get('Workspace'),
    send_default_pii=True,
    traces_sample_rate=0.0,
    release=os.environ.get('SENTRY_RELEASE')
)
```

filename = `libraries/logger.py`
```python
import simplejson as json
import structlog_sentry_lambda

SENTRY_LOGGER = structlog_sentry_lambda.get_logger()
logger = SENTRY_LOGGER.bind()


def debug(log_message):
    logger.debug(json.dumps(log_message, sort_keys=True, default=str))


def error(log_message):
    logger.error(json.dumps(log_message, sort_keys=True, default=str))


def exception(log_message):
    logger.exception(json.dumps(log_message, sort_keys=True, default=str))
    
    
def warning(log_message):
    logger.warning(json.dumps(log_message, sort_keys=True, default=str))


def info(log_message):
    logger.info(json.dumps(log_message, sort_keys=True, default=str))


def main(log_message):
    logger.info(json.dumps(log_message, sort_keys=True, default=str))


def log(log_message):
    logger.info(json.dumps(log_message, sort_keys=True, default=str))

```

filename = `index.py`

```python
import sys
sys.path.append('../libraries/')
from libraries import sentry
from libraries import logger

def main(event, context):
    logger.info(event)
    logger.error("Trigger an alert in Sentry")
    return True
```
