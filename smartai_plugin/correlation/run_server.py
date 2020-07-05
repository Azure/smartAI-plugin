from os import environ
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

from .correlation_plugin_service import CorrelationPluginService
from smartai_plugin.common.plugin_model_api import api, PluginModelAPI, PluginModelListAPI, PluginModelTrainAPI, \
    PluginModelInferenceAPI, app, PluginModelParameterAPI

correlation = CorrelationPluginService()

api.add_resource(PluginModelListAPI(correlation), '/correlation/models')
api.add_resource(PluginModelAPI(correlation), '/correlation/model', '/correlation/model/<model_key>')
api.add_resource(PluginModelTrainAPI(correlation), '/correlation/<model_key>/train')
api.add_resource(PluginModelInferenceAPI(correlation), '/correlation/<model_key>/inference')
api.add_resource(PluginModelParameterAPI(correlation), '/correlation/parameters')

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    PORT = environ.get('SERVER_PORT', 56789)
    app.run(HOST, PORT, threaded=True, use_reloader=False)

