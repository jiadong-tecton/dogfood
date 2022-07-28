from tecton import Entity

loan_candidate = Entity(
    name='loan_candidate',
    join_keys=['UNIQUEID'],
    description='A loan candidate',
    owner='jiadong@tecton.ai'
)

branch_id = Entity(
    name='branch_id',
    join_keys=['branch_id'],
    description='A branch of the leander',
    owner='jiadong@tecton.ai'
)

loan_default = Entity(
    name='loan_default',
    join_keys=['loan_default'],
    description='if a loan defaults',
    owner='jiadong@tecton.ai'
)
