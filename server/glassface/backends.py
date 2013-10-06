class Backend:
    def authenticate(**credentials):
        """We could authenticate the token by checking with OpenAM
        Server.  We don't do that here, instead we trust the middleware to do it.
        """
        try:
            user= User.objects.get(username=credentials['remote_user'])
            return user
        except:
            return False