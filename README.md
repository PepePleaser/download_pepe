<body>
    <h1>Pepe Images Downloader</h1>
    <p>This script fetches the latest 100 images that are at least 512x512 pixels for a given search query using the Google Search API, saves the image URLs to a JSON file, and downloads the images from the URLs to a specified directory.</p>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3.6 or higher</li>
        <li><code>google-api-python-client</code> package</li>
        <li><code>requests</code> package</li>
    </ul>
    <p>You can install the required packages using the following command:</p>
    <pre><code>pip install google-api-python-client requests</code></pre>
    <h2>Getting a Google Search API Key</h2>
    <p>To use the Google Search API, you need to obtain an API key and a custom search engine ID. Follow these steps:</p>
    <ol>
        <li>Go to the <a href="https://console.cloud.google.com/">Google Cloud Console</a>.</li>
        <li>Create a new project or select an existing one.</li>
        <li>Click on "Enable APIs and Services" and search for "Custom Search API".</li>
        <li>Click on "Enable" to enable the Custom Search API for your project.</li>
        <li>Click "Create credentials" and follow the instructions to create an API key.</li>
        <li>Copy your API key and save it for later use.</li>
    </ol>
    <p>Next, create a custom search engine:</p>
    <ol>
        <li>Go to the <a href="https://developers.google.com/custom-search/v1/introduction">Google Custom Search JSON API</a> page.</li>
        <li>Click "Get started" and follow the instructions to create a custom search engine.</li>
        <li>Make sure to enable "Image search" in the custom search engine settings.</li>
        <li>Copy your custom search engine ID (cx) and save it for later use.</li>
    </ol>
    <h2>Running the Code</h2>
    <ol>
        <li>Replace <code>'YOUR_GOOGLE_API_KEY'</code> and <code>'YOUR_CUSTOM_SEARCH_ENGINE_ID'</code> in the script with your actual API key and custom search engine ID.</li>
        <li>Set the search query and output directory in the <code>if __name__ == '__main__':</code> block:</li>
    </ol>
    <pre><code>query = 'your_search_query'
output_dir = 'output_directory'</code></pre>
    <p>Run the script:</p>
    <pre><code>python pepe.py</code></pre>
    <p>The script will fetch the latest 100 image URLs for the search query that are at least 512x512 pixels, save them to a JSON file called 'pepe.json', and download the images from the URLs to the specified output directory.</p>
</body>
</html>
