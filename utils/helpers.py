import random, json

def genera_random_color(valorSemilla):
    random.seed(valorSemilla)
    
    color_ranges = [
        (100, 200, 200, 255, 50, 150),  #verde claros
        (50, 200, 150, 255, 50, 200),   #verdes campo caza
        (150, 255, 100, 255, 50, 150),  #marrones, amarillos verdosos
        (200, 255, 100, 200, 50, 150),  #naranjas, rojos
        (100, 200, 100, 200, 160, 255)  #celestes y grises rosados
    ]
    
    r_min, r_max, g_min, g_max, b_min, b_max = random.choice(color_ranges)
    
    r = random.randint(r_min, r_max)
    g = random.randint(g_min, g_max)
    b = random.randint(b_min, b_max)

    return f"#{r:02x}{g:02x}{b:02x}"


def serializa_parcela(parcela, en_fiesta=None):
    return {
        'id': parcela.id,
        'nombre': parcela.nombre,
        'tipo': parcela.tipo,
        'localizacion': json.loads(parcela.localizacion) if parcela.localizacion else None,
        'detalles': parcela.detalles,
        'en_fiesta': en_fiesta
    }