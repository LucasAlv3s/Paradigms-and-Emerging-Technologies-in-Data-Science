# Exportar feiçòes como KML 

import processing, os

camada = 'Bordeada'

nome_campo = 'id'#É o nome do campo para o arquivo de saída

# Pasta de saida dos arqvivos KML

pasta = r'C:\users\sazon\OneDrive\Área de Trabalho\plano de voo'

layer = QgsProject.instance().mapLayersByName(camada)[0]

campos - layer.fields()

crsSrc = layer.crs()

# Transformação para WGS84

crsDest = QgsCoordinateReferenceSystem('EPSG:4326')

towgs84 = QgsCoordinateTransform(crsSrc, crsDest, QgsProject.instance())