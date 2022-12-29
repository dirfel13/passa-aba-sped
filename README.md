# passa-aba-sped
Script em Python para passar a abas de um usuário a outro no Sped.

O Sped é um dos sistemas informatizados do Exército Brasileiro, nele tramitam documentos administrativos por meio da ebnet (intranet do Exército).

Cada usuário possuiuma ou mais aba dependendo de quantos encargos possui na Organização Militar, essas abas devem ser passadas a outro militar em caso de afastamentos (férias, missão, passagem de função, ...).

Muitas vezes a atribuição da passar abas a outros usuários é da Seção de Informática da OM. Esse script visa automatizar esse processo controlando o browser do usuário e realizando essa tarefa de maneira muito rápida.

as tecnologias utilizadas para que esse script funcione são:
- Navegador Google Chrome;
- Chromedriver;
- Linguagem python3; e
- Bibliteca Selenium.


# Passo-a-passo
Para executar o script siga os passo a seguir:
1. Instale o naegador Google Chrome

2. Verifique qual a versão foi instalada

3. Baixe o chromedriver da versão do navegador em: https://chromedriver.chromium.org/downloads
- Obs: Toda vez que o navegador for atualizado, é necessário uma nova versão do driver.

4. Instale o Python3 em seu computador

5. Edite o script (auto_passa_aba.py), com um editor de código ou bloco de notas, colocando as informações necessárias para o login no sistema e os dados da aba e de quem receberá ela.

6. Crie um script para cada usuário que deseja passar a aba.

7. Execute o arquivo do script (.py)


Caso deseje realizar um pull request, sinta-se a vontade, todas as melhorias são bem vindas.
Recomendo conhecimento básico de python3 para utilizar
