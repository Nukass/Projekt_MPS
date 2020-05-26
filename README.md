# Projekt_MPS
Projekt na předmět MPS, kde nás učí pan Vintera Jiří, Ing.
Jedná se o jednoduchý projekt v jazyku "Python" za použití "Flask",
kde se vytvořil přihlašovací systém v podobě webové stránky.
Nejsou zde žádné role v podobě adminstrátora nebo uživatele.
Program umožňuje:
  Registraci uživatele, kde se vyplní:
    Uživatelské jméno;
      Lze použít i diakritiku
    Heslo;
      Lze použít i diakritiku
    Email;
      Do této kolonky nelze zapsat jakýkoliv email, musí mít určitou "kostru".
      Kostra obsahuje:
        Uživatelské jméno emailu;
        Zavináč;
        Doménu;
    Pokud nic nevyplníte, tak vás to bude postupně žádat a vyplnění nevyplněných polí.
  Přihlášení uživatele probíhá obdobně jako registrace, akorát zde již není potřeba použít email.
  Po přihlášení vás to přesměruje na domovskou stránku, kde si můžete povšimnout hlavního nadpisu, který tvoří název stránky.
  Vpravo od tohoto nadpisu je ikona umožnujíčí odhlášení uživatele.
  O řádek níže je další nadpis, kde je napsáno "Profil" a hned pod ním jsem detaily přihlášeného uživatele,
  kde je opět nadpis: "Detaily účtu"
  Pod ním je vypsáno:
    Uživatelské jméno;
    Heslo;
    Email;
Po odhlášení se znovu můžete přihlásit pod stejnými údaji, které se načtou z databáze.
