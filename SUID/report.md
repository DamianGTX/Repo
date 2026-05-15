# Report

Byla zneužita zranitelnost PATH Hijacking v SUID programu `/usr/bin/syscheck`.
Program spouštěl příkaz `date` bez absolutní cesty, což umožnilo podvrhnout vlastní skript spuštěný s právy root.
UID představuje skutečného uživatele procesu, zatímco EUID určuje oprávnění používaná při běhu programu.
SUID program běžel s EUID=root, i když jej spustil běžný uživatel student.
Systém lze zabezpečit používáním absolutních cest, odstraněním zbytečných SUID bitů a nepoužíváním `system()` v privilegovaných programech.
