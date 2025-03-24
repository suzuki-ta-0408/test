"""
CodeGuru Lambdaコードスキャン検証のためのダミーシークレット情報
"""
API_KEY = "SECRET-KEY-1234" 
PASSWORD = "password_2025!"
aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"
aws_secret_access_key = "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"
aws_secret_access_key = "Gi3RU8Qo9CGUsDTnMcASiQW2PtoqJoJbgiFksaD1"
aws_secret_access_key = "Gi3RU8Qo9CGUsDTnMcASiQW2PtoqJoJb4GtugoaD"
test = "EC2InstancePassword"

def lambda_handler(event, context):
    """
    codeguru で検知されるかを試すテスト用のコード
    """
    print(API_KEY)
    return