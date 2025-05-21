# #КЛАСС — управление статистикой убийств
class MurderStatsManager:
    def __init__(self):
        # #ИНИЦИАЛИЗАЦИЯ — создаём пустую структуру данных
        self.data = {}

    # #МЕТОД — добавление или обновление данных
    def add_data(self, continent, country, city, count):
        if continent not in self.data:
            self.data[continent] = {}
        if country not in self.data[continent]:
            self.data[continent][country] = {}
        self.data[continent][country][city] = count

    # #МЕТОД — получить всю статистику
    def get_stats(self):
        return self.data

    # #МЕТОД — получить данные по конкретному городу
    def get_city_stats(self, continent, country, city):
        try:
            return self.data[continent][country][city]
        except KeyError:
            return None  # #ОБРАБОТКА — безопасное возвращение, если данных нет

    # #МЕТОД — удалить город и при необходимости пустые уровни
    def remove_city(self, continent, country, city):
        try:
            del self.data[continent][country][city]
            # #ЕСЛИ — страна осталась пустой, удаляем
            if not self.data[continent][country]:
                del self.data[continent][country]
            # #ЕСЛИ — континент остался пустым, удаляем
            if not self.data[continent]:
                del self.data[continent]
        except KeyError:
            pass  # #ЕСЛИ — элемента нет, просто пропускаем

    # #МЕТОД — красивый вывод данных
    def pretty_print(self):
        for continent, countries in self.data.items():
            print(f"{continent}")
            for country, cities in countries.items():
                print(f"  {country}")
                for city, count in cities.items():
                    print(f"    {city}: {count} mõrvad")


# #ТЕСТОВЫЙ ЗАПУСК — запускается, если файл выполняется напрямую
if __name__ == "__main__":
    stats = MurderStatsManager()

    # #ЕВРОПА
    stats.add_data("Europe", "Estonia", "Tallinn", 5)
    stats.add_data("Europe", "Finland", "Helsinki", 3)

    # #АЗИЯ
    stats.add_data("Asia", "Japan", "Tokyo", 8)

    # #АФРИКА — добавлено во втором коммите
    stats.add_data("Africa", "Nigeria", "Lagos", 7)
    stats.add_data("Africa", "South Africa", "Cape Town", 4)

    # #ПОЛУЧЕНИЕ — данных по городу
    print("Tokyo linna statistika:", stats.get_city_stats("Asia", "Japan", "Tokyo"))

    # #УДАЛЕНИЕ — Tallinn из статистики
    stats.remove_city("Europe", "Estonia", "Tallinn")

    # #КРАСИВЫЙ ВЫВОД
    print("\nMõrvade üldstatistika:")
    stats.pretty_print()
