import azure.functions as func
import json
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Configure logging
        logging.basicConfig(level=logging.INFO)

        # Parse the request body as JSON
        data = req.get_json()

        # Access specific data from the parsed JSON
        ticket_id = data.get("ticket", {}).get("id")
        priority = data.get("ticket", {}).get("priority")
        status = data.get("ticket", {}).get("status")
        description = data.get("ticket", {}).get("description")
        comment = data.get("ticket", {}).get("comment")

        # Process the data or perform any desired actions
        result = f"Received ticket with ID: {ticket_id}, Priority: {priority}, Status: {status}, Description: {description}, Comment: {comment}"

        # Log the information
        logging.info(result)

        # Send a JSON response
        return func.HttpResponse(
            body=json.dumps({"result": result}),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        # Log any errors
        logging.error(f"Error: {e}")

        # Send an error response
        return func.HttpResponse(
            body=json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        )
