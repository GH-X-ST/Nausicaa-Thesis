#!/usr/bin/env python3
"""Validate the Google Scholar-facing thesis landing page."""

from __future__ import print_function

import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


TITLE = "Viability-Guided Sim-to-Real Transfer for a Small Fixed-Wing Glider in Uncertain Indoor Updrafts"
PUBLIC_BASE = "https://gh-x-st.github.io/Nausicaa-Thesis/"
PDF_URL = (
    PUBLIC_BASE
    + "Viability-Guided%20Sim-to-Real%20Transfer%20for%20a%20Small%20Fixed-Wing%20Glider%20"
    + "in%20Uncertain%20Indoor%20Updrafts.pdf"
)
PUBLICATIONS_URL = PUBLIC_BASE + "publications.html"
REQUIRED_META = (
    "citation_title",
    "citation_author",
    "citation_publication_date",
    "citation_dissertation_institution",
    "citation_doi",
    "citation_pdf_url",
)


class ScholarHTMLParser(HTMLParser):
    def __init__(self):
      HTMLParser.__init__(self)
      self.has_html = False
      self.has_head = False
      self.has_body = False
      self.in_body = False
      self.in_h1 = False
      self.skip_depth = 0
      self.metas = {}
      self.h1_values = []
      self.h1_classes = []
      self._current_h1 = []
      self.body_text = []
      self.canonical = None
      self.has_script = False

    def handle_starttag(self, tag, attrs):
      tag = tag.lower()
      attrs_dict = dict((name.lower(), value) for name, value in attrs)

      if tag == "html":
        self.has_html = True
      elif tag == "head":
        self.has_head = True
      elif tag == "body":
        self.has_body = True
        self.in_body = True
      elif tag == "meta":
        name = attrs_dict.get("name")
        content = attrs_dict.get("content")
        if name and content is not None:
          self.metas[name.lower()] = content
      elif tag == "link":
        rel = attrs_dict.get("rel", "")
        if "canonical" in rel.lower().split():
          self.canonical = attrs_dict.get("href")

      if self.in_body and tag in ("script", "style", "noscript"):
        if tag == "script":
          self.has_script = True
        self.skip_depth += 1
      elif self.in_body and tag == "h1":
        self.in_h1 = True
        self._current_h1 = []
        self.h1_classes.append(attrs_dict.get("class", ""))

    def handle_endtag(self, tag):
      tag = tag.lower()
      if self.in_body and tag in ("script", "style", "noscript") and self.skip_depth:
        self.skip_depth -= 1
      elif self.in_body and tag == "h1" and self.in_h1:
        text = normalize_text(" ".join(self._current_h1))
        self.h1_values.append(text)
        self.in_h1 = False
        self._current_h1 = []
      elif tag == "body":
        self.in_body = False

    def handle_data(self, data):
      if self.in_body and not self.skip_depth:
        self.body_text.append(data)
        if self.in_h1:
          self._current_h1.append(data)


def normalize_text(value):
    return " ".join(value.split())


def fail(failures, message):
    failures.append(message)


def validate_index(repo_root, failures, warnings):
    index_path = repo_root / "index.html"
    if not index_path.exists():
      fail(failures, "index.html is missing")
      return

    html = index_path.read_text(encoding="utf-8")
    parser = ScholarHTMLParser()
    try:
      parser.feed(html)
    except Exception as exc:
      fail(failures, "index.html could not be parsed as HTML-ish content: {0}".format(exc))
      return

    if not parser.has_html:
      fail(failures, "index.html is missing an <html> element")
    if not parser.has_head:
      fail(failures, "index.html is missing a <head> element")
    if not parser.has_body:
      fail(failures, "index.html is missing a <body> element")

    for meta_name in REQUIRED_META:
      if meta_name not in parser.metas:
        fail(failures, "index.html is missing <meta name=\"{0}\">".format(meta_name))

    if parser.metas.get("citation_title") != TITLE:
      fail(failures, "citation_title does not match the exact thesis title")

    author = parser.metas.get("citation_author")
    if author not in ("Li, Hanchen", "Hanchen Li"):
      fail(failures, "citation_author must be exactly 'Li, Hanchen' or 'Hanchen Li'")
    elif author != "Li, Hanchen":
      warnings.append("citation_author is accepted, but 'Li, Hanchen' is preferred")

    if parser.metas.get("citation_publication_date") != "2026/06/30":
      fail(failures, "citation_publication_date must be 2026/06/30")

    citation_pdf_url = parser.metas.get("citation_pdf_url")
    if citation_pdf_url:
      parsed = urlparse(citation_pdf_url)
      base = urlparse(PUBLIC_BASE)

      if parsed.scheme != "https" or not parsed.netloc:
        fail(failures, "citation_pdf_url must be an absolute HTTPS URL")
      if parsed.scheme != base.scheme or parsed.netloc != base.netloc:
        fail(failures, "citation_pdf_url must use the same public host as index.html")
      if not parsed.path.startswith(base.path):
        fail(failures, "citation_pdf_url must be in the same public subdirectory as index.html")

      relative_pdf_path = unquote(parsed.path[len(base.path):]) if parsed.path.startswith(base.path) else ""
      if not relative_pdf_path or "/" in relative_pdf_path or "\\" in relative_pdf_path:
        fail(failures, "citation_pdf_url must point to a PDF file directly in the public thesis directory")
      else:
        local_pdf = repo_root / relative_pdf_path
        if not local_pdf.exists():
          fail(failures, "Local PDF referenced by citation_pdf_url does not exist: {0}".format(relative_pdf_path))
        else:
          size = local_pdf.stat().st_size
          if size > 5_000_000:
            if size <= 5 * 1024 * 1024:
              warnings.append(
                  "Scholar PDF is {0} bytes: above decimal 5,000,000 bytes but below 5 MiB; "
                  "Google Scholar states a 5 MB limit, so confirm after deployment.".format(size)
              )
            else:
              fail(failures, "Scholar PDF is {0} bytes, above the 5 MB limit".format(size))

    h1_values = [value for value in parser.h1_values if value]
    if h1_values != [TITLE]:
      fail(failures, "body must contain exactly one visible <h1> with the thesis title")
    if not parser.h1_classes or "citation_title" not in parser.h1_classes[0].split():
      fail(failures, "the visible <h1> should use class=\"citation_title\" for parser fallback")

    top_body = normalize_text(" ".join(parser.body_text))[:1500]
    if "Hanchen Li" not in top_body and "Li, Hanchen" not in top_body:
      fail(failures, "visible author text must appear near the top of the body")
    if "Abstract" not in top_body:
      fail(failures, "the visible abstract must begin near the top of the body")

    abstract_pos = html.find('id="abstract-heading"')
    downloads_pos = html.find('id="downloads-heading"')
    if abstract_pos == -1:
      fail(failures, "index.html is missing the visible Abstract heading")
    if downloads_pos == -1:
      fail(failures, "index.html is missing the visible Downloads heading")
    if abstract_pos != -1 and downloads_pos != -1 and abstract_pos > downloads_pos:
      fail(failures, "the visible abstract should appear before download links in the HTML source")
    if parser.has_script:
      fail(failures, "index.html should not use script tags for the Scholar landing page")


def validate_robots(repo_root, failures):
    robots_path = repo_root / "robots.txt"
    if not robots_path.exists():
      fail(failures, "robots.txt is missing")
      return

    lines = [line.strip() for line in robots_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    required = [
        "User-agent: Googlebot",
        "Allow: /",
        "User-agent: *",
        "Sitemap: https://gh-x-st.github.io/Nausicaa-Thesis/sitemap.xml",
    ]
    for line in required:
      if line not in lines:
        fail(failures, "robots.txt is missing separate line: {0}".format(line))

    for line in lines:
      if "User-agent:" in line and "Allow:" in line:
        fail(failures, "robots.txt must keep User-agent and Allow on separate lines")
      if "Allow:" in line and "Sitemap:" in line:
        fail(failures, "robots.txt must keep Allow and Sitemap on separate lines")


def validate_sitemap(repo_root, failures):
    sitemap_path = repo_root / "sitemap.xml"
    if not sitemap_path.exists():
      fail(failures, "sitemap.xml is missing")
      return

    try:
      root = ET.parse(str(sitemap_path)).getroot()
    except ET.ParseError as exc:
      fail(failures, "sitemap.xml is not valid XML: {0}".format(exc))
      return

    locs = set()
    for element in root.iter():
      if element.tag.rsplit("}", 1)[-1] == "loc" and element.text:
        locs.add(element.text.strip())

    for url in (PUBLIC_BASE, PUBLICATIONS_URL, PDF_URL):
      if url not in locs:
        fail(failures, "sitemap.xml is missing URL: {0}".format(url))


def main():
    repo_root = Path(__file__).resolve().parents[1]
    failures = []
    warnings = []

    validate_index(repo_root, failures, warnings)
    validate_robots(repo_root, failures)
    validate_sitemap(repo_root, failures)

    for warning in warnings:
      print("WARNING: {0}".format(warning))

    if failures:
      for failure in failures:
        print("FAIL: {0}".format(failure), file=sys.stderr)
      return 1

    print("Scholar page validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
