from django.apps import AppConfig


class YoutubeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'youtubeApp'

    def ready(self):
        from rooms import updater
        updater.start()
    