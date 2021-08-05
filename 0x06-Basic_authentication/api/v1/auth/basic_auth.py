#!/usr/bin/env python3
"""basic auth module"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic ") \
                and not authorization_header.endswith(" "):
            return None

        return "".join(list(authorization_header)[6:])
