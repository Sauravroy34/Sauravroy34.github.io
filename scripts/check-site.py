#!/usr/bin/env python3
"""Check generated internal links and the site's required crawl signals."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


SITE_ORIGIN = "https://Sauravroy34.github.io"
REQUIRED_SITEMAP_URLS = {
    f"{SITE_ORIGIN}/about/",
    f"{SITE_ORIGIN}/posts/molecular-graphs-vs-smiles-chemistry-ai/",
    f"{SITE_ORIGIN}/research/",
}
REQUIRED_REDIRECT = Path("posts/diffusion_based_poem_genrator/index.html")
REDIRECT_TARGET = f"{SITE_ORIGIN}/posts/diffusion-based-poem-genrator/"
OBSOLETE_CVS = {
    Path("CV/CV_NEW.pdf"),
    Path("CV/CV_NEW_SAURAV.pdf"),
    Path("CV/Saurav_cv.pdf"),
    Path("CV/Saurav_updated_cv.pdf"),
}
URL_ATTRIBUTES = {
    "a": "href",
    "img": "src",
    "link": "href",
    "script": "src",
    "source": "src",
}


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attribute = URL_ATTRIBUTES.get(tag)
        if not attribute:
            return
        values = dict(attrs)
        value = values.get(attribute)
        if value:
            self.references.append(value)


def resolve_reference(site_root: Path, page: Path, reference: str) -> Path | None:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None

    path = unquote(parsed.path)
    if path.startswith("/"):
        candidate = site_root / path.lstrip("/")
    else:
        candidate = page.parent / path

    if path.endswith("/"):
        candidate /= "index.html"
    elif not candidate.suffix and not candidate.is_file():
        candidate /= "index.html"

    try:
        candidate.resolve().relative_to(site_root.resolve())
    except ValueError:
        return Path("__outside_site__")
    return candidate


def check_internal_links(site_root: Path) -> list[str]:
    failures: list[str] = []
    for page in sorted(site_root.rglob("*.html")):
        parser = ReferenceParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for reference in parser.references:
            target = resolve_reference(site_root, page, reference)
            if target is not None and not target.is_file():
                failures.append(
                    f"{page.relative_to(site_root)}: {reference} -> missing {target.relative_to(site_root) if target != Path('__outside_site__') else 'path outside site'}"
                )
    return failures


def check_sitemap(site_root: Path) -> list[str]:
    sitemap = site_root / "sitemap.xml"
    if not sitemap.is_file():
        return ["sitemap.xml is missing"]

    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = {
        element.text
        for element in ET.parse(sitemap).findall("sm:url/sm:loc", namespace)
        if element.text
    }
    missing = sorted(REQUIRED_SITEMAP_URLS - urls)
    return [f"sitemap.xml is missing required URL: {url}" for url in missing]


def check_redirect(site_root: Path) -> list[str]:
    redirect = site_root / REQUIRED_REDIRECT
    if not redirect.is_file():
        return [f"intentional redirect is missing: {REQUIRED_REDIRECT}"]

    content = redirect.read_text(encoding="utf-8").lower()
    failures = []
    if 'name=robots content="noindex"' not in content:
        failures.append(f"{REQUIRED_REDIRECT} is missing its noindex directive")
    if REDIRECT_TARGET.lower() not in content:
        failures.append(f"{REQUIRED_REDIRECT} does not point to {REDIRECT_TARGET}")
    return failures


def check_obsolete_files(site_root: Path) -> list[str]:
    return [
        f"obsolete generated file is still present: {path}"
        for path in sorted(OBSOLETE_CVS)
        if (site_root / path).exists()
    ]


def check_homepage_gateway(site_root: Path) -> list[str]:
    homepage = site_root / "index.html"
    if not homepage.is_file():
        return ["homepage is missing"]

    content = homepage.read_text(encoding="utf-8")
    requirements = {
        'AI in science, from code to evidence': "AI-in-science gateway heading",
        'class=home-primary href=/research/': "primary Research action",
        'href=/posts/olmo_learns_chemistry/': "OLMo entry point",
        'href=/posts/molgan/': "MolGAN entry point",
        'href=/posts/jwst-light-curve-and-planet-spectra/': "JWST entry point",
        'id=home-latest-title': "latest-notes section",
    }
    return [
        f"homepage is missing {label}"
        for marker, label in requirements.items()
        if marker not in content
    ]


def check_chemistry_entry_post(site_root: Path) -> list[str]:
    page = site_root / "posts/molecular-graphs-vs-smiles-chemistry-ai/index.html"
    if not page.is_file():
        return ["chemistry-AI entry post is missing"]

    content = page.read_text(encoding="utf-8")
    requirements = {
        "Molecular Graphs vs SMILES": "focused page title",
        f'href={SITE_ORIGIN}/posts/molecular-graphs-vs-smiles-chemistry-ai/': "self-canonical URL",
        'name=ROBOTS content="INDEX, FOLLOW"': "index, follow directive",
        'href=/posts/molgan/': "MolGAN internal link",
        'href=/posts/olmo_learns_chemistry/': "OLMo internal link",
        'href=/research/': "Research internal link",
        'class=entry-primary': "primary Research action",
    }
    return [
        f"chemistry-AI entry post is missing {label}"
        for marker, label in requirements.items()
        if marker not in content
    ]


def main() -> int:
    site_root = Path(sys.argv[1] if len(sys.argv) > 1 else "docs").resolve()
    if not site_root.is_dir():
        print(f"site directory does not exist: {site_root}", file=sys.stderr)
        return 2

    failures = [
        *check_internal_links(site_root),
        *check_sitemap(site_root),
        *check_redirect(site_root),
        *check_obsolete_files(site_root),
        *check_homepage_gateway(site_root),
        *check_chemistry_entry_post(site_root),
    ]
    if failures:
        print("Site checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    html_count = len(list(site_root.rglob("*.html")))
    print(f"Site checks passed for {html_count} generated HTML pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
