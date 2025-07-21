from django.apps import AppConfig


class PanelPrincipalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'panel_principal'

    def ready(self):
        import panel_principal.signals
