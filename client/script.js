/**
 * Fetches all events from the Flask backend and
 * displays them in the All Events list.
 */
async function getEvents() {
    // Fetch all events from the Flask backend
    const response = await fetch("http://127.0.0.1:5000/events");
    const events = await response.json();

    // Select the event list from the HTML
    const eventList = document.getElementById("event-list");

    // Clear the current list before rebuilding it
    eventList.innerHTML = "";

    // Create and display a list item for each event
    events.forEach((event) => {
        const listItem = document.createElement("li");
        listItem.textContent = event.title;
        eventList.append(listItem);
    });
}

// Select the event form
const form = document.querySelector("form");


/**
 * Handles submission of the Add an Event form.
 * Sends the new event to the Flask backend and
 * refreshes the event list after it is created.
 */
form.addEventListener("submit", async (event) => {
    // Prevent the default form submission and page refresh
    event.preventDefault();

    // Retrieve the event title entered by the user
    const titleInput = document.getElementById("title");
    const title = titleInput.value;

    // Send the new event to the Flask backend
    const response = await fetch("http://127.0.0.1:5000/events", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title
        })
    });

    // Convert the response from JSON
    const newEvent = await response.json();

    // Refresh the list to display the newly created event
    await getEvents();

    // Clear the submit input field
    titleInput.value = "";
});


// Load all existing events when the page opens
getEvents();