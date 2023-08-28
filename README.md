# FindandConnectUsersOnLinkedIn
A python script to automate finding people on LinkedIn associated with a certain domain and working in a specified location and to connect with them.

Steps to get API keys:
Create a LinkedIn Developer Account:

Go to the LinkedIn Developer portal: https://www.linkedin.com/developers/
1. Log in with your LinkedIn account or create one if you don't have an account.
2. Once logged in, click on the "My Apps" tab in the top navigation menu.
3. Click the "Create App" button.
4. Fill in the required details for your application, including the name, description, logo, and the business email associated with the app.
5. Specify the URLs where LinkedIn will redirect users after they grant access to your application. These URLs are used in the OAuth 2.0 authorization process.
6. Choose the permissions your application will require. This determines the scope of access you'll have to user data.
7. Review and accept LinkedIn's terms of use for developers.
8. Depending on the permissions you're requesting, LinkedIn might require you to submit your application for review. This is especially true if you're requesting access to sensitive user data.
9. Once your application is created, you'll be provided with an API Key (Client ID) and an API Secret Key (Client Secret). These are required to authenticate your application when making API requests.

Steps to use the script
1. Replace the ENTER-YOUR-CLIENT-ID ENTER-YOUR-CLIENT-SECRET with your Client Key and Client Secret.
2. Run python3 conn.py in your terminal
