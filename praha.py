import psycopg


# ==========================================
# Připojení k databázi
# ==========================================
def connect():
    try:
        conn = psycopg.connect(
            host="localhost",
            dbname="obce",
            user="student",
            password="heslo"
        )
        return conn

    except Exception as e:
        print("Chyba připojení:")
        print(e)
        return None


# ==========================================
# Menu
# ==========================================
def menu():
    print("\n=========================")
    print("DEMOGRAFIE ČR")
    print("=========================")
    print("1 - Seznam okresů")
    print("2 - Obce v okrese")
    print("3 - Hledat obec")
    print("4 - Statistiky okresu")
    print("0 - Konec")
    print("=========================")


# ==========================================
# Výpis okresů
# ==========================================
def vypis_okresu(conn):

    sql = """
        SELECT id_okres, nazev
        FROM okresy
        ORDER BY nazev
    """

    try:
        with conn.cursor() as cur:
            cur.execute(sql)

            print("\nSEZNAM OKRESŮ")
            print("-" * 40)

            for id_okres, nazev in cur.fetchall():
                print(f"{id_okres:<10} {nazev}")

    except Exception as e:
        print("Chyba:", e)


# ==========================================
# Obce v okrese
# ==========================================
def obce_v_okrese(conn):

    okres = input("Zadej kód okresu: ").strip()

    sql_okres = """
        SELECT nazev
        FROM okresy
        WHERE id_okres = %s
    """

    sql_obce = """
        SELECT
            nazev,
            pocet_obyvatel,
            prumerny_vek
        FROM obce_pob
        WHERE id_okres = %s
        ORDER BY nazev
    """

    try:
        with conn.cursor() as cur:

            cur.execute(sql_okres, (okres,))
            radek = cur.fetchone()

            if radek is None:
                print("Okres nebyl nalezen.")
                return

            print(f"\nOKRES: {radek[0]}")
            print("-" * 60)

            cur.execute(sql_obce, (okres,))
            data = cur.fetchall()

            if not data:
                print("V okrese nejsou žádné obce.")
                return

            print(
                f"{'Obec':30}"
                f"{'Obyvatel':>12}"
                f"{'Prům. věk':>12}"
            )

            print("-" * 60)

            for obec, obyv, vek in data:
                print(
                    f"{obec:30}"
                    f"{obyv:>12,}"
                    f"{vek:>12.1f}"
                )

    except Exception as e:
        print("Chyba:", e)


# ==========================================
# Hledání obce
# ==========================================
def hledani_obce(conn):

    text = input("Zadej část názvu obce: ").strip()

    sql = """
        SELECT
            nazev,
            pocet_obyvatel,
            prumerny_vek
        FROM obce_pob
        WHERE LOWER(nazev) LIKE LOWER(%s)
        ORDER BY nazev
    """

    try:
        with conn.cursor() as cur:

            cur.execute(sql, (f"%{text}%",))
            data = cur.fetchall()

            if not data:
                print("Žádná obec nebyla nalezena.")
                return

            print("\nNALEZENÉ OBCE")
            print("-" * 60)

            print(
                f"{'Název':30}"
                f"{'Obyvatel':>12}"
                f"{'Prům. věk':>12}"
            )

            print("-" * 60)

            for obec, obyv, vek in data:
                print(
                    f"{obec:30}"
                    f"{obyv:>12,}"
                    f"{vek:>12.1f}"
                )

    except Exception as e:
        print("Chyba:", e)


# ==========================================
# Statistiky okresu
# ==========================================
def statistika_okresu(conn):

    okres = input("Zadej kód okresu: ").strip()

    sql = """
        SELECT
            o.nazev,
            SUM(b.pocet_obyvatel),
            AVG(b.prumerny_vek),
            SUM(b.pocet_muzi),
            SUM(b.pocet_zeny)
        FROM okresy o
        JOIN obce_pob b
            ON o.id_okres = b.id_okres
        WHERE o.id_okres = %s
        GROUP BY o.nazev
    """

    try:
        with conn.cursor() as cur:

            cur.execute(sql, (okres,))
            data = cur.fetchone()

            if data is None:
                print("Okres nebyl nalezen.")
                return

            nazev, obyv, vek, muzi, zeny = data

            print("\nSTATISTIKA OKRESU")
            print("-" * 40)
            print("Okres:", nazev)
            print(f"Počet obyvatel : {obyv:,}")
            print(f"Průměrný věk   : {vek:.2f}")
            print(f"Počet mužů     : {muzi:,}")
            print(f"Počet žen      : {zeny:,}")

            if zeny > 0:
                pomer = muzi / zeny
                print(f"Poměr M/Ž      : {pomer:.2f}")

    except Exception as e:
        print("Chyba:", e)


# ==========================================
# Hlavní program
# ==========================================
def main():

    conn = connect()

    if conn is None:
        return

    while True:

        menu()

        volba = input("Volba: ")

        if volba == "1":
            vypis_okresu(conn)

        elif volba == "2":
            obce_v_okrese(conn)

        elif volba == "3":
            hledani_obce(conn)

        elif volba == "4":
            statistika_okresu(conn)

        elif volba == "0":
            print("Program ukončen.")
            break

        else:
            print("Neplatná volba.")

    conn.close()


if __name__ == "__main__":
    main() 
