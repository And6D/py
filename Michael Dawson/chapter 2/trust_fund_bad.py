# Рантье (версия с ошибкой)
# Демонстрирует логическую ошибку
print("""Pантье Программа подсчитывает ваши ежемесячные расходы. 
Эту статистику нужно знать, чтобы у вас не закончились деньги и вам не пришлось искать работу.
Введите суммы расходов по всем статьям, перечисляемым ниже. 
Вы богаты - так не мелочитесь. пишите суммы в долларах. без центов.
Правильно выбранный тип""")
саг = input("Техническое обслуживание машины 'Ламборгини': ")
гent = input("Съем роскошной квартиры на Манхэттене: ")
jet = input("Apeндa самолета: ")
gifts = input ("Подарки: ")
food = input("Oбeды и ужины в ресторанах: ")
staff = input("Жалованье прислуги (дворецкий. повар. водитель. секретарь): ")
guгu = input( "Плата личному психоаналитику: ")
games = input("Компьютерные игры: ")
total = саг + гent + jet + gifts + food + staff + guгu + games
print("\nОбщая сумма:", total)
input("\n\nHaжмитe Enteг. чтобы выйти.")