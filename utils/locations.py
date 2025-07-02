PROVINCIAS = [
    ('', 'Selecciona una provincia'),
    ('Álava', 'Álava'), ('Albacete', 'Albacete'), ('Alicante', 'Alicante'), ('Almería', 'Almería'),
    ('Asturias', 'Asturias'), ('Ávila', 'Ávila'), ('Badajoz', 'Badajoz'), ('Barcelona', 'Barcelona'),
    ('Burgos', 'Burgos'), ('Cáceres', 'Cáceres'), ('Cádiz', 'Cádiz'), ('Cantabria', 'Cantabria'),
    ('Castellón', 'Castellón'), ('Ceuta', 'Ceuta'),('Ciudad Real', 'Ciudad Real'), ('Córdoba', 'Córdoba'), ('Cuenca', 'Cuenca'),
    ('Gerona', 'Gerona'), ('Granada', 'Granada'), ('Guadalajara', 'Guadalajara'), ('Guipúzcoa', 'Guipúzcoa'),
    ('Huelva', 'Huelva'), ('Huesca', 'Huesca'), ('Islas Baleares', 'Islas Baleares'), ('Jaén', 'Jaén'),
    ('La Coruña', 'La Coruña'), ('La Rioja', 'La Rioja'), ('Las Palmas', 'Las Palmas'), ('León', 'León'),
    ('Lérida', 'Lérida'), ('Lugo', 'Lugo'), ('Madrid', 'Madrid'), ('Málaga', 'Málaga'), ('Melilla', 'Melilla'),
    ('Murcia', 'Murcia'), ('Navarra', 'Navarra'), ('Orense', 'Orense'), ('Palencia', 'Palencia'),
    ('Pontevedra', 'Pontevedra'), ('Salamanca', 'Salamanca'), ('Santa Cruz de Tenerife', 'Santa Cruz de Tenerife'),
    ('Segovia', 'Segovia'), ('Sevilla', 'Sevilla'), ('Soria', 'Soria'), ('Tarragona', 'Tarragona'),
    ('Teruel', 'Teruel'), ('Toledo', 'Toledo'), ('Valencia', 'Valencia'), ('Valladolid', 'Valladolid'),
    ('Vizcaya', 'Vizcaya'), ('Zamora', 'Zamora'), ('Zaragoza', 'Zaragoza')
]

COMUNIDADES_AUTONOMAS = [
    ('', 'Selecciona una comunidad autónoma'),
    ('Andalucía', 'Andalucía'), ('Aragón', 'Aragón'), ('Asturias', 'Asturias'),
    ('Baleares', 'Baleares'), ('Canarias', 'Canarias'), ('Cantabria', 'Cantabria'),
    ('Castilla-La Mancha', 'Castilla-La Mancha'), ('Castilla y León', 'Castilla y León'),
    ('Cataluña', 'Cataluña'), ('Ceuta', 'Ceuta'), ('Extremadura', 'Extremadura'), ('Galicia', 'Galicia'),
    ('Madrid', 'Madrid'), ('Melilla', 'Melilla'), ('Murcia', 'Murcia'), ('Navarra', 'Navarra'),
    ('La Rioja', 'La Rioja'), ('País Vasco', 'País Vasco'), ('Valencia', 'Valencia')
]

PROVINCIAS_POR_COMUNIDAD = {
    'Andalucía': ['Almería', 'Cádiz', 'Córdoba', 'Granada', 'Huelva', 'Jaén', 'Málaga', 'Sevilla'],
    'Aragón': ['Huesca', 'Teruel', 'Zaragoza'],
    'Asturias': ['Asturias'],
    'Baleares': ['Islas Baleares'],
    'Canarias': ['Las Palmas', 'Santa Cruz de Tenerife'],
    'Cantabria': ['Cantabria'],
    'Castilla-La Mancha': ['Albacete', 'Ciudad Real', 'Cuenca', 'Guadalajara', 'Toledo'],
    'Castilla y León': ['Ávila', 'Burgos', 'León', 'Palencia', 'Salamanca', 'Segovia', 'Soria', 'Valladolid', 'Zamora'],
    'Cataluña': ['Barcelona', 'Gerona', 'Lérida', 'Tarragona'],
    'Ceuta': ['Ceuta'],
    'Extremadura': ['Badajoz', 'Cáceres'],
    'Galicia': ['La Coruña', 'Lugo', 'Orense', 'Pontevedra'],
    'Madrid': ['Madrid'],
    'Melilla': ['Melilla'],
    'Murcia': ['Murcia'],
    'Navarra': ['Navarra'],
    'La Rioja': ['La Rioja'],
    'País Vasco': ['Álava', 'Guipúzcoa', 'Vizcaya'],
    'Valencia': ['Alicante', 'Castellón', 'Valencia']
}
