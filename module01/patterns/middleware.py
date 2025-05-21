from django.http import HttpResponseForbidden

BLOCKED_IPS = {"192.168.1.10", "10.0.0.1"}  # Add your blocked IPs here

# client -> BlockIPMiddleware -> server


class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)
        if ip in BLOCKED_IPS:
            return HttpResponseForbidden("Your IP is blocked.")
        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

middlwares = [
    "BlockIPMiddleware",
]
