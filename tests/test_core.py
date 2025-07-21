import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scholr import get_scholar_profile

profile_id = "your_profile_id_here"
profile_url = "your_profile_url_here"

def test_get_scholar_profile():
    profile = get_scholar_profile(profile_url)

    print("Profile basic information:")
    print(profile)

if __name__ == "__main__":
    test_get_scholar_profile()
