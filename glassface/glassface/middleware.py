from django.contrib.auth import authenticate, login

class AuthMiddleware( object ):
    """Authentication Middleware for OpenAM using a cookie with a token.
    Backend will get user.
    """
    def process_request(self, request):
        if "post_username" not in request.POST:
            return
        user = authenticate(remote_user=request.POST["post_username"])
        request.user = user
        login(request, user)
