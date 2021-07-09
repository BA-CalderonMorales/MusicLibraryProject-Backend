from django.apps import AppConfig


class MusicConfig(AppConfig):
    # name is overridden by 'api-overview' in music app url patterns
    name = 'music'
