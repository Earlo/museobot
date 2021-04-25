class Question:
    def __init__(self, text, options, correct):
        self.text = text
        self.options = options
        self.correct = correct


QDict = {
    'lör0': Question(
        text="Oispa?",
        options={
                'lör0_a': 'Wappu',
                'lör0_b': 'Kaljaa',
                'lör0_c': 'Viinaa',
                'lör0_d': 'Ei darra',
            },
        correct = 'lör0_X'
    ),
    'lör1': Question(
        text="Rahat vai kolmipyörä?",
        options={
                'lör1_a': 'Rahat',
                'lör1_b': 'Kolmipyörä',
                'lör1_c': 'Piip paap',
                'lör1_d': 'Kvaak Kvaak',
            },
        correct = 'lör1_X'
    ),
    #Sunnuntai
    'su0': Question(
        text="Mihin käyttöön Smökki alunperin rakennettiin?",
        options={
                'su0_a': 'Väliaikainen työmaaruokala',
                'su0_b': 'Tanssilava',
                'su0_c': 'Keilahalli',
                'su0_d': 'Opiskelijoiden juhlatila',
            },
        correct = 'su0_a'
    ),
    'su1': Question(
        text="Mikä tämä on?",
        options={
                'su1_a': 'Ossin pylväs',
                'su1_b': 'Reikä kivessä',
                'su1_c': 'Servin pårtti',
                'su1_d': 'Jämerän silmä',
            },
        correct = 'su1_d'
    ),
    'su2': Question(
        text="Milloin nykyinen Otaniemen rantasauna eli Rantsu on rakennettu?",
        options={
                'su2_a': '1969',
                'su2_b': '1982',
                'su2_c': '1985',
                'su2_d': '1991',
            },
        correct = 'su2_c'
    ),
    'su3': Question(
        text="Kuka henkilö toimi Dipolin kunniatalonmiehenä?",
        options={
                'su3_a': 'Marsalkka Mannerheim',
                'su3_b': 'Elisabeth Rehn',
                'su3_c': 'Paavo Väyrynen',
                'su3_d': 'Urho Kaleva Kekkonen',
            },
        correct = 'su3_d'
    ),
    'su4': Question(
        text="Kuka tai mikä taho lahjoitti Dipolin lipputankojen juoksupyörien voitelukannut?",
        options={
                'su4_a': 'KY',
                'su4_b': 'KONE Oyj',
                'su4_c': 'Koneinsinöörikilta',
                'su4_d': 'Poliisiopisto',
            },
        correct = 'su4_a'
    ),
    # Ma
    'ma0': Question(
        text="Minkä niminen on TKK:n varhaisimman edeltäjäkoulun ensimmäinen rakennus?",
        options={
                'ma0_a': 'Vanha Ylioppilastalo',
                'ma0_b': 'Vanha Poli',
                'ma0_c': 'Domus Litonii',
                'ma0_d': 'Polysteekki',
            },
        correct = 'ma0_c'
    ),
    'ma1': Question(
        text="KY-talo on tunnettu monista pitkäikäisistä ja arvokkaista perinteistä.\nTähän aiheeseen liittyen; mikä onkaan KY-kierros?",
        options={
                'ma1_a': 'Valmistunut KTM tarjoaa kierroksen alakertsillä',
                'ma1_b': 'Kierros missä käydään jokaisessa KY-talon kerhotilassa',
                'ma1_c': 'Viuhahdus KY-talon korttelin ympäri',
                'ma1_d': 'Approkierros KY-talon ja Töölön kampuksen ympäristössä olevissa kuppiloissa',
            },
        correct = 'ma1_c'
    ),
    'ma2': Question(
        text="Missä seuraavista paikoista Taideteollisen korkeakoulun opetusta ei ole järjestetty?",
        options={
                'ma2_a': 'Arabianranta',
                'ma2_b': 'Ateneum',
                'ma2_c': 'Lasipalatsi',
                'ma2_d': 'Kansakoulun talo',
            },
        correct = 'ma2_c'
    ),
    'ma3': Question(
        text="Missä käytössä Vanhan Polin rakennus on nykyisin?",
        options={
                'ma3_a': 'Hotellina',
                'ma3_b': 'Keilahallina',
                'ma3_c': 'Sisäampumaratana',
                'ma3_d': 'Asuinrakennuksena',
            },
        correct = 'ma3_a'
    ),
    'ma4': Question(
        text="Missä sijaitsee kolmas Pro Teekkari -patsas?",
        options={
                'ma4_a': 'Lohjalla',
                'ma4_b': 'Tampereella',
                'ma4_c': 'Turussa',
                'ma4_d': 'Forssassa',
            },
        correct = 'ma4_d'
    ),
    #Ti
    'ke0': Question(
        text="Mikä näistä ei ole teekkarilakki?",
        options={
                'ti0_a': 'Vihreä tupsulakki',
                'ti0_b': 'Sinitupsuinen lakki',
                'ti0_c': 'Harmaa lakki',
                'ti0_d': 'Kukkakokardihattu',
            },
        correct = 'ti0_b'
    ),
    'ti1': Question(
        text="Kuinka monta vuotta vanha teekkarilakki on tänä vuonna?",
        options={
                'ti1_a': '98 vuotta',
                'ti1_b': '128 vuotta',
                'ti1_c': '139 vuotta',
                'ti1_d': '149 vuotta',
            },
        correct = 'ti1_b'
    ),
    'ti2': Question(
        text="Minkä paikkakuntien teekkarilakkeja nämä ovat?",
        options={
                'ti2_a': 'Vaasa ja Turku',
                'ti2_b': 'Tampere ja Oulu',
                'ti2_c': 'Vaasa ja Oulu',
                'ti2_d': 'Tampere ja Turku',
            },
        correct = 'ti2_c'
    ),
    'ti3': Question(
        text="Mihin erikoistarkoitukseen ei ole pysyvää lakinkäyttölupaa?",
        options={
                'ti3_a': 'Radiodiodin tekijöille Radiodiodin markkinointitehtävissä',
                'ti3_b': 'Museo-oppaille museon edustustehtävissä',
                'ti3_c': 'Kahden teekkarin mennessä naimisiin',
                'ti3_d': 'Marmon-auton kuljettajille ja esittelijöille',
            },
        correct = 'ti3_c'
    ),
    'ti4': Question(
        text="Kuinka monta erilaista virallista teekkarilakkimallia on käytössä Suomessa wappuna 2022?",
        options={
                'ti4_a': '8',
                'ti4_b': '9',
                'ti4_c': '15',
                'ti4_d': '16',
            },
        correct = 'ti4_d'
    ),
    #Ke
    'ke0': Question(
        text="Mikä on teekkareiden ensimmäinen wappulehti?",
        options={
                'ke0_a': 'Tamppi',
                'ke0_b': 'Julkku',
                'ke0_c': 'Waputin',
                'ke0_d': 'Äpy',
            },
        correct = 'ke0_c'
    ),
    'ke1': Question(
        text="Kuka on tämän tohtorinhatun omistaja?",
        options={
                'ke1_a': 'Jorma Eloranta',
                'ke1_b': 'Teemu Kerppu',
                'ke1_c': 'Linus Torvalds',
                'ke1_d': 'Kalle Ala-Viikari',
            },
        correct = 'ke1_b'
    ),
    'ke2': Question(
        text="Minkä niminen tämä Äpy on?",
        options={
                'ke2_a': 'Räpylä-Äpy',
                'ke2_b': 'Kapula-Äpy',
                'ke2_c': 'Konferenssi-Äpy',
                'ke2_d': 'Luuri-Äpy',
            },
        correct = 'ke2_a'
    ),
    'ke3': Question(
        text="Minkä puolesta tempaistiin vuonna 2016?",
        options={
                'ke3_a': 'Nuorten hyvinvoinnin puolesta',
                'ke3_b': 'Kylterien muutto Otaniemeen',
                'ke3_c': 'Peruskoulutuksen puolesta',
                'ke3_d': 'Wiikon Wappusaunan puolesta',
            },
        correct = 'ke3_c'
    ),
    'ke4': Question(
        text="Mikä sinne kuulumaton objekti löytyi Vasa-laivan kannelta sitä nostettaessa?",
        options={
                'ke4_a': 'Sammunut teekkari',
                'ke4_b': 'Jallupullo',
                'ke4_c': 'Paavo Nurmen patsas',
                'ke4_d': 'Teekkarilakki',
            },
        correct = 'ke4_c'
    ),
    #To
    'to0': Question(
        text="Mikä seuraavista juhlista on historialtaan pitkäikäisin?",
        options={
                'to0_a': 'Lakinlaskijaiset',
                'to0_b': 'Teekkariperinnejuhla',
                'to0_c': 'Dipolin Wappu',
                'to0_d': 'Gravitaatio',
            },
        correct = 'to0_d'
    ),
    'to1': Question(
        text="Mikä seuraavista oli TKY:n julkaisema sitsiopas?",
        options={
                'to1_a': 'Sitsikorvat ja 100 muuta vinkkiä akateemisiin pöytäjuhliin',
                'to1_b': 'Janostaan teekkari muistetaan',
                'to1_c': 'Opas alkoholittomiin sitsijuomiin',
                'to1_d': 'Elomme päivät epäselvät',
            },
        correct = 'to1_c'
    ),
    'to2': Question(
        text="Dipolissa juhlittiin vuonna 2017 Suomi100 itsenäisyyspäivän juhlia.\nMinä vuonna vastaavat itsenäisyyspäivän juhlat järjestettiin Dipolissa edellisen kerran ja kenen/keiden toimesta?",
        options={
                'to2_a': '2012 - AYY',
                'to2_b': '1997 - TKY & HYY',
                'to2_c': '1987 - TKY, KY & TOKYO',
                'to2_d': '1977 - TKY',
            },
        correct = 'to2_c'
    ),
    'to3': Question(
        text="Millä nimellä tunnetaan TOKYO:n vuosijuhla?",
        options={
                'to3_a': 'Maskerad',
                'to3_b': 'Sherylin syndet',
                'to3_c': 'Krokotiili Genan syntymäpäivät',
                'to3_d': 'Torso party',
            },
        correct = 'to3_a'
    ),
    'to4': Question(
        text="Kuka julistaa Wappuriehan?",
        options={
                'to4_a': 'Suomen Tasavallan Presidentti',
                'to4_b': 'Espoon kaupunginjohtaja',
                'to4_c': 'Aalto-yliopiston rehtori',
                'to4_d': 'Kilon poliisi',
            },
        correct = 'to4_d'
    ),
    #Loppu
    'loppu0': Question(
        text="Mielipiteet kysymyksistä?",
        options={
                'loppu0_a': 'Hyviä',
                'loppu0_b': 'Huonoja',
                'loppu0_c': 'Helppoja',
                'loppu0_d': 'Vaikeita',
            },
        correct = 'loppu0_XXX'
    ),
    'loppu1': Question(
        text="Mielipiteet kysymyksistä?",
        options={
                'loppu1_a': 'Hyviä',
                'loppu1_b': 'Huonoja',
                'loppu1_c': 'Helppoja',
                'loppu1_d': 'Vaikeita',
            },
        correct = 'loppu1_XXX'
    ),
    'loppu2': Question(
        text="Mielipiteet kysymyksistä?",
        options={
                'loppu2_a': 'Hyviä',
                'loppu2_b': 'Huonoja',
                'loppu2_c': 'Helppoja',
                'loppu2_d': 'Vaikeita',
            },
        correct = 'loppu2_XXX'
    ),
    'loppu3': Question(
        text="Mielipiteet kysymyksistä?",
        options={
                'loppu3_a': 'Hyviä',
                'loppu3_b': 'Huonoja',
                'loppu3_c': 'Helppoja',
                'loppu3_d': 'Vaikeita',
            },
        correct = 'loppu3_XXX'
    ),
    'loppu4': Question(
        text="Mielipiteet kysymyksistä?",
        options={
                'loppu4_a': 'Hyviä',
                'loppu4_b': 'Huonoja',
                'loppu4_c': 'Helppoja',
                'loppu4_d': 'Vaikeita',
            },
        correct = 'loppu4_XXX'
    ),
}
