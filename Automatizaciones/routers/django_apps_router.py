class DjangoAppsRouter:
    """
    Envía lecturas, escrituras y migraciones de las apps internas de Django
    a 'admin_db', y deja el resto en 'default'.
    """
    DJANGO_APPS = {
        'admin',
        'auth',
        'contenttypes',
        'sessions',
        'messages',
        'static_files',
        'panel_principal'
    }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.DJANGO_APPS:
            return 'admin_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.DJANGO_APPS:
            return 'admin_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permite relaciones entre objetos aunque estén en bases de datos diferentes.
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.DJANGO_APPS:
            return db == 'admin_db'
        return db == 'default'