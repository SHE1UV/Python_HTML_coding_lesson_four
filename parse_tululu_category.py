import os
import json
import pathlib
import argparse
from time import sleep

import requests
from urllib.parse import unquote, urljoin, urlsplit
from bs4 import BeautifulSoup

from tools import check_for_redirect,parse_book_page,download_txt,download_image
