from .utils import html_get
from .parser import parse_scholar_profile

GOOGLE_SCHOLAR_URL = "https://scholar.google.com"

def get_scholar_profile(profile: str) -> dict:
    if "scholar.google." not in profile:
        profile = f"{GOOGLE_SCHOLAR_URL}/citations?user={profile}"
    
    html = html_get(profile)
    profile_info = parse_scholar_profile(html)

    return profile_info