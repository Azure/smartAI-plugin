import time
import logging
from os import environ

from .azureblob import AzureBlob
from .azuretable import AzureTable

logger = logging.getLogger(__name__)

thumbprint = str(time.time())

def init_monitor(config): 
    azure_table = AzureTable(environ.get('AZURE_STORAGE_ACCOUNT'), environ.get('AZURE_STORAGE_ACCOUNT_KEY'))
    if not azure_table.exists_table(config.az_tsana_moniter_table):
        azure_table.create_table(config.az_tsana_moniter_table)
    tk = time.time()
    azure_table.insert_or_replace_entity(config.az_tsana_moniter_table, config.tsana_app_name, 
                        thumbprint, 
                        ping = tk)

def run_monitor(config): 
    azure_table = AzureTable(environ.get('AZURE_STORAGE_ACCOUNT'), environ.get('AZURE_STORAGE_ACCOUNT_KEY'))
    if not azure_table.exists_table(config.az_tsana_moniter_table):
        return

    tk = time.time()
    azure_table.insert_or_replace_entity(config.az_tsana_moniter_table, config.tsana_app_name, 
                        thumbprint, 
                        ping = tk)    

def stop_monitor(config):
    logger.info('Monitor exit! ')

    try: 
        azure_table = AzureTable(environ.get('AZURE_STORAGE_ACCOUNT'), environ.get('AZURE_STORAGE_ACCOUNT_KEY'))
        if not azure_table.exists_table(config.az_tsana_moniter_table):
            return
        azure_table.delete_entity(config.az_tsana_moniter_table, config.tsana_app_name, 
                            thumbprint)       
    except:
        pass