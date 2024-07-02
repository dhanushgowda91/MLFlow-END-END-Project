from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"
try:
    logger.info(f">>>>>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<<<<<")
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> STAGE { STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "DATA VALIDATION STAGE"
try:
    logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<")
    obj= DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage { STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)
    raise e
    