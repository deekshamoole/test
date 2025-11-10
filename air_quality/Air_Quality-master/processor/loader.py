from models.air_quality import AirQualityRecord
from datetime import datetime
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.exc import SQLAlchemyError

class AirQualityLoader:
    def __init__(self, session):
        self.session = session

    def save_data(self, data):
        results = data.get("results", [])
        if not results:
            print("No results returned from API.")
            return

        print(f"Received {len(results)} measurement(s)")
        inserted_count = 0

        for measurement in results:
            try:
                date_utc = datetime.fromisoformat(
                    measurement["datetime"]["utc"].replace("Z", "+00:00")
                )
                record_dict = {
                    "location": str(measurement.get("locationsId")),
                    "country": "N/A",
                    "parameter": "pm25",
                    "value": measurement.get("value"),
                    "unit": "\u00b5g/m\u00b3",
                    "date_utc": date_utc,
                }

                stmt = insert(AirQualityRecord).values(**record_dict)
                stmt = stmt.prefix_with("OR IGNORE")  # skip duplicates

                self.session.execute(stmt)
                inserted_count += 1

            except SQLAlchemyError as e:
                self.session.rollback()
                print(f"Skipping record due to database error: {e}")
            except Exception as e:
                print(f"Skipping record due to error: {e}")

        self.session.commit()
        print(f"Committed {inserted_count} new record(s)")
