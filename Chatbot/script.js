function sendMessage() {
  var userInput = document.getElementById("user-input").value;
  document.getElementById("conversation").innerHTML +=
    '<div class="bubble user-bubble">' +
    '<p class="message speech-right">' +
    userInput +
    "</p>" +
    "</div>";

  // Fetch request to Python backend
  fetch("http://localhost:5000/chatbot", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ input: userInput }),
  })
    .then((response) => response.json())
    .then((data) => {
      var botResponse = data.response;
      document.getElementById("conversation").innerHTML +=
        '<div class="response-bot">' +
        '<div class="bubble bot-bubble">' +
        '<p class="message speech-left">' +
        botResponse +
        "</p>" +
        "</div>" +
        "</div>";

      // Scroll to the bottom of the conversation div
      scrollToBottom();
    })
    .catch((error) => console.error("Error:", error));

  document.getElementById("user-input").value = "";
}

function scrollToBottom() {
  var conversationDiv = document.getElementById("conversation");
  conversationDiv.scrollTop = conversationDiv.scrollHeight;
}

// Listen for keydown event on the input field
document
  .getElementById("user-input")
  .addEventListener("keydown", function (event) {
    // Check if the pressed key is Enter (keyCode 13)
    if (event.keyCode === 13) {
      event.preventDefault(); // Prevent the default Enter key behavior (e.g., line break in the input field)
      sendMessage(); // Call the sendMessage function
    }
  });
