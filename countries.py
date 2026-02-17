afrika = [
        "Jazoir", "Angola", "Benin", "Botsvana", "Burkina-Faso",
        "Burundi", "Chad", "Jibuti", "Misr", "Efiopiya",
        "Gabon", "Gambiya", "Gana", "Gvineya", "Keniya",
        "Lesoto", "Liberiya", "Liviya", "Madagaskar", "Malavi",
        "Mali", "Marokash", "Mozambik", "Namibiya", "Niger",
        "Nigeriya", "Ruanda", "Senegal", "Somali", "Janubiy Afrika Respublikasi",
        "Sudan", "Tanzaniya", "Tunis", "Uganda", "Zambiya", "Zimbabve"
]
osiyo = [
        "O‘zbekiston", "Qozog‘iston", "Qirg‘iziston", "Tojikiston", "Turkmaniston",
        "Xitoy", "Hindiston", "Pokiston", "Afg‘oniston", "Eron",
        "Iroq", "Turkiya", "Saudiya Arabistoni", "BAA", "Qatar",
        "Yaponiya", "Janubiy Koreya", "Shimoliy Koreya",
        "Indoneziya", "Malayziya", "Tailand", "Vetnam", "Filippin"
]
    
yevropa = [
        "Buyuk Britaniya", "Fransiya", "Germaniya", "Italiya", "Ispaniya",
        "Portugaliya", "Niderlandiya", "Belgiya", "Shveysariya", "Avstriya",
        "Polsha", "Chexiya", "Slovakiya", "Vengriya", "Ruminiya",
        "Bolgariya", "Gretsiya", "Ukraina", "Belarus",
        "Norvegiya", "Shvetsiya", "Finlyandiya"
]
    
shimoliy_amerika = [
        "AQSh", "Kanada", "Meksika", "Kuba", "Yamayka",
        "Panama", "Kosta-Rika", "Gvatemala", "Gonduras", "Salvador"
]
    
janubiy_amerika = [
        "Braziliya", "Argentina", "Chili", "Peru", "Kolumbiya",
        "Venesuela", "Ekvador", "Boliviya", "Paragvay", "Urugvay"
]
    
avstraliya = [
        "Avstraliya", "Yangi Zelandiya", "Papua-Yangi Gvineya",
        "Fidji", "Solomon orollari", "Samoa"
]
def qita_aniqla(davlat):
    if davlat in afrika:
        return f"Bu Afrika qit'asiga tegishli davlat. Bu qit'ada {len(afrika)}ta davlat bor"
    elif davlat in osiyo:
        return f"Bu Osiyo qit'asig ategishli davlat. Bu qit'ada {len(osiyo)}ta davlat bor"
    elif davlat in yevropa:
        return f"Bu yevropa qit'asiga tegishli davlat. Bu qit'ada {len(yevropa)}ta davlat bor"
    elif davlat in avstraliya:
        return f"Bu Avstraliya qit'asiga tegishli davlat. Bu qit'ada {len(avstraliya)}ta davlat bor"
    elif davlat in shimoliy_amerika:
        return f"Bu Shimoliy Amerika qit'asiga tegishli davlat. Bu qit'ada {len(shimoliy_amerika)}ta davlat bor"
    else:
        return f"Bu Janubiy Amerika qit'asiga tegishli davlat. Bu qit'ada {len(janubiy_amerika)}ta davlat bor"
        
print(qita_aniqla("Italiya"))