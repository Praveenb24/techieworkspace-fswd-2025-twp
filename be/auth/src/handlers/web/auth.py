"""
Authentication request handlers.
"""

# Import the base handler from custom modules.
from handlers.base import BaseHandler

# Import custom module.
from utils.form import validate
from utils.exception import ValidationError
from models.employee import EmployeeModel

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
        try:
            # Step 1: Collect user data.
            user_data = {
                'name': self.get_argument("name"),
                'email': self.get_argument("email"),
                'phone': self.get_argument("phone"),
                'username': self.get_argument("username"),
                'password': self.get_argument("password")
            }

            # Step 2: Validate user data.
            is_valid, errors = validate(user_data)
            if not is_valid:
                raise ValueError(errors)

            # Step 3: Instantiate employee model and verify whether given username is exist.
            user = EmployeeModel()
            if user.read_by_username(user_data['username']):
                raise ValidationError("Username already exists.")

            self.vars['notify'] = [
                {"status": "Success", "message": "Account created successfully."}
            ]
            self.render('signup.html', **self.vars)
        except ValueError as ve:
            for e in ve.args[0].items():
                self.vars['notify'].append({'status':'Error','message':f'{e[0].upper()}: {e[1]}'})
            self.render('signup.html', **self.vars)
        except ValidationError as ve:
            self.vars['notify'].append({'status':'Error','message':ve})
            self.render('signup.html', **self.vars)
        except Exception as e:
            print(e)
            self.vars['notify'] = [{'status':'Error','message':'Internal server error.'}]
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
        self.vars['title'] = f"Login your account - {self.config['app']['name']}"
        try:
            # Step 1: Collect user data.
            user_data = {
                'username': self.get_argument("username"),
                'password': self.get_argument("password")
            }

            # Step 2: Validate user data.
            is_valid, errors = validate(user_data)
            if not is_valid:
                raise ValueError(errors)

            # Step 3: Instantiate user model and fetch existing user data for given username.
            user = EmployeeModel()
            existing_user_data = user.read_by_username(user_data['username'])
            if not existing_user_data:
                raise ValidationError("Invalid credentials.")

            account_microservice_url = self.config['app']['account_microservice']['url']
            self.redirect(f"{account_microservice_url}/dashboard", permanent=False)
        except ValueError as ve:
            for e in ve.args[0].items():
                self.vars['notify'].append({'status':'Error','message':f'{e[0].upper()}: {e[1]}'})
            self.render('login.html', **self.vars)
        except ValidationError as ve:
            self.vars['notify'].append({'status':'Error','message':ve})
            self.render('login.html', **self.vars)
        except Exception as e:
            print(e)
            self.vars['notify'] = [
                {'status':'Error','message':'Internal server error.'}
            ]
            self.render('login.html', **self.vars)


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