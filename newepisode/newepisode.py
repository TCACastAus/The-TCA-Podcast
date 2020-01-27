"""Add a new episode."""

import requests
from jinja2 import Template

"""
Items that need to be filled:
title: Episode 5 - The Newborns Strike Back
date: 2018-12-19 15:00:00 +1100
file_url: https://ia801504.us.archive.org/14/items/TCACastEpisode5/Episode%205.mp3
duration: 01.15.12
length: 153022020
synopsis: Longer information about the episode
"""

episode = input("Episode (5) ")
subtitle = input("Subtitle: (The Newborns Strike Back) ")
date = input("Date: (2018-12-19) ")
file_url = input("File URL ")
synopsis = input("Synopsis: ")
duration = input("Duration: (01.15.12) ")

# based on the url, we can get the size of the file
length = requests.head(file_url).headers["content-length"]

# load the template
with open("./podcast_post_template.md") as template_file:
    template_text = template_file.read()


template = Template(template_text)
rendered_template = template.render(
    title=f"Episode {episode} - {subtitle}",
    date=f"{date} 15:00:00 +1100",
    file_url=file_url,
    synopsis=synopsis,
    duration=duration,
    length=length,
)

with open(f"../_posts/{date}-episode-{episode}.md", "w") as output_file:
    output_file.write(rendered_template)
