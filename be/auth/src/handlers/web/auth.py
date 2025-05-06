"""
Authentication request handlers.
"""

# Import the base handler from custom modules.
from handlers.base import BaseHandler


class RootHandler(BaseHandler):
    """
    Handles requests to the root URL ("/") of the application.

    The RootHandler is responsible for redirecting any requests to the root URL ("/")
    to the login page ("/login"). This ensures that users are directed to the appropriate
    entry point of the application, typically where authentication occurs.

    Methods:
        get: Processes GET requests to the root URL and redirects to the login page.
    """

    def get(self):
        """
        Processes GET requests to the root URL ("/").

        This method automatically redirects users to the login page ("/login").
        It does not return any content directly but issues an HTTP 302 redirect.

        Returns:
            None: This method does not return a value.
        """
        self.redirect("/login", permanent=False)


class SignupHandler(BaseHandler):
    """
    Handles routes related to user signup.

    Methods:
        get: Processes GET requests to render the signup page.
        post: Processes POST requests to handle user signup and redirect to the login page.
    """

    def get(self):
        """
        Processes GET requests to render the signup page.

        Returns:
            None: This method does not return a value but renders the 'signup.html' template.
        """
        self.vars['title'] = f"Create your account - {self.config['app']['name']}"
        self.render('signup.html', **self.vars)

    def post(self):
        """
        Processes POST requests to handle user signup.

        Returns:
            None: This method does not return a value but redirects to the '/login' route.
        """
        self.vars['title'] = f"Create your account - {self.config['app']['name']}"
        self.render('signup.html', **self.vars)


class LoginHandler(BaseHandler):
    """
    Handles routes related to user login.

    Methods:
        get: Processes GET requests to render the login page.
        post: Processes POST requests to handle user login and redirect to the home page.
    """

    def get(self):
        """
        Processes GET requests to render the login page.

        Returns:
            None: This method does not return a value but renders the 'login.html' template.
        """
        self.vars['title'] = f"Login your account - {self.config['app']['name']}"
        self.render('login.html',**self.vars)

    def post(self):
        """
        Processes POST requests to handle user login.

        Returns:
            None: This method does not return a value but redirects to the '/home' route.
        """
        account_microservice_url = self.config['app']['account_microservice']['url']
        self.redirect(f"{account_microservice_url}/dashboard", permanent=False)


class LogoutHandler(BaseHandler):
    """
    Handles routes related to user logout.

    Methods:
        get: Processes GET requests to handle user logout and redirect to the login page.
    """

    def get(self):
        """
        Processes GET requests to handle user logout.

        Returns:
            None: This method does not return a value but redirects to the '/login' route.
        """
        self.redirect("/login", permanent=False)