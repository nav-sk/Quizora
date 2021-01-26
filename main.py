### Quizora v2.0(beta)
### Dev: WhiteHat StormBreakers

## uses kivy == 2.0.0, kivymd == 0.104.2.dev, python3 == 3.9.0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# importing necessary modules
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.behaviors import FocusBehavior
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.card import MDCard
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.utils import rgba
from kivy.uix.screenmanager import SlideTransition
from kivy.core.window import Window
import importlib


# Setting window size for mobile view
Window.size= (320, 650)


# defining classes required for Scoreboard data
class Content0(MDBoxLayout):
    pass


class Content1(MDBoxLayout):
    pass


class Content2(MDBoxLayout):
    pass


class Content3(MDBoxLayout):
    pass


class Content4(MDBoxLayout):
    pass


class Content5(MDBoxLayout):
    pass


class Content6(MDBoxLayout):
    pass


class Content7(MDBoxLayout):
    pass


class Content8(MDBoxLayout):
    pass


class Content9(MDBoxLayout):
    pass


# Customised Buttons for Dialogs
class CustButton1(MDRaisedButton):
    pass


class CustButton2(MDRaisedButton):
    pass


# Custom content for Dialogs
class QuizLoader(MDRelativeLayout):
    pass


class AboutDialog(MDBoxLayout):
    pass


# Customised Card for Score
class CustomCard(MDBoxLayout):
    pass


# Items for backdrop firstlayer of ScoreBoard Sreen
class ItemFirstLayer(OneLineAvatarListItem):
    icon = StringProperty()


# Defining MainApp Class inherited from the MDApp class where the app get started
class MainApp(MDApp):
    # Setting the mainlayout of the app
    def build(self):
        Window.bind(on_keyboard = self.key_input)
        self.root = Factory.MainLayout()

    # letting the app not to stop while in background
    def on_pause(self):
        return True

    # handling the 'esc' key in Windows and back button in Android
    def key_input(self, window, key, scancode, codepoint, modifier):
        if key == 27:
            if self.root.ids.mgr.current == 'Home':

                if self.root.ids.btm_nav.previous_tab.text == 'Quiz_Zone':
                    self.quit_app_dialog.open()

                if self.root.ids.btm_nav.previous_tab.text == 'Score':
                    self.root.ids.btm_nav.switch_tab('Quiz_Zone')

            if self.root.ids.mgr.current == 'Quiz_page':
                self.confirm_exit('Quiz')

            if self.root.ids.mgr.current == 'Result':
                self.confirm_exit('Result')

            return True
        else:
            return False


    # initialising the data on app start-up
    def on_start(self):
        c0, c1, c2, c3, c4, c5, c6, c7, c8, c9 = Content0(), Content1(), Content2(), Content3(), Content4(), Content5(), Content6(), Content7(), Content8(), Content9()
        self.contents = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]
        self.tiles = ['apple', 'python', 'india', 'android', 'earth', 'space', 'marvel', 'game', 'naming', 'tech']
        self.score_icons = ['apple.png', 'python.png', 'india.png', 'android.png', 'earth.png', 'space.png',
                            'marvel.png', 'game.png', 'naming.png', 'tech.png']
        self.end_load = MDDialog(type = 'custom', content_cls = QuizLoader())
        self.about = MDDialog(type = 'custom', content_cls = AboutDialog(), buttons = [
            MDFlatButton(text = 'CANCEL', on_release = self.close_dialog, text_color = rgba(0, 36, 106, 255))])
        self.dialog = MDDialog(type = 'custom', content_cls = QuizLoader())
        self.confirm_exit_quiz = MDDialog(title = 'Are you sure to leave ?',
                                          text = 'The current progress will be lost.',
                                          type = 'alert',
                                          buttons = [MDFlatButton(text = 'CANCEL', text_color = rgba(77, 0, 85, 255),
                                                                  on_release = self.close_dialog), CustButton1()])
        self.confirm_exit_result = MDDialog(title = 'Are you sure to leave ?',
                                            type = 'confirmation',
                                            buttons = [MDFlatButton(text = 'CANCEL', text_color = rgba(77, 0, 85, 255),
                                                                    on_release = self.close_dialog), CustButton1()])
        self.confirm_skip = MDDialog(title = 'Skip Question ?',
                                     type = 'confirmation',
                                     buttons = [MDFlatButton(text = 'CANCEL', on_release = self.close_dialog,
                                                             text_color = rgba(0, 36, 106, 255)),
                                                CustButton2(text = ' SKIP ', on_release = self.switch_qn)])
        self.force_end_dialog = MDDialog(title = 'Confirm ending the quiz ?',
                                         type = 'confirmation',
                                         buttons = [MDFlatButton(text = 'CANCEL', on_release = self.close_dialog,
                                                                 text_color = rgba(0, 36, 106, 255)),
                                                    CustButton2(text = '   YES   ', on_release = self.force_end_result)])
        self.quit_app_dialog = MDDialog(title = 'Are you sure to quit the app ?',
                                        type = 'confirmation',
                                        buttons = [MDFlatButton(text = 'CANCEL', on_release = self.close_dialog,
                                                                text_color = rgba(0, 36, 106, 255)),
                                                   CustButton2(text = '   QUIT   ', on_release = self.stop)])
        self.menu = MDDropdownMenu(items = [{'text': 'About', 'height': '30dp', 'bot_pad': '5dp'}], width_mult = 2,
                                   radius = [dp(4)],
                                   selected_color = [150, 150, 150, 150], caller = self.root.ids.tb_dots)
        self.about.update_height(dp(600))
        self.menu.bind(on_release = self.menu_callback)
        self.set_scoreboard()


    # setting the scoreboard data
    def set_scoreboard(self):

        self.conts = [self.root.ids.cont0, self.root.ids.cont1, self.root.ids.cont2, self.root.ids.cont3,
                      self.root.ids.cont4, self.root.ids.cont5, self.root.ids.cont6, self.root.ids.cont7,
                      self.root.ids.cont8, self.root.ids.cont9]

        for i in range(10):
            self.root.ids.front_layer.add_widget(
                ItemFirstLayer(text = self.tiles[i].title() + ' Quiz', icon = 'Images/Score/' + self.score_icons[i]))
            self.root.ids.front_layer.children[i].source = self.score_icons[i]

        contents = self.contents
        for i in range(10):
            card = contents[i]
            self.conts[i].add_widget(card)


    # callback to close backdrop while leaving scoreboard
    def close_backdrop(self):
        if self.root.ids.btm_nav.previous_tab.text == 'Score':
            self.root.ids.backdrop.close()


    # callback on backdrop close
    def backdrop_onclose(self):
        self.root.ids.backdrop.left_action_items = [['bullseye-arrow', lambda x: None]]
        self.root.ids.backdrop.title = 'ScoreBoard'
        self.root.ids.backdrop.radius_left = dp(25)


    # callback on backdrop open
    def backdrop_onopen(self):
        self.root.ids.backdrop.left_action_items = [['close', lambda x: self.root.ids.backdrop.close()]]
        self.root.ids.backdrop.radius_left = dp(0)


    # requesting confirmation from the user to leave the screen
    def confirm_exit(self, cur_scr):
        if cur_scr == 'Quiz':
            self.confirm_exit_quiz.open()
        elif cur_scr == 'Result':
            self.confirm_exit_result.open()


    # callback for pressing menu item in quiz_zone
    def menu_callback(self, instance_menu, instance_menu_item):
        if instance_menu_item.text == 'About':
            self.about.open()
            self.menu.dismiss()


    # showing up of loading spinner
    def quiz_loading_dialog(self, dest):
        self.quiz_name = dest
        self.dialog.open()
        Clock.schedule_once(self.set_quiz, 2)


    # callback for back button in appbar
    def callback(self, dest):
        if dest in self.tiles:
            self.quiz_loading_dialog(dest)
        elif dest == 'Home':
            self.root.ids.mgr.transition = SlideTransition(direction = 'right')
            self.root.ids.mgr.current = 'Home'
            self.close_dialog()
        elif dest == 'Profile':
            self.root.ids.mgr.transition = SlideTransition(direction = 'left')
            self.root.ids.mgr.current = 'Profile'


    # setting quiz
    def set_quiz(self, dt):
        self.score = 0
        self.quiz(self.quiz_name)


    # opening up the quiz panel
    def quiz(self, title):
        self.data = importlib.import_module('Quiz_Data.' + title)
        self.root.ids.quiz_tb.title = title.capitalize() + ' Quiz'
        self.root.ids.mgr.transition = SlideTransition(direction = 'left')
        self.root.ids.mgr.current = 'Quiz_page'
        Clock.schedule_once(self.dialog.dismiss)
        self.get_ans(0)
        self.ans = ['None', 'None', 'None', 'None', 'None']
        self.last_opt = ''


    # reading the quiz data and saving it for processing
    def get_ans(self, i):
        self.root.ids.qn_card.text = self.data.question[i]
        self.root.ids.opt1.text = self.data.opt1[i]
        self.root.ids.opt2.text = self.data.opt2[i]
        self.root.ids.opt3.text = self.data.opt3[i]
        self.root.ids.opt4.text = self.data.opt4[i]
        self.qn_no = self.data.sno[i]


    # checking if any option is selected or not
    def is_ans(self):
        if self.ans[self.qn_no] == 'None':
            self.confirm_skip.open()
        else:
            self.switch_qn()


    # closing the dialog which is open
    def close_dialog(self, *args):
        try:
            self.confirm_skip.dismiss()
        except:
            pass

        try:
            self.force_end_dialog.dismiss()
        except:
            pass

        try:
            self.confirm_exit_quiz.dismiss()
        except:
            pass

        try:
            self.confirm_exit_result.dismiss()
        except:
            pass

        try:
            self.about.dismiss()
        except:
            pass

        try:
            self.quit_app_dialog.dismiss()
        except:
            pass


    # callback for skip quiz
    def force_end_quiz(self):
        self.force_end_dialog.open()
        self.skipped = 'Skipped Completely'


    # setting result after skip quiz
    def force_end_result(self, *args):
        self.force_end_dialog.dismiss()
        self.end_load.open()
        Clock.schedule_once(self.load_result, .3)


    # callback for switching quiz questions if not skipped
    def switch_qn(self, *args):
        index = self.qn_no
        try:
            self.confirm_skip.dismiss()
        except:
            pass

        if index != 4:
            self.get_ans(index + 1)
            self.root.ids.progress.value += 25
            self.get_response('', '')

            if index == 0:
                self.root.ids.pg1_icon.text_color = rgba(11, 158, 11, 255)
                self.root.ids.pg1_icon.icon = 'checkbox-marked-circle'
            elif index == 1:
                self.root.ids.pg2_icon.text_color = rgba(11, 158, 11, 255)
                self.root.ids.pg2_icon.icon = 'checkbox-marked-circle'
            elif index == 2:
                self.root.ids.pg3_icon.text_color = rgba(11, 158, 11, 255)
                self.root.ids.pg3_icon.icon = 'checkbox-marked-circle'
            elif index == 3:
                self.root.ids.pg4_icon.text_color = rgba(11, 158, 11, 255)
                self.root.ids.pg4_icon.icon = 'checkbox-marked-circle'
                self.root.ids.next_qn.text = 'Submit'

            if self.ans[index] == 'None':
                if index == 0:
                    self.root.ids.pg1_icon.text_color = [1, 1, 1, 1]
                    self.root.ids.pg1_back.text_color = rgba(11, 158, 11, 255)
                    self.root.ids.pg1_icon.icon = 'fast-forward'
                if index == 1:
                    self.root.ids.pg2_icon.text_color = [1, 1, 1, 1]
                    self.root.ids.pg2_back.text_color = rgba(11, 158, 11, 255)
                    self.root.ids.pg2_icon.icon = 'fast-forward'
                if index == 2:
                    self.root.ids.pg3_icon.text_color = [1, 1, 1, 1]
                    self.root.ids.pg3_back.text_color = rgba(11, 158, 11, 255)
                    self.root.ids.pg3_icon.icon = 'fast-forward'
                if index == 3:
                    self.root.ids.pg4_icon.text_color = [1, 1, 1, 1]
                    self.root.ids.pg4_back.text_color = rgba(11, 158, 11, 255)
                    self.root.ids.pg4_icon.icon = 'fast-forward'

        elif index == 4:
            if self.ans[4] == 'None':
                self.root.ids.pg5_icon.text_color = [1, 1, 1, 1]
                self.root.ids.pg5_back.text_color = rgba(11, 158, 11, 255)
                self.root.ids.pg5_icon.icon = 'fast-forward'
                self.end_load.open()
                self.save_response()
            else:
                self.root.ids.pg5_icon.text_color = [0, 1, 0, 1]
                self.root.ids.pg5_icon.icon = 'checkbox-marked-circle'
                self.end_load.open()
                self.save_response()


    # loading the result page
    def save_response(self):
        self.load_result()


    # setting the actions in quiz panel
    def get_response(self, ans, opt = ''):
        i = self.qn_no
        if opt == 'A':
            self.root.ids.opt1_icon.text_color = [0, 1, 0, 1] if self.root.ids.opt1_icon.text_color == [1, 1, 1,
                                                                                                        1] else [1, 1,
                                                                                                                 1, 1]
            self.root.ids.opt2_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt3_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt4_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt1_icon.icon = 'alpha-a-circle' if self.root.ids.opt1_icon.icon == 'alpha-a-circle-outline' else 'alpha-a-circle-outline'
            self.root.ids.opt2_icon.icon = 'alpha-b-circle-outline'
            self.root.ids.opt3_icon.icon = 'alpha-c-circle-outline'
            self.root.ids.opt4_icon.icon = 'alpha-d-circle-outline'
            self.ans[i] = self.data.opt1[i] if not self.ans[i] == ans else 'None'

        elif opt == 'B':
            self.root.ids.opt1_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt2_icon.text_color = [0, 1, 0, 1] if self.root.ids.opt2_icon.text_color == [1, 1, 1,
                                                                                                        1] else [1, 1,
                                                                                                                 1, 1]
            self.root.ids.opt3_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt4_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt1_icon.icon = 'alpha-a-circle-outline'
            self.root.ids.opt2_icon.icon = 'alpha-b-circle' if self.root.ids.opt2_icon.icon == 'alpha-b-circle-outline' else 'alpha-b-circle-outline'
            self.root.ids.opt3_icon.icon = 'alpha-c-circle-outline'
            self.root.ids.opt4_icon.icon = 'alpha-d-circle-outline'
            self.ans[i] = self.data.opt2[i] if not self.ans[i] == ans else 'None'

        elif opt == 'C':
            self.root.ids.opt1_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt2_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt3_icon.text_color = [0, 1, 0, 1] if self.root.ids.opt3_icon.text_color == [1, 1, 1,
                                                                                                        1] else [1, 1,
                                                                                                                 1, 1]
            self.root.ids.opt4_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt1_icon.icon = 'alpha-a-circle-outline'
            self.root.ids.opt2_icon.icon = 'alpha-b-circle-outline'
            self.root.ids.opt3_icon.icon = 'alpha-c-circle' if self.root.ids.opt3_icon.icon == 'alpha-c-circle-outline' else 'alpha-c-circle-outline'
            self.root.ids.opt4_icon.icon = 'alpha-d-circle-outline'
            self.ans[i] = self.data.opt3[i] if not self.ans[i] == ans else 'None'

        elif opt == 'D':
            self.root.ids.opt1_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt2_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt3_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt4_icon.text_color = [0, 1, 0, 1] if self.root.ids.opt4_icon.text_color == [1, 1, 1,
                                                                                                        1] else [1, 1,
                                                                                                                 1, 1]
            self.root.ids.opt1_icon.icon = 'alpha-a-circle-outline'
            self.root.ids.opt2_icon.icon = 'alpha-b-circle-outline'
            self.root.ids.opt3_icon.icon = 'alpha-c-circle-outline'
            self.root.ids.opt4_icon.icon = 'alpha-d-circle' if self.root.ids.opt4_icon.icon == 'alpha-d-circle-outline' else 'alpha-d-circle-outline'
            self.ans[i] = self.data.opt4[i] if not self.ans[i] == ans else 'None'

        elif opt == '':
            self.root.ids.opt1_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt2_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt3_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt4_icon.text_color = [1, 1, 1, 1]
            self.root.ids.opt1_icon.icon = 'alpha-a-circle-outline'
            self.root.ids.opt2_icon.icon = 'alpha-b-circle-outline'
            self.root.ids.opt3_icon.icon = 'alpha-c-circle-outline'
            self.root.ids.opt4_icon.icon = 'alpha-d-circle-outline'


    # algorithm for checking the correct answer and setting up the result page
    def load_result(self, *args):

        for cor_ans in self.data.correct_ans:
            if cor_ans in self.ans:
                self.score += 1

        self.scoreboard_data()
        qn_icons = ['numeric-1-box', 'numeric-2-box', 'numeric-3-box', 'numeric-4-box', 'numeric-5-box']

        cor_ans_list = []
        for i in range(5):
            for j in range(4):
                if self.data.correct_ans[i] == self.data.options[j][i]:
                    cor_ans_list.append(j)

        user_ans = []
        for i in range(5):
            for j in range(4):
                if self.ans[i] == self.data.options[j][i]:
                    user_ans.append(j)
            if self.ans[i] == 'None':
                user_ans.append('None')

        opt1_color = [[1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1]]
        opt2_color = [[1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1]]
        opt3_color = [[1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1]]
        opt4_color = [[1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1], [1, 1, 1, .1]]

        opt1_right_icon = ['', '', '', '', '']
        opt2_right_icon = ['', '', '', '', '']
        opt3_right_icon = ['', '', '', '', '']
        opt4_right_icon = ['', '', '', '', '']

        for i in range(5):
            if user_ans[i] == 0:
                opt1_color[i] = [1, 0, 0, .6]

            elif user_ans[i] == 1:
                opt2_color[i] = [1, 0, 0, .6]

            elif user_ans[i] == 2:
                opt3_color[i] = [1, 0, 0, .6]

            elif user_ans[i] == 3:
                opt4_color[i] = [1, 0, 0, .6]

            elif user_ans[i] == 'None':
                pass

        for i in range(5):
            if cor_ans_list[i] == 0:
                opt1_color[i] = [0, 1, 0, .55]

            elif cor_ans_list[i] == 1:
                opt2_color[i] = [0, 1, 0, .55]

            elif cor_ans_list[i] == 2:
                opt3_color[i] = [0, 0, 1, .55]

            elif cor_ans_list[i] == 3:
                opt4_color[i] = [0, 1, 0, .55]

        for i in range(5):
            if (user_ans[i] == 0) and (cor_ans_list[i] == 0):
                opt1_color[i] = [0, 1, 0, .5]

            elif (user_ans[i] == 1) and (cor_ans_list[i] == 1):
                opt2_color[i] = [0, 1, 0, .5]

            elif (user_ans[i] == 2) and (cor_ans_list[i] == 2):
                opt3_color[i] = [0, 1, 0, .5]

            elif (user_ans[i] == 3) and (cor_ans_list[i] == 3):
                opt4_color[i] = [0, 1, 0, .5]

        for i in range(5):
            if (user_ans[i] != 0) and (cor_ans_list[i] == 0):
                opt1_color[i] = [0, 1, 0, .55]

            elif (user_ans[i] != 1) and (cor_ans_list[i] == 1):
                opt2_color[i] = [0, 1, 0, .55]

            elif (user_ans[i] != 2) and (cor_ans_list[i] == 2):
                opt3_color[i] = [0, 1, 0, .55]

            elif (user_ans[i] != 3) and (cor_ans_list[i] == 3):
                opt4_color[i] = [0, 1, 0, .55]

        for i in range(5):
            if (user_ans[i] == 'None') and (cor_ans_list[i] == 0):
                opt1_color[i] = [1, 1, 0, .5]

            elif (user_ans[i] == 'None') and (cor_ans_list[i] == 1):
                opt2_color[i] = [1, 1, 0, .5]

            elif (user_ans[i] == 'None') and (cor_ans_list[i] == 2):
                opt3_color[i] = [1, 1, 0, .5]

            elif (user_ans[i] == 'None') and (cor_ans_list[i] == 3):
                opt4_color[i] = [1, 1, 0, .5]

        for i in range(5):
            if opt1_color[i] == [1, 1, 0, .5]:
                opt1_right_icon[i] = 'fast-forward'

            elif opt2_color[i] == [1, 1, 0, .5]:
                opt2_right_icon[i] = 'fast-forward'

            elif opt3_color[i] == [1, 1, 0, .5]:
                opt3_right_icon[i] = 'fast-forward'

            elif opt4_color[i] == [1, 1, 0, .5]:
                opt4_right_icon[i] = 'fast-forward'

        for i in range(5):
            if opt1_color[i] == [1, 0, 0, .6]:
                opt1_right_icon[i] = 'close-thick'

            elif opt2_color[i] == [1, 0, 0, .6]:
                opt2_right_icon[i] = 'close-thick'

            elif opt3_color[i] == [1, 0, 0, .6]:
                opt3_right_icon[i] = 'close-thick'

            elif opt4_color[i] == [1, 0, 0, .6]:
                opt4_right_icon[i] = 'close-thick'

        for i in range(5):
            if opt1_color[i] == [0, 1, 0, .5]:
                opt1_right_icon[i] = 'check-bold'

            elif opt2_color[i] == [0, 1, 0, .5]:
                opt2_right_icon[i] = 'check-bold'

            elif opt3_color[i] == [0, 1, 0, .5]:
                opt3_right_icon[i] = 'check-bold'

            elif opt4_color[i] == [0, 1, 0, .5]:
                opt4_right_icon[i] = 'check-bold'

        for i in range(5):
            self.root.ids.result_recycler.data.append({'text': self.data.question[i],
                                                       'qn_icon': qn_icons[i],
                                                       'opt1': self.data.opt1[i],
                                                       'opt2': self.data.opt2[i],
                                                       'opt3': self.data.opt3[i],
                                                       'opt4': self.data.opt4[i],
                                                       'opt1_back': opt1_color[i],
                                                       'opt2_back': opt2_color[i],
                                                       'opt3_back': opt3_color[i],
                                                       'opt4_back': opt4_color[i],
                                                       'opt1_right_icon': opt1_right_icon[i],
                                                       'opt2_right_icon': opt2_right_icon[i],
                                                       'opt3_right_icon': opt3_right_icon[i],
                                                       'opt4_right_icon': opt4_right_icon[i]})
        try:
            self.confirm_skip.dismiss()
        except:
            pass

        try:
            self.force_end_dialog.dismiss()
        except:
            pass

        Clock.schedule_once(self.display_result, 2)


    # showing up the result page
    def display_result(self, *args):
        self.end_load.dismiss()
        self.root.ids.mgr.current = 'Result'

    # updating the scoreboard screen
    def scoreboard_data(self):
        if self.quiz_name in self.tiles:
            self.card = self.contents[self.tiles.index(self.quiz_name)]
            obj = CustomCard()

            if self.card.children[0].text == 'UN ATTEMPTED':
                if self.score == 5:
                    obj.text = 'Excellent'
                    obj.meter = 'Images/Score/meter_5.png'
                    obj.points = ' Score: 5/5'
                    obj.star_1 = 'star'
                    obj.star_2 = 'star'
                    obj.star_3 = 'star'
                    obj.star_4 = 'star'
                    obj.star_5 = 'star'
                    obj.star1_color = rgba(255, 229, 0, 255)
                    obj.star2_color = rgba(255, 229, 0, 255)
                    obj.star3_color = rgba(255, 229, 0, 255)
                    obj.star4_color = rgba(255, 229, 0, 255)
                    obj.star5_color = rgba(255, 229, 0, 255)

                elif self.score == 4:
                    obj.text = 'Very Good'
                    obj.meter = 'Images/Score/meter_4.png'
                    obj.points = 'Score: 4/5'
                    obj.star_1 = 'star'
                    obj.star_2 = 'star'
                    obj.star_3 = 'star'
                    obj.star_4 = 'star'
                    obj.star_5 = 'star-outline'
                    obj.star1_color = rgba(255, 229, 0, 255)
                    obj.star2_color = rgba(255, 229, 0, 255)
                    obj.star3_color = rgba(255, 229, 0, 255)
                    obj.star4_color = rgba(255, 229, 0, 255)
                    obj.star5_color = rgba(255, 255, 255, 255)
                elif self.score == 3:
                    obj.text = 'Fair'
                    obj.meter = 'Images/Score/meter_3.png'
                    obj.points = 'Score: 3/5'
                    obj.star_1 = 'star'
                    obj.star_2 = 'star'
                    obj.star_3 = 'star'
                    obj.star_4 = 'star-outline'
                    obj.star_5 = 'star-outline'
                    obj.star1_color = rgba(255, 229, 0, 255)
                    obj.star2_color = rgba(255, 229, 0, 255)
                    obj.star3_color = rgba(255, 229, 0, 255)
                    obj.star4_color = rgba(255, 255, 255, 255)
                    obj.star5_color = rgba(255, 255, 255, 255)
                elif self.score == 2:
                    obj.text = 'Poor'
                    obj.meter = 'Images/Score/meter_2.png'
                    obj.points = 'Score: 2/5'
                    obj.star_1 = 'star'
                    obj.star_2 = 'star'
                    obj.star_3 = 'star-outline'
                    obj.star_4 = 'star-outline'
                    obj.star_5 = 'star-outline'
                    obj.star1_color = rgba(255, 229, 0, 255)
                    obj.star2_color = rgba(255, 229, 0, 255)
                    obj.star3_color = rgba(255, 255, 255, 255)
                    obj.star4_color = rgba(255, 255, 255, 255)
                    obj.star5_color = rgba(255, 255, 255, 255)
                elif self.score == 1 or self.score == 0:
                    obj.text = 'Very Poor'
                    obj.meter = 'Images/Score/meter_1.png'
                    obj.star_1 = 'star'
                    obj.star_2 = 'star-outline'
                    obj.star_3 = 'star-outline'
                    obj.star_4 = 'star-outline'
                    obj.star_5 = 'star-outline'
                    obj.star1_color = rgba(255, 229, 0, 255)
                    obj.star2_color = rgba(255, 255, 255, 255)
                    obj.star3_color = rgba(255, 255, 255, 255)
                    obj.star4_color = rgba(255, 255, 255, 255)
                    obj.star5_color = rgba(255, 255, 255, 255)
                    if self.score == 1:
                        obj.points = 'Score: 1/5'
                    elif self.score == 0:
                        try:
                            if not self.skipped == '':
                                obj.points = self.skipped
                        except:
                            obj.points = 'Score 0/5'

                self.card.remove_widget(self.card.children[0])
                self.conts[self.tiles.index(self.quiz_name)].remove_widget(
                    self.conts[self.tiles.index(self.quiz_name)].children[0])
                self.card.add_widget(obj)
                self.conts[self.tiles.index(self.quiz_name)].add_widget(self.card)

            else:
                if self.score == 5:
                    obj.text = 'Excellent'
                    obj.meter = 'Images/Score/meter_5.png'
                    obj.points = ' Score: 5/5'
                    obj.star_1 = 'star'
                    obj.star_2 = 'star'
                    obj.star_3 = 'star'
                    obj.star_4 = 'star'
                    obj.star_5 = 'star'
                    obj.star1_color = rgba(255, 229, 0, 255)
                    obj.star2_color = rgba(255, 229, 0, 255)
                    obj.star3_color = rgba(255, 229, 0, 255)
                    obj.star4_color = rgba(255, 229, 0, 255)
                    obj.star5_color = rgba(255, 229, 0, 255)

                elif self.score == 4:
                    obj.text = 'Very Good'
                    obj.meter = 'Images/Score/meter_4.png'
                    obj.points = 'Score: 4/5'
                    obj.star_1 = 'star'
                    obj.star_2 = 'star'
                    obj.star_3 = 'star'
                    obj.star_4 = 'star'
                    obj.star_5 = 'star-outline'
                    obj.star1_color = rgba(255, 229, 0, 255)
                    obj.star2_color = rgba(255, 229, 0, 255)
                    obj.star3_color = rgba(255, 229, 0, 255)
                    obj.star4_color = rgba(255, 229, 0, 255)
                    obj.star5_color = rgba(255, 255, 255, 255)
                elif self.score == 3:
                    obj.text = 'Fair'
                    obj.meter = 'Images/Score/meter_3.png'
                    obj.points = 'Score: 3/5'
                    obj.star_1 = 'star'
                    obj.star_2 = 'star'
                    obj.star_3 = 'star'
                    obj.star_4 = 'star-outline'
                    obj.star_5 = 'star-outline'
                    obj.star1_color = rgba(255, 229, 0, 255)
                    obj.star2_color = rgba(255, 229, 0, 255)
                    obj.star3_color = rgba(255, 229, 0, 255)
                    obj.star4_color = rgba(255, 255, 255, 255)
                    obj.star5_color = rgba(255, 255, 255, 255)
                elif self.score == 2:
                    obj.text = 'Poor'
                    obj.meter = 'Images/Score/meter_2.png'
                    obj.points = 'Score: 2/5'
                    obj.star_1 = 'star'
                    obj.star_2 = 'star'
                    obj.star_3 = 'star-outline'
                    obj.star_4 = 'star-outline'
                    obj.star_5 = 'star-outline'
                    obj.star1_color = rgba(255, 229, 0, 255)
                    obj.star2_color = rgba(255, 229, 0, 255)
                    obj.star3_color = rgba(255, 255, 255, 255)
                    obj.star4_color = rgba(255, 255, 255, 255)
                    obj.star5_color = rgba(255, 255, 255, 255)
                elif self.score == 1 or self.score == 0:
                    obj.text = 'Very Poor'
                    obj.meter = 'Images/Score/meter_1.png'
                    obj.star_1 = 'star'
                    obj.star_2 = 'star-outline'
                    obj.star_3 = 'star-outline'
                    obj.star_4 = 'star-outline'
                    obj.star_5 = 'star-outline'
                    obj.star1_color = rgba(255, 229, 0, 255)
                    obj.star2_color = rgba(255, 255, 255, 255)
                    obj.star3_color = rgba(255, 255, 255, 255)
                    obj.star4_color = rgba(255, 255, 255, 255)
                    obj.star5_color = rgba(255, 255, 255, 255)
                    if self.score == 1:
                        obj.points = 'Score: 1/5'
                    elif self.score == 0:
                        try:
                            if not self.skipped == '':
                                obj.points = self.skipped
                        except:
                            obj.points = 'Score 0/5'

                obj.sep_col = [1, 1, 1, .5]
                obj.radius = [dp(0)]
                self.card.add_widget(obj)
                children = self.card.children[::-1]

                for child in children:
                    child.back = 'Images/Score/score_card.jpg'
                    child.attempt = f'ATTEMPT :{children.index(child) + 1}'
                    child.bg_color = [1, 1, 1, .15]


    # callback for button animation in result page
    def on_scroll(self, scroll_y):
        if scroll_y - self.scroll_pos_y > 0:
            Animation(pos_hint={"center_y": -1}).start(self.root.ids.res_hm)
            Animation(pos_hint={"center_y": -1}).start(self.root.ids.res_hm_icon)
        else:
            Animation(pos_hint={"center_y": 0.06}).start(self.root.ids.res_hm)
            Animation(pos_hint={"center_y": 0.06}).start(self.root.ids.res_hm_icon)


    # displaying the score in backdrop backlayer
    def show_score(self, title):
        title = title.lower()
        title = title[-6::-1]
        title = title[::-1]
        if title in self.tiles:
            self.root.ids.mgr2.current = title
            self.root.ids.backdrop.title = 'Score: ' + title.title() + ' Quiz'
            self.root.ids.backdrop.open(open_up_to = -self.conts[self.tiles.index(title)].height)


    # defining function for resetting the data
    def reset_data(self, *args):
        self.root.ids.pg1_icon.text_color = rgba(17, 20, 219, 255)
        self.root.ids.pg1_back.text_color = [1, 1, 1, 1]
        self.root.ids.pg1_icon.icon = 'numeric-1-circle'
        self.root.ids.pg2_icon.text_color = rgba(17, 20, 219, 255)
        self.root.ids.pg2_back.text_color = [1, 1, 1, 1]
        self.root.ids.pg2_icon.icon = 'numeric-2-circle'
        self.root.ids.pg3_icon.text_color = rgba(17, 20, 219, 255)
        self.root.ids.pg3_back.text_color = [1, 1, 1, 1]
        self.root.ids.pg3_icon.icon = 'numeric-3-circle'
        self.root.ids.pg4_icon.text_color = rgba(17, 20, 219, 255)
        self.root.ids.pg4_back.text_color = [1, 1, 1, 1]
        self.root.ids.pg4_icon.icon = 'numeric-4-circle'
        self.root.ids.pg5_icon.text_color = rgba(17, 20, 219, 255)
        self.root.ids.pg5_back.text_color = [1, 1, 1, 1]
        self.root.ids.pg5_icon.icon = 'numeric-5-circle'
        self.root.ids.opt1_icon.text_color = [1, 1, 1, 1]
        self.root.ids.opt2_icon.text_color = [1, 1, 1, 1]
        self.root.ids.opt3_icon.text_color = [1, 1, 1, 1]
        self.root.ids.opt4_icon.text_color = [1, 1, 1, 1]
        self.root.ids.opt1_icon.icon = 'alpha-a-circle-outline'
        self.root.ids.opt2_icon.icon = 'alpha-b-circle-outline'
        self.root.ids.opt3_icon.icon = 'alpha-c-circle-outline'
        self.root.ids.opt4_icon.icon = 'alpha-d-circle-outline'
        self.callback('Home')
        self.root.ids.progress.value = 0
        self.root.ids.next_qn.text = 'Next'
        self.root.ids.result_recycler.data = []
        self.skipped = ''

# executing the application
if __name__ == "__main__":
    MainApp().run()
