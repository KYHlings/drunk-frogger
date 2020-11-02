from game_src.level_handler import create_level
from game_src.pause_screen import pause_screen
from game_src.score_handler import score_by_player_position, high_score_list
from sprites_classes.dead_frog import Dead_Frog
from image.image_handler import get_player_sprite, get_get_sprite, \
    get_life_sprite, get_roadkill_sprite, get_beer_sprite, get_sloshed_face, get_drowned_sprite
from sprites_classes.npc import Goat
from sprites_classes.player import Player
from quiz_ui.quiz_handler import quiz_window, quiz
from music_and_sound.sound_handler import get_level_music, get_goat_music, get_drunk_music
from game_src.window_handler import lose_window, win_window, level_title_window, draw_text
from game_src.variabels import *


def redraw_window(player, wise_goat, dead_frog, background_image, lanes, floating_lanes, score, safe_lanes,
                  level_number, question_number):
    # This function updates the window with sprites_classes each loop
    screen.blit(background_image, full_window_blit_pos)
    draw_text(f"score:{score}", score_font, BLACK, screen, 1270, 10, 'topright')
    life_x = 10
    beer_y = 405

    for i in range(player.lives):
        screen.blit(get_life_sprite(), (life_x, 10))
        life_x += 25
    for lane in floating_lanes:
        for mob in lane.floating_mobs:
            screen.blit(mob.image, mob.mob_rect)

    for lane in safe_lanes:
        for mob in lane.floating_mobs:
            screen.blit(mob.image, mob.mob_rect)

    if dead_frog.is_dead:
        if dead_frog.cause_of_death == "roadkill":
            screen.blit(dead_frog.roadkill_img, (dead_frog.dead_x, dead_frog.dead_y))
        elif dead_frog.cause_of_death == "drowned":
            screen.blit(dead_frog.drowned_img, (dead_frog.dead_x, dead_frog.dead_y))
        screen.blit(player.update_img()[0], (3000, 3000))

    else:
        screen.blit(player.update_img()[0], player.update_img()[1])
    for lane in lanes:
        for car in lane.mobs:
            screen.blit(car.image, car.mob_rect)
    if level_number == 3 and question_number < 3:
        screen.blit(get_get_sprite(),
                    (safe_lanes[question_number - 1].floating_mobs[0].mob_x + 100, wise_goat.get_y - 40))
    else:
        screen.blit(get_get_sprite(), (player.x - 20, wise_goat.get_y - 30))

    screen.blit(get_life_sprite(), (10, 435))
    screen.blit(pygame.transform.flip(get_sloshed_face(), True, True), (10, 300))
    for i in range(player.drunk_meter):
        screen.blit(get_beer_sprite(), (15, beer_y))
        beer_y -= 25

    pygame.display.update()


def game_loop(sound_fx, volume,quiz_category):
    # This function runs the main game loop
    clock = pygame.time.Clock()
    player = Player(620, 770, 40, 30, 0, get_player_sprite(0))
    dead_frog = Dead_Frog()
    pygame.display.set_caption("Drunk Frogger")
    level_number = 3
    score = 0
    while True:
        # starts game loop. Uses level number to load desiganted level.
        level_title_window(level_number)
        last_y = 770
        question_number = 1
        level = create_level(level_number)
        wise_goat = Goat(player.x, level.quiz_cord[0])
        running = True
        if player.drunk_meter > 0:
            get_drunk_music(level_number, player.drunk_meter)
        else:
            get_level_music(level_number)
        no_death, no_wrong_answers = True, True

        while running:
            # Runs individual levels.
            score, last_y = score_by_player_position(player.y, last_y, score)
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            keys = pygame.key.get_pressed()
            if dead_frog.is_dead:
                dead_frog.check_time_of_death()
            else:
                player.move(keys)
            if keys[pygame.K_p]:
                level.spawn_paused()
                volume = pause_screen(volume)
                level.spawn_resumed()
                if not volume:
                    return

            level.move_mobs()
            level.spawn_mobs()

                # Checks collision with cars in each lane.
            player, dead_frog, score, no_death = is_frog_run_over(level, player, score, dead_frog, sound_fx,
                                                                 no_death)
            # Triggers event if player is not colliding with floating mob
            player, score, dead_frog, no_death = is_frog_drowning(level, player, score, level_number, sound_fx,
                                                                  dead_frog, no_death)
            if player.lives == 0:
                return
            # Checks collision with mobs in floating lanes.
            player = is_frog_afloat(level, player)

            player, question_number, score, dead_frog, no_death, no_wrong_answers, level.spawn_timer, level.fl_spawn_timer = check_quiz(
                level, player,
                question_number, score,
                dead_frog, sound_fx,
                level_number, no_death,
                no_wrong_answers,
                wise_goat,quiz_category)
            if question_number > level.amount_quiz:
                running = False
            redraw_window(player, wise_goat, dead_frog, level.background_image, level.lanes, level.floating_lanes,
                          score, level.safe_lanes, level_number, question_number)
        level_number += 1
        if level_number == 4:
            level_number = 1


def is_frog_afloat(level, player):
    for lane in reversed(level.floating_lanes + level.safe_lanes):
        for floating_mob in lane.floating_mobs:
            if floating_mob.check_collide(player):
                player.floating = True
                if lane.is_left:
                    player.x -= lane.velocity
                    return player
                else:
                    player.x += lane.velocity
                    return player
            else:
                player.floating = False

    return player


def is_frog_run_over(level, player, score, dead_frog, sound_fx, no_death):
    for lane in level.lanes:
        for car in lane.mobs:
            if car.check_collide(player):
                score -= 20
                no_death = False
                player.lives -= 1
                if player.lives != 0:
                    dead_frog.player_died(player.x, player.y, "roadkill")
                    sound_fx.play_splat()
                    player.reset()
                    return player, dead_frog, score, no_death
                else:
                    lose_window("roadkill")
                    high_score_list(score)
                    return player, dead_frog, score, no_death
    return player, dead_frog, score, no_death


def is_frog_drowning(level, player, score, level_number, sound_fx, dead_frog, no_death):
    if level.sinking_cord[0] < player.y < level.sinking_cord[1] and not player.floating:
        score -= 20
        no_death = False
        player.lives -= 1
        if player.lives != 0:
            if level_number == 3:
                sound_fx.play_falling()
                dead_frog.player_died(player.x, player.y, "asphyxiation")
            else:
                sound_fx.play_splash()
                dead_frog.player_died(player.x, player.y, "drowned")
            player.reset()
            return player, score, dead_frog, no_death
        else:
            if level_number == 3:
                lose_window("asphyxiation")
            else:
                lose_window("drowned")
            high_score_list(score)
            return player, score, dead_frog, no_death
    return player, score, dead_frog, no_death


def check_quiz(level, player, question_number, score, dead_frog, sound_fx, level_number, no_death, no_wrong_answers,
               wise_goat,quiz_category):
    if player.y <= level.quiz_cord[question_number - 1]:
        level.spawn_paused()
        get_goat_music()

        # This if statement checks if the player answers correctly. If the player answers correctly they trigger the win function
        # if they do not answer correctly they get moved to the start position and adds one to the drunk_meter integer
        if not quiz_window(quiz(quiz_category), player.drunk_meter):
            score -= 100
            no_wrong_answers = False
            if player.drunk_meter == 4:
                lose_window("alcohol_poisoning")
                high_score_list(score)
                level.spawn_resumed()
                return player, question_number, score, dead_frog, no_death, no_wrong_answers, level.spawn_timer, level.fl_spawn_timer
            player.drunk_meter += 1
            dead_frog.roadkill_img = get_roadkill_sprite(player.drunk_meter)
            dead_frog.drowned_img = get_drowned_sprite(player.drunk_meter)
            sound_fx.play_burp()
            player.drunken_consequence()
            get_drunk_music(level_number, player.drunk_meter)
            player.reset()
            level.spawn_resumed()
            return player, question_number, score, dead_frog, no_death, no_wrong_answers, level.spawn_timer, level.fl_spawn_timer
        else:
            score += 100
            question_number += 1
            if question_number == level.amount_quiz + 1:
                if no_death:
                    score += 200
                if no_wrong_answers:
                    score += 200
                win_window()
                player.reset()
                level.spawn_resumed()
                return player, question_number, score, dead_frog, no_death, no_wrong_answers, level.spawn_timer, level.fl_spawn_timer
            else:
                wise_goat.get_y = level.quiz_cord[question_number - 1]
                if player.drunk_meter == 0:
                    get_level_music(level_number)
                else:
                    get_drunk_music(level_number, player.drunk_meter)
                    level.spawn_resumed()
                    return player, question_number, score, dead_frog, no_death, no_wrong_answers, level.spawn_timer, level.fl_spawn_timer
    return player, question_number, score, dead_frog, no_death, no_wrong_answers, level.spawn_timer, level.fl_spawn_timer
