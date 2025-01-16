import boto3
import re
import json

def get_bedrock_client():
    return boto3.client(
        service_name='bedrock-runtime',
        region_name='us-west-2'
    )

def llm_call(prompt: str, system_prompt: str = "") -> str:
    client = get_bedrock_client()
    
    try:
        messages = [{
            "role": "user",
            "content": [{"text": prompt}]
        }]
        
        system_messages = [system_prompt] if system_prompt else []
        
        response = client.converse(
            #modelId='us.anthropic.claude-3-5-sonnet-20241022-v2:0',  # Claude 3.5 Sonnet v2 (Cross-inference)
            modelId='anthropic.claude-3-sonnet-20240229-v1:0',        # Claude 3 Sonnet
            messages=messages,
            system=system_messages,
            inferenceConfig={
                "temperature": 0.1,
                "maxTokens": 4096,
                "topP": 1
            }
        )
        
        output_message = response['output']['message']
        return output_message['content'][0]['text']
        
    except Exception as e:
        print(f"Error in llm_call: {str(e)}")
        raise

def extract_xml(text: str, tag: str) -> str:
    """Extract content from XML-like tags in text."""
    match = re.search(f'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
    return match.group(1) if match else ""
