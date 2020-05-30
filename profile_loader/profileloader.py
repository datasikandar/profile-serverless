import json

with open('profile.json') as f:
  data = json.load(f)

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
          "Access-Control-Allow-Origin": "http://khansikandar.com",
           "Access-Control-Allow-Credentials": "true"
        },
        'body': json.dumps(
          {
            'data': data
          }
        )
    }