import re
from urllib.parse import urlparse
import tldextract


def extract_features(url):

    parsed = urlparse(url)

    extracted = tldextract.extract(url)

    domain = extracted.domain
    subdomain = extracted.subdomain
    suffix = extracted.suffix

    features = {}

    features["url_length"] = len(url)

    features["domain_length"] = len(domain)

    features["path_length"] = len(parsed.path)

    features["query_length"] = len(parsed.query)

    features["num_dots"] = url.count(".")

    features["num_hyphens"] = url.count("-")

    features["num_slashes"] = url.count("/")

    features["num_at"] = url.count("@")

    features["num_question"] = url.count("?")

    features["num_equals"] = url.count("=")

    features["num_percent"] = url.count("%")

    features["num_ampersand"] = url.count("&")

    features["has_https"] = int(parsed.scheme == "https")

    features["has_ip"] = int(
        re.search(
            r"^(?:\d{1,3}\.){3}\d{1,3}$",
            parsed.hostname or ""
        ) is not None
    )

    features["subdomain_count"] = (
        len(subdomain.split("."))
        if subdomain else 0
    )

    suspicious_words = [
        "login",
        "verify",
        "secure",
        "account",
        "update",
        "password",
        "bank",
        "confirm"
    ]

    features["suspicious_words"] = sum(
        word in url.lower()
        for word in suspicious_words
    )

    features["has_port"] = int(parsed.port is not None)

    return features
