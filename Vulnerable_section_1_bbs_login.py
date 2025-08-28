 
 from core.template import UserTemplates
 from lib.common import session_member_key
from lib.dependency.dependencies import set_current_connect
 from lib.member import is_super_admin
 from lib.social import providers
 from lib.social.social import SocialProvider, oauth
 async def login(
         request: Request,
         member_service: Annotated[MemberService, Depends()],
         mb_id: str = Form(...),
         mb_password: str = Form(...),
         auto_login: bool = Form(default=False),
        url: str = Form(default="/")
 ):
     """로그인 폼화면에서 로그인"""
     member = member_service.authenticate_member(mb_id, mb_password)