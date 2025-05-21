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

    # #МЕТОД — красивый вывод данных
    def pretty_print(self):
        for continent, countries in self.data.items():
            print(f"{continent}")
            for country, cities in countries.items():
                print(f"  {country}")
                for city, count in cities.items():
                    print(f"    {city}: {count} mõrvad")


# #ТЕСТОВЫЙ ЗАПУСК
if __name__ == "__main__":
    stats = MurderStatsManager()

    # #ЕВРОПА
    stats.add_data("Europe", "Estonia", "Tallinn", 5)
    stats.add_data("Europe", "Finland", "Helsinki", 3)

    # #АЗИЯ
    stats.add_data("Asia", "Japan", "Tokyo", 8)

    # #КРАСИВЫЙ ВЫВОД
    print("\nMõrvade üldstatistika:")
    stats.pretty_print()
