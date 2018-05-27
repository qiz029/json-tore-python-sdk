from jtSDK.jtClient import client

client = client()
print("status is: {0}".format(client.jt_status()))
data = {"message": "i like to eat chicken",
        "date": "05-26-2018"}
print("create index status is: {0}".format(client.create_index(1, data)))
print(client.get_index(1))
print("delete index status is: {0}".format(client.delete_index(1)))
