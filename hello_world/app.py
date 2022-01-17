import json
from aws_lambda_powertools import Tracer, Logger
from aws_lambda_powertools.utilities.data_classes import (
    event_source,
    APIGatewayProxyEvent
)


tracer = Tracer()
logger = Logger()


@event_source(data_class=APIGatewayProxyEvent)
@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event: APIGatewayProxyEvent, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    logger.info("Running Hello World function")
    logger.info(f"Method: {event.http_method}")
    logger.info(f"Path: {event.path}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
