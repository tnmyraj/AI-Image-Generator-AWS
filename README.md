This project uses **AWS Bedrock**, **Lambda**, **API Gateway**, and **S3** to create an AI-powered image generator.

### ⚙️ Workflow
1. User sends a text prompt via API Gateway.
2. Lambda calls **Amazon Titan Image Generator** through Bedrock.
3. The generated image is stored in S3.
4. A **pre-signed URL** is returned to the user.

### 🧩 Technologies
- AWS Lambda
- Amazon Bedrock (Titan Image Generator)
- Amazon S3
- AWS API Gateway
- Postman (for testing)

### 🧠 Key Learning
Explored serverless architecture and GenAI model integration on AWS.
