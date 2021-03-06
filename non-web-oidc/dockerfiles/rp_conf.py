# If BASE is https these has to be specified
SERVER_CERT = "certs/server.crt"
SERVER_KEY = "certs/server.key"
CA_BUNDLE = None

VERIFY_SSL = False

# information used when registering the client
ME = {
    "application_type": "web",
    "redirect_uris": ["{base}authz_cb"],
    "response_types": ["code"]
}

PAM_DATABASE = "pam.db"

BEHAVIOUR = {
    "response_type": "code",
    "scope": ["openid", "auth_test"],
}

CLIENTS = {
    "": {
        "client_info": ME,
        "behaviour": BEHAVIOUR
    }
}