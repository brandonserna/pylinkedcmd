import re
import validators

def actionable_id(identifier_string, return_resolver=True):
    if validators.url(identifier_string):
        if "/staff-profiles/" in identifier_string.lower():
            return {
                "url": identifier_string,
                "usgs_web_url": identifier_string
            }

    if validators.email(identifier_string):
        return {
            "email": identifier_string
        }

    identifiers = {
        "doi": {
            "pattern": r"10.\d{4,9}\/[\S]+$",
            "resolver": "https://doi.org/"
        },
        "orcid": {
            "pattern": r"\d{4}-\d{4}-\d{4}-\w{4}",
            "resolver": "https://orcid.org/"
        }
    }
    for k,v in identifiers.items():
        search = re.search(v["pattern"], identifier_string)
        if search:
            d_identifier = {
                k: search.group()
            }
            if return_resolver and v["resolver"] is not None:
                d_identifier["url"] = f"{v['resolver']}{search.group().upper()}"

            return d_identifier

    return 

def chunks(dict_list, chunk_size=1000):
    for i in range(0, len(dict_list), chunk_size):
        yield dict_list[i:i+chunk_size]