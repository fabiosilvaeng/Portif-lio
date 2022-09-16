from random import randint as rd

def numbers(lenght,limit,num):
    teams = {
    1:'ABC',2:'Altos',3:'América-MG',4:'América-RN',5:'Aparecidense',6:'Athlético-PR',7:'Atlético-AC',8:'Atlético-CE',9:'Atlético-GO',10:'Atlético-MG',
    11:'Avaí',12:'Bahia',13:'Boa Esporte',14:'Boa Vista',15:'Botafogo-PB',16:'Botafogo-RJ',17:'Botafogo-SP',18:'Bragantino',19:'Brasil',20:'Brasiliense',
    21:'Brusque',22:'Campinense',23:'Caxias',24:'Ceará',25:'Chapecoense',26:'Cianorte',27:'Confiança',28:'Corinthians',29:'Coritiba',30:'CRB',
    31:'Criciúma',32:'Cruzeiro',33:'CSA',34:'Cuiabá',35:'Ferroviária-SP',36:'Ferroviário-CE',37:'Figueirense',38:'Flamengo',39:'Floresta',40:'Fluminense',
    41:'Fortaleza',42:'Goiás',43:'Grêmio',44:'Guarani',45:'Imperatriz',46:'Internacional',47:'Ituano',48:'Jacuipense',49:'Joinville',50:'Juazeirense',
    51:'Juventude',52:'Londrina',53:'Luverdense',54:'Manaus',55:'Mirasol',56:'Moto Club',57:'Náutico',58:'Novorizontino',59:'Oeste',60:'Operário',
    61:'Palmeiras',62:'Paraná',63:'Paysandu',64:'Ponte Preta',65:'Remo',66:'Sampaio Corrêa',67:'Santa Cruz',68:'Santos',69:'São Bento',70:'São José',
    71:'São Paulo',72:'São Raimundo',73:'Sport Recife',74:'Tombense',75:'Treze',76:'Vasco da Gama',77:'Vila Nova',78:'Viória',79:'Volta Redonda',80:'Ypiranga'
    }

    list_numbers = []
    if num != '':
        list_numbers.append(teams[num])
    while len(list_numbers) < lenght :
        number = str(rd(limit[0],limit[-1]))
        number = '0'+number if len(number) < 2 else number
        if number not in list_numbers:
            list_numbers.append(number)
    return list_numbers