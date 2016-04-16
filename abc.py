import urllib2
import json 
import csv
import sys

def main():

    listoflists = []
    
    #exampleFile = open('WWW.csv')
    #exampleReader = csv.reader(exampleFile)
    #exampleData = list(sys.argv(1))
    #for row in exampleData:
    #    listoflists.append(row)
   
    
    #del listoflists[0]
    values = str(sys.argv[1])
    header=  str(sys.argv[2])
    #c = a.split(',', 1)
    #print(a)
    #print(b)


    # d = 'hello,world,deryl'
    # e = str(sys.argv[1])
    # print(str(sys.argv[1]))

    # print (type(e))
    # print(e.split(','))

    #print(listoflists)

    #print(values.split(','))
    #print(header.split(','))
    abc = []
    abc.append(values.split(','))
    #print(abc)

    data =  {

        "Inputs": {

                "Input1":
                {
                    "ColumnNames" : header.split(','),
                    "Values": abc #values.split(',')
                },        },
            "GlobalParameters": {
    }
        }


    # print(data)

    body = str.encode(json.dumps(data))

   # url = 'https://ussouthcentral.services.azureml.net/workspaces/607045d56e9b4577abd84aab779dc2eb/services/7027c367da5749e3afbf9be9df0f332b/execute?api-version=2.0&details=true'
    # api_key = 'fH6A1sYHRz5fWa8Q4iHEAZpjXi0uHmK+EIHi7kwwUYueWaLNqIaS/gcr+gqr3QuP3ICgTsIX+4VYH+9+K+ifKg==' # Replace this with the API key for the web service
    

    url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/25e8f06d5e7048bfa64f92cdb249c274/execute?api-version=2.0&details=true'
    api_key = 'fy4lM67b2VzYJzELzVqqG6zxoodR1OFfi60GbTRabIHaBZfRAJrO1OHhehHKfc8n/TyJnmLGKXQ2JenfPMQUJg=='

    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers) 
    # print(req)

    try:
        response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
        #print('Number of arguments:', len(sys.argv), 'arguments.')
      #  print 'Argument List:', str(sys.argv)
        #return result
        #print("Column Names")
        #print(json.loads(result)["Results"])
        # print(dict["Results"])
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))  
        #return json.loads(error.read())


if __name__ == "__main__":
    main()
    #print('MAIN KE ANDAR')
    
