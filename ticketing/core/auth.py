# ./auth.py
from fastapi.security import OAuth2AuthorizationCodeBearer
from keycloak import KeycloakOpenID
from fastapi import Security, HTTPException, status, Depends
from pydantic import Json
from ticketing.core.custom_logger import EventellaLogger
import os

logger = EventellaLogger(__name__)

# This is just for fastapi docs
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=os.getenv('AUTHORIZATION_URL'),
    tokenUrl=os.getenv('TOKEN_URL')
)

# This actually does the auth checks
keycloak_openid = KeycloakOpenID(
    server_url=os.getenv('SERVER_URL'),
    client_id=os.getenv('CLIENT_ID'),
    realm_name=os.getenv('REALM_NAME'),
    client_secret_key=os.getenv('CLIENT_SECRET_KEY'),
    verify=True
)

async def get_idp_public_key():
    return (
        "-----BEGIN PUBLIC KEY-----\n"
        f"{keycloak_openid.public_key()}"
        "\n-----END PUBLIC KEY-----"
    )

async def get_auth(token: str = Security(oauth2_scheme)) -> Json:
    try:
        public_key = await get_idp_public_key()
        return keycloak_openid.decode_token(
            token,
            key= public_key,
            options={
                "verify_signature": True,
                "verify_aud": False,
                "exp": True
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
