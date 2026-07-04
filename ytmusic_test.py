import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ytmusic_locators import YTMusicLocators

class TestYTMusic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "uiautomator2"
        options.app_package = "com.google.android.apps.youtube.music"
        options.app_activity = "com.google.android.apps.youtube.music.activities.MusicActivity"
        options.new_command_timeout = 3600
        options.set_capability('adbExecTimeout', 60000)
        
        cls.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    def setUp(self):
        # Espera até que o aplicativo esteja pronto para interação
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(YTMusicLocators.BTN_HOME))

    # Precondicao: O usuário deve estar logado no aplicativo do YouTube Music
    def test_search_and_add_to_library_song(self):

        #Variaveis
        artista = "Imagine Dragons"
        musica = "Believer"
        termo_busca = f"{artista} {musica}"

        wait = WebDriverWait(self.driver, 20) 

        # Buscar musica para adicionar na library
        search_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.SEARCH_BUTTON))
        search_btn.click()

        search_field = wait.until(EC.presence_of_element_located(YTMusicLocators.SEARCH_FIELD))
        search_field.send_keys(termo_busca)

        search_icon = wait.until(EC.element_to_be_clickable(YTMusicLocators.SEARCH_ICON))
        search_icon.click()

        locator = YTMusicLocators.get_song_by_name(musica)
        elemento_encontrado = wait.until(EC.presence_of_element_located(locator))
            
        self.assertTrue(elemento_encontrado.is_displayed(), "A música não foi exibida")

        # save to library
        action_menu = wait.until(EC.element_to_be_clickable(YTMusicLocators.ACTION_MENU))
        action_menu.click()
        
        save_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.SAVE_TO_LIBRARY_OPTION))
        save_btn.click()

        # back home
        btn_home = wait.until(EC.element_to_be_clickable(YTMusicLocators.BTN_HOME))
        btn_home.click()

        # Verifica se a música foi adicionada à biblioteca (gambiarra pra tirar os alerts)
        library_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.LIBRARY_BTN))
        library_btn.click()
        library_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.EPISODES_FOR_LATER_CONTAINER))
        library_btn.click()
        library_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.LIBRARY_BTN))
        library_btn.click()

        selector_songs = wait.until(EC.element_to_be_clickable(YTMusicLocators.SELECTOR_SONG_IN_LIBRARY))
        selector_songs.click()

        # Verifica que a primeira música e a banda estão corretas na biblioteca (a inserida)
        music_in_library = wait.until(EC.presence_of_element_located(YTMusicLocators.MUSIC_IN_LIBRARY))
        band_in_library = wait.until(EC.presence_of_element_located(YTMusicLocators.BAND_IN_LIBRARY))   

        # Capturando os textos
        texto_musica = music_in_library.text
        texto_banda = band_in_library.text

        # Realizando as validações (Asserts)
        self.assertIn(musica, texto_musica, f"Esperado: {musica}, Encontrado: {texto_musica}")
        self.assertIn(artista, texto_banda, f"Esperado: {artista}, Encontrado: {texto_banda}")
        
        print(f"Validação concluída: {texto_musica} - {texto_banda}")

  
    def test_remove_song_from_library(self):
        wait = WebDriverWait(self.driver, 20) 

        # salvar duas musicas na library pra poder deletar uma
        for i in range(1, 4):
            xpath_menu = f'(//android.view.ViewGroup[@content-desc="Action menu"])[{i}]'
            action_menu = wait.until(EC.element_to_be_clickable(('xpath', xpath_menu)))
            action_menu.click()
            save_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.SAVE_TO_LIBRARY_OPTION))
            save_btn.click()
        
        # Tab library
        library_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.LIBRARY_BTN))
        library_btn.click()
        library_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.EPISODES_FOR_LATER_CONTAINER))
        library_btn.click()
        library_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.LIBRARY_BTN))
        library_btn.click()
        selector_songs = wait.until(EC.element_to_be_clickable(YTMusicLocators.SELECTOR_SONG_IN_LIBRARY))
        selector_songs.click()

        # Guarda qual a primeira musica
        music_in_library = wait.until(EC.presence_of_element_located(YTMusicLocators.MUSIC_IN_LIBRARY))
        texto_musica_1 = music_in_library.text

        # Remove a música da biblioteca
        action_menu = wait.until(EC.element_to_be_clickable(YTMusicLocators.ACTION_MENU))
        action_menu.click()
        remove_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.REMOVE_FROM_LIBRARY_OPTION))
        remove_btn.click()

        #clear
        clear_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.SELECTOR_X_IN_LIBRARY))
        clear_btn.click()

        # acessa songs
        selector_songs = wait.until(EC.element_to_be_clickable(YTMusicLocators.SELECTOR_SONG_IN_LIBRARY))
        selector_songs.click()

        # Verifica se a música foi removida da biblioteca
        music_in_library = wait.until(EC.presence_of_element_located(YTMusicLocators.MUSIC_IN_LIBRARY))
        texto_musica_2 = music_in_library.text
        self.assertNotEqual(texto_musica_2, texto_musica_1, f"Erro! A música '{texto_musica_1}' ainda aparece no topo da lista.")

        #clear
        clear_btn = wait.until(EC.element_to_be_clickable(YTMusicLocators.SELECTOR_X_IN_LIBRARY))
        clear_btn.click()


    # def test_explore_genres_and_moods(self):
        #pass

    #Precondicao: O usuário deve estar OFFLINE
    # def test_explore_genres_and_moods_navigation(self):
        #pass


    def tearDown(self):
        try:
            btn_home = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(YTMusicLocators.BTN_HOME))
            btn_home.click()
        except:
            print("Não foi possível retornar à home no tearDown.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()