import boto3
import boto
from boto.mturk.question import ExternalQuestion
from boto.mturk.price import Price
import settings

region_name = 'us-east-1'
endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

# Uncomment this line to use in production
# endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'

client = boto3.client('mturk',
        endpoint_url = endpoint_url,
        region_name = region_name,
        aws_access_key_id = settings.aws_access_key_id,
        aws_secret_access_key = settings.aws_secret_access_key,
        )

#5 cents per HIT
amount = "0.05"

#frame_height in pixels
frame_height = 800

#qualifications = Qualifications()
#qualifications.add(PercentAssignmentsApprovedRequirement(comparator="GreaterThan", integer_value="90"))
#qualifications.add(NumberHitsApprovedRequirement(comparator="GreaterThan", integer_value="100"))

questionform = ExternalQuestion(settings.url, frame_height).get_as_xml()

create_hit_result = client.create_hit(
        Title="Insert the title of your HIT",
        Description="Insert your description here",
        Keywords="add, some, keywords",
        AssignmentDurationInSeconds = 60*60,
        MaxAssignments=15,
        Question=questionform,
        Reward=amount,
        LifetimeInSeconds = 60*60
        )
