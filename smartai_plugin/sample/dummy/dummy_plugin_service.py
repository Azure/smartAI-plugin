import os
import json
from flask import jsonify, make_response
import uuid
from common.plugin_service import PluginService
from common.util.timeutil import get_time_offset, str_to_dt, dt_to_str, get_time_list

class DummyPluginService(PluginService):

    def __init__(self):
        super().__init__()

    def do_train(self, subscription, model_id, model_dir, parameters):
        series = self.tsanaclient.get_timeseries(parameters['apiEndpoint'], parameters['apiKey'], parameters['seriesSets'], str_to_dt(parameters['startTime']), str_to_dt(parameters['endTime']), 0, 100, parameters['fieldsFilter'])
        return "SUCCESS", ''