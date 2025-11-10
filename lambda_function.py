import json
import boto3
import base64
import datetime
client_bedrock = boto3.client('bedrock-runtime')
client_s3 = boto3.client('s3')

def lambda_handler(event, context):
    if 'queryStringParameters' in event and event['queryStringParameters']:
        input_prompt = event['queryStringParameters'].get('prompt', 'default prompt')
    else:
        input_prompt = event.get('prompt', 'default prompt')
    print(input_prompt)

    response_bedrock=client_bedrock.invoke_model( contentType='application/json', accept='application/json',  modelId='amazon.titan-image-generator-v1', body= json.dumps({
    "taskType": "TEXT_IMAGE",
    "textToImageParams": {
        "text": input_prompt,      
        "negativeText": "blurry, low quality"
    },
    "imageGenerationConfig": {
        "quality": "standard",
        "numberOfImages": 1,
        "height": 512,
        "width": 512,
        "cfgScale": 10,
        "seed": 0
    }
}))
    #print(response_bedrock)

    response_bedrock_byte = json.loads(response_bedrock['body'].read())
    print(response_bedrock_byte)

    image_base64 = response_bedrock_byte['images'][0]
    image_bytes = base64.b64decode(image_base64) 
    print(image_bytes)

    poster_name = 'posterName' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.png'  

    response_s3 = client_s3.put_object(
    Body=image_bytes,
    Bucket='designposter05',
    Key=poster_name,
    ContentType='image/png')

    generate_presigned_url = client_s3.generate_presigned_url('get_object',
    Params={'Bucket': 'designposter05', 'Key': poster_name},
    ExpiresIn=3600)
    print(generate_presigned_url)

    return {
        'statusCode': 200,
        'body': generate_presigned_url
    }
