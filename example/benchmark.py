from jtSDK.jtClient import client
import time

data = {"info": "this data is for the use of benchmarking",
        "message": "if possible, delete this when trying to use this database"}
client = client()

print("*************************************************************")
print("starting to do a performance testing on cloud based json-tore database")

# first try to write for 1000 times and record the times
total_time = 0
average_time = 0
for i in range(0, 1000):
    start = time.time()
    client.create_index(i, data)
    end = time.time()
    total_time += end - start

average_time = total_time / 1000
print("total time for writing data 1000 times is : {0} seconds".format(total_time))
print("average time for writing each times is : {0} seconds".format(average_time))

# then try to get for 1000 times
total_time = 0
average_time = 0
for i in range(0, 1000):
    start = time.time()
    client.get_index(i)
    end = time.time()
    total_time += end - start

average_time = total_time / 1000
print("total time for read data 1000 times is : {0} seconds".format(total_time))
print("average time for read each times is : {0} seconds".format(average_time))

# eventually delete for 1000 times
total_time = 0
average_time = 0
for i in range(0, 1000):
    start = time.time()
    client.delete_index(i)
    end = time.time()
    total_time += end - start

average_time = total_time / 1000
print("total time for delete data 1000 times is : {0} seconds".format(total_time))
print("average time for delete each times is : {0} seconds".format(average_time))

print("*************************************************************")
