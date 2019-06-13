#QUESTÃO 1
#DADOS DE POPULAÇÃO E NOME DO MUNICÍPIO
def ler_populacao():
    arquivo = open('populacao_CE.csv','r')
    i = 0
    populacao_total = 0
    for linha in arquivo:
        vetor1 = linha.strip('\n')
        vetor = vetor1.split(',')
        if i > 0:
            municipio = vetor[0]
            municipio_populacao.append(municipio)
            populacao_vetor = vetor[1]
            populacao.append(populacao_vetor)
        i+=1
    for i in range(len(populacao)):
        populacao_total += int(populacao[i])
    populacao_estado.append(populacao_total)
    arquivo.close() 

#FROTA TOTAL 2018
def ler_frota2018():
    arquivo = open('frota_CE_2018_06.csv','r')
    frota_total_individual = 0 # TOTAL DA FROTA DE 2018
    frota_total_automoveis = 0
    frota_total_onibus = 0
    frota_total_caminhao = 0
    i = 0
    for linha in arquivo:
        vetor1 = linha.strip('\n')
        vetor = vetor1.split(',')
        if i >0:
            frota = int(vetor[3])
            frota_total.append(frota)
            frota_automoveis_2018 = int(vetor[4])
            frota_total_2018.append(frota_automoveis_2018)
            automoveis_individual = int(vetor[4])
            automoveis.append(automoveis_individual)
            veiculos_individual = int(int(vetor[3])-int(vetor[4]))
            veiculos.append(veiculos_individual)
            onibus_i = int(vetor[15])
            onibus.append(onibus_i)
            caminhao_i = int(vetor[6])
            caminhao.append(caminhao_i)
        i+=1
    for i in range(len(frota_total)):
        frota_total_individual += frota_total[i]
    frota_total_todos.append(frota_total_individual)
    for i in range(len(frota_total_2018)):
        frota_total_automoveis += frota_total_2018[i]
    frota_total_automoveis_2018.append(frota_total_automoveis)
    for i in range(len(onibus)):
        frota_total_onibus += onibus[i]
    frota_total_onibus_2018.append(frota_total_onibus)
    for i in range(len(caminhao)):
        frota_total_caminhao += caminhao[i]
    frota_total_caminhao_2018.append(frota_total_caminhao)
    arquivo.close()

#HABITANTES POR 1000 VEICULOS OU AUTOMOVEIS
def hab_por_1000():
    for i in range(len(populacao)):
        automoveis_calculo = int(populacao[i])/(int(automoveis[i])/1000) 
        habitantes_1000_automoveis.append(automoveis_calculo)
        veiculos_calculo = int(populacao[i])/(int(veiculos[i])/1000)
        habitantes_1000_veiculos.append(veiculos_calculo)

def dicionarios():
    for i in range(len(populacao)):
        municipios_maiores = {}
        municipios_maiores['nome'] = municipio_populacao[i]
        municipios_maiores['populacao'] = int(populacao[i])
        municipios_maiores['frota_total2018'] = frota_total[i]
        municipios_maiores['habitantes_por_1000veículos'] = habitantes_1000_veiculos[i]
        municipios_maiores['frota_automoveis2018'] = automoveis[i]
        municipios_maiores['habitantes_por_1000automóveis'] = habitantes_1000_automoveis[i] 
        maiores.append(municipios_maiores)

def vinte_maiores():
    maiores_organizado = sorted(maiores, key=lambda k: k['populacao'], reverse = True)
    for i in range(len(maiores_organizado)):
        if i <20:
            maiores_correto.append(maiores_organizado[i])                     

#QUESTÃO 2
def motocicletas():
    arquivo = open('frota_CE_2018_06.csv','r')
    i = 0
    total_motocicletas = 0
    for linha in arquivo:
        vetor1 = linha.strip('\n')
        vetor = vetor1.split(',')
        if i > 0:
            total_motocicletas += int(vetor[13])
            motocicletas_individual.append(int(vetor[13]))
        i+=1
    total_motocicletas_lista.append(total_motocicletas)
    arquivo.close()
def percentual_motocicletas():
    for i in range(len(populacao)):
        porcentagem = (int(motocicletas_individual[i])*100)/int(total_motocicletas_lista[0])
        percentual.append(porcentagem)
def dicionario_motocicletas():
    for i in range(len(populacao)):
        maiores_motocicletas_individual = {}
        maiores_motocicletas_individual['nome'] = municipio_populacao[i]
        maiores_motocicletas_individual['frota_total2018'] = frota_total[i]
        maiores_motocicletas_individual['frota_de_motocicletas'] = motocicletas_individual[i]
        maiores_motocicletas_individual['percentual'] = percentual[i]
        maiores_motocicletas.append(maiores_motocicletas_individual)
def vinte_maiores_motocicletas():
    maiores_organizado = sorted(maiores_motocicletas, key=lambda k: k['percentual'], reverse = True)
    for i in range(len(maiores_organizado)):
        if i <20:
            maiores_motocicletas_organizado.append(maiores_organizado[i])

#QUESTÃO 3
def dicionario_automoveis1000():
    for i in range(len(populacao)):
        maiores_automoveis = {}
        maiores_automoveis['nome'] = municipio_populacao[i]
        maiores_automoveis['frota_total2018'] = frota_total[i]
        maiores_automoveis['frota_de_automoveis'] = automoveis[i]
        maiores_automoveis['hab_por_1000'] = habitantes_1000_automoveis[i]
        maiores_automoveis_organizado.append(maiores_automoveis)
def vinte_maiores_automoveis():
    maiores_organizado = sorted(maiores_automoveis_organizado, key=lambda k: k['hab_por_1000'], reverse = True)
    for i in range(len(maiores_organizado)):
        if i <20:
            maiores_automoveis1000.append(maiores_organizado[i])

#QUESTÃO 4
def ler_frota2010():
    arquivo = open('frota_CE_2010_06.csv','r')
    frota_total_individual_2010 = 0
    i = 0
    for linha in arquivo:
        vetor1 = linha.strip('\n')
        vetor = vetor1.split(',')
        if i >0:
            frota = int(vetor[4])
            frota_total_2010.append(frota)
            automoveis_individual_2010 = int(vetor[4])
            automoveis_2010.append(automoveis_individual_2010)
        i+=1
    for i in range(len(frota_total_2010)):
        frota_total_individual_2010 += frota_total_2010[i]
    frota_total_automoveis_2010.append(frota_total_individual_2010)
    arquivo.close() 
def taxa_crescimento():
    for i in range(len(automoveis_2010)):
        percentual = ((int(automoveis[i])*100)/int(automoveis_2010[i]))
        crescimento.append(percentual)
    crescimento_e = ((int(frota_total_automoveis_2018[0])*100)/int(frota_total_automoveis_2010[0]))
    crescimento_estado.append(crescimento_e)
def dicionario_crescimento():
    for i in range(len(populacao)): 
        maiores_automoveisq4 = {}
        maiores_automoveisq4['nome'] = municipio_populacao[i]
        maiores_automoveisq4['hab_por_1000'] = habitantes_1000_automoveis[i]
        maiores_automoveisq4['automoveis2010'] = automoveis_2010[i]
        maiores_automoveisq4['automoveis2018'] = automoveis[i]
        maiores_automoveisq4['crescimento'] = crescimento[i]
        maiores_automoveis_organizadoq4.append(maiores_automoveisq4)
def vinte_maiores_automoveisq4():
    maiores_organizado = sorted(maiores_automoveis_organizadoq4, key=lambda k: k['hab_por_1000'], reverse = True)
    for i in range(len(maiores_organizado)):
        if i <20:
            maiores_automoveisq4.append(maiores_organizado[i])

#QUESTÃO 5
def percentual_populacao_estado():
    for i in range(len(populacao)):
        porcentagem = (int(populacao[i])/int(populacao_estado[0])) * 100
        percentual_populacao.append(porcentagem)
    for i in range(len(populacao)):
        porcentagem = (int((automoveis[i]*100))/int((frota_total_automoveis_2018[0])))
        percentual_automoveis.append(porcentagem)
    for i in range(len(onibus)):
        porcentagem = int((onibus[i]*100))/int(frota_total_onibus_2018[0])
        percentual_onibus.append(porcentagem)
    for i in range(len(caminhao)):
        porcentagem = int((caminhao[i]*100))/int(frota_total_caminhao_2018[0])
        percentual_caminhao.append(porcentagem) 
def escrever_arquivoq5():
    arquivo = open('resumo_NN_TT.csv','w')
    arquivo.write("QUESTÃO 5\n")
    arquivo.write("NOME,POPULAÇÃO,POPULAÇÃO/ESTADO,AUTOMÓVEIS2018,AUTOMÓVEIS/ESTADO,ÔNIBUS2018,ÔNIBUS/ESTADO,CAMINHÃO2018,CAMINHÃO/ESTADO\n")
    for i in range(len(populacao)):
        arquivo.write(str(municipio_populacao[i]) + "," + str(populacao[i]) + "," + str(percentual_populacao[i]) + "," + str(automoveis[i]) + "," + str(percentual_automoveis[i]) + "," + str(onibus[i]) + "," + str(percentual_onibus[i]) + "," + str(caminhao[i]) + "," + str(percentual_caminhao[i]) +","+"\n")
    arquivo.close()
#GERAL
def escrever_arquivo():
    arquivo = open('resultado_NN_TT.txt','w')
    arquivo.write("QUESTÃO 1:\n")
    arquivo.write("NOME,POPULAÇÃO,TOTAL,HABITANTES/1000VEÍCULOS,AUTOMÓVEIS,HABITANTES/1000AUTOMÓVEIS\n")
    for i in range(len(maiores_correto)):
        arquivo.write(str(maiores_correto[i]['nome']) + "," + str(maiores_correto[i]['populacao']) + "," + str(maiores_correto[i]['frota_total2018']) + "," + str(maiores_correto[i]['habitantes_por_1000veículos']) +"%"+ "," + str(maiores_correto[i]['frota_automoveis2018']) + "," + str(maiores_correto[i]['habitantes_por_1000automóveis'])+"%" +"\n")
    arquivo.write("\nQUESTÃO 2:\n")
    arquivo.write("NOME,TOTAL,MOTOCICLETAS,PERCENTUALMOTOCICLETAS\n")
    for i in range(len(maiores_motocicletas_organizado)):
        arquivo.write(str(maiores_motocicletas_organizado[i]['nome'] + "," + str(maiores_motocicletas_organizado[i]['frota_total2018']) + "," + str(maiores_motocicletas_organizado[i]['frota_de_motocicletas']) + "," + str(maiores_motocicletas_organizado[i]['percentual']) + "%" +"\n"))
    arquivo.write("\nQUESTÃO 3:\n")
    arquivo.write("NOME,POPULAÇÃO,AUTOMÓVEIS,HABITANTES/1000AUTOMÓVEIS\n")
    for i in range(len(maiores_automoveis1000)):
        arquivo.write(str(maiores_automoveis1000[i]['nome'] + "," + str(maiores_automoveis1000[i]['frota_total2018']) + "," + str(maiores_automoveis1000[i]['frota_de_automoveis']) + "," + str(maiores_automoveis1000[i]['hab_por_1000']) + "%" +"\n"))
    arquivo.write("\nQUESTÃO 4:\n")
    arquivo.write("NOME,AUTOMOVEIS2010,AUTOMOVEIS2018,CRESCIMENTO\n")
    for i in range(len(maiores_automoveisq4)):
        arquivo.write(str(maiores_automoveisq4[i]['nome']) + "," + str(maiores_automoveisq4[i]['automoveis2010']) + "," + str(maiores_automoveisq4[i]['automoveis2018']) + "," + str(maiores_automoveisq4[i]['crescimento']) + "%" +"\n")
    arquivo.write("CEARÁ," + str(frota_total_automoveis_2018[0]) + "," + str(frota_total_automoveis_2010[0]) + "," + str(crescimento_estado[0]) +"%" +"\n" )
    arquivo.close()          
# #VARIÁVEIS GLOBAIS DA FUNÇÃO LER_POPULAÇÃO
municipio_populacao = []
populacao = []
populacao_estado = []
ler_populacao()

#VARIÁVEIS GLOBAIS DA FUNÇÃO LER_FROTA2010
frota_total = []
frota_total_todos = []
veiculos = []
automoveis = []
frota_total_2018 =[]
frota_total_automoveis_2018 = []
onibus = []
frota_total_onibus_2018 = []
caminhao = []
frota_total_caminhao_2018 = []
ler_frota2018()

#VARIÁVEIS GLOBAIS DA FUNÇÃO HAB_POR_1000
habitantes_1000_veiculos = []
habitantes_1000_automoveis = []
hab_por_1000()

#VARIÁVEIS GLOBAIS DA FUNÇÃO DICIONARIOS
maiores = []
dicionarios()

#VARIAVEIS GLOBAIS DA FUNÇÃO VINTE_MAIORES
maiores_correto = []
vinte_maiores()

#VARIÁVEIS GLOBAIS DA FUNÇÃO MOTOCICLETAS
total_motocicletas_lista = []
motocicletas_individual = []
motocicletas()

#VARIÁVEIS GLOBAIS DA FUNÇÃO PERCENTUAL_MOTOCICLETAS
percentual = []
percentual_motocicletas()

#VARIÁVEIS GLOBAIS DA FUNÇÃO DICIONARIO_MOTOCICLETAS
maiores_motocicletas = []
dicionario_motocicletas()

#VARIAVEIS GLOBAIS DA FUNÇÃO VINTE_MAIORES_MOTOCICLETAS
maiores_motocicletas_organizado = []

#VARIÁVEIS GLOBAIS DA FUNÇÃO VINTE_MAIORES_MOTOCICLETAS
vinte_maiores_motocicletas()

#VARIÁVEIS GLOBAIS DA FUNÇÃO DICIONARIO_AUTOMOVEIS1000
maiores_automoveis1000 = []
maiores_automoveis_organizado = []
dicionario_automoveis1000()

#VARIÁVEIS GLOBAIS DA FUNÇÃO VINTE_MAIORES_AUTOMOVEIS
vinte_maiores_automoveis()

#VARIÁVEIS GLOBAIS DA FUNÇÃO LER_FROTA2010
frota_total = []
automoveis_2010 = []
frota_total_automoveis_2010 = []
frota_total_2010 = []
ler_frota2010()

#VARIÁVEIS GLOBAIS DA FUNÇÃO TAXA_CRESCIMENTO
crescimento = []
crescimento_estado = []
taxa_crescimento()

#VARIÁVEIS GLOBAIS DA FUNÇÃO DICIONARIO_CRESCIMENTO
maiores_automoveis_organizadoq4 = []
maiores_automoveisq4 =[]
dicionario_crescimento()

#VÁRIAVEIS GLOBAIS DA FUNÇÃO VINTE_MAIORES_AUTOMOVEIS_Q4
vinte_maiores_automoveisq4()

#VARIÁVEIS GLOBAIS DA FUNÇÃO PERCENTUAL_POPULACAO_ESTADO
percentual_populacao = []
percentual_automoveis = []
percentual_onibus = []
percentual_caminhao = []
percentual_populacao_estado()

#VARIÁVEIS GLOBAIS DA FUNÇÃO ESCREVER_ARQUIVO
escrever_arquivo()

#VARIÁVEIS GLOBAIS DA FUNÇÃO ESCREVER_ARQUIVOQ5
escrever_arquivoq5()