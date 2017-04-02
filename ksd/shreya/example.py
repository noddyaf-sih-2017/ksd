from shreya import models as shreya_models

def query_ml_status():
	ml_status = shreya_models.MLStatus().load()
	return ml_status.allow

def set_ml_status(bool_value):
	ml_status = shreya_models.MLStatus.load()
	ml_status.allow = bool_value
	ml_status.save()
