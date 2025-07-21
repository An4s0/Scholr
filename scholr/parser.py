from bs4 import BeautifulSoup

def parse_scholar_profile(html: str) -> dict:
    soup = BeautifulSoup(html, 'html.parser')
    
    profile_info = {}

     # Extracting the name
    name_tag = soup.find('div', id='gsc_prf_in')
    if name_tag:
        profile_info['name'] = name_tag.text.strip()
    else:
        print("Profile not found")
        exit(1)

    # Extracting the affiliation
    affiliation_tag = soup.find('div', class_='gsc_prf_il')
    if affiliation_tag:
        profile_info['affiliation'] = affiliation_tag.text.strip()

    # Extracting the research interests
    interests = [a.text for a in soup.select('#gsc_prf_int a')]
    profile_info['interests'] = interests

    # Extracting the profile image URL
    img_tag = soup.find('img', id='gsc_prf_pup-img')
    if img_tag and img_tag.get('src'):
        profile_info['photo_url'] = img_tag['src']

    # Extracting statistics
    stats = soup.select('table#gsc_rsb_st td.gsc_rsb_std')
    if len(stats) >= 6:
        profile_info['citations_all'] = stats[0].text
        profile_info['citations_since_2019'] = stats[1].text
        profile_info['h_index_all'] = stats[2].text
        profile_info['h_index_since_2019'] = stats[3].text
        profile_info['i10_index_all'] = stats[4].text
        profile_info['i10_index_since_2019'] = stats[5].text

    return profile_info