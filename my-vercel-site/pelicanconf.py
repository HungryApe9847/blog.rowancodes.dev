AUTHOR = 'Rowan'
SITENAME = 'Blog.RowanCodes'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'En'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "pelican-themes/bootstrap2-dark"

# Blogroll
LINKS = (
    ("Main Site", "https://rowancodes.dev/"),
    ("First Game on Site", "https://rowancodes.dev/slimesurvivors"),
)

# Social widget
SOCIAL = (
    ("Me on Scratch", "https://scratch.mit.edu/users/X-Robotic/"),
)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/icon1.png': {'path': 'icon1.png'},
    'extra/nyan-cat.gif': {'path': 'nyan-cat.gif'},
}