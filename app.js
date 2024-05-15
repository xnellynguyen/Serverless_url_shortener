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
        const data = await response.json();

        if (response.ok) {
            responseElement.textContent = `Short URL: ${window.location.origin}/redirect/${data.shortUrl}`;
        } else {
            responseElement.textContent = 'Error creating short URL: ' + (data.error || 'Unknown error');
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
        const response = await fetch(`${apiBaseUrl}/redirect/${shortUrl}`, { redirect: 'follow' });

        if (response.redirected) {
            window.location.href = response.url;
        } else {
            const data = await response.json();
            responseElement.textContent = data.error || 'Error redirecting to original URL.';
        }
    } catch (error) {
        responseElement.textContent = 'Error redirecting to original URL. See console for details.';
        console.error('Error:', error);
    }
}
