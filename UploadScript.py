import boto3
import pandas as pd
import os

# 配置参数
ACCESS_KEY = 'xxx'
SECRET_KEY = 'xxx'
REGION = 'us-east-1'
TABLE_NAME = 'GenAI-AssetDemo-Database'

# 初始化 DynamoDB 客户端
dynamodb = boto3.resource('dynamodb', 
                          region_name=REGION, 
                          aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
table = dynamodb.Table(TABLE_NAME)


# 删除表中所有Items
t = 0
response = table.scan()
items = response['Items']
for item in items:
    print("Deleting item:", item['AssetID'])
    table.delete_item(
        Key={'AssetID': item['AssetID']} 
    )
    t += 1
print(f"{t} items deleted.")

# 读取数据文件
def read_file(filepath):
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        return pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file type")

# 在这里修改数据文件
FILEPATH = os.environ.get("FILE_PATH")
df = read_file(FILEPATH)
items = df.to_dict(orient='records')

# 上传至DynamoDB
t = 0
for item in items:
    print("Uploading item:", item['AssetID'])
    table.put_item(Item=item)
    t += 1
print(f"{t} items inserted.")


''''
t = 0
with open('AgentDemosData.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # 插入每一行数据到 DynamoDB 表
        table.put_item(Item=row)
        print(row)
        t += 1
print(f"{t} items inserted.")
'''
