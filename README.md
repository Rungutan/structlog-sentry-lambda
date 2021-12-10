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

Example:

```shell
import os
import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),

    integrations=
    [AwsLambdaIntegration(timeout_warning=True)]
    if str(os.getenv('SENTRY_INTEGRATION', 'lambda')).lower() == 'lambda'
    else [],

    environment=os.environ.get('SENTRY_ENV'),
    send_default_pii=False,
    traces_sample_rate=1.0,
    release=os.environ.get('SENTRY_RELEASE')
)


import structlog_sentry_lambda

SENTRY_LOGGER = structlog_sentry_lambda.get_logger()
logger = SENTRY_LOGGER.bind()
logger.info("This is a breadcrumb")
logger.error("This will trigger an error in Sentry")
```
