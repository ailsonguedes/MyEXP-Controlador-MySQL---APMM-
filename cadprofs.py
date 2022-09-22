from PyQt5 import uic,QtWidgets
import pandas as pd
import mysql.connector

numero_id = 0

banco = mysql.connector.connect (
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_professores"
)

def main_screen():
    print("Confere")
    linha1 = cadprofs_mainscreen.lineEdit_1.text() #nome
    linha2 = cadprofs_mainscreen.lineEdit_2.text() #cpf
    linha3 = cadprofs_mainscreen.lineEdit_3.text() #colegio atual
    linha4 = cadprofs_mainscreen.lineEdit_4.text() #endereço
    linha5 = cadprofs_mainscreen.lineEdit_5.text() #nivel
    linha6 = cadprofs_mainscreen.lineEdit_6.text() #nascimento
    linha7 = cadprofs_mainscreen.lineEdit_7.text() #valorplano
    linha8 = cadprofs_mainscreen.lineEdit_8.text() #celular
    linha9 = cadprofs_mainscreen.lineEdit_9.text() #observacoes

    sexo = ""
    nascimento = ""
    contratacao = ""
    plano = ""

    if cadprofs_mainscreen.radioButton_1.isChecked():
        print("sexo masculino foi selecionado")
        sexo = "masculino"
    elif cadprofs_mainscreen.radioButton_2.isChecked():
        print("sexo feminino foi selecionado")
        sexo = "feminino"
    else:
        print("none")
        sexo = "none"

    if cadprofs_mainscreen.checkBox.isChecked():
        print("Contratado foi selecionado")
        contratacao = "Contratado"
    elif cadprofs_mainscreen.checkBox_2.isChecked():
        print("Efetivo foi selecionado")
        contratacao = "Efetivo"
    else:
        print("none")
        contratacao = "none"
    

    if cadprofs_mainscreen.checkBox_3.isChecked():
        print("Sim foi selecionado")
        plano = "sim"
    elif cadprofs_mainscreen.checkBox_4.isChecked():
        print("Não foi selecionado")
        plano = "Não"
    else:
        print("none")
        plano = "none"

    #cadprofs_mainscreen.dateEdit

    print("Nome:", linha1) #Nome
    print("Cpf:", linha2) #Cpf
    print("Instituição de Ensino:", linha3) #Colégio Atual
    print("Endereço:", linha4) #Nascimento
    print("Nivel:", linha5)
    print("Data de Nascimento:", linha6)
    print("Valor do Plano:", linha7)
    print("Celular:", linha8)
    print("Observações:", linha9)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO lista_dados (nome,cpf,colegio,endereco,nivel,nascimento,sexo,contratacao,plano,valorplano,celular,observacoe) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6), sexo, contratacao, plano, str(linha7), str(linha8), str(linha9))
    cursor.execute(comando_SQL, dados)
    banco.commit() 

    cadprofs_mainscreen.lineEdit_1.setText("")
    cadprofs_mainscreen.lineEdit_2.setText("")
    cadprofs_mainscreen.lineEdit_3.setText("")
    cadprofs_mainscreen.lineEdit_4.setText("")
    cadprofs_mainscreen.lineEdit_5.setText("")
    cadprofs_mainscreen.lineEdit_6.setText("")
    cadprofs_mainscreen.lineEdit_7.setText("")
    cadprofs_mainscreen.lineEdit_8.setText("")
    cadprofs_mainscreen.lineEdit_9.setText("")

def edit_screen():
    cadprofs_editscreen.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM lista_dados"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    cadprofs_editscreen.tableWidget.setRowCount(len(dados_lidos))
    cadprofs_editscreen.tableWidget.setColumnCount(13)

    for i in range (0, len(dados_lidos)):
        for j in range (0, 13):
            cadprofs_editscreen.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def menu_edit():
    global numero_id
    linha = cadprofs_editscreen.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM lista_dados")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM lista_dados WHERE id =" + str(valor_id))
    lista_dados = cursor.fetchall()
    cadprofs_menueditscreen.show()

    numero_id = valor_id

    cadprofs_menueditscreen.lineEdit_1.setText(str(lista_dados[0][0]))
    cadprofs_menueditscreen.lineEdit_2.setText(str(lista_dados[0][1]))
    cadprofs_menueditscreen.lineEdit_3.setText(str(lista_dados[0][2]))
    cadprofs_menueditscreen.lineEdit_4.setText(str(lista_dados[0][3]))
    cadprofs_menueditscreen.lineEdit_5.setText(str(lista_dados[0][5]))
    cadprofs_menueditscreen.lineEdit_6.setText(str(lista_dados[0][6])) 
    cadprofs_menueditscreen.lineEdit_7.setText(str(lista_dados[0][4]))
    cadprofs_menueditscreen.lineEdit_8.setText(str(lista_dados[0][7]))
    cadprofs_menueditscreen.lineEdit_9.setText(str(lista_dados[0][8]))
    cadprofs_menueditscreen.lineEdit_10.setText(str(lista_dados[0][9]))
    cadprofs_menueditscreen.lineEdit_11.setText(str(lista_dados[0][10]))
    cadprofs_menueditscreen.lineEdit_13.setText(str(lista_dados[0][11]))
    cadprofs_menueditscreen.lineEdit_12.setText(str(lista_dados[0][12]))

def salvar_edit():
    global numero_id

    nome = cadprofs_menueditscreen.lineEdit_2.text()
    cpf = cadprofs_menueditscreen.lineEdit_3.text()
    colegio = cadprofs_menueditscreen.lineEdit_4.text()
    endereco = cadprofs_menueditscreen.lineEdit_5.text()
    nivel = cadprofs_menueditscreen.lineEdit_6.text()
    nascimento = cadprofs_menueditscreen.lineEdit_7.text()
    sexo = cadprofs_menueditscreen.lineEdit_8.text()
    contratacao = cadprofs_menueditscreen.lineEdit_9.text()
    plano = cadprofs_menueditscreen.lineEdit_10.text()
    valorplano = cadprofs_menueditscreen.lineEdit_11.text()
    observacoe = cadprofs_menueditscreen.lineEdit_12.text()
    celular = cadprofs_menueditscreen.lineEdit_13.text()

    cursor = banco.cursor()
    cursor.execute("UPDATE lista_dados SET nome = '{}', cpf = '{}', colegio = '{}', nascimento = '{}', endereco = '{}', nivel = '{}',  sexo = '{}', contratacao = '{}', plano = '{}', valorplano = '{}', celular = '{}', observacoe = '{}' WHERE id = {}".format(nome,cpf,colegio,nascimento,endereco,nivel,sexo,contratacao,plano,valorplano,celular,observacoe,numero_id))

    cadprofs_menueditscreen.close()
    cadprofs_editscreen.close()
    edit_screen()

def delete_line():
    linha = cadprofs_editscreen.tableWidget.currentRow()
    cadprofs_editscreen.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM lista_dados")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM lista_dados WHERE id =" + str(valor_id))

def gen_csv():
    print('funcionou')
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM lista_dados"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    csvc = pd.DataFrame(data= dados_lidos)
    csvc.columns = ['ID', 'NOME', 'CPF','COLÉGIO','ENDEREÇO', 'NÍVEL', 'NASCIMENTO', 'SEXO', 'CONTRATAÇÃO', 'PLANO DE SAÚDE', 'VALOR DO PLANO', 'CELULAR', 'OBSERVAÇÕES'] 
    csvc.to_csv('cadastro_professores.csv', index= False)

    cadprofs_editscreen.close()

def gen_excel():
    print('funcionou')
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM lista_dados"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    xlsc = pd.DataFrame(data= dados_lidos)
    xlsc.columns = ['ID', 'NOME', 'CPF','COLÉGIO','ENDEREÇO', 'NÍVEL', 'NASCIMENTO', 'SEXO', 'CONTRATAÇÃO', 'PLANO DE SAÚDE', 'VALOR DO PLANO', 'CELULAR', 'OBSERVAÇÕES'] 
    xlsc.to_excel('cadastro_professores.xls', index= False)

    cadprofs_editscreen.close()

app=QtWidgets.QApplication([])
cadprofs_mainscreen=uic.loadUi("cadprofs.ui") # tela 1 (tela principal)
cadprofs_editscreen=uic.loadUi("cadprofsedit.ui") # tela 2 (tela de edição)
cadprofs_menueditscreen=uic.loadUi("cadprofsmenuedit.ui") # tela 3 (menu de edição)

cadprofs_mainscreen.pushButton_1.clicked.connect(main_screen) #chama a função main_screen
cadprofs_mainscreen.pushButton_2.clicked.connect(edit_screen) #chama a função edit_screen
cadprofs_editscreen.pushButton_3.clicked.connect(menu_edit) #chama a função menu_edit
cadprofs_menueditscreen.pushButton_7.clicked.connect(salvar_edit) #salva os dados editados
cadprofs_editscreen.pushButton_4.clicked.connect(delete_line) #deleta os dados selecionados
cadprofs_editscreen.pushButton_5.clicked.connect(gen_csv) #gera um arquivo csv
#cadprofs_editscreen.pushButton_6.clicked.connect(gen_excel) #gera um arquvo excel

cadprofs_mainscreen.show()
app.exec()



""" create table lista_dados (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50),
    cpf VARCHAR (20), 
    colegio VARCHAR(50),
    nascimento VARCHAR(50),
    endereco VARCHAR(50),
    nivel VARCHAR(50),
    sexo VARCHAR(50),
    contratacao VARCHAR(50),
    plano VARCHAR(50),
    valorplano VARCHAR(50),
    celular VARCHAR(50),
    observacoe VARCHAR(250),
    PRIMARY KEY (id)
); """

# - POWERED BY: Ailson Guedes Da Fonseca
# - LinkedIn: https://www.linkedin.com/in/ailson-guedes-059795149/
# - GitHub: https://github.com/ailsonguedes