from django.db.utils import ConnectionHandler

class InspectorConnectionHandler(ConnectionHandler):
    setting_name = 'INSPECTOR_DATABASES'