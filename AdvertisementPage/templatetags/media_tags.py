import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_media(adv):
    # 1. Сначала проверяем YouTube
    if adv.youtube_url:
        # Регулярное выражение для извлечения ID видео из любых ссылок YouTube
        regex = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/|youtube\.com\/shorts\/)([a-zA-Z0-9_-]{11})'
        match = re.search(regex, adv.youtube_url)
        if match:
            video_id = match.group(1)
            return mark_safe(f'''
                            <div class="video-wrapper">
                                <iframe 
                                    width="100%" 
                                    height="315" 
                                    src="https://www.youtube.com/embed/{video_id}" 
                                    frameborder="0" 
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                    allowfullscreen>
                                </iframe>
                            </div>
                            <div style="margin-top: 5px;">
                                <a href="https://www.youtube.com/watch?v={video_id}" target="_blank" style="font-size: 12px; color: #666; text-decoration: none;">
                                    🔗 Не відображається відео? Дивитися на YouTube
                                </a>
                            </div>
                        ''')
        else:
            return mark_safe(
                f'<a href="{adv.youtube_url}" target="_blank" class="btn btn-outline-primary">Переглянути на YouTube</a>')

    # 2. Если YouTube нет, работаем с файлом
    if adv.media:
        url = adv.media.url.lower()
        if url.endswith(('.mp4', '.mkv', '.webm')):
            return mark_safe(f'''
                <video width="100%" controls>
                    <source src="{adv.media.url}">
                </video>
            ''')
        elif url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
            return mark_safe(f'<img src="{adv.media.url}" style="max-width:100%; height:auto;">')
        else:
            return mark_safe(f'<a href="{adv.media.url}" class="btn">Завантажити файл</a>')

    return ""