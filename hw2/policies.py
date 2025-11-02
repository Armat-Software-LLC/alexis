# Content Security Policy

CSP_POLICY_ALLOW = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline'; "
    "style-src 'self' 'unsafe-inline'; "
    "img-src 'self' data:; "
    "font-src 'self'; "
    "connect-src 'self' "
    "frame-ancestors 'none'; "
    "base-uri 'self'; "
    "form-action 'self'"
)

CSP_POLICY_DENY = (
    "default-src 'self'; "
    "script-src 'none'; "
    "style-src 'self' 'unsafe-inline'; "
    "img-src 'none'; "
    "font-src 'self'; "
    "connect-src 'self' "
    "frame-ancestors 'none'; "
    "base-uri 'self'; "
    "form-action 'self'"
)