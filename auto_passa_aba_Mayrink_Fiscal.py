# ----------- IMPORTANTE1! VOCÊ DEVE TER O GOOGLE CHROME INSTALADO EM SUA MAQUINA -------------
# ----------- IMPORTANTE2! VOCÊ DEVE TER O ARQUIVO CHROMEDRIVER.EXE (OU EQUIVALENTE PARA LINUX) DA VERSÃO DO NAVEGADOR NA PASTA DESSE ARQUIVO -------------

# ----------- IMPORTANTE3! TIRE O # DA LINNHA 6 SOMENTE NA PRIMEIRA VEZ QUE EXECUTAR -------------

#!pip install selenium

# ----------- IMPORTANTE! Coloque os parametros iniciais abaixo -------------
# ----------- IMPORTANTE! Crie um arquivo desse para cada processo de passagem de aba -------------

url = "http://sped.suaom.eb.mil.br" #url da tela de login do sped de sua om

# Obtendo as informações iniciais de login do sped:
usuario = 'usuario' #troque o texto entre aspas pelo seu nome de usuário

senha = input('Digite sua senha: ') #não mexa nessa linha a menos que queira adicionar um # no inicio da linha
# senha = '123456' #caso somente você tenha acesso a esse computador, insira sua senha no espaço entre aspas dessa linha, remova o # dessa linha e coloque # no inicio da linha de cima


nomeAbaAdm = "SPED2" # esse é o nome da aba de adm que você tem acesso

nomeAbaModificar = "Fisc Adm - Ch" # esse é o nome da aba que você quer transferir o detentor

usuarioRecebeAba = "Cap JOSÉ" # esse é o nome do usuário que vai receber a aba



# --------------------------------------------------------------------------------------------------------------


# # A PARTIR DESSE PONTO, NÃO MEXA EM NADA A MENOS QUE VOCÊ SAIBA O QUE ESTÁ FAZENDO!

#preparando ambientes e importando bibliotecas necessárias
from selenium import webdriver #carregar webdriver
from selenium.webdriver.common import keys #usar teclado
from selenium.webdriver.common import by #localizar xpath
from selenium.webdriver.support.select import Select #para trabalhar com select
from selenium.webdriver.support.ui import WebDriverWait #async methods
import warnings
warnings.filterwarnings("ignore")


nav = webdriver.Chrome("./chromedriver.exe") #abre navegador

# %%
# entra na tela de login do sped
nav.get(url) #get(url)
nav.maximize_window

# %%
#fazer login no sped
nav.find_element_by_xpath('/html/body/form/center/div/div[3]/table/tbody/tr[3]/td/input').send_keys(usuario)
nav.find_element_by_xpath('/html/body/form/center/div/div[3]/table/tbody/tr[5]/td/input').send_keys(senha)
loadcnet = False
nav.find_element_by_xpath('/html/body/form/center/div/div[3]/table/tbody/tr[7]/td/input').click()

# %%
# seleciona a aba
nav.get(url + '/sped/design/eb/banner.jsp')
nav.find_element_by_xpath('/html/body/div[3]/span[5]/a').click()


# %%
# clica em contas
nav.get(url + '/sped/administracao/usuario/UsuarioAction.do?method=listarUsuario')

# %%
# escolhe a conta desejada
# nomeAbaModificar
aaa = nav.find_element_by_link_text(nomeAbaModificar).click()

# %%
# marca a associação ativa se houver
nav.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[3]/td/table[2]/tbody/tr[3]/td/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td[1]/div/input').click()
nav.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[3]/td/table[3]/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr/td[1]/div/input').click()
nav.back()

# %%
# clica em adicionar associação
nav.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[3]/td/table[3]/tbody/tr[3]/td/table/tbody/tr[5]/td/table/tbody/tr/td[3]/div/input').click()


# %%
# escolhe o usuario
selectElm = nav.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[4]/td[2]/select')
sel_obj = Select(selectElm)
try:
    sel_obj.select_by_visible_text(usuarioRecebeAba).click()
except:
    print('selecionou')

# %%
# salva
nav.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[13]/td/table/tbody/tr/td[3]/div/input').click()


# %%
# fecha o browser
nav.close()


