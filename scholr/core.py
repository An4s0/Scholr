from .utils import html_get
from .parser import parse_scholar_profile

GOOGLE_SCHOLAR_URL = "https://scholar.google.com"

def get_scholar_profile(profile: str) -> dict:
    if "scholar.google." not in profile:
        profile = f"{GOOGLE_SCHOLAR_URL}/citations?user={profile}"

    profile_info = None
    all_pubs = []
    start = 0 

    while True:
        url = f"{profile}&cstart={start}&pagesize=100&hl=en&view_op=list_works"
        html = html_get(url)
        if not html or "Please show you're not a robot" in html:
            print("Blocked by Google Scholar or empty page")
            break

        page_info = parse_scholar_profile(html)

        if profile_info is None:
            profile_info = {k: v for k, v in page_info.items() if k != "publications"}

        pubs = page_info.get("publications", [])
        if len(pubs) == 1:
            break
        all_pubs.extend(pubs)
        start += 100

    profile_info["publications"] = all_pubs

    return profile_info