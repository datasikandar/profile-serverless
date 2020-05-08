import json

with open('profile.json') as f:
  data = json.load(f)

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
          "Access-Control-Allow-Origin": "*",
           "Access-Control-Allow-Credentials": "true"
        },
        'body': json.dumps(
          {
            'message': data
          }
        )
    }