from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for date_interval in self.dates:
            start, end = date_interval
            rental_days = [start + timedelta(days=x) for x in range((end - start).days + 1)]
            for rental_day in rental_days:
                yield str(rental_day)
        return []


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
