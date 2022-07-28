from tecton import FeatureService
from fv.loan_higher_than_avg import loan_higher_than_avg
from fv.default_loan_count import default_loan_count

fraud_detection_feature_service = FeatureService(
    name='loan_default_feature_service',
    features=[loan_higher_than_avg, default_loan_count]
)
