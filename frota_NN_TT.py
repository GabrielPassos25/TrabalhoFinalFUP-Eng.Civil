#QUESTÃO 1
#DADOS DE POPULAÇÃO E NOME DO MUNICÍPIO
def ler_populacao():
    arquivo = open('populacao_CE.csv','r')
    i = 0
    for linha in arquivo:
        vetor1 = linha.strip('\n')
        vetor = vetor1.split(',')
        if i > 0:
            municipio = vetor[0]
            municipio_populacao.append(municipio)
            populacao_vetor = vetor[1]
            populacao.append(populacao_vetor)
        i+=1
    arquivo.close() 

#FROTA TOTAL 2018
def ler_frota2018():
    arquivo = open('frota_CE_2018_06.csv','r')
    frota_total_individual = 0 # TOTAL DA FROTA DE 2018
    i = 0
    for linha in arquivo:
        vetor1 = linha.strip('\n')
        vetor = vetor1.split(',')
        if i >0:
            frota = int(vetor[3])
            frota_total.append(frota)
            automoveis_individual = int(vetor[4])
            automoveis.append(automoveis_individual)
            veiculos_individual = int(int(vetor[3])-int(vetor[4]))
            veiculos.append(veiculos_individual)
        i+=1
    for i in range(len(frota_total)):
        frota_total_individual += frota_total[i]
    frota_total_todos.append(frota_total_individual)
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
    print(maiores_correto)                      

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
        print(maiores_motocicletas_organizado)
        arquivo.write(str(maiores_motocicletas_organizado[i]['nome'] + "," + str(maiores_motocicletas_organizado[i]['frota_total2018']) + "," + str(maiores_motocicletas_organizado[i]['frota_de_motocicletas']) + "," + str(maiores_motocicletas_organizado[i]['percentual']) + "%" +"\n"))
    arquivo.write("\nQUESTÃO 3:\n")
    arquivo.write("NOME,POPULAÇÃO,AUTOMÓVEIS,HABITANTES/1000AUTOMÓVEIS\n")
    for i in range(len(maiores_automoveis1000)):
        arquivo.write(str(maiores_automoveis1000[i]['nome'] + "," + str(maiores_automoveis1000[i]['frota_total2018']) + "," + str(maiores_automoveis1000[i]['frota_de_automoveis']) + "," + str(maiores_automoveis1000[i]['hab_por_1000']) + "%" +"\n"))
    arquivo.close()          
#VARIÁVEIS GLOBAIS DA FUNÇÃO LER_POPULAÇÃO
municipio_populacao = []
populacao = []
ler_populacao()

#VARIÁVEIS GLOBAIS DA FUNÇÃO LER_FROTA2010
frota_total = []
frota_total_todos = []
veiculos = []
automoveis = []
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

#VARIÁVEIS GLOBAIS DA FUNÇÃO ESCREVER_ARQUIVO
escrever_arquivo()
