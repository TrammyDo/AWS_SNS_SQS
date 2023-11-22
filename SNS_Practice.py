import boto3

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

topic = createTopic (sns, 'Test')
queue = createQueue(sqs, 'queue')

sns.subscribe (
  TopicArn = 'arn:aws:sns:us-east-1:951039571551:Test',
  Protocol="sqs",
  Endpoint=queue.attributes["QueueArn"]
)

sendMessageToSNS (sns, "my queue works :)")
