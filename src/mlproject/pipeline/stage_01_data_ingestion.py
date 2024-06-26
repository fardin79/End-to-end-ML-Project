from mlproject.config.configuration import ConfigurationManger
from mlproject.components.data_ingestion import DataIngestion
from mlproject import logger

STAGE_NAME="Data Ingestion stage"



class DataIngestionTraningPipeline:
    def __init__(self):
        pass
    def main(self):
        
        config=ConfigurationManger()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} start <<<<<<")
        obj=DataIngestionTraningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
                            