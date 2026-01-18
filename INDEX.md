# 📑 PROJECT RPL - Navigation Guide

Panduan navigasi lengkap PROJECT RPL untuk menemukan apa yang Anda cari.

---

## 🎯 Start Here

### 🔰 Pertama Kali?
1. **Baca:** [README.md](README.md) - Penjelasan project
2. **Setup:** [docs/INSTALLATION.md](docs/INSTALLATION.md) - Cara install
3. **Coba:** [docs/USER_GUIDE.md](docs/USER_GUIDE.md) - Cara main game
4. **Explore:** Run salah satu game dari terminal

### 👨‍💻 Developer?
1. **Baca:** [docs/DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) - Architecture & guidelines
2. **Explore:** [src/games/](src/games/) - Code structure
3. **Test:** [tests/](tests/) - Unit tests
4. **Contribute:** Tambah game baru atau improve existing

### 📊 Project Manager?
1. **Overview:** [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
2. **Checklist:** [COMPLETION_CHECKLIST.md](COMPLETION_CHECKLIST.md)
3. **Status:** Semua task sudah completed ✅

---

## 📂 File Structure & Navigation

### 🎮 Menjalankan Games

```
src/games/
├── dice_game.py              → Game Lempar Dadu
├── guessing_game.py          → Game Tebak Angka
├── rock_paper_scissors.py    → Gunting Batu Kertas
└── qr_generator.py           → Pembuat Kode QR

Cara menjalankan:
$ python -m src.games.dice_game
```

### 📖 Dokumentasi

```
docs/
├── INSTALLATION.md           → How to install (Setup guide)
├── USER_GUIDE.md            → How to use (User manual)
├── DEVELOPER_GUIDE.md       → How to develop (Dev guide)
├── EXAMPLE_OUTPUTS.md       → Real output examples (LENGKAP!)
├── SCREENSHOTS.md           → 📸 Visual outputs (15+ contoh)
└── QUICK_OUTPUTS.md         → ⚡ Quick reference outputs

Di root:
├── README.md                → Main documentation (dengan contoh di awal!)
├── PROJECT_SUMMARY.md       → Project overview
└── COMPLETION_CHECKLIST.md  → What's been done
```

### 🧪 Testing

```
tests/
├── test_dice_game.py                 → Dice game tests
├── test_guessing_game.py             → Guessing game tests
├── test_rock_paper_scissors.py       → RPS game tests
└── test_qr_generator.py              → QR gen tests

Cara menjalankan:
$ pytest tests/ -v
```

### ⚙️ Configuration

```
├── requirements.txt         → Python packages to install
├── setup.cfg               → Project metadata
├── .gitignore              → Git ignore rules
└── .venv/                  → Virtual environment
```

---

## 🔍 Cari Tahu Lebih Lanjut

### ❓ "Bagaimana cara install PROJECT RPL?"
→ Baca: [docs/INSTALLATION.md](docs/INSTALLATION.md)

### ❓ "Bagaimana cara main setiap game?"
→ Baca: [docs/USER_GUIDE.md](docs/USER_GUIDE.md)

### ❓ "Saya developer, mau nambah game baru"
→ Baca: [docs/DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md)

### ❓ "Apa contoh output setiap game?"
→ Baca: [docs/EXAMPLE_OUTPUTS.md](docs/EXAMPLE_OUTPUTS.md)

### ❓ "Ada error saat install/run"
→ Baca: [README.md](README.md#-troubleshooting)

### ❓ "Project structure gimana?"
→ Baca: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

### ❓ "Apa aja yang udah selesai?"
→ Baca: [COMPLETION_CHECKLIST.md](COMPLETION_CHECKLIST.md)

---

## 📋 Quick Reference

### Game Files

| Game | File | Run Command |
|------|------|-------------|
| 🎲 Dice | `src/games/dice_game.py` | `python -m src.games.dice_game` |
| 🔢 Guessing | `src/games/guessing_game.py` | `python -m src.games.guessing_game` |
| ✂️ RPS | `src/games/rock_paper_scissors.py` | `python -m src.games.rock_paper_scissors` |
| 📱 QR | `src/games/qr_generator.py` | `python -m src.games.qr_generator` |

### Important Documents

| Document | Purpose | For Whom | Lines |
|----------|---------|---------|-------|
| README.md | Main documentation | Everyone | 470+ |
| INSTALLATION.md | Setup guide | First-time users | 250+ |
| USER_GUIDE.md | How to use | Players | 600+ |
| DEVELOPER_GUIDE.md | Development guide | Developers | 700+ |
| EXAMPLE_OUTPUTS.md | Real examples (DETAILED!) | Everyone | 500+ |
| SCREENSHOTS.md | 📸 Visual outputs | Everyone | 600+ |
| QUICK_OUTPUTS.md | ⚡ Quick reference | Everyone | 400+ |
| PROJECT_SUMMARY.md | Project overview | Managers | 300+ |
| COMPLETION_CHECKLIST.md | What's done | Managers | 100+ |

---

## 📸 Quick Peek - Output Examples

### Ingin melihat seperti apa outputnya?

| Game | Output File | Link |
|------|-------------|------|
| 🎲 Dice Game | `QUICK_OUTPUTS.md` | [Lihat Output](docs/QUICK_OUTPUTS.md#1️⃣-game-lempar-dadu---🎲-dice-game) |
| 🔢 Guessing Game | `QUICK_OUTPUTS.md` | [Lihat Output](docs/QUICK_OUTPUTS.md#2️⃣-game-tebak-angka---🔢-guessing-game) |
| ✂️ Rock Paper Scissors | `QUICK_OUTPUTS.md` | [Lihat Output](docs/QUICK_OUTPUTS.md#3️⃣-gunting-batu-kertas---✂️-rock-paper-scissors) |
| 📱 QR Generator | `QUICK_OUTPUTS.md` | [Lihat Output](docs/QUICK_OUTPUTS.md#4️⃣-pembuat-kode-qr---📱-qr-code-generator) |
| 🧪 Test Results | `QUICK_OUTPUTS.md` | [Lihat Output](docs/QUICK_OUTPUTS.md#🧪-test-output---pytest-results) |

**Quick Reference:** [docs/QUICK_OUTPUTS.md](docs/QUICK_OUTPUTS.md)  
**Detailed Examples:** [docs/SCREENSHOTS.md](docs/SCREENSHOTS.md)

---

## 🚀 Common Tasks

### Task 1: Setup & Run Game

```bash
# 1. Setup
cd PROJECT_RPL
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt

# 2. Run game
python -m src.games.dice_game
```

**Help:** [docs/INSTALLATION.md](docs/INSTALLATION.md)

### Task 2: Play a Game

Setelah setup, pilih salah satu:

```bash
python -m src.games.dice_game
python -m src.games.guessing_game
python -m src.games.rock_paper_scissors
python -m src.games.qr_generator
```

**Help:** [docs/USER_GUIDE.md](docs/USER_GUIDE.md)

### Task 3: Run Tests

```bash
# Install test packages
pip install pytest pytest-cov

# Run tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=src --cov-report=html
```

**Help:** [README.md#-unit-tests](README.md#-unit-tests)

### Task 4: Add New Game

```bash
# 1. Create file
# src/games/my_new_game.py

# 2. Create test
# tests/test_my_new_game.py

# 3. Update __init__.py
# tests/

# 4. Test it
pytest tests/test_my_new_game.py
```

**Help:** [docs/DEVELOPER_GUIDE.md#-adding-new-games](docs/DEVELOPER_GUIDE.md#-adding-new-games)

### Task 5: Troubleshoot Issues

1. Cek error message dengan teliti
2. Baca: [README.md#-troubleshooting](README.md#-troubleshooting)
3. Baca: [docs/INSTALLATION.md#-troubleshooting](docs/INSTALLATION.md#-troubleshooting)
4. Follow instruksi yang sesuai

---

## 🎯 Learning Path

### Beginner
1. Read: [README.md](README.md)
2. Follow: [docs/INSTALLATION.md](docs/INSTALLATION.md)
3. Try: Run one game
4. Learn: [docs/USER_GUIDE.md](docs/USER_GUIDE.md)

### Intermediate
1. Explore: `src/games/` code
2. Run: `pytest tests/` tests
3. Modify: Change game parameters
4. Create: Add improvements

### Advanced
1. Read: [docs/DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md)
2. Design: New game idea
3. Develop: Implement your game
4. Test: Write comprehensive tests
5. Document: Add documentation

---

## 💡 Pro Tips

### Tip 1: Quick Access
Bookmark ini file untuk reference cepat!

### Tip 2: Search
Gunakan `Ctrl + F` untuk search di file markdown

### Tip 3: Terminal Shortcuts
```bash
# Alias untuk quick access (di .bashrc atau .zshrc)
alias dice="python -m src.games.dice_game"
alias guess="python -m src.games.guessing_game"
alias rps="python -m src.games.rock_paper_scissors"
alias qr="python -m src.games.qr_generator"
```

### Tip 4: Virtual Environment
Always activate venv sebelum run program!

### Tip 5: Tests
Run tests setelah setiap perubahan code

---

## 📞 Need Help?

### Documentation First
Cek dokumentasi relevant terlebih dahulu:
- [README.md](README.md)
- [docs/INSTALLATION.md](docs/INSTALLATION.md)
- [docs/USER_GUIDE.md](docs/USER_GUIDE.md)
- [docs/DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md)

### Common Solutions
Baca troubleshooting section di:
- [README.md#-troubleshooting](README.md#-troubleshooting)
- [docs/INSTALLATION.md#-troubleshooting](docs/INSTALLATION.md#-troubleshooting)

### Still Stuck?
Hubungi developer atau buat GitHub issue

---

## 📊 Directory Tree

```
PROJECT_RPL/
├── README.md ⭐ START HERE
├── INSTALLATION.md → Full setup guide
├── PROJECT_SUMMARY.md → Overview
├── COMPLETION_CHECKLIST.md → Status
├── INDEX.md ← YOU ARE HERE
│
├── src/ → Source code
│   └── games/ → 4 games
│
├── tests/ → Unit tests
│
├── docs/ → Detailed documentation
│   ├── INSTALLATION.md
│   ├── USER_GUIDE.md
│   ├── DEVELOPER_GUIDE.md
│   └── EXAMPLE_OUTPUTS.md
│
├── requirements.txt → Dependencies
├── setup.cfg → Config
├── .gitignore → Git rules
└── .venv/ → Virtual env
```

---

## ✅ Recommended Flow

1. **First Visit?**
   - Read [README.md](README.md)
   - Follow [docs/INSTALLATION.md](docs/INSTALLATION.md)
   - Bookmark this page

2. **Want to Play?**
   - Setup virtual environment
   - Install requirements
   - Run game from [USER_GUIDE.md](docs/USER_GUIDE.md)

3. **Want to Develop?**
   - Read [docs/DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md)
   - Explore code in `src/`
   - Create new game

4. **Got Issues?**
   - Check [README.md#-troubleshooting](README.md#-troubleshooting)
   - Check installation doc
   - Try workarounds

---

**Happy Exploring! 🎉**

Last Updated: January 18, 2026
