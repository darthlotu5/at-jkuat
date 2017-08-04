#! /usr/local/lib/python2.7
from flask import Flask
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

app = Flask(__name__)


@app.route("/sms")
def sms():
    # Specify your login credentials
    username = "Nyongesa"
    apikey   = '445c171832b1631a7570fd4961cea4e18fc7747cf4a8d80a12a85c79b04c38f6'
    
    # NOTE: If connecting to the sandbox, please use your sandbox login credentials
    # Specify the numbers that you want to send to in a comma-separated list
    # Please ensure you include the country code (+254 for Kenya)

    to= "+254703554404"

    # And of course we want our recipients to know what we really do

    message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
    
    # Create a new instance of our awesome gateway class
    
    # gateway = AfricasTalkingGateway(username, apikey)
    
    # NOTE: If connecting to the sandbox, please add the sandbox flag to the constructor:
    # *************************************************************************************
                # ****SANDBOX****
    gateway    = AfricasTalkingGateway(username, apikey, "sandbox");
    # **************************************************************************************
    # Any gateway errors will be captured by our custom Exception class below, 
    # so wrap the call in a try-catch block
    
    try:
        # Thats it, hit send and we'll take care of the rest.
        
        results = gateway.sendMessage(to, message)
        message = "Succes"
        for recipient in results:
            # status is either "Success" or "error message"
            print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                recipient['status'],
                                                                recipient['messageId'],
                                                                recipient['cost'])
                            
    except AfricasTalkingGatewayException, e:
        message = "Fail"
        print 'Encountered an error while sending: %s' % str(e)

    return message
if __name__ == '__main__':
    app.run(debug=True)