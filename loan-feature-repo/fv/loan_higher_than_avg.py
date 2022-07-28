from tecton import RequestSource, on_demand_feature_view
from tecton.types import String, Timestamp, Float64, Field, Bool
from fv.avg_loan import avg_loan

request_schema = [Field('DISBURSED_AMOUNT', Float64)]
loan_request = RequestSource(schema=request_schema)
output_schema = [Field('loan_higher_than_avg', Bool)]


@on_demand_feature_view(
    sources=[loan_request, avg_loan],
    mode='python',
    schema=output_schema,
    description='The loan amount is higher than the avg loan amount a branch usually gives out.'
)
def loan_higher_than_avg(loan_request, avg_loan):
    loan_mean = 0 if avg_loan[
        'DISBURSED_AMOUNT_mean_180d_1d'] is None else float(avg_loan['DISBURSED_AMOUNT_mean_180d_1d'])
    return {'loan_higher_than_avg': float(loan_request['DISBURSED_AMOUNT']) > loan_mean}
