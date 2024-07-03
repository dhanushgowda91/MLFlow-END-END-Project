from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"
try:
    logger.info(f">>>>>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<<<<<")
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<<<<\n\n{'=+' * 55}")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "DATA VALIDATION STAGE"
try:
    logger.info(f">>>>>>>>>>>>>> STAGE {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<")
    obj= DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<<<<\n\n{'=+' * 55}")
except Exception as e:
    logger.exception(e)
    raise e
    


STAGE_NAME = "DATA TRANSFORMATION STAGE"
try:
    logger.info(f">>>>>>>>>>>>>> STAGE {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<")
    obj= DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<<<<\n\n{'=+' * 55}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "MODEL TRAINER STAGE"
try:
    logger.info(f">>>>>>>>>>>>>> STAGE {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<")
    obj= ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<<<<\n\n{'=+' * 55}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "MODEL EVALUATION STAGE"

try:
    logger.info(f">>>>>>>>>>>>>> STAGE {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<")
    obj= ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<<<<\n\n{'=+' * 55}")
except Exception as e:
    logger.exception(e)
    raise e