# HidroAgro Nusantara — Android

Game HTML dibungkus WebView native (package `id.hidroagro.nusantara`). Save game memakai localStorage dan tetap tersimpan.

## Cara paling mudah: build APK otomatis via GitHub (tanpa Android Studio)
1. Buat repo GitHub baru, upload seluruh isi folder ini (termasuk folder `.github`).
2. Buka tab **Actions** → **Build APK** → **Run workflow**.
3. Setelah selesai (±3–5 menit), unduh artifact **HidroAgro-Nusantara-apk** → ekstrak → `app-debug.apk`.
4. Kirim APK ke HP, buka, izinkan "Instal dari sumber tidak dikenal", lalu instal.

## Alternatif: Android Studio
1. (Opsional, agar offline) `python3 tools/vendor_assets.py`
2. Buka folder ini di Android Studio → Build → Build APK(s).

Catatan: tanpa langkah vendor, game tetap jalan tetapi butuh internet (Tailwind, ikon, font dimuat dari CDN).
