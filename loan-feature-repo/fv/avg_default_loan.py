from tecton import batch_feature_view, Aggregation
from data_source import loan_batch
from entity import loan_default
from datetime import datetime, timedelta


@batch_feature_view(
    sources=[loan_batch],
    entities=[loan_default],
    mode='spark_sql',
    online=False,
    offline=False,
    feature_start_time=datetime(2021, 1, 1),
    owner="jiadong@tecton.ai",
    batch_schedule=timedelta(days=1),
    aggregation_interval=timedelta(days=1),
    aggregations=[Aggregation(
        column='SEC_OVERDUE_ACCTS', function='mean', time_window=timedelta(days=180))],
)
def avg_default_loan(loan_batch):
    return f'''
        SELECT 
            TO_TIMESTAMP(adjusted_timestamp),
            double(SEC_OVERDUE_ACCTS) as SEC_OVERDUE_ACCTS,
            loan_default
        FROM
            {loan_batch}
        '''
