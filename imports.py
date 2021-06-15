import discord
import time, datetime, random, os, math, string, sys

import asyncio
import traceback
import requests

from bs4 import BeautifulSoup

import json
import html

from googleapiclient.discovery import build

import re

import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


this_is_my_DEVELOPER_KEY = os.environ["DEVELOPER_KEY"]
