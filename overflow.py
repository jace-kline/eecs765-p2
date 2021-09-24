
def output_request(buffer):
    request = "GET /weblogic/ " + buffer + "\r\n\r\n"
    print(request)

def sendAs():
    output_request("A"*5000)

def sendPatternCreate():
    with open('pattern_create.txt', 'r') as f:
        pattern = f.read()
        output_request(pattern)

if __name__ == "__main__":
    sendPatternCreate()