old  = open("descincro.srt","r") # Ariquivo desincronizado
new  = open("sinc.srt","a")      # Arquivo a sincronizar

global val

# Define valor global para utilização ao longo do script
val = inicio()

# Recebe correção em segundos positivos
def inicio():
    delay = int(input('\n\nDefina um numero para correcao em segundos\n\n'))
    return delay


# Verifica se é linha de contagem
def ehnum(val):
    try:
        val = int(val)
        return True
    except :
        return False

# rennova, hora, minuto e segundos
def hms(h, m, s):
    temp = val
    if (s+temp) > 59 and m == 59:
        h       = h + 1
        m       = 0
        s       = (s+temp) - 60
    elif (s+temp) > 59 :
        m       = m + 1
        s       = (s+temp) - 60
    else:
        s = temp + s
    return h, m, s


# Se valor for menor que 10, retorna string concatenada com 0 na frente
def isLessTTen(value):
    if value<10:
        return '0'+str(value)
    else:
        return str(value)


# faz montagem 00:00:00
def rebuild(h, m, s):
    h   = isLessTTen(h)
    m   = isLessTTen(m)
    s   = isLessTTen(s)
    done   = h + ':' + m + ':' + s
    return done

# Retorna linha com valores convertidos
def conversion(line):
    hourB  , hourE     = int(line[0:2]), int(line[17:19])
    minuteB, minuteE   = int(line[3:5]), int(line[20:22])
    secondB, secondE   = int(line[6:8]), int(line[23:25])
    hourB, minuteB, secondB = hms(hourB, minuteB, secondB)
    hourE, minuteE, secondE = hms(hourE, minuteE, secondE)
    doneB = rebuild(hourB, minuteB, secondB)
    doneE = rebuild(hourE, minuteE, secondE)
    line = line.replace(line[0:8], doneB)
    line = line.replace(line[17:25], doneE)
    return line


# Loop sobre linhas do arquivo antigo, reescrevendo linhas do tempo.
for line in old.readlines():
    if    ehnum(line[0:2])\
      and ehnum(line[3:5])\
      and ehnum(line[6:8]):
        new.write(conversion(line))
    else:
        new.write(line)
