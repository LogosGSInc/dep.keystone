# The Way - Torah Study App (Flutter)

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Flutter](https://img.shields.io/badge/Flutter-3.27+-02569B.svg)
![License](https://img.shields.io/badge/license-Open%20Source-green.svg)

**The Way** is a comprehensive Torah study Progressive Web App designed to be 100% free and open-source. Built with Flutter for production-grade performance and scalability.

---

## 🎨 Design System

### Visual Theme
- **Primary Colors**: Sky Blue (#87CEEB), Pearl White (#F8F8FF), Gold (#FFD700)
- **Typography**: Brush Script (headers), Lora Serif (body), Frank Ruehl (Hebrew)
- **Borders**: Black 2px solid borders with gold accents
- **Dark Mode**: OLED black background optimized for night study

### Mood
Peaceful, inspiring, and scholarly—designed for focused Torah study.

---

## ✨ Features

### Core Features (v1.0)
- ✅ **Daily Torah Portion**: Automatic weekly updates with embedded Parasha schedule
- ✅ **Prayer for Discernment**: Opening prayer before study (expandable card)
- ✅ **Hebrew Text + Translation**: JPS 1917 English with Hebrew original
- ✅ **Classical Commentaries**: Rashi, Ibn Ezra, Ramban, Sforno
- ✅ **Personal Notes**: Auto-save with local storage
- ✅ **Festival Calendar**: Complete Jewish holiday information
- ✅ **Offline-First**: Zero internet required for core functionality
- ✅ **Parasha Schedule**: Pre-loaded for 5786-5790 Jewish years

### Enhanced Features (Roadmap)
- 🚧 **Full Torah Browser**: Navigate any book/chapter/verse
- 🚧 **Search Engine**: Keyword search across Torah and commentaries
- 🚧 **Bookmarking System**: Save favorite verses
- 🚧 **Highlighting System**: 5-color verse marking
- 🚧 **Reading Plans**: Daily/weekly study tracks
- 🚧 **Study Streaks**: Gamification with achievement badges
- 🚧 **Share Verses**: Generate formatted images for social media
- 🚧 **Audio Player**: Torah reading audio files
- 🚧 **Multiple Translations**: Additional translations beyond JPS 1917
- 🚧 **Notifications**: Daily study reminders
- 🚧 **Multi-Language UI**: English, Hebrew, Pashto, Dari, Hindi, Mandarin, Spanish

---

## 🏗️ Architecture

**Pattern**: Clean Architecture + MVVM + Repository Pattern

```
lib/
├── core/                    # Shared infrastructure
│   ├── constants/          # Colors, fonts, strings
│   ├── theme/              # Light, dark, sepia themes
│   ├── utils/              # Hebrew calendar, search engine
│   └── widgets/            # Reusable UI components
│
├── features/               # Feature modules (16 total)
│   ├── daily/             # Daily Torah portion
│   ├── torah_browser/     # Full navigation system
│   ├── commentaries/      # Commentary viewer
│   ├── parasha/           # Weekly portion
│   ├── festivals/         # Jewish holidays
│   ├── notes/             # Personal study notes
│   ├── bookmarks/         # Favorite verses
│   ├── highlights/        # Color-coded marking
│   ├── reading_plans/     # Study tracks
│   ├── search/            # Search engine
│   ├── share/             # Social media sharing
│   ├── audio/             # Audio player
│   ├── streaks/           # Gamification
│   ├── notifications/     # Reminders
│   ├── settings/          # App configuration
│   └── prayer/            # Prayer texts
│
└── main.dart              # App entry point
```

**State Management**: Riverpod 2.x  
**Local Storage**: Hive (encrypted)  
**Offline Data**: Embedded JSON assets

---

## 🚀 Getting Started

### Prerequisites
- Flutter SDK 3.27+
- Dart 3.2+
- Android Studio / VS Code
- Android SDK (for Android builds)
- Xcode (for iOS builds, Mac only)

### Installation

1. **Clone Repository**
```bash
git clone https://github.com/yourusername/the-way-torah-app.git
cd the-way-torah-app/torah_study_pro
```

2. **Install Dependencies**
```bash
flutter pub get
```

3. **Generate Code** (Hive adapters, Riverpod providers)
```bash
flutter pub run build_runner build --delete-conflicting-outputs
```

4. **Run App**
```bash
# Development mode
flutter run

# Release mode (Android)
flutter run --release

# Specific device
flutter run -d <device-id>
```

---

## 📦 Building for Production

### Android (APK)
```bash
flutter build apk --release --split-per-abi
```
Output: `build/app/outputs/flutter-apk/`

### Android (App Bundle for Play Store)
```bash
flutter build appbundle --release \
  --obfuscate \
  --split-debug-info=build/app/outputs/symbols
```
Output: `build/app/outputs/bundle/release/app-release.aab`

### iOS (App Store)
```bash
flutter build ipa --release
```
Output: `build/ios/archive/Runner.xcarchive`

### Web (PWA)
```bash
flutter build web --release --web-renderer canvaskit
```
Output: `build/web/`

---

## 🧪 Testing

### Run All Tests
```bash
flutter test
```

### Test Coverage
```bash
flutter test --coverage
genhtml coverage/lcov.info -o coverage/html
open coverage/html/index.html
```

**Coverage Target**: >90%

---

## 📁 Project Status

### ✅ Completed (Phase 1)
- [x] Project structure
- [x] Theme system (light/dark)
- [x] Core constants (colors, fonts)
- [x] Navigation architecture
- [x] Daily screen with prayer card
- [x] Torah portion display
- [x] Commentary selector
- [x] Personal notes with auto-save
- [x] Festival calendar
- [x] Settings screen
- [x] Resource links

### 🚧 In Progress (Phase 2)
- [ ] Full Torah browser implementation
- [ ] Hive database integration
- [ ] Search engine
- [ ] Bookmarking system
- [ ] Parasha scheduler (5786+ years)

### 📋 Pending (Phase 3+)
- [ ] Reading plans
- [ ] Study streaks
- [ ] Audio player
- [ ] Verse sharing (image generator)
- [ ] Multi-translation viewer
- [ ] Highlighting system
- [ ] Notifications
- [ ] Multi-language UI (7 languages)

---

## 🎨 Design Specifications

### Typography Scale
- **Headlines**: 32sp (Brush Script Bold)
- **Titles**: 24sp (Brush Script)
- **Subtitles**: 20sp (Brush Script Medium)
- **Body**: 16sp (Lora Serif)
- **Hebrew**: 20sp (Frank Ruehl)
- **Captions**: 14sp (Lora Serif)

### Color Palette
#### Light Mode
- Primary: Sky Blue `#87CEEB`
- Surface: Pearl White `#F8F8FF`
- Accent: Gold `#FFD700`
- Text: Black `#000000`

#### Dark Mode (OLED)
- Background: Pure Black `#000000`
- Surface: Dark Gray `#121212`
- Accent: Soft Gold `#DAA520`
- Text: Pearl White `#F8F8FF`

---

## 🛠️ Development Tools

### VS Code Extensions
- Flutter
- Dart
- Flutter Riverpod Snippets
- Error Lens

### Android Studio Plugins
- Flutter
- Dart
- Rainbow Brackets

---

## 📚 Resources & Credits

**Torah Texts:**
- [Sefaria.org](https://www.sefaria.org) - Jewish texts library
- JPS 1917 English Translation (Public Domain)
- Leningrad Codex Hebrew Text

**Commentaries:**
- Rashi (Rabbi Shlomo Yitzchaki)
- Ibn Ezra (Abraham ibn Ezra)
- Ramban (Nachmanides)
- Sforno (Obadiah Sforno)

**Study Resources:**
- [TorahClass.com](https://www.torahclass.com) - Video studies
- [Chabad.org](https://www.chabad.org/parshah) - Weekly Parasha
- [HebCal.com](https://www.hebcal.com) - Hebrew calendar

---

## 🤝 Contributing

This project is 100% free and open-source. Contributions welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📜 License

**Open Source** - Free for personal and educational use.

All Torah texts, translations, and commentaries are sourced from public domain materials or licensed for free use.

---

## 📧 Contact

**Developer**: DJ  
**Project**: The Way Torah Study App  
**Ecosystem**: Companion to Truth Daily (Flutter)

---

## 🙏 Support

If you find this app helpful:
- ⭐ Star the repository
- 📢 Share with your community
- 🐛 Report bugs
- 💡 Suggest features
- 🤝 Contribute code

**Support Partner Organizations:**
- Donate to [Sefaria.org](https://www.sefaria.org/donate)
- Support [TorahClass.com](https://www.torahclass.com)

---

**Built with ❤️ for Torah study**
