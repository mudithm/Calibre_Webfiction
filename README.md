RSS integration for various web fiction sites (RoyalRoad, ScribbleHub, WuxiaWorld) 

Very early stages, built from on code from [this gist](https://gist.github.com/GandaG/2114eae3e2b1bceab6b7473f20fd97b4) by [GandaG](https://gist.github.com/GandaG)

----

Use:
Insert a comma-separated list of the form `Title,rss url` following the format of royalroad_urls.txt (no space before/after the comma)

Insert the Local RSS Feeds.recipe as a news recipe in Calibre

you'll definitely have to change the hard-coded paths I used in the python files and in the recipe

---

If you want to add another source, you can modify the if/elif clauses containing the "children" assignment in rss_royalroad.py and determine which classes are assigned to the main "div" containing the content of each chapter for that site.

If you think you need to add some headers to the get requests, you can add them to the request statement in the same file