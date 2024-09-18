// Fetch the initial state of the button when the page loads
window.onload = function() {
    fetch('/get_button_state')
        .then(response => response.json())
        .then(data => {
            document.getElementById('currentState').innerText = data.state === 1 ? 'ON' : 'OFF';
        });
};

// Toggle the button state when the button is clicked
function toggleButtonState() {
    fetch('/toggle_button', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('currentState').innerText = data.new_state === 1 ? 'ON' : 'OFF';
    });
}
