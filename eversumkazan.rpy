init:

	$ mods["matonshade_start"]=u"{color=#000000}МатонШэйд{/color}"
	image cg takei_shk_msh = "mods/matonshade/image/cg_msh/takei_shk_msh.jpg"
    image cg titles_in_intro_1 = "mods/matonshade/image/cg_msh/titles_in_intro_1.jpg"
    image cg titles_in_intro_2 = "mods/matonshade/image/cg_msh/titles_in_intro_2.jpg"
    image cg titles_in_intro_3 = "mods/matonshade/image/cg_msh/titles_in_intro_3.jpg"
    image cg titles_in_intro_4 = "mods/matonshade/image/cg_msh/titles_in_intro_4.jpg"
    image cg titles_in_intro_5 = "mods/matonshade/image/cg_msh/titles_in_intro_5.jpg"
    image cg titles_in_intro_6 = "mods/matonshade/image/cg_msh/titles_in_intro_6.jpg"
    image cg titles_in_intro_7 = "mods/matonshade/image/cg_msh/titles_in_intro_7.jpg"
    image cg titles_in_intro_8 = "mods/matonshade/image/cg_msh/titles_in_intro_8.jpg"
    image cg titles_in_intro_9 = "mods/matonshade/image/cg_msh/titles_in_intro_9.jpg"
    image cg white_world_0 = "mods/matonshade/image/photo/white_world_0.jpg"
    image cg white_world_1 = "mods/matonshade/image/photo/white_world_1.jpg"
    image cg matonshade_in_logo = "mods/matonshade/image/cg_msh/matonshade_in_logo.jpg"
    image slava big = "mods/matonshade/image/spt_msh/slava/slava_big.png"
    image slava normal = "mods/matonshade/image/spt_msh/slava/slava_normal.jpg"
    image slava uuu = "mods/matonshade/image/spt_msh/slava/slava_uuu.png"
    image pozner seat = "mods/matonshade/image/spt_msh/slava/pozner_seat.jpg"
    image pozner seat2 = "mods/matonshade/image/spt_msh/slava/pozner_seat2.jpg"
    image boys_love = "mods/matonshade/image/spt_msh/slava/boys_love_novel.jpg"
    image slava smile = "mods/matonshade/image/spt_msh/slava/slava_smile.png"
    image cg white_click = "mods/matonshade/image/cg_msh/white_click.png"
    image cg anim_mshade = "mods/matonshade/image/cg_msh/anim_mshade.jpg"
    image slava evil = "mods/matonshade/image/spt_msh/slava/slava_evil.png"
    image slava passive = "mods/matonshade/image/spt_msh/slava/slava_passive.png"
    image smsh normal = "mods/matonshade/image/spt_msh/smart_phone/smsh_normal.png"
    image smsh apps = "mods/matonshade/image/spt_msh/smart_phone/smsh_apps.png"
    image smsh off = "mods/matonshade/image/spt_msh/smart_phone/smsh_off.png"
    image smsh type = "mods/matonshade/image/spt_msh/smart_phone/smsh_type.png"
	$ titles_greetings = "mods/matonshade/music/titles_greetings.mp3"
    $ matonshade_in = "mods/matonshade/music/matonshade_in.mp3"
    $ cow_bust_msh = "mods/matonshade/music/cow_bust_msh.mp3"
    $ arriving_msh = "mods/matonshade/music/arriving_msh.mp3"
    $ clock_choice = "mods/matonshade/music/clock_choice.mp3"
    $ colonky_msh = "mods/matonshade/music/colonky_msh.mp3"
    $ jay_sean_ride_it = "mods/matonshade/music/jay_sean_ride_it.mp3"
    $ leaving1_msh = "mods/matonshade/music/leaving1_msh.mp3"
    $ leaving2_msh = "mods/matonshade/music/leaving2_msh.mp3"

label matonshade_start:

    show white with fade2
    show cg white_click
    $ renpy.pause(0)
    sv "Это Я"
    play music cow_bust_msh
    hide cg
    show slava big
    sv "Слава{w}. А на ближайшее время и ты тоже. {w}Сорян, я одеваюсь, как раз когда мы только встретелись."
    sv "- {w}_ {w}-"
    show slava big:
        linear 6 yalign -0.4
    $ renpy.pause(5, hard=True)
    sv "Ой. {w}Пролетел."
    show slava big:
        linear 1 yalign .1
    $ renpy.pause(1, hard=True)
    show slava big:
        linear 3 rotate 360
    sv "Юххуууу. Встретились."
    hide slava big with dissolve

label matonshade_slava3:

    show slava normal with dissolve
    $ renpy.pause(1, hard=True)
    play music cow_bust_msh
    sv "Я вызвал тебя за советом. {w}Ну еще, чтобы хорошо провести время?"
    sv "Осторожно! {w}Не забудь свое имя... {w}И себя в процессе. {w}На счет одежды - я не пионер. {w}Это все фестиваль советской культуры, на который я сегодня еду."
    sv "Ну что все обо мне? Давай о тебе. {w}Мда, функционал ограничен конечно. {w}Как к тебе обращаться?"
    hide slava normal
    show slava normal at cleft with dissolve
    stop music fadeout 2
    menu:
        "{b}Мужской род{/b}":
            jump matonshade_man
            
        "{b}Женский род{/b}":
            jump matonshade_woman

        "{b}Мне все равно{/b}":
            sv "А мне привычнее в мужском."
            jump matonshade_man

label matonshade_man:

    play music titles_greetings
    sv "Ну хорошо. А ты играл в БЛ?"
    menu:
        "{b}Я играл в БЛ{/b}":
            show boys_love at right with flash
            show slava smile
            sv "Да ладно! Интересно, зачем тебе яой? Бойс Лав - мужская любовь. {w}Ну а из нормального? В бесконечное лето тоже играл?"
            hide boys_love
            hide slava smile
            show slava normal at cleft
			           jump matonshade_blbl
        "{b}Нет, я не играю в БЛ{/b}":
            sv "Правильно. А в бесконечное лето играл?"
            jump matonshade_blbl
        
label matonshade_blbl:

    menu:
        "{b}Конечно же{/b}":
            sv "Тогда так. Эта история не связана с оригиналом. Но действующие лица плюс-минус те же. 
            {w}Что? {w}Ну не знаю, я не виделся с ними так много, чтобы заскучать."
            sv "Действие происходит в наши дни ~условно. И никаких путешествий в прошлое. Просто фест советской культуры."
        "{b}Нет{/b}":
            sv "Ты многое упустил. {w}Но ничего, особых навыков здесь не нужно. Да и история эта с оригиналом не связана. {w}Происходит в наши дни ~условно. И никаких путешествий в прошлое. Просто фест советской культуры."

    stop music fadeout 2
    hide slava normal
	$ renpy.pause (1, hard=True)
    show slava uuu at cright
    play music slava_tolky1 fadein 2
    sv "- {w}На самом деле. {w}Все уже устали от этих модов на бл..." 
    show pozner seat at left with flash
    show slava uuu at cright
    pozner "Секундочку. Все уже устали от {w}однотипных модов!"
    hide slava uuu with dissolve
    show slava smile at cright with dissolve
    show slava smile:
        zoom 2
    sv "Благодарим за экспертное мнение. {w}Стоп. Вы играете в БЛ? {w}(ну мы-то с тобой знаем, что БЛ это Бойс Лав - яой, вот сейчас будет умора.)"
    pozner "Знаете, у меня нет на это времени{b}.{/b}"
    hide pozner seat
    show slava uuu at cright
    sv "Слив."
    show slava normal
    sv "Мне надо уладить технические детали перед продолжением."
	
	label matonshade_white_world:
    $ persistent.sprite_time = "day"
    $ day_time()
    show cg white_world_0 with fade3
    show cg white_world_1 with pixellate
    hide white_world_0
    play ambience ambience_boat_station_day
    play sound_loop ambience_cold_wind_loop
    mior "Ты там сам с собой разговариваешь?"
    thsh "Мику и девчонки махали руками на берегу. Парни наблюдали с причала."
    sv "Разговариваю. От восхищения!"
    shor "Что, так красивошно?"
    sv "Оттуда поллагеря видно, загляденье."
    dvor "Насмотрелся, Колумб? Новых земель не открыл случайно?"
    sv "Ага. Посторонитесь, я к вам причаливать буду."
    mior "Разобьешь."
    stop sound_loop fadeout 3
    sv "Чего-чего? Песок же. Обо что бить? Разве что об тебя."
    mior "Грубиян Слава вернулся."
    sv "Дает о себе знать привычка разговаривать с собой."
    stop music
    play music music_list["glimmering_coals"] fadein 2
    play sound sfx_boat_impact
    usor "Грубиянам вход воспрещен!"
    play sound sfx_boat_impact
    thsh "Ульяна молнией хватает весло с причала и отталкивает лодку со Славой от берега."
    usor "Все, земли тебе не видать."
    thsh "Девчонки ухахатываются. Парни подходят в плотную к ограде причала."
    sv "Ты раскачиваешь!"
    slor "Ульян, пусть причаливает, мы его на берегу и возьмем."
    usor "Ну ладно."
    stop music fadeout 2
    thsh "Бросает весло и убегает. {w}Минутой позже Слава сходит на берег."
    play music music_list["what_do_you_think_of_me"]
    hide cg with dissolve
    scene bg ext_beach_day with flash
    show sl smile2 sport at fleft with fade2 
    sv "Спасибо, Славь, а то я что-то не очень..."
    show mi happy swim at fright with fade2
    mior "Я не обиделась."
    show un smile3 sport at left with fade2
    unor "Устал? Гребсти-то."
    sv "Плечи гудят..."
    thsh "Со стороны лагеря плетется Ульяна. Руками обхватывает тяжелый камень."
    show un surprise sport
    show sl surprise sport
    sv "Хотя вот, кто устал. {w}Чего это ты?"
    usor "Хуух."
    thsh "Отпускает камень."
    show mi upset swim
    show us dontlike sport at cleft with fade2
    usor "Да если бы я успела."
    show us grin sport
    usor "Кинула бы камень в воду и тебя бы волнами захлестнуло."
    sv "Интересно, как-нибудь попробуем."
    show un laugh2 sport
    show un grin sport
    unor "Ну Ульян, ты как всегда."
    show us sad sport
    show us sad sport:
        linear 1 xalign 0.9
    show sl shy sport
    show mi shy swim
    usor "Он тут Микочку обижает."
    stop music fadeout 2
    sv "Если бы рядом со мной кидал камни каждый, кому я что-то ляпнул, то я был бы погребен навсегда."
    play music music_list["forest_maiden"] fadein 2
    show us surp1 sport
    show mi smile swim
    sv "Но вы бы тогда не узнали кое-что."
    sv "Ребята, я вам такое должен показать. {w}Там, на острове стоит камера и перевалочный пункт. А рядом вообще самое красивое место."
    show un smile2 sport
    unor "Ага. А меня не взял с собой."
    show sh smile pioneer
    shor "Камера? Так, все, собираемся."
    stop music fadeout 2
    play music white_world_2
    sv "А где Юнона? {w}А, да. {w}Ее здесь нет."
    stop music fadeout 6
    show black with pixellate
    hide sl
    hide un
    hide us
    hide mi
    hide sh
	
	return