import asyncio
import json
from typing import TYPE_CHECKING, ClassVar, Iterator, Optional
from urllib.parse import urlencode, quote, urlparse

from tiktok_api.api.hashtag_async import HashtagaSync


def generate_js_fetch(method: str, url: str, headers: dict) -> str:
    """Generate a javascript fetch function for use in playwright"""
    headers_js = json.dumps(headers)
    return f"""
        () => {{
            return new Promise((resolve, reject) => {{
                fetch('{url}', {{ method: '{method}', headers: {headers_js} }})
                    .then(response => response.text())
                    .then(data => resolve(data))
                    .catch(error => reject(error.message));
            }});
        }}
    """


class Hashtag:
    parent: ClassVar[HashtagaSync]

    id: Optional[str]
    """The ID of the hashtag"""
    name: Optional[str]
    """The name of the hashtag (omiting the #)"""
    as_dict: dict
    """The raw data associated with this hashtag."""

    def __init__(
            self,
            name: Optional[str] = None,
            data: Optional[dict] = None,
    ):
        """
        You must provide the name or id of the hashtag.
        """

        if name is not None:
            self.name = name

        if data is not None:
            self.as_dict = data
            self.__extract_from_data()

    def __extract_from_data(self):
        pass

    async def videos(self, count=30, cursor=0, **kwargs) -> Iterator:

        found = 0
        while found < count:
            params = {
                "challengeID": 1594201347146754,
                "count": 30,
                "cursor": 1,
            }
            params2 = {**self.parent.params, **params}
            resp = await self.make_request(
                url="https://www.tiktok.com/api/challenge/item_list/",
                params=params2,
                headers=self.parent.headers
            )

            for video in resp("itemList", []):
                yield video
                found += 1

            if not resp.get("hasMore", False):
                return

            cursor = resp.get("cursor")

    async def make_request(self, url, params, headers):
        encoded_params = f"{url}?{urlencode(params, safe='=', quote_via=quote)}"
        result = await self.run_fetch_script(encoded_params, headers=headers)

        try:
            data = json.loads(result)
            if data.get("status_code") != 0:
                return data
        except:
            await asyncio.sleep(1)

    async def sign_url(self, encoded_params, session_index):
        pass

    async def run_fetch_script(self, url: str, headers: dict, **kwargs):
        """
        Execute a javascript fetch function in a session

        Args:
            url (str): The url to fetch.
            headers (dict): The headers to use for the fetch.

        Returns:
            any: The result of the fetch. Seems to be a string or dict
        """
        js_script = generate_js_fetch("GET", url, headers)
        result = await self.parent.page.evaluate(js_script)
        return result

