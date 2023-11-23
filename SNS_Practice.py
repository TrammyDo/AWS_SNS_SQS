import boto3
import json

def createTopic (sns, topicName):
  return sns.create_topic (
    Name = topicName
  )

def addSubscriber (sns, email):
  sns.subscribe (
    TopicArn = 'arn:aws:sns:us-east-1:951039571551:ExampleTopic',
    Protocol = 'email',
    Endpoint = email
  )

def sendMessageToSNS (sns, message):
  response = sns.publish (
    TopicArn = 'arn:aws:sns:us-east-1:951039571551:Test',
    Message = message
  )
  
def createQueue (sqs, queueName):
  return sqs.create_queue(
    QueueName=queueName, 
    Attributes={'DelaySeconds': '5'}
  )

sns = boto3.client('sns')
sqs = boto3.resource('sqs')

# topic = createTopic (sns, 'Test')
queue = createQueue(sqs, 'queue')

# sns.subscribe (
#   TopicArn = 'arn:aws:sns:us-east-1:951039571551:Test',
#   Protocol="sqs",
#   Endpoint=queue.attributes["QueueArn"]
# )

# sendMessageToSNS (sns, "my queue works :)")

sqsClient = boto3.client ('sqs')
queueUrl = sqsClient.get_queue_url (
  QueueName = "queue"
)

messages = sqsClient.receive_message (
  QueueUrl = queueUrl['QueueUrl'],
  MaxNumberOfMessages = 1
)
print (messages)
message_body = messages["Messages"][0]["Body"]
print (message_body)