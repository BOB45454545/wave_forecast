from src.Database import db_services
from src.wave_api import get_hourly_weather

if __name__ == "__main__":
    hourly_dataframe = get_hourly_weather()
    db_services.insert_data_to_db(hourly_dataframe)