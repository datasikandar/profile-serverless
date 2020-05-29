import json

with open('profile.json') as f:
  data = json.load(f)

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
          "Access-Control-Allow-Origin": "http://profile-angular.s3-website-us-east-1.amazonaws.com",
           "Access-Control-Allow-Credentials": "true"
        },
        'body': json.dumps(
          {
            'data': data
          }
        )
    }