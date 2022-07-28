from tecton import FileConfig, BatchSource, HiveConfig


# def raw_data_deserialization(df):
#    from pyspark.sql.functions import col, from_json, from_utc_timestamp, when
#    from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType, BooleanType, IntegerType
#    return (
#        df.select(
#            col('UNIQUEID'),
#        )
#    )
loan_batch = BatchSource(
    name='loan_batch',
    batch_config=FileConfig(
        uri='s3://tecton.ai.public/jiadong/loan_default_data/part-00000-tid-3354476786284508882-a3a23c47-056c-49f0-9f0a-425cfbda7229-2911-1-c000.csv',
        # uri='s3://tecton.ai.public/jiadong/loan_default_data',
        # uri='s3://tecton.ai.public/data/ad_impressions.csv',
        file_format='csv'
        # post_processor=raw_data_deserialization
        # timestamp_field='adjusted_timestamp'
    ),
    owner='jiadong@tecton.ai'
)

# batch_config = HiveConfig(
#    database='demo_loan_db',
#    table='demo_loan_crawler_tableloan_default_data',
#    timestamp_field='adjusted_timestamp',
# )
# loan_batch = BatchSource(
#    name='loan_batch',
#    batch_config=batch_config,
#    owner='jiadong@tecton.ai'
# )
