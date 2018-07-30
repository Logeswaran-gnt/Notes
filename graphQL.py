import graphene
class Query(graphene.ObjectType):
    hello = graphene.String(description='A typical hello world')
    my = graphene.String(description='A typo world')

    def resolve_hello(self, info):
        return ['aa','World']
    def resolve_my(self,info):
        return 'dear'

schema = graphene.Schema(query=Query)


query = '''
    query ss {
      my,hello
    }
'''
result = schema.execute(query)
print(dict(result.data))
