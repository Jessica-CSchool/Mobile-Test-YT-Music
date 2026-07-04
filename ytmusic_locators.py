from appium.webdriver.common.appiumby import AppiumBy

class YTMusicLocators:

    # busca musica
    SEARCH_BUTTON = (AppiumBy.ID, "com.google.android.apps.youtube.music:id/action_search_button")
    SEARCH_FIELD = (AppiumBy.ID, "com.google.android.apps.youtube.music:id/search_edit_text")
    SEARCH_ICON = (AppiumBy.ID, "com.google.android.apps.youtube.music:id/search_type_icon")
    
    #resultado da busca
    RESULTS_SELECTOR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(4)')
    @staticmethod
    def get_song_by_name(nome_musica):
        return (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().descriptionContains("{nome_musica}")')
    
    # O botão de 3 pontinhos (Action menu) para abrir o menu da música
    ACTION_MENU = (AppiumBy.ACCESSIBILITY_ID, "Action menu")
    
    # Opção "Save to library" / "Remove from library"
    SAVE_TO_LIBRARY_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(4)')
    REMOVE_FROM_LIBRARY_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Remove from library")')

    # Botao no menu do footer
    LIBRARY_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Library")')
    BTN_HOME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Home")')
    BTN_EXPLORE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Explore")')

    #menu suspenso library
    LIBRARY_SELECTION_LIST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Library")')

    # tabs da library
    SELECTOR_SONG_IN_LIBRARY = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Songs")')
    SELECTOR_X_IN_LIBRARY = (AppiumBy.ID, 'com.google.android.apps.youtube.music:id/search_clear_button_icon')
    EPISODES_FOR_LATER_CONTAINER = (AppiumBy.ID, 'com.google.android.apps.youtube.music:id/details_container')
    
    # elementos da library
    MUSIC_IN_LIBRARY = (AppiumBy.ID, 'com.google.android.apps.youtube.music:id/title')
    BAND_IN_LIBRARY = (AppiumBy.ID, 'com.google.android.apps.youtube.music:id/subtitle')

    #menu explore
    GENRES_AND_MOODS_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(10)')
    GENRES_AND_MOODS_TITLE = (AppiumBy.ID, 'com.google.android.apps.youtube.music:id/two_line_header')
    GENRE_BLUES = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Blues")')
    GENRE_AFRICAN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("African")')
    GENRE_TITLE_PAGE = (AppiumBy.ID, 'com.google.android.apps.youtube.music:id/toolbar_title')

    #Offline message
    NETWORK_ERROR_MESSAGE = (AppiumBy.ID, 'com.google.android.apps.youtube.music:id/error_message_text')
    
