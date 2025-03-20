import json
from idt_scrapper.main import startup

scraper=startup()
scraper.update_influencers()

def lambda_handler(event, context):
    # EventBridge Trigger (Scheduled)
    if "source" in event and event["source"] == "aws.events":
        print("Triggered by EventBridge (Scheduled Event)")
        return {"statusCode": 200, "body": json.dumps("Scheduled task completed.")}

    # SQS Trigger
    if "Records" in event:
        print("Triggered by SQS")
        for record in event["Records"]:
            message_body = record["body"]
            print(f"Processing SQS Message: {message_body}")
        return {"statusCode": 200, "body": json.dumps("SQS messages processed.")}

    return {"statusCode": 400, "body": json.dumps("Unknown trigger source")}
