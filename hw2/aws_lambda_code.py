import json
from math import sqrt

def isPrime(n):
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for x in range(3, int(sqrt(n) + 1), 2):
            if n % x == 0:
                return False
        return True
    return False

def lambda_handler(event, context):
    # TODO implement
    result = isPrime(int(event['queryStringParameters']['q']))
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
