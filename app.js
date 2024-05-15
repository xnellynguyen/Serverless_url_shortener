// Your API base URL
const apiBaseUrl = 'https://ltpyck8rlb.execute-api.us-east-2.amazonaws.com/prod';

// Function to create a short URL
async function createShortUrl() {
    const longUrl = document.getElementById('longUrl').value;
    const responseElement = document.getElementById('shortUrlResult');

    if (!longUrl) {
        responseElement.textContent = 'Please enter a long URL.';
        return;
    }

    try {
        const response = await fetch(`${apiBaseUrl}/create?url=${encodeURIComponent(longUrl)}`);
        const resultText = await response.text();
        const data = JSON.parse(resultText);
        const responseBody = JSON.parse(data.body);

        if (response.ok) {
            const shortUrl = responseBody.shortUrl;
            if (shortUrl) {
                responseElement.textContent = `Short URL hash: ${shortUrl}`;
            } else {
                responseElement.textContent = 'Error: Short URL is undefined.';
            }
        } else {
            responseElement.textContent = 'Error creating short URL: ' + (data.error || 'Server responded with an error');
        }
    } catch (error) {
        responseElement.textContent = 'Error creating short URL. See console for details.';
        console.error('Error:', error);
    }
}

// Function to redirect to the original URL
async function redirectToOriginalUrl() {
    const shortUrl = document.getElementById('shortUrl').value;
    const responseElement = document.getElementById('redirectResult');

    if (!shortUrl) {
        responseElement.textContent = 'Please enter a short URL hash.';
        return;
    }

    try {
        const response = await fetch(`${apiBaseUrl}/redirect?url=${encodeURIComponent(shortUrl)}`);
        const resultText = await response.text();  // Get the response text
        const data = JSON.parse(resultText); // Parse the text into JSON
        const responseBody = JSON.parse(data.body);

        console.log('Extracted data:', responseBody);
        // Extract the location from the response body
        const location = responseBody.location;
        console.log('Extracted location:', location);

        if (response.status === 302 && location) {
            window.location.href = location;
        } else {
            responseElement.textContent = data.error || 'Error redirecting to original URL.';
        }
    } catch (error) {
        responseElement.textContent = 'Error redirecting to original URL. See console for details.';
        console.error('Error:', error);
    }
}
