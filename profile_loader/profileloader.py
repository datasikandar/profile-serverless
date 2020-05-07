import json

with open('profile.json') as f:
  data = json.load(f)

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(
          {
            'message': data
          }
        )
    }