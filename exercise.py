import queue


q = queue.Queue()

def generate_request():
    request = 'request 1'
    q.put(request)
    print('Request genarated and added to queue')
    
def process_request():
    if q != None:
        request = q.get()
        print("Processing request:", request)
    else: 
        print('Queue is empty.First write make some request')
        
while True:
   
    generate_request()
    
    process_request()
    