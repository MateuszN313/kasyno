[git_cheat_sheet_readme.md](https://github.com/user-attachments/files/27101796/git_cheat_sheet_readme.md)
# 📦 Git – podstawowe komendy

| Komenda | Co robi | Kiedy używasz |
|--------|--------|--------------|
| `git clone github_repository_address` | Pobiera repozytorium z GitHuba na Twój komputer | Gdy zaczynasz pracę z istniejącym projektem |
| `git init` | Tworzy nowe repozytorium Git w folderze | Gdy zaczynasz projekt od zera |
| `git checkout branch` | Przełącza Cię na inny branch | Gdy chcesz pracować na innej gałęzi |
| `git checkout -b new_branch` | Tworzy nowy branch i od razu na niego przechodzi | Gdy zaczynasz nową funkcję/feature |
| `git add .` | Dodaje wszystkie zmiany do tzw. staging area | Przed zrobieniem commita |
| `git commit -m "commit_message"` | Zapisuje zmiany w historii projektu | Po zakończeniu jakiegoś kawałka pracy |
| `git merge branch` | Łączy wskazany branch z aktualnym | Gdy chcesz połączyć zmiany (np. feature → main) |
| `git remote add origin github_repository_address` | Podpina zdalne repo (GitHub) do lokalnego | Gdy masz lokalny projekt i chcesz go wrzucić na GitHub |
| `git pull origin branch` | Pobiera i scala zmiany z GitHuba | Gdy chcesz mieć aktualny kod |
| `git pull --no-commit origin branch` | Pobiera zmiany, ale nie robi automatycznego commita | Gdy chcesz najpierw przejrzeć zmiany |
| `git push origin branch` | Wysyła zmiany na GitHuba | Po commitach |
| `git push -u origin branch` | To samo co push + ustawia domyślny branch do push/pull | Pierwszy push nowego brancha |

---

# 🚀 Przykład workflow (branch → commit → push → pull request)

## 1. Sklonuj repo
```bash
git clone https://github.com/user/projekt.git
cd projekt
```

## 2. Stwórz nowego brancha
```bash
git checkout -b feature/login-system
```

## 3. Zrób zmiany w kodzie
Np. dodajesz system logowania.

## 4. Dodaj zmiany
```bash
git add .
```

## 5. Commit
```bash
git commit -m "Add basic login system"
```

## 6. Push na GitHub
```bash
git push -u origin feature/login-system
```

## 7. Pull Request
1. Wejdź na GitHub
2. Kliknij **"Compare & pull request"**
3. Dodaj opis zmian
4. Kliknij **"Create Pull Request"**

---
