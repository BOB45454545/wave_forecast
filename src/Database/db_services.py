import psycopg2

# Assuming you already have the 'hourly_dataframe' from your existing code
# Replace with the actual dataframe variable name if different
# hourly_dataframe = <your_existing_dataframe>

conn = psycopg2.connect(
    dbname="wave_forecast_db",
    user="postgres",
    password="newpassword",
    host="localhost",  # Docker container name or IP address
    port="5432"
)
cur = conn.cursor()


def insert_data_to_db(data_frame):
    # Create table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS wave_forecast (
        date TIMESTAMP PRIMARY KEY,
        wave_height FLOAT,
        swell_wave_height FLOAT
    );"""
    cur.execute(create_table_query)
    conn.commit()

    # Insert data from the DataFrame into PostgreSQL
    insert_query = """
        INSERT INTO wave_forecast (date, wave_height, swell_wave_height)
        VALUES (%s, %s, %s)
        ON CONFLICT (date) DO NOTHING
    """
    for row in data_frame.itertuples(index=False):
        cur.execute(insert_query, (row.date, row.wave_height, row.swell_wave_height))

    conn.commit()

    # Print confirmation message
    print("Data successfully inserted into the database.")
