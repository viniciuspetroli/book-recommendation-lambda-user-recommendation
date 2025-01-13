class DynamoService:
    def __init__(self, session, table):
        self.client = session.client('dynamodb')
        self.table = table
    
    def get_item(self, key):
        response = self.client.get_item(TableName=self.table,Key=key)
        return response
    
    #Just a comment to push the code