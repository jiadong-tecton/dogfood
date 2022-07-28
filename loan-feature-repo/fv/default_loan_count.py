from tecton import batch_feature_view, Aggregation
from data_source import loan_batch
from entity import loan_candidate
from datetime import datetime, timedelta


@batch_feature_view(
    sources=[loan_batch],
    entities=[loan_candidate],
    mode='spark_sql',
    online=True,
    offline=True,
    ttl=timedelta(days=365),
    feature_start_time=datetime(2021, 1, 1),
    owner="jiadong@tecton.ai",
    batch_schedule=timedelta(days=1),
)
def default_loan_count(loan_batch):
    return f'''
        SELECT 
            TO_TIMESTAMP(adjusted_timestamp),
            double(SEC_OVERDUE_ACCTS) as SEC_OVERDUE_ACCTS,
            UNIQUEID
        FROM
            {loan_batch}
        '''
