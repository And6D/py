import re

text = """ Wake up
Wake up
Grab a brush and put a little make-up
Hide the scars to fade away the shake-up
Hide the scars to fade away the...
Why did you leave the keys upon the table?
Here you go create another fable
You wanted to
Grab a brush and put a little makeup
You wanted to
Hide the scars to fade away the shake-up
You wanted to
Wh did you leave the keys upon the table?
You wanted to
I do not think you trust
In... My... Self-righteous suicide
I... Cry... When angels deserve to die
Wake up
Wake up
Grab a brush and put a little make-up
Hide the scars to fade away the
Hide the scars to fade away the shake-up)
Why'd you leave the keys upon the table?
Here you go create another fable
You wanted to
Grab a brush and put a little make-up
You wanted to
Hide the scars to fade away the shake-up
You wanted to
Why'd you leave the keys upon the table?
You wanted to
I don't think you trust
In... My... Self-righteous suicide
I... Cry... When angels deserve to die
In, my, Self-righteous suicide
I, cry, when angels deserve to die
Father (father)
Father (father)
Father (father)
Father (father)
Father, into your hands I commend my spirit
Father, into your hands
Why have you forsaken me?
In your eyes forsaken me
In your thoughts forsaken me
In your heart forsaken me, oh
Trust in my self-righteous suicide
I cry when angels deserve to die
In my self-righteous suicide
I cry when angels deserve to die"""

print(len(text))
result = re.match("Wake", text)
print(result)

result = re.search("Father", text)
print(result)
print(result[0]) # выводит значение поиска

searchres = re.findall("fade away", text)
print(searchres[0], "finded ", len(searchres), " times in ", "text")

r = re.split("\n", text)
print(r)

text_url = """<p>По ходу оперативной работы Путину приходилось ежедневно разъезжать на своём автомобиле
<a href="/wiki/%D0%92%D0%90%D0%97-2106" title="ВАЗ-2106">«Жигули» шестой модели</a>. 
В течение командировки по выслуге лет Путин повышен в звании до подполковника и в должности до
старшего помощника начальника отдела. Вскоре после падения 
<a href="/wiki/%D0%91%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D1%82%D0%B5%D0%BD%D0%B0" title="Берлинская стена">Берлинской стены</a>,
5 декабря 1989 года толпа немецких демонстрантов пыталась взять штурмом особняк советской резидентуры по улице Angelikastrasse 4 с целью захвата архивов КГБ,
однако Путину без применения табельного оружия удалось уговорить собравшихся разойтись. Большой объём секретных оперативных документов он сжёг в печке резидентуры.
В январе 1990 года Путин завершил командировку в ГДР и вернулся в Ленинград<sup id="cite_ref-Кондрашов_35-5" class="reference"><a href="#cite_note-Кондрашов-35">[35]</a></sup>.
</p>""" # текст удалить все кроме текста

print(len(text_url))

tp = (re.sub("<p>", " ", text_url)) # замена одного элемента на другой
tp1 = (re.sub("</p>" , " ", tp))
tp2 = (re.sub(" ", " ", tp1))
print(tp2)
print(re.fullmatch("</p>", text_url)) # проверка точного совпадения
result1 = re.search(r"<.", text_url)
print(result1)


"""Урок 13 регулярные выражения"""

testtxt = "Как я постоянно говорю, у нас в год выходит три-четыреновые (переводные, конечно) книги о «Битлз» и «битлах», хотя самой группы официально не существует с 1970 года. А спустя десять +7(908)8066456 лет не стало и Джона Леннона, которого 9 декабря 1980 года застрелил Марк Чэпмен – через минуту после того, как Леннон дал ему автограф. О Ленноне за последние два года вышли две отличные биографии – «Кто убил Джона Леннона» Лесли Энн Джонс +79088083477 (в «Бомборе» в 2020 году) и роскошное подробнейшее жизнеописание Рэя Коннели «Быть Джоном Ленноном» (в прошлом году в «Азбуке»). Так что вряд ли книга Джеймса Паттерсона сообщит какую-то новую 8(908)8083456 информацию, хотя, конечно, всегда что-то есть новое. Например, Паттерсон сосредатачивается на описании всяких фриков, безумцев и придурков, которые возникали на пути 8-908-808-34-00 «Битлз» - от констебля Нормана Пилчера, арестовавшего Леннона за хранение марихуаны до Чарльза Мэнсона, переполошившего всех признанием, что услышал в песне Helter Skelter 89008083456 тайный призыв к революции. Так что Чэпмен был не единственным безумцем. Накануне роковой встречи с Ленноном он встретил в метро другую рок-звезду, Джеймса Тейлора, и попытался с ним заговорить. А Тейлор когда-то девять месяцев провел в психушке и сразу понял, 8 908 808 34 99 с кем он говорит. Сказал «мужик, мне идти надо» - и на полной скорости ушел. А потом увидел этого парня в сводке новостей, он убил Джона Леннона. Надо же, какой факт, не знал об этом."
d1 = testtxt.replace("+7","8")
d2 = d1.replace("-", "")
d3 = d2.replace(" ", "")
d4 = d3.replace(")", "(")
d5 = d4.replace("(", "")
print(testtxt)
numbers = re.findall("8\d{10}", d5)
print(numbers)
