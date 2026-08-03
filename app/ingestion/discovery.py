import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


class DocumentationDiscovery:
    """
    Discover documentation pages from a documentation website.
    """

    def __init__(self):
        self.visited = set()

    def discover(
        self,
        root_url: str,
        max_pages: int = 100
    ) -> list[str]:

        urls = []
        queue = [root_url]

        root_domain = urlparse(root_url).netloc

        while queue and len(urls) < max_pages:

            url = queue.pop(0)

            if url in self.visited:
                continue

            self.visited.add(url)

            try:

                response = requests.get(
                    url,
                    timeout=10
                )

                if response.status_code != 200:
                    continue

                urls.append(url)

                soup = BeautifulSoup(
                    response.text,
                    "html.parser"
                )

                for link in soup.find_all("a", href=True):

                    absolute = urljoin(
                        url,
                        link["href"]
                    )

                    parsed = urlparse(absolute)

                    if parsed.netloc != root_domain:
                        continue

                    absolute = absolute.split("#")[0]

                    if absolute not in self.visited:
                        queue.append(absolute)

            except Exception:
                pass

        return urls