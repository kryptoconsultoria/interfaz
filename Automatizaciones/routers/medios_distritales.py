# books/medios_distritales.py
class MediosdistritalesRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'medios_distritales':
            return 'medios_distritales_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'medios_distritales':
            return 'medios_distritales_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'medios_distritales':
            return 'medios_distritales_db'
        return True