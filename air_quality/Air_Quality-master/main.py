from db.database import init_db, SessionLocal
from api.client import OpenAQClient
from processor.loader import AirQualityLoader

def main():
    init_db()
    session = SessionLocal()

    client = OpenAQClient()
    loader = AirQualityLoader(session)

    all_data = client.fetch_all_data()
    for data in all_data:
        loader.save_data(data)

    print("Air quality data saved for PM2.5 parameter.")

if __name__ == "__main__":
    main()