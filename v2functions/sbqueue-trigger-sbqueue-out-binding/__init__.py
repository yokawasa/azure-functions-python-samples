import logging
import azure.functions as func

def main(msgIn: func.ServiceBusMessage, msgOut: func.Out[str]):
    body = msgIn.get_body().decode('utf-8')
    logging.info(f'Processed Service Bus Queue message: {body}')
    msgOut.set(body)
