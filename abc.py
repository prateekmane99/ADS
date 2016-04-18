import urllib2
import json 
import csv
import sys

def main():

    typee = sys.argv[1]

    if typee == "2":
        header = sys.argv[2]
        kopi = str(sys.argv[3])
        abc = []
        abc.append(kopi.split(','))
        header = header.split(',')
      

        data =  {

            "Inputs": {

                    "Input1":
                    {
                        "ColumnNames" : header,
                        "Values": abc #values.split(',')
                    },        },
                "GlobalParameters": {
        }
            }


        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/25e8f06d5e7048bfa64f92cdb249c274/execute?api-version=2.0&details=true'
        api_key = 'fy4lM67b2VzYJzELzVqqG6zxoodR1OFfi60GbTRabIHaBZfRAJrO1OHhehHKfc8n/TyJnmLGKXQ2JenfPMQUJg=='

        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib2.Request(url, body, headers) 

        try:
            response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

            result = response.read()
            print(result)
        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))  
    else:
        listoflists = []
        values = str(sys.argv[1])
        header=  str(sys.argv[2])
        abc = []
        abc.append(values.split(','))

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

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/8aba4c4d1e034b56941f1f916e884791/services/25e8f06d5e7048bfa64f92cdb249c274/execute?api-version=2.0&details=true'
        api_key = 'fy4lM67b2VzYJzELzVqqG6zxoodR1OFfi60GbTRabIHaBZfRAJrO1OHhehHKfc8n/TyJnmLGKXQ2JenfPMQUJg=='

        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib2.Request(url, body, headers) 

        try:
            response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

            result = response.read()
            print(result)
        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())

            print(json.loads(error.read()))  
        #return json.loads(error.read())


if __name__ == "__main__":
    main()
    #print('MAIN KE ANDAR')
    
