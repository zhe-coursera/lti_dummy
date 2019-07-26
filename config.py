"""
Configuration file for flask sample application
"""
import os

# enable CSRF
WTF_CSRF_ENABLED = True

# secret key for authentication
SECRET_KEY = "you-will-never-guess"

PYLTI_CONFIG = {
    "consumers": {
        "__consumer_key__": {
            "secret": "__lti_secret__",
        }
    }
}