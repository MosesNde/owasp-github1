 from .group import Group
 from .identity import IdentityProvider
 
__version__ = '0.3.4'
 __all__ = ('Multipass', 'AuthProvider', 'IdentityProvider', 'AuthInfo', 'IdentityInfo', 'Group', 'MultipassException',
            'AuthenticationFailed', 'IdentityRetrievalFailed', 'GroupRetrievalFailed', 'NoSuchUser',
            'InvalidCredentials')