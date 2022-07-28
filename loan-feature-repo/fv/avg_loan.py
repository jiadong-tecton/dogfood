from tecton import batch_feature_view, Aggregation
from data_source import loan_batch
from entity import loan_candidate, branch_id
from datetime import datetime, timedelta


@batch_feature_view(
    sources=[loan_batch],
    entities=[branch_id],
    mode='spark_sql',
    online=True,
    offline=True,
    feature_start_time=datetime(2021, 1, 1),
    owner="jiadong@tecton.ai",
    batch_schedule=timedelta(days=1),
    aggregation_interval=timedelta(days=1),
    aggregations=[Aggregation(
        column='DISBURSED_AMOUNT', function='mean', time_window=timedelta(days=180))],
)
def avg_loan(loan_batch):
    return f'''
        SELECT 
            TO_TIMESTAMP(adjusted_timestamp),
            branch_id,
            double(DISBURSED_AMOUNT) as DISBURSED_AMOUNT
        FROM
            {loan_batch}
        '''
