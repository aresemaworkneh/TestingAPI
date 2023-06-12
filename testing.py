import requests

# Define the base URL for the GitHub API
base_url = "https://api.github.com"

# Send a GET request to retrieve user data from the API
def test_get_request():
    endpoint = "/users/octocat"  # Replace "octocat" with a valid GitHub username
    url = base_url + endpoint
    response = requests.get(url)
    
    # Validate the response
    assert response.status_code == 200
    
    # Perform assertions on the retrieved data
    data = response.json()
    assert "id" in data  # Verify that the "id" field exists in the response
    assert data["login"] == "octocat"  # Verify the username

# Run the test function
test_get_request()
