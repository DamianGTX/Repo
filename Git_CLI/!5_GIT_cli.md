### 🧠 Tahák na Git – základní příkazy

| Příkaz             | Popis                                                                                         | Příklad použití                                                                                  |
|:------------------ |:--------------------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------ |
| **`git init`**     | Inicializuje nový lokální Git repozitář ve složce (vytvoří podadresář `.git`).                | `git init`                                                                                       |
| **`git add`**      | Přidá změny (soubor nebo více souborů) do *staging area* – připraví je pro commit.            | `git add index.html`<br>`git add .` *(všechny změny)*                                            |
| **`git commit`**   | Uloží změny z *staging area* do historie repozitáře s popisnou zprávou.                       | `git commit -m "Přidal jsem úvodní stránku"`                                                     |
| **`git status`**   | Zobrazí aktuální stav repozitáře – které soubory byly změněny, přidány nebo nejsou sledované. | `git status`                                                                                     |
| **`git log`**      | Vypíše historii commitů (s ID, autorem, datem a zprávou).                                     | `git log`<br>`git log --oneline` *(zkrácený přehled)*                                            |
| **`git branch`**   | Zobrazí seznam větví nebo vytvoří novou větev.                                                | `git branch` *(zobrazí seznam)*<br>`git branch feature-login` *(vytvoří novou větev)*            |
| **`git checkout`** | Přepne se na jinou větev nebo obnoví soubory do určité verze.                                 | `git checkout main` *(přepne na větev)*<br>`git checkout a1b2c3d` *(přepne na konkrétní commit)* |
