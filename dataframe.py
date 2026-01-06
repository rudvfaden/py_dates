from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, date_format, datediff
from pyspark.sql.types import StructType, StructField, DateType
from datetime import datetime, timedelta
from danish_banking_holidays.calendar import DanishBankingCalendar

# Initialize Spark
spark = SparkSession.builder.appName("DanishBankingHolidayApp").getOrCreate()

# Define date range
start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 12, 31)

# Create list of dates
current_date = start_date
date_list = []
holidays_data = []

while current_date <= end_date:
    date_list.append((current_date.date(),))
    current_date += timedelta(days=1)

# Create DataFrame with dates
dates_df = spark.createDataFrame(date_list, ["date"])

# Get Danish banking holidays
calendar = DanishBankingCalendar()
for year in range(start_date.year, end_date.year + 1):
    holidays_dict = calendar.get_holidays(start_date.year)
    holidays_dates = list(holidays_dict.keys())
    holidays_data.append(holidays_dates)

# Create DataFrame with holidays

holidays_df = spark.createDataFrame(holidays_data, ["holiday_date"])

# Join with holidays to mark banking holidays
result_df = dates_df.join(
    holidays_df, 
    col("date") == col("holiday_date"), 
    "left"
).withColumn(
    "is_banking_holiday", 
    col("holiday_date").isNotNull()
)

# Show results
print("Date DataFrame with Banking Holiday Flag:")
result_df.show(20)

print(f"\nTotal days: {result_df.count()}")
print(f"Banking holidays: {result_df.filter(col('is_banking_holiday')).count()}")
