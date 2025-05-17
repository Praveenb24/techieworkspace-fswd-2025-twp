"""
User request handler module.
"""

# Import the base handler class from custom modules.
from handlers.base import BaseHandler


class RootHandler(BaseHandler):
    """
    Handles requests to the root URL ("/") of the account service.

    The RootHandler is responsible for redirecting any requests to the root URL ("/")
    of the account service to the dashboard page ("/dashboard"). This ensures that users
    accessing the account service are immediately redirected to their dashboard, which is
    typically the main interface for account-related actions.

    Methods:
        get: Processes GET requests to the root URL and redirects to the dashboard page.
    """

    def get(self):
        """
        Processes GET requests to the root URL ("/") of the account service.

        This method automatically redirects users to the dashboard page ("/dashboard").
        It does not return any content directly but issues an HTTP 302 redirect.

        Returns:
            None: This method does not return a value.
        """
        self.redirect("/dashboard", permanent=False)


class DashboardHandler(BaseHandler):
    """
    Handler for managing routes related to the home page.

    Methods:
        get: Processes GET requests to render the home page.
    """

    def get(self):
        """
        Processes GET requests to the home route and renders the home page.

        Returns:
            None: This method does not return a value 
                  but renders the 'home.html' template.
        """
        self.vars['title'] = f"Dashboard - {self.config['app']['name']}"
        self.render('dashboard.html', **self.vars)
