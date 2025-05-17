"""
Authenticated base request handler.
"""

# Import hashing module.
import jwt

# Import Tornado web framework module.
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """
    A base request handler that provides common functionality for all authenticated request handlers.

    Properties:
        db (Database): Provides access to the MySQL database instance.
        config (dict): Provides access to the application configuration settings.

    Methods:
        initialize: Sets up common properties and settings for the handler.
        get_template_namespace: Retrieves the template namespace
                                with additional configuration settings.
    """

    @property
    def mysql(self):
        """
        Provides access to the MySQL database instance.

        Returns:
            Database: The database instance from the application.
        """
        return self.application.mysql

    @property
    def config(self):
        """
        Provides access to the application configuration settings.

        Returns:
            dict: The configuration settings of the application.
        """
        return self.application.config

    def prepare(self):
        token = self.get_signed_cookie("user")
        auth_service_url = self.config['app']['auth_microservice']['url']

        if not token:
            self.set_status(401)
            self.redirect(f"{auth_service_url}/login")
            return

        try:
            self.current_user = jwt.decode(token, self.config['app']['app_secret'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            self.clear_all_cookies(
                'user',
                httponly=True,
                secure=True,
                domain=self.config['app']['domain']
            )
            self.set_status(401)
            self.redirect(f"{auth_service_url}/login")
            return
        except jwt.InvalidTokenError:
            self.set_status(401)
            self.redirect(f"{auth_service_url}/login")
            return
        except Exception as e:
            print(e)

    def initialize(self):
        """
        Sets up common properties and settings for the handler.

        Returns:
            None: This method does not return a value.
        """
        self.vars = {}
        self.vars['title'] = self.config['app']['name']
        self.vars['notify'] = []
        self.vars['api_microservice_url'] = self.config['app']['api_microservice']['url']
        self.vars['auth_microservice_url'] = self.config['app']['auth_microservice']['url']
        self.vars['account_microservice_url'] = self.config['app']['account_microservice']['url']
        self.vars['chat_microservice_url'] = self.config['app']['chat_microservice']['url']
        self.vars['cdn_url'] = self.config['app']['cdn']['url']