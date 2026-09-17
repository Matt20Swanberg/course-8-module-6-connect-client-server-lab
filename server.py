from flask import Flask, jsonify, request
from flask_cors import CORS

from data import event_list

# Create the Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing so the frontend
# can communicate with the Flask backend
CORS(app)

@app.route("/")
def welcome():
    """
    Return a welcome message for the API.

    Returns:
        Response: A JSON response containing a success status
        and welcome message.
    """
    return jsonify({
        "status": "success",
        "message":"Welcome to my lab"
        }), 200


@app.route("/events", methods=["GET"])
def get_data():
    """
    Return all events in the event catalog.

    Returns:
        Response: A JSON list containing all available events
        with a 200 OK status code.
    """
    return jsonify(event_list), 200


@app.route("/events", methods=["POST"])
def create_event():
    """
    Create and add a new event to the event catalog.

    The request must include a title. A unique ID is automatically
    generated based on the highest existing event ID.

    Returns:
        Response: The newly created event with a 201 Created
        status code.

        Response: An error message with a 400 Bad Request status
        code if the title is missing.
    """

    # Retrieve the JSON data sent with the request   
    new_event = request.get_json()

    # Validate that the required title field was provided
    if "title" not in new_event:
        return jsonify({"error": "Title not found"}), 400

    # Generate a unique ID by finding the highest existing ID
    # and incrementing it by one
    new_id = max(event["id"] for event in event_list) +  1

    # Add the generated ID to the new event
    new_event["id"] = new_id

    # Add the new event to the event list
    event_list.append(new_event)

    # Return the newly created event
    return jsonify(new_event), 201

if __name__ == "__main__":
    # Run the Flask development server with debug mode enabled
    app.run(debug=True)
