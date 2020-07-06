from requests import Request
from .correlation_plugin_service import CorrelationPluginService
from os import environ

if __name__ == '__main__':    

    environ['SERVICE_CONFIG_FILE'] = 'plugin_service/correlation/config/exp_stock_service_config.yaml'

    correlation_plugin = CorrelationPluginService()
    request = Request()
    request.data = r'{"groupId":"8e826a5d-1b01-4ff4-a699-38bea97e17de","seriesSets":[{"seriesSetId":"b643e346-6883-4764-84a5-e63a3788eec9","metricId":"dc5b66cf-6dd0-4c83-bb8f-d849e68a7660","dimensionFilter":{"ts_code":"600030.SH"},"seriesSetName":"Stock price_high","metricMeta":{"granularityName":"Daily","granularityAmount":0,"datafeedId":"29595b1c-531f-445c-adcf-b75b2ab93c34","metricName":"high","datafeedName":"Stock price","dataStartFrom":1105315200000}},{"seriesSetId":"0d4cce4d-f4d4-4cef-be87-dbd28062abfc","metricId":"3274f7e6-683b-4d92-b134-0c1186e416a1","dimensionFilter":{},"seriesSetName":"Stock price_change","metricMeta":{"granularityName":"Daily","granularityAmount":0,"datafeedId":"29595b1c-531f-445c-adcf-b75b2ab93c34","metricName":"change","datafeedName":"Stock price","dataStartFrom":1105315200000}}],"gran":{"granularityString":"Daily","customInSeconds":0},"instance":{"instanceName":"Correlation_Instance_1586447708033","instanceId":"528cbe52-cb6a-44c0-b388-580aba57f2f7","status":"Active","appId":"173276d9-a7ed-494b-9300-6dd1aa09f2c3","appName":"Correlation","appDisplayName":"Correlation","appType":"Internal","remoteModelKey":"","params":{"missingRatio":0.5,"target":{"filters":{"ts_code":"600030.SH"},"metricId":"dc5b66cf-6dd0-4c83-bb8f-d849e68a7660","name":"Stock price_high"},"waitInSeconds":60,"windowSize":28},"hookIds":[]},"startTime":"2020-03-18T00:00:00Z","endTime":"2020-03-18T00:00:00Z","modelId":""}'
    
    correlation_plugin.create(request)
    
    #correlation_plugin.update(request)
    
    #correlation_plugin.train(request, '11111')
    
    correlation_plugin.inference(request,'11111')