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
	
	return