class MurderStatsManager:
    def __init__(self):
        self.data = {}

    def add_data(self, continent, country, city, count):
        if continent not in self.data:
            self.data[continent] = {}
        if country not in self.data[continent]:
            self.data[continent][country] = {}
        self.data[continent][country][city] = count

    def get_stats(self):
        return self.data


if __name__ == "__main__":
    stats = MurderStatsManager()

    stats.add_data("Europe", "Estonia", "Tallinn", 5)
    stats.add_data("Europe", "Finland", "Helsinki", 3)

    stats.add_data("Asia", "Japan", "Tokyo", 8)

    from pprint import pprint
    pprint(stats.get_stats())

### 1. get_city_stats(continent, country, city)

#Возвращает данные об убийствах по указанному городу.

### 2. remove_city(continent, country, city)

#Удаляет указанный город из структуры self.data.

### 3. **Добавь данные по Африке.**

#1. Сделай минимум 2 коммита.
#2. Выполни push в ветку feature-extensions.
