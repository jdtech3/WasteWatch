function displayText() {
    // Get the user input
    const userInput = document.getElementById("userInput").value;

    // Check if the input is not empty
    if (userInput.trim() !== "") {
        // Create a new element to display the text
        const outputDiv = document.getElementById("output");
        const newText = document.createElement("p");
        newText.textContent = `Starting equipment count for  ${userInput}...`;

        // Append the new element to the output div
        outputDiv.appendChild(newText);

        // Clear the input field
        document.getElementById("userInput").value = "";

        // Fetch the graph image from the Python server
        fetch('/get_graph_image')
            .then(response => response.blob())
            .then(data => {
                // Create an <img> element and set its src attribute to the retrieved image data
                const imgElement = document.createElement('img');
                imgElement.src = URL.createObjectURL(data);

                // Append the <img> element to a container div on your webpage
                const containerDiv = document.getElementById('graphContainer');
                containerDiv.appendChild(imgElement);
            })
            .catch(error => console.error(error));

    }




}
