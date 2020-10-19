Система для игры "Брейн-ринг"
=============================

Краткое описание
----------------

Эта программа предназначена для проведения игры "Брейн-ринг" для двух команд.

Программа управляется с помощью клавиатуры.

Описание игры
-------------

В игре могут принимать участие 2 команды, снабжённых кнопками (красная и зелёная). Ведущий задаёт вопрос и запускает таймер. Когда команда нажимает кнопку, происходит остановка таймера. В случае неправильного ответа ведущий запускает таймер снова, а если та или иная команда даёт правильный ответ, то ведущий обнуляет таймер и добавляет очки команде. Правильно ответившая команда получает одно очко, но если обе команды ответили неправильно, то в случае правильного ответа на следующем вопросе какая-либо команда может получить два очка. Если на два вопроса подряд не было дано правильного ответа, то команда, ответившая на следующий вопрос правильно, может получить три очка. Если же на три вопроса подряд никто не ответил, то обе команды дисквалифицируются.

Когда таймер не запущен, любое нажатие кнопки является фальстартом, а команда, его допустившая, снимается с вопроса.

Интерфейс
---------

Экран разделён на две половины. 

В левой половине экрана находится счёт игры: слева - счёт красной команды, справа - счёт зелёной команды. В центре находится небольшой квадрат, окрашенный в цвет команды, которой следует начислить очки. По умолчанию квадрат окрашен в красный цвет. Переключается кнопкой `[Numpad /]`.

В самом низу экрана находится значение, соответствующее количеству начисляемых очков. При нажатии кнопки `[Numpad +]` добавляется столько очков, сколько указано внизу. Потом количество начисляемых очков становится равным единице.

Обнуление счёта происходит при нажатии кнопки `[Backspace]`.

В правой половине экрана находится таймер: в центре находится значение, соответствующее количеству секунд, прошедших с момента запуска таймера. Таймер запускается кнопкой `[Enter]`, обнуляется - кнопкой `[Space]`. При нажатии кнопки команды фон окрашивается в цвет команды, нажавшей свою кнопку.

Если таймер не запущен, то любое нажатие кнопки команды обрабатывается как фальстарт, а значение таймера окрашивается в цвет провинившейся команды.

Клавиши управления системой
---------------------------

Клавиша         |Производимое действие
----------------|-----------------------------------------------------
`Enter`         | запуск таймера
`Space`         | обнуление таймера
`Numpad /`      | переключение команды, которой следует начислить очки
`Numpad +`      | начисление очков выбранной команде
`Backspace`     | обнуление счёта
`Esc`           | выход из программы
`Left`          | уменьшение количества начисляемых очков
`Right`         | увеличение количества начисляемых очков
`Правая кнопка` | нажатие кнопки красной командой
`Средняя кнопка`| нажатие кнопки зелёной командой

Аппаратура для проведения Брейн-ринга
-------------------------------------

Для отображения состояния Брейн-системы необходимо два монитора.

Для соревнования команд в скорости необходимы кнопки на основе компьютерных мышей. Кнопки должны быть сделаны из компьютерных USB-мышей, подведённой к ним кнопки и корпуса, в котором находится вся конструкция. Кнопка должна быть подключена к группе контактов, соответствующей кнопке мыши, которая отвечает за остановку таймера для ответа команды. Красной команде соответствует правая кнопка мыши, зелёной команде - средняя. В принципе, конструкция кнопки может быть реализована как угодно, главное - необходимо учитывать вышеуказанное условие.

Требования к системе
--------------------

- Python 3.4 и выше;

- Pygame 1.9.3 и выше.
