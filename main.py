"""
Bible App for Python 3.11
Run with: python bible_app.py
"""

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard

# Set window size
Window.size = (400, 700)

KV = '''
ScreenManager:
    HomeScreen:
    ChaptersScreen:
    VersesScreen:

<HomeScreen>:
    name: 'home'
    
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 0
        
        MDTopAppBar:
            title: "Holy Bible"
            elevation: 4
            md_bg_color: 0.12, 0.12, 0.12, 1
            specific_text_color: 1, 1, 1, 1
            size_hint_y: None
            height: dp(56)
        
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(60)
            padding: [dp(20), dp(10), dp(20), 0]
            
            MDSegmentedButton:
                size_hint_x: 1
                height: dp(40)
                
                MDSegmentedButtonItem:
                    text: "Old Testament"
                    on_release: app.load_books('old')
                    selected: True
                
                MDSegmentedButtonItem:
                    text: "New Testament"
                    on_release: app.load_books('new')
        
        ScrollView:
            MDBoxLayout:
                id: books_container
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(20)
                adaptive_height: True

<ChaptersScreen>:
    name: 'chapters'
    
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            id: chapters_bar
            title: "Chapters"
            elevation: 4
            md_bg_color: 0.12, 0.12, 0.12, 1
            specific_text_color: 1, 1, 1, 1
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
            size_hint_y: None
            height: dp(56)
        
        ScrollView:
            MDBoxLayout:
                id: chapters_container
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(20)
                adaptive_height: True

<VersesScreen>:
    name: 'verses'
    
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            id: verses_bar
            title: "Verses"
            elevation: 4
            md_bg_color: 0.12, 0.12, 0.12, 1
            specific_text_color: 1, 1, 1, 1
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
            right_action_items: [["bookmark-outline", lambda x: app.show_message("Bookmark added!")]]
            size_hint_y: None
            height: dp(56)
        
        ScrollView:
            MDBoxLayout:
                id: verses_container
                orientation: 'vertical'
                spacing: dp(15)
                padding: dp(20)
                adaptive_height: True
'''

class HomeScreen(Screen):
    pass

class ChaptersScreen(Screen):
    pass

class VersesScreen(Screen):
    pass

class BibleApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_book = ""
        self.current_chapter = 1
        self.previous_screen = "home"
        
        # Complete Bible books
        self.old_testament = [
            "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
            "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
            "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles",
            "Ezra", "Nehemiah", "Esther", "Job", "Psalms",
            "Proverbs", "Ecclesiastes", "Song of Solomon", "Isaiah",
            "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea",
            "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum",
            "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi"
        ]
        
        self.new_testament = [
            "Matthew", "Mark", "Luke", "John", "Acts",
            "Romans", "1 Corinthians", "2 Corinthians", "Galatians",
            "Ephesians", "Philippians", "Colossians", "1 Thessalonians",
            "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus",
            "Philemon", "Hebrews", "James", "1 Peter", "2 Peter",
            "1 John", "2 John", "3 John", "Jude", "Revelation"
        ]
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.material_style = "M2"
        
        return Builder.load_string(KV)
    
    def go_back(self):
        """Navigate back to previous screen"""
        if self.root.current == "chapters":
            self.root.current = "home"
        elif self.root.current == "verses":
            self.root.current = "chapters"
    
    def show_message(self, message):
        """Show a snackbar message"""
        from kivymd.uix.snackbar import Snackbar
        Snackbar(text=message, bg_color=[0.2, 0.2, 0.2, 1]).open()
    
    def load_books(self, testament):
        """Load books into home screen"""
        home_screen = self.root.get_screen('home')
        books_container = home_screen.ids.books_container
        books_container.clear_widgets()
        
        books = self.old_testament if testament == 'old' else self.new_testament
        
        for book in books:
            # Create a card for each book
            card = MDCard(
                orientation='vertical',
                size_hint_y=None,
                height=dp(60),
                padding=dp(15),
                md_bg_color=[0.15, 0.15, 0.15, 1],
                radius=[10, 10, 10, 10],
                ripple_behavior=True,
                on_release=lambda x, b=book: self.open_chapters(b)
            )
            
            # Add book name
            label = MDLabel(
                text=book,
                theme_text_color="Custom",
                text_color=[1, 1, 1, 1],
                size_hint_y=None,
                height=dp(30),
                font_style="Title",
                role="medium"
            )
            
            card.add_widget(label)
            books_container.add_widget(card)
    
    def open_chapters(self, book):
        """Open chapters for selected book"""
        self.current_book = book
        self.root.current = 'chapters'
        
        chapters_screen = self.root.get_screen('chapters')
        chapters_screen.ids.chapters_bar.title = book
        chapters_container = chapters_screen.ids.chapters_container
        chapters_container.clear_widgets()
        
        # Determine number of chapters (simplified)
        num_chapters = 50 if book in ["Psalms", "Genesis"] else 24
        
        for i in range(1, min(num_chapters + 1, 31)):  # Show up to 30 chapters
            # Create chapter card
            card = MDCard(
                orientation='vertical',
                size_hint_y=None,
                height=dp(60),
                padding=dp(15),
                md_bg_color=[0.15, 0.15, 0.15, 1],
                radius=[10, 10, 10, 10],
                ripple_behavior=True,
                on_release=lambda x, c=i: self.open_verses(c)
            )
            
            label = MDLabel(
                text=f"Chapter {i}",
                theme_text_color="Custom",
                text_color=[1, 1, 1, 1],
                font_style="Title",
                role="medium"
            )
            
            card.add_widget(label)
            chapters_container.add_widget(card)
    
    def open_verses(self, chapter):
        """Open verses for selected chapter"""
        self.current_chapter = chapter
        self.root.current = 'verses'
        
        verses_screen = self.root.get_screen('verses')
        verses_screen.ids.verses_bar.title = f"{self.current_book} {chapter}"
        verses_container = verses_screen.ids.verses_container
        verses_container.clear_widgets()
        
        # Sample verses from different books
        verses = {
            "Genesis": [
                "In the beginning God created the heavens and the earth.",
                "Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.",
                "And God said, 'Let there be light,' and there was light.",
                "God saw that the light was good, and he separated the light from the darkness.",
                "God called the light 'day,' and the darkness he called 'night.' And there was evening, and there was morning - the first day."
            ],
            "John": [
                "In the beginning was the Word, and the Word was with God, and the Word was God.",
                "He was with God in the beginning.",
                "Through him all things were made; without him nothing was made that has been made.",
                "In him was life, and that life was the light of all mankind.",
                "The light shines in the darkness, and the darkness has not overcome it."
            ],
            "Psalms": [
                "Blessed is the one who does not walk in step with the wicked or stand in the way that sinners take or sit in the company of mockers.",
                "But whose delight is in the law of the LORD, and who meditates on his law day and night.",
                "That person is like a tree planted by streams of water, which yields its fruit in season and whose leaf does not wither - whatever they do prospers.",
                "Not so the wicked! They are like chaff that the wind blows away.",
                "Therefore the wicked will not stand in the judgment, nor sinners in the assembly of the righteous."
            ]
        }
        
        # Get verses for current book or use default
        book_verses = verses.get(self.current_book, [
            f"Verse {i}: This is a sample verse from {self.current_book} chapter {chapter}." 
            for i in range(1, 11)
        ])
        
        for i, verse_text in enumerate(book_verses[:10], 1):
            # Create verse card
            card = MDCard(
                orientation='vertical',
                size_hint_y=None,
                height=dp(80),
                padding=dp(15),
                md_bg_color=[0.12, 0.12, 0.12, 1],
                radius=[8, 8, 8, 8],
                ripple_behavior=True
            )
            
            # Verse number
            number_label = MDLabel(
                text=f"{i}",
                theme_text_color="Custom",
                text_color=[0.9, 0.6, 0.1, 1],
                size_hint_y=None,
                height=dp(20),
                font_style="Label",
                role="small"
            )
            
            # Verse text
            text_label = MDLabel(
                text=verse_text,
                theme_text_color="Custom",
                text_color=[1, 1, 1, 0.9],
                size_hint_y=None,
                height=dp(50),
                font_style="Body",
                role="large"
            )
            
            card.add_widget(number_label)
            card.add_widget(text_label)
            verses_container.add_widget(card)

if __name__ == "__main__":
    BibleApp().run()