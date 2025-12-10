# Git (cli) - 3.část

## Git Branch (větev)

### Práce s Git Branches

V Gitu znamená **branch** novou a zároveň oddělenou verzi hlavního repozitáře.</br>

![](branches.png)</br>

Řekněme, že máte velký projekt a potřebujete na něm aktualizovat design UI.

Jak by to fungovalo bez a s Git:

Bez Gitu:

- Vytvoř kopie všech relevantních souborů, aby nebyla ovlivněna živá verze
- Začni pracovat na novém designu UI a zjisti, že kód závisí na kódu v jiných souborech, které je také třeba změnit!
- Vytvoř kopie závislých souborů. Ujisti se, že každá závislost souboru odkazuje na správný název souboru.
- STAV NOUZE! Někde jinde v projektu je nesouvisející chyba, kterou je třeba co nejdříve opravit!
- Ulož všechny soubory a poznamenej si názvy kopií, na kterých jsi pracoval
- Pracuj na nesouvisející chybě a oprav ji.
- Vrať se k úpravě designu UI a dokonči práci tam.
- Zkopíruj kód nebo přejmenuj soubory, aby byla aktuální živá verze
  (o dva týdny později si uvědomíš, že nesouvisející chyba nebyla v nové verzi  opravena, protože jsi před opravou zkopíroval soubory)

S Git:

- S novou větví nazvanou new-design uprav kód přímo bez dopadu na hlavní větev.
- STAV NOUZE! Někde jinde v projektu je nesouvisející chyba, kterou je třeba co nejdříve opravit!
- Vytvoř novou větev z hlavního projektu s názvem small-error-fix.
- Oprav nesouvisející chybu a sluč větev small-error-fix s hlavní větví.
- Vrať se do větve new-design a dokonči práci tam
- Sluč větev new-design s hlavní větví (upozorni na opravu malé chyby)

Větve ti umožňují pracovat na různých částech projektu bez dopadu na hlavní větev.

Po dokončení práce lze větev sloučit s hlavním projektem.

Můžeš dokonce přepínat mezi větvemi a pracovat na různých projektech, aniž by se navzájem rušily.

Větvení v Gitu je velmi lehké a rychlé!

### Nová Git Branch

Pojď přidat některé nové funkce na stránku index.html.

Cílem je pracovat v místním úložišti ale bez narušení nebo případného zničení hlavního projektu.

Vytvoř tedy novou větev:

```
git branch hello-world-images
```

Nyní máš vytvořenou novou větev s názvem „hello-world-images“

Přesvědč se, zda se nová větev skutečně vytvořila:

```
git branch
  hello-world-images
* master
```

Vidíš novou větev s názvem "hello-world-images", ale * vedle master určuje, že jsi právě na této větvi.

**checkout** je příkaz používaný k přepnutí do jiné větve. Přesune tě z aktuální větve do větve zadané na konci příkazu:

```
git checkout hello-world-images
Switched to branch 'hello-world-images'
```

Nyní se přesunul náš současný pracovní prostor z hlavní větve do nové.

Otevři svůj oblíbený editor a proveď změny.

Nyní přidej tento obrázek (img\_hello\_world.jpg)</br>

![HW](img_hello_world.jpg)</br>

do pracovního adresáře a také řádek kódu do souboru index.html:

```
<!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
<link rel="stylesheet" href="bluestyle.css">
</head>
<body>

<h1>Hello world!</h1>
<div><img src="img_hello_world.jpg" alt="Hello World from Space"
style="width:100%;max-width:960px"></div>
<p>This is the first file in my new Git Repo.</p>
<p>A new line in our file!</p>

</body>
</html> 
```

Nyní zkontroluj stav aktuální větve:

```
git status
On branch hello-world-images
Changes not staged for commit:
  (use "git add ..." to update what will be committed)
  (use "git restore ..." to discard changes in working directory)
        modified:   index.html

Untracked files:
  (use "git add ..." to include in what will be committed)
        img_hello_world.jpg

no changes added to commit (use "git add" and/or "git commit -a")
```

Pojďme si tedy projít, co se zde stalo:

 Došlo ke změnám v našem index.html, ale soubor není připraven pro commit a soubor
 img\_hello\_world.jpg není sledován

Potřebujeme tedy přidat oba soubory do prostředí staging area pro tuto větev:

```
git add --all
```

Použití --all místo jednotlivých názvů souborů přidá všechny změněné (nové, upravené a smazané) soubory.

Zkontroluj stav větve:

```
git status
On branch hello-world-images
Changes to be committed:
  (use "git restore --staged ..." to unstage)
    new file: img_hello_world.jpg
    modified: index.html
```

Nyní potvrď změmy pomocí commit:

```
git commit -m "Added image to Hello World"
[hello-world-images 0312c55] Added image to Hello World
2 files changed, 1 insertion(+)
create mode 100644 img_hello_world.jpg
```

Nyní máš novou větev, která se liší od větve master.

Pozn: Příkazem checkout se přepneš do jiné větve. Použitím volby -b v příkazu checkout se vytvoří nová větev pokud neexistuje.

### Přepínání mezi Git branch

Nyní se podívejme, jak rychle a snadno lze pracovat s různými větvemi a jak dobře to funguje.

Momentálně jsi ve větvi hello-world-images. Do této větve byl přidán obrázek, takže uveďme seznam souborů v aktuálním adresáři:

```
ls
README.md  bluestyle.css  img_hello_world.jpg  index.html
```

Ve výpisu vidíš nový soubor img\_hello\_world.jpg, a pokud otevřeš soubor html, vidíš, že kód byl změněn. Vše je jak má být.

Nyní se podívej, co se stane, když změníš větev na hlavní.

```
git checkout master
Switched to branch 'master'
```

Nový obrázek by neměl být součástí této větve. Znovu vypiš soubory v aktuálním adresáři:

```
ls
README.md  bluestyle.css  index.html
```

img\_hello\_world.jpg tam opravdu není! A pokud otevřeš soubor html, uvidíš, že se kód vrátil do stavu, v jakém byl před změnou.

Vidíš, jak snadná je práce s větvemi? A jak ti to umožňuje pracovat na různých věcech?

## Pohotovostní Git branch

Nyní si představ, že ještě pracuješ ve větvi s obrázky hello-world-images, ale potřebuješ opravit chybu na masteru.

Nechceš pracovat přímo ve větvi master ale nechceš pracovat ani ve větvi s obrázky hello-world, protože to ještě není hotové.

Takže si vytvoříš novou větev, která se bude používat pro nouzovou situaci:

```
git checkout -b emergency-fix
Switched to a new branch 'emergency-fix'
```

Nyní máš vytvořenou novou větev z master a a nacházíš se v ní. Chybu můžeš bezpečně opravit, aniž by to mělo vliv na ostatní větve.

Oprav imaginární chybu:

```
 <!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
<link rel="stylesheet" href="bluestyle.css">
</head>
<body>

<h1>Hello world!</h1>
<p>This is the first file in my new Git Repo.</p>
<p>This line is here to show how merging works.</p>

</body>
</html>
```

V tomto souboru byly provedené změny a potřebuješ tyto změny dostat do hlavní větve.

Zkontroluj stav: 

```
git status
On branch emergency-fix
Changes not staged for commit:
  (use "git add ..." to update what will be committed)
  (use "git restore ..." to discard changes in working directory)
        modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
```

Přesuň změny v souboru index.html do stage area a následně potvrď příkazem commit.

```
git add index.html
git commit -m "updated index.html with emergency fix"
[emergency-fix dfa79db] updated index.html with emergency fix
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Nyní máme opravu připravenou pro master a potřebujeme sloučit dvě větve.

### Spojení (merge) Git Branches

Nouzovou opravu máme připravenou, a tak pojďme sloučit hlavní větev a větev nouzových oprav (emergency-fix).

Nejprve se přepni na větev master:

```
git checkout master
Switched to branch 'master'
```

Nyní spoj aktuální větev (master) s větví emergency-fix:

```
git merge emergency-fix
Updating 09f4acd..dfa79db
Fast-forward
 index.html | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Vzhledem k tomu, že větev emergency-fix pochází přímo z větve master a během práce nebyly provedeny žádné další změny v masteru, Git to považuje za pokračování masteru. Takže může bez problémů sloučit hlavní i emergency-fix jedním commitem.

Protože hlavní a emergency-fix jsou nyní v podstatě stejné, můžeme emergency-fix odstranit, protože již není potřeba:

```
git branch -d emergency-fix
Deleted branch emergency-fix (was dfa79db).
```

### Konflikt při spojení Git Branches

Nyní se můžeš přesunout do větve hello-world-images a pokračovat v práci. Přidej další soubor obrázku (img_hello_git.jpg)</br>

![](img_hello_git.jpg)</br>

a změňte index.html, aby se zobrazil:

```
git checkout hello-world-images
Switched to branch 'hello-world-images'
```

```
 <!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
<link rel="stylesheet" href="bluestyle.css">
</head>
<body>

<h1>Hello world!</h1>
<div><img src="img_hello_world.jpg" alt="Hello World from Space" style="width:100%;max-width:960px"></div>
<p>This is the first file in my new Git Repo.</p>
<p>A new line in our file!</p>
<div><img src="img_hello_git.jpg" alt="Hello Git" style="width:100%;max-width:640px"></div>

</body>
</html> 
```

Nyní můžeš vše v této větvi přesunout do staging area a následně potvrdit commitem:

```
git add --all
git commit -m "added new image"
[hello-world-images 1f1584e] added new image
 2 files changed, 1 insertion(+)
 create mode 100644 img_hello_git.jpg
```

Vidíš, že index.html byl změněn v obou větvích. Nyní je vše připraveno pro připojení větve hello-world-images do master. Ale co se stane se změnami, které byly nedávno provedené v masteru?

```
git checkout master
git merge hello-world-images
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

Sloučení se nezdařilo, protože existuje konflikt mezi verzemi pro index.html. Zkontroluj stav:

```
git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
        new file:   img_hello_git.jpg
        new file:   img_hello_world.jpg

Unmerged paths:
  (use "git add ..." to mark resolution)
        both modified:   index.html
```

To potvrzuje, že došlo ke konfliktu v index.html, ale soubory obrázků jsou připraveny a připraveny k potvrzení.

Takže ten konflikt musíš odstranit. Otevři soubor v editoru:

```
 <!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
<link rel="stylesheet" href="bluestyle.css">
</head>
<body>

<h1>Hello world!</h1>
<div><img src="img_hello_world.jpg" alt="Hello World from Space" style="width:100%;max-width:960px"></div>
<p>This is the first file in my new Git Repo.</p>
<<<<<<< HEAD
<p>This line is here to show how merging works.</p>
=======
<p>A new line in our file!</p>
<div><img src="img_hello_git.jpg" alt="Hello Git" style="width:100%;max-width:640px"></div>
>>>>>>> hello-world-images

</body>
</html> 
```

Vidíš rozdíly mezi verzemi a uprav je, jak potřebuješ:

```
 <!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
<link rel="stylesheet" href="bluestyle.css">
</head>
<body>

<h1>Hello world!</h1>
<div><img src="img_hello_world.jpg" alt="Hello World from Space" style="width:100%;max-width:960px"></div>
<p>This is the first file in my new Git Repo.</p>
<p>This line is here to show how merging works.</p>
<div><img src="img_hello_git.jpg" alt="Hello Git" style="width:100%;max-width:640px"></div>

</body>
</html> 
```

Nyní můžeš přesunou index.html do staging area a zkontrolovat stav:

```
git add index.html
git status
On branch master
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        new file:   img_hello_git.jpg
        new file:   img_hello_world.jpg
        modified:   index.html
```

Konflikt byl opraven a k dokončení sloučení můžeme použít commit:

```
git commit -m "merged with hello-world-images after fixing conflicts"
[master e0b6038] merged with hello-world-images after fixing conflicts
```

Nyní smaž větev hello-world-images:

```
git branch -d hello-world-images
Deleted branch hello-world-images (was 1f1584e).
```

**Dobrá práce! Nyní lépe rozumíš tomu, jak fungují Git branches a jejich spojování. Je čas začít pracovat se vzdáleným úložištěm!**
