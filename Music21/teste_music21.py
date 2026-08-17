from music21 import corpus, converter

# Mude a linha abaixo para o caminho do SEU arquivo (já convertido para .xml ou .mid)
# Se deixar comentado, ele usará um exemplo do próprio music21
arquivo_musica = 'bach/bwv323.xml' 
# arquivo_musica = 'C:\Users\ageno\OneDrive\Área de Trabalho\SIBELIUS - MUSESCORE - MIDI\61933472-Minha-Pa-tria-Para-Cristo-coro-masculino.mxl'

# 1. Carregar a música
try:
    score = corpus.parse(arquivo_musica)
    print(f"Sucesso! Métrica detectada: {score.analyze('key')}")
except:
    print("Arquivo não encontrado. Verifique o caminho!")
    exit()

# 2. Analisar harmonia (Chordify)
chords = score.chordify()

print(f"\nExtraindo os primeiros 10 acordes:")
# Pega apenas os primeiros 10 acordes para ser rápido
lista_acordes = chords.recurse().getElementsByClass('Chord')

for c in lista_acordes[:10]:
    print(f"Compasso {c.measureNumber}: {c.pitchedCommonName}")