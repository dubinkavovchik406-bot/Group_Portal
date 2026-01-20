import re
from django import template

register = template.Library()

@register.filter
def is_video(file_url):
    return file_url.lower().endswith(('.mp4', '.mkv', '.webm', '.mov'))

@register.filter
def youtube_id(url):
    regex = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/|youtube\.com\/shorts\/)([a-zA-Z0-9_-]{11})'
    match = re.search(regex, url)
    return match.group(1) if match else None