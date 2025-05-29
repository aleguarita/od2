from collections import Counter


#! Tabela 9.5
tesouro_aleatorio = [
    # Covil
    {
        'tipo': 'A',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 12000}),
        'po': {'chance': 2, 'rolamento': '2d6 * 1000'},
        'pp': {'chance': 2, 'rolamento': '1d6 * 1000'},
        'pc': {'chance': 1, 'rolamento': '1d6 * 1000'},
        'gemas': {'chance': 3, 'rolamento': '6d6'},
        'objetos_de_valor': {'chance': 3, 'rolamento': '6d6'},
        'itens_magicos': {'chance': 2, 'itens': Counter({'qualquer': 3})},
    },
    {
        'tipo': 'B',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 1400}),
        'po': {'chance': 1, 'rolamento': '1d3 * 1000'},
        'pp': {'chance': 1, 'rolamento': '1d6 * 1000'},
        'pc': {'chance': 3, 'rolamento': '1d8 * 1000'},
        'gemas': {'chance': 1, 'rolamento': '1d6'},
        'objetos_de_valor': {'chance': 1, 'rolamento': '1d6'},
        'itens_magicos': {'chance': 1, 'itens': Counter({'arma': 1})},
    },
    {
        'tipo': 'C',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 650}),
        'pp': {'chance': 2, 'rolamento': '1d4 * 1000'},
        'pc': {'chance': 2, 'rolamento': '1d12 * 1000'},
        'gemas': {'chance': 1, 'rolamento': '1d4'},
        'objetos_de_valor': {'chance': 1, 'rolamento': '1d4'},
        'itens_magicos': {'chance': 1, 'itens': Counter({'qualquer': 2})},
    },
    {
        'tipo': 'D',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 3400}),
        'po': {'chance': 3, 'rolamento': '1d6 * 1000'},
        'pp': {'chance': 1, 'rolamento': '1d12 * 1000'},
        'pc': {'chance': 1, 'rolamento': '1d8 * 1000'},
        'gemas': {'chance': 2, 'rolamento': '1d8'},
        'objetos_de_valor': {'chance': 2, 'rolamento': '1d8'},
        'itens_magicos': {'chance': 1, 'itens': Counter({'qualquer': 2, 'poção': 1})},
    },
    {
        'tipo': 'E',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 1800}),
        'po': {'chance': 1, 'rolamento': '1d8 * 1000'},
        'pp': {'chance': 2, 'rolamento': '1d12 * 1000'},
        'pc': {'chance': 1, 'rolamento': '1d10 * 1000'},
        'gemas': {'chance': 1, 'rolamento': '1d10'},
        'objetos_de_valor': {'chance': 1, 'rolamento': '1d10'},
        'itens_magicos': {'chance': 1, 'itens': Counter({'qualquer': 3, 'pergaminho': 1})},
    },
    {
        'tipo': 'F',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 4000}),
        'po': {'chance': 2, 'rolamento': '1d12 * 1000'},
        'pp': {'chance': 1, 'rolamento': '2d10 * 1000'},
        'gemas': {'chance': 1, 'rolamento': '2d12'},
        'objetos_de_valor': {'chance': 1, 'rolamento': '1d12'},
        'itens_magicos': {'chance': 2, 'itens': Counter({'poção': 1, 'pergaminho': 1, 'não arma': 3})},
    },
    {
        'tipo': 'G',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 14000}),
        'po': {'chance': 3, 'rolamento': '10d4 * 1000'},
        'gemas': {'chance': 1, 'rolamento': '3d6'},
        'objetos_de_valor': {'chance': 1, 'rolamento': '1d10'},
        'itens_magicos': {'chance': 2, 'itens': Counter({'qualquer': 4, 'pergaminho': 1})},
    },
    {
        'tipo': 'H',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 27000}),
        'po': {'chance': 3, 'rolamento': '10d6 * 1000'},
        'pp': {'chance': 3, 'rolamento': '1d10 * 1000'},
        'pc': {'chance': 1, 'rolamento': '3d8 * 1000'},
        'gemas': {'chance': 3, 'rolamento': '1d10'},
        'objetos_de_valor': {'chance': 3, 'rolamento': '10d4'},
        'itens_magicos': {'chance': 1, 'itens': Counter({'qualquer': 4, 'poção': 1, 'pergaminho': 1})},
    },
    {
        'tipo': 'I',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 2800}),
        'gemas': {'chance': 3, 'rolamento': '2d6'},
        'objetos_de_valor': {'chance': 3, 'rolamento': '2d6'},
        'itens_magicos': {'chance': 1, 'itens': Counter({'qualquer': 1})},
    },
    {
        'tipo': 'J',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 25}),
        'pp': {'chance': 1, 'rolamento': '1d3 * 1000'},
        'pc': {'chance': 1, 'rolamento': '1d4 * 1000'},
    },
    {
        'tipo': 'K',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 15}),
        'pp': {'chance': 1, 'rolamento': '1d2 * 1000'},
    },
    {
        'tipo': 'L',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 200}),
        'gemas': {'chance': 3, 'rolamento': '1d4'},
    },
    {
        'tipo': 'M',
        'categoria': 'covil',
        'tesouro_rapido': Counter({'po': 40000}),
        'po': {'chance': 5, 'rolamento': '8d10 * 1000'},
        'pp': {'chance': 3, 'rolamento': '10d6 * 1000'},
        'gemas': {'chance': 3, 'rolamento': '5d4'},
        'objetos_de_valor': {'chance': 2, 'rolamento': '2d6'},
    },
    {
        'tipo': 'N',
        'categoria': 'covil',
        'itens_magicos': {'chance': 2, 'itens': Counter({'poção': '2d4'})},
    },
    {
        'tipo': 'O',
        'categoria': 'covil',
        'itens_magicos': {'chance': 3, 'itens': Counter({'poção': '1d4'})},
    },
    # Individual
    {
        'tipo': 'P',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'pp': 1}),
        'pc': {'chance': 6, 'rolamento': '3d8'},
    },
    {
        'tipo': 'Q',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 1}),
        'pp': {'chance': 6, 'rolamento': '3d6'},
    },
    {
        'tipo': 'R',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 3}),
        'po': {'chance': 6, 'rolamento': '1d6'},
        'equipamentos': {'chance': 2, 'rolamento': 1}
    },
    {
        'tipo': 'S',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 5}),
        'po': {'chance': 6, 'rolamento': '2d4'},
        'equipamentos': {'chance': 2, 'rolamento': 1}
    },
    {
        'tipo': 'T',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 17}),
        'po': {'chance': 6, 'rolamento': '1d6 * 5'},
        'equipamentos': {'chance': 2, 'rolamento': 2}
    },
    {
        'tipo': 'U',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 90}),
        'po': {'chance': 1, 'rolamento': '1d10'},
        'pp': {'chance': 1, 'rolamento': '1d10'},
        'pc': {'chance': 1, 'rolamento': '1d10'},
        'objetos_de_valor': {'chance': 1, 'rolamento': '1'},
        'itens_magicos': {'chance': 1, 'itens': Counter({'qualquer': 1})},
        'equipamentos': {'chance': 1, 'rolamento': '1d4'}
    },
    {
        'tipo': 'V',
        'categoria': 'individual',
        'tesouro_rapido': Counter({'po': 175}),
        'po': {'chance': 2, 'rolamento': '1d10'},
        'pp': {'chance': 2, 'rolamento': '1d10'},
        'objetos_de_valor': {'chance': 1, 'rolamento': '1d4'},
        'itens_magicos': {'chance': 2, 'itens': Counter({'qualquer': 1})},
        'equipamentos': {'chance': 1, 'rolamento': '1d6'}
    }
]

#! Tabela 9.6
equipamentos_raridade = [
    ((2, 2), "raro"),
    ((3, 3), "raro"),
    ((4, 4), "incomum"),
    ((5, 5), "incomum"),
    ((6, 6), "comum"),
    ((7, 7), "comum"),
    ((8, 8), "comum"),
    ((9, 9), "comum"),
    ((10, 10), "incomum"),
    ((11, 11), "incomum"),
    ((12, 12), "raro")
]

equipamentos_tipos = [
    ((2, 2), {
        "comum": "símbolo divino",
        "incomum": "aljava (1d6 flechas)",
        "raro": "porta mapas"
    }),
    ((3, 3), {
        "comum": "saco de dormir",
        "incomum": "martelo",
        "raro": "pena e tinta"
    }),
    ((4, 4), {
        "comum": "ração de viagem (1d4)",
        "incomum": "óleo",
        "raro": "corrente"
    }),
    ((5, 5), {
        "comum": "pederneira",
        "incomum": "água benta",
        "raro": "algema"
    }),
    ((6, 6), {
        "comum": "corda de cânhamo (15m)",
        "incomum": "pá ou picareta",
        "raro": "giz"
    }),
    ((7, 7), {
        "comum": "tochas (1d4)",
        "incomum": "arpéu",
        "raro": "caixa pequena"
    }),
    ((8, 8), {
        "comum": "mochila",
        "incomum": "lamparina",
        "raro": "coberta de inverno"
    }),
    ((9, 9), {
        "comum": "odre",
        "incomum": "vela (1d4)",
        "raro": "espelho"
    }),
    ((10, 10), {
        "comum": "saco de estopa",
        "incomum": "cravos ou ganchos (1d4)",
        "raro": "cadeado"
    }),
    ((11, 11), {
        "comum": "traje de exploração",
        "incomum": "traje de inverno",
        "raro": "traje nobre"
    }),
    ((12, 12), {
        "comum": "ferramenta de ladrão",
        "incomum": "lanterna furta-fogo",
        "raro": "rede"
    })
]
